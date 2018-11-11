#### Setup API Test framework using your most comfortable tech stack
- 语言：python3.6
- 自动化框架：httprunner(unittest、requests)

#### The tests will run in different environments, so make the endpoint url configurable
- 编辑配置文件：`vim ./debugtalk.py`
- 修改 base_url

#### Tests should be able to run from command line
- run testcases: `hrun testcases/bank_t.yml` or `hrun testcases`
- 建议自己搭建接口自动化独立的web服务，方便持续集成
    - web框架：django
    - 分布式任务框架：celery
    - 暴露api，方便持续集成平台实时触发接口自动化
##### 原始需求
- 接口请求方式：POST
- 有一个字段接收传入银行所属的国家，且只支持：US、AU、CN
- 有一个字段接收传入支付方式，且仅支持：LOCAL 、SWIFT
- 有一个字段接收快捷支付代码
##### 接口设计
- method：POST
- Payload fields
    - payment_method：mandatory，(LOCAL | SWIFT)
    - bank_country_code:  mandatory，(US | AU | CN)
    - account_name:  mandatory，any character，1<length<11
    - account_number: mandatory,
        - US: 0<length<18，any character
        - AU: 5<length<10，any character
        - CN: 7<length<21，any character
    - swift_code：mandatory(SWIFT)
        - SWIFT：
            - swift_code[4:6] = bank_country_code
            - length = 8 or length =11
    - bsb：mandatory(AU)，length = 6
    - aba：mandatory(US)，length = 9
- response：
    - success：status_code：200
    - failed:：
        - account_number' is required
        - Length of account_number should be between 7 and 11 when bank_country_code is 'US'
        - The swift code is not valid for the given bank country code: US
        - Length of 'swift_code' should be either 8 or 11

#####测试用例
`用例参见脚本，先仅做初步覆盖`
##### 缺陷报告
`缺陷报告参见report，执行失败处均为bug，暂不而外记录`
