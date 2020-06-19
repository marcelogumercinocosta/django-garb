(function ($) {
    // SELECTPICKER DATA-API
    // =====================

    function garb_select() { 
        $('select').each(function () {
            var prefixElement = true;
            if($(this).prop("id")){
                if ( $(this).attr("id").includes('-')) {
                    var selectElement = $(this).attr("id").split('-');
                    if ( selectElement[1] === '__prefix__') {
                        prefixElement = false;
                    }
                }
            }

            if ( ! $('select').attr("multiple") && prefixElement) {
                $.fn.selectpicker.Constructor.DEFAULTS.styleBase = null;
                $.fn.selectpicker.Constructor.DEFAULTS.noneSelectedText = '---------'
                $(this).selectpicker();
            }
        });
    } 
    $(document).on("mousedown",'.add-row td a',function() {
        setTimeout(function(){ garb_select()}, 200);
    });
    $(document).on("mousedown",'div.add-row a',function() {
        setTimeout(function(){ garb_select()}, 200);
    });
    garb_select();

    $('input').on("keyup", function (e) {
        if ($(this).parents( ".form-row" ).hasClass('is-invalid') ) {
            $(this).parents( ".form-row" ).removeClass('is-invalid');
        }
    });

    $('input').on("keyup", function () {
        if ($(this).hasClass('is-invalid') ) {
            $(this).removeClass('is-invalid');
        }
    });
    
    $('.dropdown-toggle').on("click", function () {
        if ($(this).parents( ".form-row" ).hasClass('is-invalid') ) {
            $(this).parents( ".form-row" ).removeClass('is-invalid');
        }
    });
    
    $('.dropdown-toggle').on("click", function () {
        if ($(this).parents(".select").find('select').hasClass('is-invalid') ) {
            $(this).parents(".select").find('select').removeClass('is-invalid');
            $(this).parents(".form-group").find('.invalid-feedback').remove();
        }
    });

    if(document.forms[0] != 'undefined') {
        var form = $('form');
        var initialState = form.serialize();
        $(".btn-verify-form").click(function(e) {
            if (initialState !== form.serialize()) {
                e.preventDefault();
                alert('Precisa salvar antes!');
            }
        });
    }

})(jQuery);
