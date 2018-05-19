from flask_wtf import Form
from wtforms import StringField, validators


class RegistrationForm(Form):
    username = StringField('username', [validators.Length(min=2, max=18, message="请检查用户名长度是否在2~18之间")])
    password = StringField('password', [validators.Length(min=6, max=15, message="请检查用密码长度是否在6~15之间")])
    repassword = StringField('repassname', [validators.EqualTo("password", message="两次密码不一致!!!")])
    email = StringField('email', [validators.Email(message="非法邮箱地址")])

# 常用验证方法
# 验证函数       说　　明
# Email       验证电子邮件地址
# EqualTo     比较两个字段的值；常用于要求输入两次密码进行确认的情况
# IPAddress   验证 IPv4 网络地址
# Length      验证输入字符串的长度
# NumberRange 验证输入的值在数字范围内
# Optional    无输入值时跳过其他验证函数
# Required    确保字段中有数据
# Regexp      使用正则表达式验证输入值
# URL         验证 URL
# AnyOf       确保输入值在可选值列表中
# NoneOf      确保输入值不在可选值列表中
