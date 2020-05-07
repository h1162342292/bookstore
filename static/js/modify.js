$(function () {

    var error_pwd = false;
    var error_cpwd = false;



    $('#pwd').blur(function () {
        check_pwd();
    });

    $('#cpwd').blur(function () {
        check_cpwd();
    });






    function check_pwd() {
        var len = $('#pwd').val().length;
        if (len < 6 ) {
            $('#pwd').next().html('密码不能少于六位')
            $('#pwd').next().show();
            error_name = true;
            return;
        }
        else {
            $('#pwd').next().hide();
            error_name = false;
        }

    }

    function check_cpwd() {
        var pwd = $('#pwd').val();
        var cpwd = $('#cpwd').val();
        if (pwd!=cpwd) {
            $('#cpwd').next().html('密码不一致');
            $('#cpwd').next().show();
            error_password = true;
        }
        else {
            $('#cpwd').next().hide();
            error_password = false;
        }
    }





    $('#login_form').submit(function () {
        check_pwd();
        check_cpwd();


        if (error_pwd == false && error_cpwd == false) {
            return true;
        }
        else {
            return false;
        }

    });


})