/**
 * Created by Administrator on 2016-3-1.
 */


$(function(){
	$("#kinMaxShow").kinMaxShow({
        //设置焦点图高度(单位:像素) 必须设置 否则使用默认值 500
        height:330,
        //设置焦点图 按钮效果
        button:{
            //设置按钮上面不显示数字索引(默认也是不显示索引)
            showIndex:false,
            //按钮常规下 样式设置 ，css写法，类似jQuery的 $('xxx').css({key:value,……})中css写法。
            //【友情提示：可以设置透明度哦 不用区分浏览器 统一为 opacity，CSS3属性也支持哦 如：设置按钮圆角、投影等，只不过IE8及以下不支持】
            normal:{background:'url(/static/images/index/button.png) no-repeat -14px 0',marginRight:'8px',border:'0',right:'44%',bottom:'20px'},
            //当前焦点图按钮样式 设置，写法同上
            focus:{background:'url(/static/images/index/button.png) no-repeat 0 0',border:'0'}
        }
        //焦点图切换回调，每张图片淡入、淡出都会调用。并且传入2个参数(index,action)。index 当前图片索引 0为第一张图片，action 切入 或是 切出 值:fadeIn或fadeOut
        //函数内 this指向 当前图片容器对象 可用来操作里面元素。本例中的焦点图动画主要就是靠callback实现的。
    });
});