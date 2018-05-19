from flask import Flask, render_template, request
from flask import redirect, url_for
from config.verify import RegistrationForm
from config.sql_manager import create_userinfo, found_userinfo
# from sql_manager import reset_userinfo, drop_userinfo
from flask_wtf import CSRFProtect
from config import csrf_config
app = Flask(__name__)

# 防止csrf攻击
app.config.from_object(csrf_config)
CSRFProtect(app)


# 简单的访问
@app.route('/login', methods=['GET', 'POST'])
def login():
    # csrf验证
    form = RegistrationForm(request.form)
    if request.method == "GET":
        return render_template("login.html", form=form)
    else:
        # 和数据库比对用户名密码
        print(form.username.data)
        userdata = found_userinfo(form.username.data)
        # print(userdata.username)
        if userdata:
            if userdata.password == form.password.data:
                return "欢迎:{}".format(userdata.username)
            else:
                form.password.errors = "密码错误!!!"
                return render_template("login.html", form=form)
        else:
            form.username.errors = "用户名不存在!!!"
            return render_template("login.html", form=form)


@app.route('/register', methods=['GET', 'POST'])
def register():
    # csrf验证
    form = RegistrationForm(request.form)
    if request.method == "GET":
        return render_template("register.html", form=form)
    else:
        if form.validate():
            username = form.username.data
            password = form.password.data
            email = form.email.data
            result = create_userinfo(username=username, password=password, email=email)
            print("恭喜:%s,注册成功" % result)
            return redirect(url_for("login"))
        else:
            print(form.errors)
            return render_template("register.html", form=form)


if __name__ == "__main__":
    app.debug = True
    app.run(host='0.0.0.0', port='80')
