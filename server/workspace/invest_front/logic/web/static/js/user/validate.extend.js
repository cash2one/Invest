/**
 * Created by Administrator on 2015/2/10 0010.
 */
/**
 *
 */

$(function() {
    /**
     * jQuery.validator 验证增加手机验证方法
     */
    jQuery.validator.addMethod("mobilecheck", function(value, element) {   //添加phonecheck方法，来自定义check规则
        string = value.match(/^(1)[0-9]{10}$/);
        if(string != null){
            return true;
        }else{
            return false;
        }
    }, "请输如11位手机号码");

    /**
     * jQuery.validator 验证增加异步验证手机方法
     */
    jQuery.validator.addMethod("mobileajax", function(value, element, params) {   //添加phonecheck方法，来自定义check规则
        var ok = '';
        $.ajax({
            url: params, //验证页面，存在输入1，不存在输出0，不要输出其他的内容
            data: 'mobile=' + encodeURIComponent(value),
            async: false, /////////关键，设置为同步
            type: 'POST',
            dataType: 'text',
            success: function (data) {
                data = parseInt(data);
                ok = data == 1 ? true : false;
            },
            error: function (xhr) {
                alert('动态网页有问题！\n' + xhr.responseText);
                ok = false;
            }
        });
        return ok;
    }, "手机已存在");

	/**
     * jQuery.validator 验证增加中文=
     */
    jQuery.validator.addMethod("cncheck", function(value, element, params) {   //添加phonecheck方法，来自定义check规则
        string = /^[\u4E00-\u9FA5]+$/;
        if (value.length >= 2 && string.test(value)) {
            return true;
        }else{
            return false;
        }
    }, "请输入验证码");

	 /**
     * jQuery.validator 验证增加异步验证手机方法
     */
    jQuery.validator.addMethod("usernamecheck", function(value, element, params) {   //添加phonecheck方法，来自定义check规则
        var ok = '';
        $.ajax({
            url: params, //验证页面，存在输入1，不存在输出0，不要输出其他的内容
            data: 'username=' + encodeURIComponent(value),
            async: false, /////////关键，设置为同步
            type: 'GET',
            dataType: 'text',
            success: function (data) {
                data = parseInt(data);
                ok = data == 1 ? true : false;
            },
            error: function (xhr) {
                alert('动态网页有问题！\n' + xhr.responseText);
                ok = false;
            }
        });
        return ok;
    }, "用户名已注册");

	jQuery.validator.addMethod("usernameischeck", function(value, element, params) {   //添加phonecheck方法，来自定义check规则
        var ok = '';
        $.ajax({
            url: params, //验证页面，存在输入1，不存在输出0，不要输出其他的内容
            data: 'username=' + encodeURIComponent(value),
            async: false, /////////关键，设置为同步
            type: 'GET',
            dataType: 'text',
            success: function (data) {
                data = parseInt(data);
                ok = data == 0 ? false : true;
            },
            error: function (xhr) {
                alert('动态网页有问题！\n' + xhr.responseText);
                ok = false;
            }
        });
        return ok;
    }, "用户名已注册");

});