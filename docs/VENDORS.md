# Front-end vendor inventory

The files listed here are copied into the Python package and served locally.
Run `npm ci && npm run vendor:sync` to reproduce them, then update the SHA-256
column after reviewing upstream release notes. Versions are exact in
`package-lock.json`; no runtime template references `latest` or a CDN for these
components.

| Component | Previous | Bundled | Official source | License |
| --- | --- | --- | --- | --- |
| Bootstrap CSS/JS | 4.5.2 | 5.3.8 | https://github.com/twbs/bootstrap/releases/tag/v5.3.8 | MIT |
| bootstrap-select | 1.13.17 | 1.14.0-beta3 | https://github.com/snapappointments/bootstrap-select/releases/tag/v1.14.0-beta3 | MIT |
| jQuery | 3.5.1 | 3.7.1 | https://github.com/jquery/jquery/releases/tag/3.7.1 | MIT |
| jQuery Toast Plugin | unrecorded | 1.3.2 | https://github.com/kamranahmedse/jquery-toast-plugin/tree/v1.3.2 | MIT |
| Pace | 1.0.0 | 1.2.4 | https://github.com/CodeByZach/pace/tree/v1.2.4 | MIT |

bootstrap-select 1.14.0-beta3 is the newest upstream release line that declares
Bootstrap 5 support. Its localized scripts are synchronized from the same npm
artifact as the core plugin.

## Bundled asset checksums

| Asset | SHA-256 |
| --- | --- |
| `bootstrap/bootstrap.min.css` | `d85327d99c7a3ee1f9b5d0500d1370acea3ad2db39c163c2f51f232baedbdede` |
| `bootstrap/bootstrap.bundle.min.js` | `e4fd49181388c48ec5040bd3fe66f57c29c8e67fcd8502b3354b96ec7ab47cc7` |
| `bootstrap-select/css/bootstrap-select.min.css` | `7300c976e6ccb2f209700618e445d4640b902f14a510bc45610971becc5d62cf` |
| `bootstrap-select/js/bootstrap-select.min.js` | `a1b2cfb8b839c71376302daccc46972da37cb4429881e08c9fe4d23ccc6a39f1` |
| `jquery/jquery.min.js` | `fc9a93dd241f6b045cbff0481cf4e1901becd0e12fb45166a8f17f95823f0b1a` |
| `jquery-toast-plugin/jquery.toast.min.css` | `5a896b35367d958d102f97f4fd08b5cb0dd11a70cb8a0d8754b624aec866ed8d` |
| `jquery-toast-plugin/jquery.toast.min.js` | `e7acec4e5330cc646d2c2e2de756a52e1e5c298be2d219db8445d04d553fcd94` |
| `pace/pace.min.js` | `82a77b6138e0fc1b5fa964b0b093af9dd97407173c8052262c4917413f3eaa3d` |

## Previous asset checksums

| Asset | SHA-256 |
| --- | --- |
| `bootstrap/bootstrap.min.css` | `5b0fbe5b7ad705f6a937c4998ad02f73d8f0d976fe231b74aef0ec996990c93a` |
| `bootstrap/bootstrap.min.js` | `79c599dd760cec0c1621a1af49d9a2a49da5d45e1b37d4575bace0a5e0226582` |
| `bootstrap-select/js/bootstrap-select.min.js` | `40e134d86968d42d601f33fde8939ac7220cb785d216ffdec596982d8e1dc0ed` |
| `jquery-toast-plugin/jquery.toast.min.js` | `c2d725124b278c6bc6a4a87b311b667f2853426e52dca5fbdc2a621f678b7530` |
| `pace/pace.min.js` | `579a10a2485055e988338be054f866cbe713c8510442130cbda0ce11ced6c49f` |
| `admin/js/vendor/jquery/jquery.min.js` | `f7f6a5894f1d19ddad6fa392b2ece2c5e578cbf7da4ea805b6885eb6985b6e3d` |

## Compatibility gate

jQuery 4.0.0 was rejected on 2026-08-20 because bootstrap-select 1.14.0-beta3
declares the peer range `jquery >=1.9.1 <4`; npm correctly refused the dependency
tree. The build therefore fixes jQuery 3.7.1, the newest compatible 3.x release,
and the browser suite verifies bootstrap-select, toasts, Django inline formsets
and Garb scripts with that version.
