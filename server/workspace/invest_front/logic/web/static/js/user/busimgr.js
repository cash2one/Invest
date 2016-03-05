$(document).ready(function() {
	var announcement = getcookie('announcement__2');
	if(announcement==null || announcement=='') {
		$("#announcement").fadeIn("slow");
	}
});
function applyinfo(id, name) {
	window.top.art.dialog({id:'info'}).close();
	window.top.art.dialog(
        {
            title:'贷款申请 《'+name+'》',id:'info',iframe:'?m=loan&c=index&a=applyinfo&id='+id,width:'700',height:'460'
        },
        function(){
            var d = window.top.art.dialog({id:'info'}).data.iframe;d.document.getElementById('dosubmit').click();
            return false;},
        function(){
            window.top.art.dialog({id:'info'}).close()
        }
    );
}
