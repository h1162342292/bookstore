$(function () {

    var error_name = false;
    var error_password = false;



    $('#user_name').blur(function () {
        check_user_name();
    });

    $('#pwd').blur(function () {
        check_pwd();
    });






    function check_user_name() {
        var len = $('#user_name').val().length;
        if (len < 5 || len > 20) {
            $('#user_name').next().html('请输入5-20个字符的用户名')
            $('#user_name').next().show();
            error_name = true;
            return;
        }
        else {
            $('#user_name').next().hide();
            error_name = false;
        }

    }

    function check_pwd() {
        var len = $('#pwd').val().length;
        if (len < 8 || len > 20) {
            $('#pwd').next().html('密码最少8位，最长20位')
            $('#pwd').next().show();
            error_password = true;
        }
        else {
            $('#pwd').next().hide();
            error_password = false;
        }
    }





    $('#login_form').submit(function () {
        check_user_name();
        check_pwd();


        if (error_name == false && error_password == false) {
            return true;
        }
        else {
            return false;
        }

    });


})