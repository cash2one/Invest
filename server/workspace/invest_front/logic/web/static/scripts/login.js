/**
 * Created by Administrator on 2016-3-4.
 */

$(function() {
	$('#myform').validate({
	rules: {
		username : {
			required : true,
			rangelength : [4,16],
			usernameischeck : '/is_username_exist'
			},
		password : {
			required : true,
			rangelength : [6,16]
			}
		},
    	messages: {
    		username : {
				required : "请输入用户名",
				rangelength : "用户名长度是4-16",
				usernameischeck : "用户名不存在,请注册"
        	},
        	password : {
				required : "请输入您的登录密码",
				rangelength : "密码长度必须再6-16位之间"
			}
		},
    	highlight: function (element) {
        	$(element).addClass('hasError');
    	},
    	success : function (element){
			$(element).removeClass('hasError');
    	},
		errorPlacement: function(error, element) {
			error.appendTo(element.parent().parent());
		},
		errorElement : 'span',
		errorClass : 'tanwz4 tan'
	});
});