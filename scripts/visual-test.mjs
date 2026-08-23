import fs from 'node:fs';
import path from 'node:path';
import process from 'node:process';
import { chromium } from 'playwright-core';
import { HtmlValidate } from 'html-validate';
import pixelmatch from 'pixelmatch';
import { PNG } from 'pngjs';

const update = process.argv.includes('--update');
const baseUrl = process.env.GARB_VISUAL_URL || 'http://127.0.0.1:8765';
const baselineDir = path.resolve('tests/visual/baseline');
const actualDir = path.resolve('tests/visual/actual');
const diffDir = path.resolve('tests/visual/diff');
const themes = ['default', 'light', 'hybrid', 'dark', 'alive'];
const failures = [];
const browserErrors = [];
const validatedUrls = new Set();
const htmlValidate = new HtmlValidate({
  extends: ['html-validate:recommended'],
  rules: {
    'no-inline-style': 'off',
    'no-trailing-whitespace': 'off',
    'attribute-boolean-style': 'off',
    'attr-quotes': 'off',
    'form-dup-name': 'off',
    'prefer-native-element': 'off',
    'prefer-button': 'off',
    'prefer-tbody': 'off',
    'require-sri': 'off',
    'script-type': 'off',
    'unique-landmark': 'off',
    'void-style': 'off',
    'wcag/h63': 'off',
  },
});

for (const directory of [baselineDir, actualDir, diffDir]) {
  fs.mkdirSync(directory, { recursive: true });
}

function compare(name, actualPath) {
  const baselinePath = path.join(baselineDir, `${name}.png`);
  if (update) {
    fs.copyFileSync(actualPath, baselinePath);
    return;
  }
  if (!fs.existsSync(baselinePath)) {
    failures.push(`${name}: baseline ausente (execute npm run test:visual:update)`);
    return;
  }
  const baseline = PNG.sync.read(fs.readFileSync(baselinePath));
  const actual = PNG.sync.read(fs.readFileSync(actualPath));
  if (baseline.width !== actual.width || baseline.height !== actual.height) {
    failures.push(`${name}: dimensão ${actual.width}x${actual.height}, esperada ${baseline.width}x${baseline.height}`);
    return;
  }
  const diff = new PNG({ width: actual.width, height: actual.height });
  const changed = pixelmatch(baseline.data, actual.data, diff.data, actual.width, actual.height, {
    threshold: 0.12,
  });
  const ratio = changed / (actual.width * actual.height);
  if (ratio > 0.01) {
    fs.writeFileSync(path.join(diffDir, `${name}.png`), PNG.sync.write(diff));
    failures.push(`${name}: ${(ratio * 100).toFixed(2)}% dos pixels diferem (tolerância 1%)`);
  }
}

async function capture(page, name, url, theme = 'default') {
  await page.goto(`${baseUrl}${url}`, { waitUntil: 'networkidle' });
  await page.evaluate(selectedTheme => {
    document.body.classList.remove('default', 'light', 'hybrid', 'dark', 'alive');
    document.body.classList.add(selectedTheme);
  }, theme);
  await page.evaluate(() => document.fonts.ready);
  const sourceResponse = await page.request.get(`${baseUrl}${url}`);
  const html = await sourceResponse.text();
  fs.writeFileSync(path.join(actualDir, `${name}.html`), html);
  if (!validatedUrls.has(url)) {
    const report = await htmlValidate.validateString(html);
    if (!report.valid) {
      const messages = report.results.flatMap(result => result.messages).slice(0, 8);
      failures.push(`${name}: HTML inválido: ${messages.map(message => `${message.ruleId} ${message.message} (${message.line}:${message.column})`).join(' | ')}`);
    }
    validatedUrls.add(url);
  }
  const actualPath = path.join(actualDir, `${name}.png`);
  await page.screenshot({ path: actualPath, animations: 'disabled', caret: 'hide' });
  compare(name, actualPath);
}

const browser = await chromium.launch({
  executablePath: process.env.CHROME_BIN || '/usr/bin/google-chrome',
  headless: true,
});
const page = await browser.newPage({
  viewport: { width: 1680, height: 984 },
  deviceScaleFactor: 1,
  locale: 'pt-BR',
  timezoneId: 'America/Sao_Paulo',
});
page.on('console', message => {
  if (message.type() === 'error') browserErrors.push(`console: ${message.text()}`);
});
page.on('pageerror', error => browserErrors.push(`pageerror: ${error.message}`));
page.on('requestfailed', request => {
  if (request.url().startsWith(baseUrl)) {
    browserErrors.push(`request: ${request.url()} (${request.failure()?.errorText})`);
  }
});

await capture(page, 'login-default', '/admin/login/');
await page.locator('#id_username').fill('garb-admin');
await page.locator('#id_password').fill('garb-admin');
await Promise.all([
  page.waitForURL('**/admin/**'),
  page.locator('button[type=submit], input[type=submit]').first().click(),
]);

await page.locator('#dropdownMenuLink').click();
if (!(await page.locator('.headerlogin .dropdown-menu').isVisible())) {
  failures.push('dropdown do usuário não abriu');
}
await page.keyboard.press('Escape');

await capture(page, 'index-default', '/admin/');
for (const theme of themes) {
  await capture(page, `list-${theme}`, '/admin/tests/blog/', theme);
}

if (await page.locator('#menu [data-bs-toggle="collapse"]').count()) {
  const triggers = page.locator('#menu [data-bs-toggle="collapse"]');
  const trigger = triggers.first();
  const target = await trigger.getAttribute('href');
  await trigger.click();
  await page.locator(target).waitFor({ state: 'hidden' });
  await trigger.click();
  await page.locator(target).waitFor({ state: 'visible' });
  await page.waitForFunction(selector => document.querySelector(selector)?.classList.contains('show'), target).catch(() => null);
  if (!(await page.locator(target).getAttribute('class')).includes('show')) {
    failures.push('submenu lateral não alternou');
  }
}

if (!(await page.locator('.bootstrap-select').count())) {
  failures.push('bootstrap-select não inicializou na listagem');
} else {
  await page.locator('.bootstrap-select button').first().click();
  if (!(await page.locator('.bootstrap-select .dropdown-menu.show').count())) {
    failures.push('dropdown de select não abriu');
  }
  await page.keyboard.press('Escape');
}

await page.evaluate(() => window.jQuery.toast({ text: 'Visual toast', position: 'bottom-right', hideAfter: false }));
if (!(await page.locator('.jq-toast-wrap').isVisible())) failures.push('toast não ficou visível');
if (await page.evaluate(() => typeof window.Pace === 'undefined')) failures.push('Pace não foi carregado');

await capture(page, 'change-default', '/admin/tests/blog/1/change/');
await page.evaluate(() => {
  const row = document.createElement('div');
  row.innerHTML = '<select id="id_dynamic-0-category"><option value="">---------</option><option value="1">Technology</option></select>';
  document.querySelector('#content-main').appendChild(row);
  row.dispatchEvent(new CustomEvent('formset:added', { bubbles: true, detail: { formsetName: 'dynamic' } }));
});
if (!(await page.locator('#id_dynamic-0-category').evaluate(element => element.parentElement.classList.contains('bootstrap-select')))) {
  failures.push('select de inline dinâmico não foi inicializado');
}

await capture(page, 'delete-default', '/admin/tests/blog/1/delete/');
await capture(page, 'history-default', '/admin/tests/blog/1/history/');

await browser.close();
if (browserErrors.length) failures.push(...browserErrors);
if (failures.length) {
  console.error(failures.join('\n'));
  process.exitCode = 1;
} else {
  console.log(`${update ? 'Baselines atualizadas' : 'Comparação visual aprovada'}: 10 capturas, 5 temas, sem erros JavaScript.`);
}
