# 数据库设计

*  login 登陆用的表

| 字段      |     数据类型|   示例| 描述|
| -------- | --------| ------ |-------|
| user_id|   varchar|  woshiyigenicheng|登陆时的用户名（key）,可以根据此字段寻找user_info的phone_number登陆|
| password| varchar| asd212;',aqddq'asd1+L|密码字段|


* user_info 用户基本信息

| 字段      |     数据类型|   示例| 描述|
| -------- | --------| ------ |-------|
| user_info| varchar  |  woshiyigenicheng|用户名|
|phone_number|varchar(11)|13012341234| 电话号码
|phone_number_checked| int| 1234| 手机验证码,每次手机验证时刷新|
|is_face_checked| tinyint(1)| 1(成功)0(失败)| 是否进行人脸识别|
|is_identify_checked| tinyint(1)| 1(成功)0(失败)| 是否进行身份证识别|
|work_info|varchar|深圳腾讯公司总部|工作信息|
|address|varchar|深圳腾讯公司总部旁边的小区|地址信息|
|emergency_contact|varchar|13012341235|紧急联系人号码|
|credit_number| int|100|信用积分|

* band_card_info 银行卡信息

| 字段      |     数据类型|   示例| 描述|
| -------- | --------| ------ |-------|
| user_id|   varchar|   woshiyigenicheng|用户名|
|bank_card_number|char(19)|6222123412341234123|银行卡信息|
|description|varchar|我的小金库|银行卡的描述|



* loan_info 借款信息(每次发布一个借款生成一个)

| 字段      |     数据类型|   示例| 描述|
| -------- | --------| ------ |-------|
| loan_id|   int|  1001|借款记录的id号|
|user_id| varchar|woshiyigenicheng|贷款人的id号|
|create_date|date|2017-08-29|创建借款记录的日期|
|load_money|int|100000|借款的金额|
|remain_money|int|200|还差的金额|
|bid_valide_period|int|20|标的有效期 单位：天|
|load_duration|int|3| 借款期限 单位：月|
|rate|double|0.03| 利率 单位%|
|borrow_style|tinyint(1)|0|借款方式 0:极速 1:散标|
|usage|varchar|我不是非法集资|借款原因|
|repay_style|tinyint(1)|0|还款方式 0：一次性 1：分期|
|state|tinyint|2| 借款状态 0：接标中 1：接标完成 2：被取消/失效|

* repay_info 每个用户投一次钱更新一条(不管标最终是否中)

| 字段      |     数据类型|   示例| 描述|
| -------- | --------| ------ |-------|
| repay_id|   int|  1005  |还款信息的id|
|loan_id|int|1001|还款记录对应的借款记录id号|
|repay_user_id|varchar|woshiyigejiekuanren|借款人的用户名|
|state|tinyint|1|借款信息 0:标还没开始 1：标失效 2：正在偿还 3：逾期未还|
|repay_total|double|200.08|需要一共偿还的钱|
|remain_money|double|19.88|还剩多少钱没有偿还|
|next_date|date|2019—08-29|下一个还款日期|
|next_repay_money|double|19.88|下次要偿还多少钱|
|overdue_days|int|10|超期多少天（state为3时）|
* credit_change 记录信用变化

| 字段      |     数据类型|   示例| 描述|
| -------- | --------| ------ |-------|
| id|   int|  1003|记录信息的id|
|user_id|varchar|woshiyigenicheng|信用变化的用户名|
|description|varchar|添加信用报告|信用记录变化的原因|
|change|double| 3|信用积分变化的数值（可为负数）|
|date|datatime|2017-08-29 15:37:00|创建时间|
