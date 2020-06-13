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
})(jQuery);
