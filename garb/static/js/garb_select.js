(function ($) {
    // SELECTPICKER DATA-API
    // =====================
    function garb_select() { 
        $('select').each(function () {
            var selectElement = $(this).attr("id").split('-');
            if ( ! $('select').attr("multiple") && (selectElement[1] !== '__prefix__')) {
                $.fn.selectpicker.Constructor.DEFAULTS.styleBase = null;
                $.fn.selectpicker.Constructor.DEFAULTS.noneSelectedText = '---------'
                $(this).selectpicker();
            }
        });
    } 
    $(document).on("mousedown",'.add-row td a',function() {
        setTimeout(function(){ garb_select()}, 100);
    });
    garb_select();
})(jQuery);
