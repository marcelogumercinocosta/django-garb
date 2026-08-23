(function ($) {
    'use strict';

    function isTemplateSelect(element) {
        return element.id && element.id.indexOf('-__prefix__-') !== -1;
    }

    function initializeSelects(root) {
        if (!$.fn.selectpicker) {
            return;
        }

        $.fn.selectpicker.Constructor.DEFAULTS.styleBase = null;
        $.fn.selectpicker.Constructor.DEFAULTS.noneSelectedText = '---------';

        $(root).find('select').addBack('select').each(function () {
            var $select = $(this);
            if ($select.is('[multiple]') || isTemplateSelect(this)) {
                return;
            }
            if ($select.parent().hasClass('bootstrap-select')) {
                $select.selectpicker('refresh');
            } else {
                $select.selectpicker();
            }
        });
    }

    function clearInvalidState(element) {
        var $element = $(element);
        $element.removeClass('is-invalid');
        $element.closest('.form-row').removeClass('is-invalid');
    }

    $(function () {
        initializeSelects(document);

        $(document).on('formset:added', function (event, row) {
            initializeSelects(row || event.target);
        });

        $(document).on('keyup click', 'input', function () {
            clearInvalidState(this);
        });

        $(document).on('click', '.bootstrap-select .dropdown-toggle', function () {
            var $select = $(this).closest('.bootstrap-select').find('select');
            clearInvalidState($select);
            $select.closest('.form-group').find('.error-feedback').remove();
            $select.closest('.form-row').find('.errorlist').remove();
        });

        var $forms = $('form');
        if ($forms.length) {
            var initialState = $forms.serialize();
            $('.btn-verify-form').on('click', function (event) {
                if (initialState !== $forms.serialize()) {
                    event.preventDefault();
                    window.alert('Precisa salvar antes!');
                }
            });
        }
    });
})(jQuery);
