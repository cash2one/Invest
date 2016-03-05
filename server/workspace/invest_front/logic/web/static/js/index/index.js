/**
 * Created by Administrator on 2016-3-1.
 */


$(function(){
	$("#kinMaxShow").kinMaxShow({
        //���ý���ͼ�߶�(��λ:����) �������� ����ʹ��Ĭ��ֵ 500
        height:330,
        //���ý���ͼ ��ťЧ��
        button:{
            //���ð�ť���治��ʾ��������(Ĭ��Ҳ�ǲ���ʾ����)
            showIndex:false,
            //��ť������ ��ʽ���� ��cssд��������jQuery�� $('xxx').css({key:value,����})��cssд����
            //��������ʾ����������͸����Ŷ ������������� ͳһΪ opacity��CSS3����Ҳ֧��Ŷ �磺���ð�ťԲ�ǡ�ͶӰ�ȣ�ֻ����IE8�����²�֧�֡�
            normal:{background:'url(/static/img/index/button.png) no-repeat -14px 0',marginRight:'8px',border:'0',right:'44%',bottom:'20px'},
            //��ǰ����ͼ��ť��ʽ ���ã�д��ͬ��
            focus:{background:'url(/static/img/index/button.png) no-repeat 0 0',border:'0'}
        }
        //����ͼ�л��ص���ÿ��ͼƬ���롢����������á����Ҵ���2������(index,action)��index ��ǰͼƬ���� 0Ϊ��һ��ͼƬ��action ���� ���� �г� ֵ:fadeIn��fadeOut
        //������ thisָ�� ��ǰͼƬ�������� ��������������Ԫ�ء������еĽ���ͼ������Ҫ���ǿ�callbackʵ�ֵġ�
    });
});