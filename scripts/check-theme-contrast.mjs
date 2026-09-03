const palette = {
  navy: '#052455',
  navyHover: '#103D7F',
  orange: '#FF7A00',
  orangeText: '#C45100',
  white: '#FFFFFF',
  surface: '#F4F6F8',
  muted: '#5D6778',
  border: '#8792A2',
};

const checks = [
  ['texto sobre menu', palette.white, palette.navy, 4.5],
  ['texto sobre menu em hover', palette.white, palette.navyHover, 4.5],
  ['texto principal sobre branco', palette.navy, palette.white, 4.5],
  ['texto principal sobre superfície', palette.navy, palette.surface, 4.5],
  ['texto secundário sobre branco', palette.muted, palette.white, 4.5],
  ['link laranja sobre branco', palette.orangeText, palette.white, 4.5],
  ['texto de botão sobre laranja', palette.navy, palette.orange, 4.5],
  ['destaque laranja sobre menu', palette.orange, palette.navy, 3],
  ['borda de campo sobre branco', palette.border, palette.white, 3],
];

function luminance(hex) {
  const channels = hex.slice(1).match(/.{2}/g).map(channel => {
    const value = Number.parseInt(channel, 16) / 255;
    return value <= 0.04045 ? value / 12.92 : ((value + 0.055) / 1.055) ** 2.4;
  });
  return 0.2126 * channels[0] + 0.7152 * channels[1] + 0.0722 * channels[2];
}

function contrast(foreground, background) {
  const values = [luminance(foreground), luminance(background)].sort((a, b) => b - a);
  return (values[0] + 0.05) / (values[1] + 0.05);
}

const failures = [];
for (const [name, foreground, background, minimum] of checks) {
  const ratio = contrast(foreground, background);
  if (ratio < minimum) failures.push(`${name}: ${ratio.toFixed(2)}:1 < ${minimum}:1`);
  else console.log(`✓ ${name}: ${ratio.toFixed(2)}:1`);
}

if (failures.length) {
  console.error(failures.join('\n'));
  process.exitCode = 1;
}
