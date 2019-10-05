user_success = [{"user": "18684720553", "pwd": "python", "expected": "我的帐户[小小鸟]"}]



user_error = [
    {"user": "", "pwd": "", "expected": "请输入手机号"},
    {"user": "135", "pwd": "", "expected": "请输入正确的手机号"},
    {"user": "13423456789", "pwd": "", "expected": "请输入密码"}
]

user_error_shouquan = [
    {"user": "13423456789", "pwd": "123", "expected": "此账号没有经过授权，请联系管理员!"}
]