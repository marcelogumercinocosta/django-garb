function viewMonitoramento() {
    let storage_var = $('#view_monitoramento').attr('data-name')
    let view_monitoramento = sessionStorage.getItem(storage_var)
    if ((view_monitoramento == 0) || (view_monitoramento == null)) {
        $(".headerlogin").show();
        $("aside").show();
        $('#view_monitoramento').html('<i class="fa fa-eye fa-lg p-1"></i>');
        $('.breadcrumbs').removeClass("d-flex justify-content-end");
    } else {
        $(".headerlogin").hide();
        $("aside").hide();
        $('#view_monitoramento').html('<i class="fa fa-eye-slash fa-lg p-1"></i>');
        $('.breadcrumbs').addClass( "d-flex justify-content-end");
    }
}

$('#view_monitoramento').on('click', function(){
    let storage_var = $('#view_monitoramento').attr('data-name')
    let view_monitoramento = sessionStorage.getItem(storage_var)
    if (view_monitoramento == 1) {
        sessionStorage.setItem(storage_var, 0);
    } else {
        sessionStorage.setItem(storage_var, 1);
    }
    viewMonitoramento()
});


viewMonitoramento()