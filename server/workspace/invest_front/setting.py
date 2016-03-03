# coding=utf-8
"""
Created on 2015-4-22

@author: Jay
"""
from invest_setting import *

SERVICE_TYPE = ST_INVEST_FRONT
VERSION = "0.0.1"

# 导航栏名字ID列表
LOAN_NAV_BAR_ID_LS = [
    # index
    LBL_ROOT,
    LBL_KNOWLEDGE,
    LBL_CASE,
    LBL_PROBLEM,
    LBL_LOGIN,

    # about
    LBL_ABOUT,
    LBL_CONTACT,
    LBL_COOPERATION,
    LBL_RECRUIT
] = xrange(0, 9)

# INDEX导航栏详细信息列表
INDEX_NAV_BAR_DIC = {
    # index
    LBL_ROOT:       {"idx": 0, "des": "首页",     "url": "/",                "html": "/index/index.html"},
    LBL_KNOWLEDGE:  {"idx": 1, "des": "贷款攻略", "url": "/knowledge",        "html": "/util/list.html"},
    LBL_CASE:       {"idx": 2, "des": "贷款案例", "url": "/case",             "html": "/util/list.html"},
    LBL_PROBLEM:    {"idx": 3, "des": "常见问题", "url": "/problem",          "html": "/util/list.html"},
    LBL_ABOUT:      {"idx": 4, "des": "关于宏圆", "url": "/about",            "html": "/about/about.html"},
    LBL_LOGIN:      {"idx": 5, "des": "经理登录", "url": "/login",            "html": "/login/login.html"},
}

# ABOUT导航栏详细信息列表
ABOUT_NAV_BAR_DIC = {
    LBL_ABOUT:      {"idx": 0, "des": "关于我们", "url": "/about",            "html": "/about/about.html"},
    LBL_CONTACT:    {"idx": 1, "des": "联系我们", "url": "/about/contact",     "html": "/about/contact.html"},
    LBL_COOPERATION:{"idx": 2, "des": "商务合作", "url": "/about/cooperation", "html": "/about/cooperation.html"},
    LBL_RECRUIT:    {"idx": 3, "des": "招贤纳士", "url": "/about/recruit",     "html": "/about/recruit.html"},
}

LOAN_NAV_BAR_DIC = {}
LOAN_NAV_BAR_DIC.update(INDEX_NAV_BAR_DIC)
LOAN_NAV_BAR_DIC.update(ABOUT_NAV_BAR_DIC)

# 贷款产品链接
LOAN_PRODUCT_DIC = {
    LP_HOUSE_MORTGAGE:   {"id": LP_HOUSE_MORTGAGE,   "idx": 0,  "title": "房产抵押贷款",    "color": "#FF3300", "sub_title": "让房产变成提款机",   "des": "最高可贷5000万 | 最长可贷10年 | 可用于经营或消费", "img": "/static/images/index/lp/lp_hm.png"},
    LP_CAR_OWN_MORTGAGE: {"id": LP_CAR_OWN_MORTGAGE, "idx": 1,  "title": "汽车抵押贷款",    "color": "#669933", "sub_title": "钱借到，车照开",     "des": "最高可贷50万 | 最长可贷3年 | 可用于经营或消费",    "img": "/static/images/index/lp/lp_com.png"},
    LP_NEW_NOT_MORTGAGE: {"id": LP_NEW_NOT_MORTGAGE, "idx": 2,  "title": "新一贷无抵押贷款","color": "#009966", "sub_title": "无需抵押担保，期限长", "des": "最高可贷50万 | 最长可贷4年 | 可用于经营或消费",    "img": "/static/images/index/lp/lp_nnm.png"},
    LP_XIAMEN_PRI_LOAN:  {"id": LP_XIAMEN_PRI_LOAN,  "idx": 3,  "title": "厦门私借",       "color": "#009966", "sub_title": "个人私借： 当天放款", "des": "最高可贷500万 | 最长可贷1年 | 可用于经营或消费",   "img": "/static/images/index/lp/lp_xpl.png"},
    LP_CAR_USE_MORTGAGE: {"id": LP_CAR_USE_MORTGAGE, "idx": 4,  "title": "车抵贷(押车)",   "color": "#993300", "sub_title": "车抵贷（押车）",      "des": "最高可贷500万 | 最长可贷4年 | 可用于经营或消费",   "img": "/static/images/index/lp/lp_cum.png"},
    LP_INSURANCE_LOAN:   {"id": LP_INSURANCE_LOAN,   "idx": 5,  "title": "保险保单贷款",    "color": "#FF9900", "sub_title": "有保险保单就能贷款",  "des": "最高50万 | 最长合同4年 | 保费30倍",             "img": "/static/images/index/lp/lp_il.png"},
}
for dic in LOAN_PRODUCT_DIC.values():
    dic["url"] = "/loan_product?lp_type=%s" % dic['idx']

# 首页动画列表
LOAN_ANI_LS =[
    {"id":LP_HOUSE_MORTGAGE,   "img": "/static/images/index/ani_hm.jpg"},
    {"id":LP_CAR_OWN_MORTGAGE, "img": "/static/images/index/ani_cm.jpg"}
]
for dic in LOAN_ANI_LS:
    dic['url'] = LOAN_PRODUCT_DIC[dic['id']]['url']
    dic['title'] = LOAN_PRODUCT_DIC[dic['id']]['title']

# 贷款优势
LOAN_ADV_LS = [
    {"title": "门槛", "sub_title": "低", "des": "月收入4000元即可申请", "img": "/static/images/index/la/la_1.png"},
    {"title": "额度", "sub_title": "大", "des": "最高借款额度达50万元", "img": "/static/images/index/la/la_2.png"},
    {"title": "放款", "sub_title": "快", "des": "3个工作日内即可审核完成", "img": "/static/images/index/la/la_3.png"},
    {"title": "利息", "sub_title": "低", "des": "月综合费率低至0.58%", "img": "/static/images/index/la/la_4.png"},
]


# 贷款业务链接
LOAN_BUSINESS_DIC = {
    LB_PINGAN_XINYI_DAI:        {"id": LB_PINGAN_XINYI_DAI,        "idx": 0, "title": "平安新一贷", "des": "平安新一贷是一款什么产品？新一贷是平安银行向拥有连续稳定工资收入的受薪人士或连续稳定经营收入的自...", "img": "/static/images/index/lb/lb_paxyd.jpg"},
    LB_SMALL_PRIVATE_CONSUME:   {"id": LB_SMALL_PRIVATE_CONSUME,   "idx": 1, "title": "个人小额消费贷款", "des": "应急现金？提高生活质量？个人进修？医疗急用？购物&hellip;&hellip;通过平安产险购买平安易贷险，即可凭保单助您轻...", "img": "/static/images/index/lb/lb_spc.jpg"},
    LB_HOUSE_MORTGAGE_CONSUME:  {"id": LB_HOUSE_MORTGAGE_CONSUME,  "idx": 2, "title": "房产抵押消费", "des": "平安银行房产抵押消费贷款，让房产变成提款机！高金额金额最高可达房产价值的75%。用途广装修、购铺、买...", "img": "/static/images/index/lb/lb_hmc.jpg"},
    LB_SECOND_HAND_HOUSE_LOAN:  {"id": LB_SECOND_HAND_HOUSE_LOAN,  "idx": 3, "title": "二手房贷款", "des": "平安银行二手房贷款，圆您安居梦想！利息省超低利率，实惠划算。金额高贷款成数高至7成，轻松购房。期限...", "img": "/static/images/index/lb/lb_shhl.jpg"},
    LB_FIRST_HAND_HOUSE_LOAN:   {"id": LB_FIRST_HAND_HOUSE_LOAN,   "idx": 4, "title": "一手房贷款", "des": "平安银行一手房贷款，圆您安居梦想！利息省超低利率，实惠划算。金额高贷款成数高至7成，轻松购房。期限...", "img": "/static/images/index/lb/lb_fhhl.jpg"},
    LB_CAR_MORTGAGE_HOUSE_LOAN: {"id": LB_CAR_MORTGAGE_HOUSE_LOAN, "idx": 5, "title": "汽车抵押贷款", "des": "产品概述抵押车辆获取贷款，用于消费和经营，采用等额本息或等额本金的还款方式。产品特色▪ 车辆照开...", "img": "/static/images/index/lb/lb_cmhl.jpg"},
}
for dic in LOAN_BUSINESS_DIC.values():
    dic["url"] = "/loan_business?lb_type=%s" % dic['idx']

# 贷款常识链接
LOAN_KNOWLEDAGE_LS = [
    {"text": "• 赚钱之道：用银行的钱生钱之7招锦囊", "date": "2016-03-02"},
    {"text": "• 提高审批通过率 可在贷款申请表上觅良机", "date": "2016-03-02"},
    {"text": "• 企业申请银行贷款 将面临3种背景调查", "date": "2016-03-02"},
    {"text": "• 追寻大额无抵押贷款你应把握3大技巧", "date": "2016-03-02"},
    {"text": "• 无抵押贷款：3类人易斩过银行审批关", "date": "2016-03-02"},
]

for idx, dic in enumerate(LOAN_KNOWLEDAGE_LS):
    dic["url"] = "%s?id=%s" % (LOAN_NAV_BAR_DIC[LBL_KNOWLEDGE]['url'], idx)
    dic["more_url"] = LOAN_NAV_BAR_DIC[LBL_KNOWLEDGE]['url']
    dic['idx'] = idx


# 贷款案例链接
LOAN_CASE_LS = [
    {"text": "• 【案例分享】汽车抵押贷款为新婚夫妇提", "otext": "• 【案例分享】汽车抵押贷款为新婚夫妇提供婚庆资金"},
    {"text": "• 【案例分享】汽车抵押贷款为女士个人消", "otext": "• 【案例分享】汽车抵押贷款为女士个人消费提供帮助"},
    {"text": "• 【案例分享】汽车抵押贷款可以提供原材", "otext": "• 【案例分享】汽车抵押贷款可以提供原材料进购资金"},
    {"text": "• 【案例分享】平安银行车抵贷让您圆梦  ", "otext": "• 【案例分享】平安银行车抵贷让您圆梦"},
    {"text": "• 【案例分享】平安车抵贷帮您解决淘宝卖", "otext": "• 【案例分享】平安车抵贷帮您解决淘宝卖家快递费"},
]

for idx, dic in enumerate(LOAN_CASE_LS):
    dic["url"] = "%s?id=%s" % (LOAN_NAV_BAR_DIC[LBL_CASE]['url'], idx)
    dic["more_url"] = LOAN_NAV_BAR_DIC[LBL_CASE]['url']
    dic['idx'] = idx


# 常见问题
LOAN_PROBLEM_LS=[
    {"text": "• 我的情况能否申请创业贴息贷款？"},
    {"text": "• 想要开店，是否能申请贷款"},
    {"text": "• 什么是二次抵押?"},
    {"text": "• 所有的二手房都能办抵押贷款吗？"},
    {"text": "• 个人信息遭泄露该如何维权？"},
]

for idx, dic in enumerate(LOAN_PROBLEM_LS):
    dic["url"] = "%s?id=%s" % (LOAN_NAV_BAR_DIC[LBL_PROBLEM]['url'], idx)
    dic["more_url"] = LOAN_NAV_BAR_DIC[LBL_PROBLEM]['url']
    dic['idx'] = idx

# 职位信息
RECRUIT_LS = [
    {"job_name": "信用管理专员",
     "duty_detail_ls": ["1. 审核贷款申请人资料是否齐全以及真实性；",
                        "2. 按照要求对贷款申请人进行调查，分析审核贷款人资信条件，撰写调查报告；",
                        "3. 与其他部门同事合作，完善核审流程，加强信用管理，降低风险及信贷损失；",
                        "4. 在工作中积极提出自己的意见和建议，优化工作流程。"
                        ],
     "req_detail_ls": ["1. 营销、管理、金融、经济等相关专业本科或以上学历；",
                       "2. 2年以上工作经验，有信贷、担保相关工作经验者优先考虑；",
                       "3. 工作主动负责，认真仔细，勤勉敬业，善于沟通，有较强的客户服务意识；",
                       "4. 具有良好的客户沟通、人际交往及维系客户关系的能力；",
                       "5. 能很快的学习新事物和新知识；",
                       "6. 思维敏捷，具备创造性市场开拓的能力；",
                       "7. 诚实守信，为人谦虚、正直，性格开朗，责任心强，具有高度的团队合作精神和高度的工作热情：",
                       "8. 有强烈的创业意识，愿与公司一同成长。",
                       ],
     "address_detail": "厦门、福州、漳州、龙岩、三明",
     },
    {"job_name": "客户理财顾问",
     "duty_detail_ls": ["1. 根据公司产品特点，以电话方式进行潜在客户的开发，为客户建立、提供专业的资产管理咨询服务；",
                        "2. 根据业务要求，定期做客户回访，做好老客户维护和在开发，主动、积极地为客户提供各类理财产品；",
                        "3. 完成销售经理制定的销售目标；",
                        "4. 根据销售经理的要求按时保质的完成销售报告；",
                        "5. 根据一线工作了解到的客户反馈，向公司提出产品及流程优化建议。"
                        ],
     "req_detail_ls": ["1. 专科或以上学历，营销、管理、金融等专业优先考虑；",
                       "2. 1年以上工作经验，有银行理财产品经验优先考虑；",
                       "3. 具有良好的客户沟通、人际交往及维系客户关系的能力；",
                       "4. 能够有效开发客户资源；",
                       "5. 诚实守信，为人谦虚、勤奋努力，具有高度的团队合作精神和高度的工作热情。",
                       ],
     "address_detail": "厦门、福州、漳州、龙岩、三明",
     },
    {"job_name": "贵宾理财经理",
     "duty_detail_ls": ["1. 根据公司产品特点，进行潜在客户的开发，为客户建立、提供专业的资产管理咨询服务；",
                        "2. 负责贵宾客户维护提升工作，为贵宾客户提供专业化的理财服务等工作；",
                        "3. 完成销售经理制定的销售目标；",
                        "4. 根据销售经理的要求按时保质的完成销售报告；",
                        "5. 管理营销团队，与销售经理一起做好营销团队的管理工作，并定期向销售经理汇报；",
                        "6. 根据一线工作了解到的客户反馈，向公司提出产品及流程优化建议。"
                        ],
     "req_detail_ls": ["1. 本科或以上学历，营销、管理、金融等专业优先考虑；",
                       "2. 2年以上工作经验，有银行理财产品经验优先考虑；",
                       "3. 具有良好的客户沟通、人际交往及维系客户关系的能力；",
                       "4. 具有敏锐的市场洞察力和准确的客户分析能力，能够有效开发客户资源；",
                       "5. 强烈的时间观念和服务意识，灵活熟练的谈判技巧；",
                       "6. 有广泛的社会关系网络和客户人脉资源，具有开发大客户经验者优先；",
                       "7. 诚实守信，为人谦虚、勤奋努力，具有高度的团队合作精神和高度的工作热情。"
                       ],
     "address_detail": "厦门、福州、漳州、龙岩、三明",
     },
    {"job_name": "个贷直销",
     "duty_detail_ls": ["1. 负责个人信用贷款产品的营销推广及客户关系维护；",
                        "2. 完成公司及部门经理分配的销售任务；",
                        "3. 完成销售报告，并向公司及部门负责人做工作汇报；",
                        "4. 根据一线工作了解到的客户反馈，向公司提出产品及流程优化建议。",
                        ],
     "req_detail_ls": ["1. 大学专科以上学历，营销、管理、金融等专业优先考虑;",
                       "2. 1年以上工作经验，有银行信用卡、消费贷款等相关金融信贷产品推广工作经验者优先考虑；",
                       "3. 具有良好的客户沟通、人际交往及维系客户关系的能力；",
                       "4. 能够有效开发客户资源；",
                       "5. 勤奋努力，具有吃苦耐劳以达成工作目标的毅力和决心；",
                       "6. 诚实守信，为人谦虚、具有高度的团队合作精神和高度的工作热情。",
                       ],
     "address_detail": "厦门、福州、漳州、龙岩、三明",
     }
]