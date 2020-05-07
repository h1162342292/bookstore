$(function () {

    var error_name = false;
    var error_password = false;



    $('#phone').blur(function () {
        check_phone();
    });

    $('#code').blur(function () {
        check_pwd();
    });






    function check_phone() {
        var len = $('#phone').val().length;
        if (len != 11) {
            $('#phone').next().html('请输入11位的手机号码')
            $('#phone').next().show();
            error_name = true;
            return;
        }
        else {
            $('#phone').next().hide();
            error_name = false;
        }

    }

    function check_pwd() {
        var len = $('#pwd').val().length;
        if (len != 4) {
            $('#pwd').next().html('必须输入验证码')
            $('#pwd').next().show();
            error_password = true;
        }
        else {
            $('#pwd').next().hide();
            error_password = false;
        }
    }





    // $('#login_form').submit(function () {
    //     check_phone();
    //     check_pwd();
    //
    //
    //     if (error_name == false && error_password == false) {
    //         return true;
    //     }
    //     else {
    //         return false;
    //     }
    //
    // });
    $('#btn_send').click(

        function () {

           var phone = $('#phone').val();
           check_phone();
           $.getJSON('/user/send',{'phone':phone},function (data) {
               alert(data.msg);
           });
        }
    );

})