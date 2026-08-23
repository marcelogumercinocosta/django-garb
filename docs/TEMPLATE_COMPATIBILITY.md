# Django Admin template compatibility

The overrides in `garb/templates/admin/` were compared with the admin templates
shipped by Django 5.1, 5.2, and 6.0. They remain overrides only where Garb owns
layout, styling, or behavior; replacing them with upstream copies would remove
the documented visual identity.

Relevant contracts reconciled during the comparison:

- the base shell now exposes language direction, the public body-class block,
  UTC metadata, a main-content target, and POST logout;
- change forms retain `form_top`, error-aware titles, current media loading,
  inline prefixes, and asynchronous `change_form.js` initialization;
- change lists load `media.css`, current filters, and gate top and bottom bulk
  actions with `show_admin_actions`;
- tabular and stacked inlines use current empty-form IDs, accessible headings,
  collapsible fieldsets, and fieldset prefixes;
- related widgets expose `data-model-ref`, popup metadata, explicit icon sizes,
  and view/change/add/delete permissions;
- delete, history, login, password-change, password-reset, error, and email
  templates were exercised through render and functional smoke tests.

Garb-specific breadcrumbs, cards, toolbars, tables, two-column forms, submit
boxes, and menu markup remain deliberate visual customizations. The browser
suite checks their resulting HTML in a real browser and rejects failed local
assets or uncaught JavaScript errors.
