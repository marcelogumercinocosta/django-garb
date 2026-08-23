import { copyFile, cp, mkdir, rm } from "node:fs/promises";
import { dirname } from "node:path";

const files = {
  "node_modules/bootstrap/dist/css/bootstrap.min.css": "garb/static/vendor/bootstrap/bootstrap.min.css",
  "node_modules/bootstrap/dist/css/bootstrap.min.css.map": "garb/static/vendor/bootstrap/bootstrap.min.css.map",
  "node_modules/bootstrap/dist/css/bootstrap-reboot.min.css": "garb/static/vendor/bootstrap/bootstrap-reboot.min.css",
  "node_modules/bootstrap/dist/css/bootstrap-reboot.min.css.map": "garb/static/vendor/bootstrap/bootstrap-reboot.min.css.map",
  "node_modules/bootstrap/dist/js/bootstrap.bundle.min.js": "garb/static/vendor/bootstrap/bootstrap.bundle.min.js",
  "node_modules/bootstrap/dist/js/bootstrap.bundle.min.js.map": "garb/static/vendor/bootstrap/bootstrap.bundle.min.js.map",
  "node_modules/bootstrap-select/dist/css/bootstrap-select.min.css": "garb/static/vendor/bootstrap-select/css/bootstrap-select.min.css",
  "node_modules/bootstrap-select/dist/js/bootstrap-select.min.js": "garb/static/vendor/bootstrap-select/js/bootstrap-select.min.js",
  "node_modules/bootstrap-select/dist/js/bootstrap-select.min.js.map": "garb/static/vendor/bootstrap-select/js/bootstrap-select.min.js.map",
  "node_modules/jquery/dist/jquery.min.js": "garb/static/vendor/jquery/jquery.min.js",
  "node_modules/jquery/dist/jquery.js": "garb/static/vendor/jquery/jquery.js",
  "node_modules/jquery-toast-plugin/dist/jquery.toast.min.css": "garb/static/vendor/jquery-toast-plugin/jquery.toast.min.css",
  "node_modules/jquery-toast-plugin/dist/jquery.toast.min.js": "garb/static/vendor/jquery-toast-plugin/jquery.toast.min.js",
  "node_modules/pace-js/pace.min.js": "garb/static/vendor/pace/pace.min.js"
};

for (const [source, destination] of Object.entries(files)) {
  await mkdir(dirname(destination), { recursive: true });
  await copyFile(source, destination);
}

const localeSource = "node_modules/bootstrap-select/dist/js/i18n";
const localeDestination = "garb/static/vendor/bootstrap-select/js/i18n";
await rm(localeDestination, { recursive: true, force: true });
await cp(localeSource, localeDestination, { recursive: true });
