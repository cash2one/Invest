/**
 * 浼氬憳涓績鍏敤js
 *
 */

/**
 * 闅愯棌html element
 */
function hide_element(name) {
	$('#'+name+'').fadeOut("slow");
}

/**
 * 鏄剧ずhtml element
 */
function show_element(name) {
	$('#'+name+'').fadeIn("slow");
}

$(document).ready(function(){
銆€銆€$("input.input-text").blur(function () { this.className='input-text'; } );
銆€銆€$(":text").focus(function(){this.className='input-focus';});
});

/**
 * url璺宠浆
 */
function redirect(url) {
	if(url.indexOf('://') == -1 && url.substr(0, 1) != '/' && url.substr(0, 1) != '?') url = $('base').attr('href')+url;
	location.href = url;
}


function thumb_images(uploadid,returnid) {
	var d = window.top.art.dialog({id:uploadid}).data.iframe;
	var in_content = d.$("#att-status").html().substring(1);
	if(in_content=='') return false;
	if($('#'+returnid+'_preview').attr('src')) {
		$('#'+returnid+'_preview').attr('src',in_content);
	}
	$('#'+returnid).val(in_content);
}
function change_images(uploadid,returnid){
	var d = window.top.art.dialog({id:uploadid}).data.iframe;
	var in_content = d.$("#att-status").html().substring(1);
	var str = $('#'+returnid).html();
	var contents = in_content.split('|');
	$('#'+returnid+'_tips').css('display','none');
	$.each( contents, function(i, n) {
		var ids = parseInt(Math.random() * 10000 + 10*i);
		str += "<div id='image"+ids+"'><input type='text' name='"+returnid+"_url[]' value='"+n+"' style='width:360px;' ondblclick='image_priview(this.value);' class='input-text'> <input type='text' name='"+returnid+"_alt[]' value='鍥剧墖璇存槑"+(i+1)+"' style='width:100px;' class='input-text' onfocus=\"if(this.value == this.defaultValue) this.value = ''\" onblur=\"if(this.value.replace(' ','') == '') this.value = this.defaultValue;\"> <a href=\"javascript:remove_div('image"+ids+"')\">绉婚櫎</a> </div><div class='bk10'></div>";
		});
	$('#'+returnid).html(str);
}
function image_priview(img) {
	window.top.art.dialog({title:'鍥剧墖鏌ョ湅',fixed:true, content:'<img src="'+img+'" />',id:'image_priview',time:5});
}

function remove_div(id) {
	$('#'+id).html(' ');
}

function select_catids() {
	$('#addbutton').attr('disabled',false);

}

//鍟嗕笟鐢ㄦ埛浼氭坊鍔? num锛屾櫘閫氱敤鎴烽粯璁や负5
function transact(update,fromfiled,tofiled, num) {
	if(update=='delete') {
		var fieldvalue = $('#'+tofiled).val();

		$("#"+tofiled+" option").each(function() {
		   if($(this).val() == fieldvalue){
			$(this).remove();
		   }
		});
	} else {
		var fieldvalue = $('#'+fromfiled).val();
		var have_exists = 0;
		var len = $("#"+tofiled+" option").size();
		if(len>=num) {
			alert('鏈€澶氭坊鍔? '+num+' 椤?');
			return false;
		}
		$("#"+tofiled+" option").each(function() {
		   if($(this).val() == fieldvalue){
			have_exists = 1;
			alert('宸茬粡娣诲姞鍒板垪琛ㄤ腑');
			return false;
		   }
		});
		if(have_exists==0) {
			obj = $('#'+fromfiled+' option:selected');
			text = obj.text();
			text = text.replace('鈹?', '');
			text = text.replace('鈹? ', '');
			text = text.replace('鈹? ', '');
			text = text.trim();
			fieldvalue = "<option value='"+fieldvalue+"'>"+text+"</option>"
			$('#'+tofiled).append(fieldvalue);
			$('#deletebutton').attr('disabled','');
		}
	}
}

function omnipotent(id,linkurl,title,close_type,w,h) {
	if(!w) w=700;
	if(!h) h=500;
	art.dialog({id:id,iframe:linkurl, title:title, width:w, height:h, lock:true},
	function(){
		if(close_type==1) {
			art.dialog({id:id}).close()
		} else {
			var d = art.dialog({id:id}).data.iframe;
			var form = d.document.getElementById('dosubmit');form.click();
		}
		return false;
	},
	function(){
			art.dialog({id:id}).close()
	});void(0);
}

String.prototype.trim = function() {
	var str = this,
	whitespace = ' \n\r\t\f\x0b\xa0\u2000\u2001\u2002\u2003\u2004\u2005\u2006\u2007\u2008\u2009\u200a\u200b\u2028\u2029\u3000';
	for (var i = 0,len = str.length; i < len; i++) {
		if (whitespace.indexOf(str.charAt(i)) === -1) {
			str = str.substring(i);
			break;
		}
	}
	for (i = str.length - 1; i >= 0; i--) {
		if (whitespace.indexOf(str.charAt(i)) === -1) {
			str = str.substring(0, i + 1);
			break;
		}
	}
	return whitespace.indexOf(str.charAt(0)) === -1 ? str : '';
}