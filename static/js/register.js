$(function () {
    var error_name = false;
    var error_pwd = false;
    var error_cpwd = false;
    var error_phone = false;
    var error_email = false;
    var error_check = false;
   $('#allow').click(
       function () {
           if ($(this).is(':checked')){
                error_check = false;
                $(this).siblings('span').hide();
           }
           else{
               error_check = true;
               $(this).siblings('span').html('请勾选同意');
               $(this).siblings('span').show();
           }
       }
   )
    $('#user_name').blur(function () {
        user_name();
    });
    $('#pwd').blur(function () {
        user_pwd();
    })
    $('#cpwd').blur(
        function () {
            user_cpwd();
        }
    )
    $('#phone').blur(
        function () {
            user_phone();
        }
    )
    $('#email').blur(
        function () {
            user_email();
            
        }
    )
    function user_name() {
        var len =$('#user_name').val().length;//val() 方法返回或设置被选元素的值，多用于input元素。
        if (len<5 || len>20){
            $('#user_name').next().html('请输入5-20个字符的用户名');
            $('#user_name').next().show();//将上面的提示信息显示出来
            error_name = true;
            return;
        }
        else {
            $('#user_name').next().hide();//表示同级的下一个元素，也就是提示信息<span>标签
            error_name =false;
        }
        var username = $('#user_name').val();
        $.getJSON('/user/check_user',{
            username:username
        },function (data) {
            if(data.msg == 'success'){
                error_name = false;
            }
            else {
                error_name = true;
            }
            $('#user_name').next().html(data.msg);
            $('#user_name').next().show();
        });
    }
    function user_pwd() {
        var len = $('#pwd').val().length;
        if(len<6){
            $('#pwd').next().html('密码不能少于六位');
            $('#pwd').next().show();
            error_pwd = true;
        }
        else {
            $('#pwd').next().hide();
            error_pwd = false;
        }
    }
    function user_cpwd() {
        var pwd = $('#pwd').val();
        var cpwd = $('#cpwd').val();
        if(pwd!=cpwd){
            $('#cpwd').next().html('密码不一致');
            $('#cpwd').next().show();
            error_cpwd = true;
        }
        else {
            $('#cpwd').next().hide();
            error_cpwd = false;
        }
    }
    function user_phone() {
        var phone = $('#phone').val().length;
        if (phone!=11){
             $('#phone').next().html('请输入正确的手机号(11位)');
            $('#phone').next().show();
            error_phone = true;
        }
        else {
            error_phone = false;
        }
    }
    function user_email() {
        var re = /^[a-z0-9][\w\.\-]*@[a-z0-9\-]+(\.[a-z]{2,5}){1,2}$/;
        if (re.test($('#email').val())) {
            $('#email').next().hide();
            error_email = false;
        }
        else {
            $('#email').next().html('你输入的邮箱格式不正确')
            $('#email').next().show();
            error_email = true;
        }
    }
    $('#reg_form').submit(function () {
        user_name();
        user_pwd();
        user_cpwd();
        user_email();
        user_phone();
          if (error_name == false && error_pwd == false && error_cpwd == false && error_email == false && error_check == false && error_phone == false) {
            return true;
        }
        else {
            return false;
        }

    });
})