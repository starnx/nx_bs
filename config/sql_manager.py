from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager
from flask import Flask
# python3 上已经不支持mysqldb,以pymysql代之
import pymysql
pymysql.install_as_MySQLdb()
app = Flask(__name__)

# 数据库配置
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:root123@localhost:3306/nx_bs?charset=utf8mb4'
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True

db = SQLAlchemy(app)
manager = Manager(app)


class User(db.Model):
    # 数据库表名
    __tablename__ = 'users'
    # primary_key:主键, unique:列是否可重复
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    password = db.Column(db.String(32), nullable=False)
    email = db.Column(db.String(320), unique=True)

    def __repr__(self):
        return '<%r>' % self.username


# 注册用户
def create_userinfo(username, password, email):
    current_userinfo = User(username=username, password=password, email=email)
    db.session.add(current_userinfo)
    db.session.commit()
    print("用户 %s 注册成功!!!" % current_userinfo)


# 删除用户
def drop_userinfo(username):
    will_drop_data = User.query.filter_by(username=username).first()
    if will_drop_data:
        db.session.delete(will_drop_data)
        db.session.commit()
        print("数据删除成功")
        print(User.query.all())
    else:
        print("用户不存在!!!")


# 修改用户信息
def reset_userinfo(username, new_name, new_password, new_email):
    will_reset_data = User.query.filter_by(username=username).first()
    # 需要先经过数据格式验证,不然会出bug,数据库会报错,必须保持和注册时候一致
    if will_reset_data:
        will_reset_data.username = new_name
        will_reset_data.password = new_password
        will_reset_data.new_email = new_email
        db.session.add(will_reset_data)
        db.session.commit()
        print("数据修改成功")
        print(User.query.all())
    else:
        print("用户不存在!!!")


# 查询用户
def found_userinfo(username):
    userdata = User.query.filter_by(username=username).first()
    if userdata:
        # username = userdata.username
        # password = userdata.password
        # email = userdata.email
        # print("---用户名:{}---密码:{}---邮箱:{}---".format(username, password, email))
        return userdata
    else:
        print("用户不存在!!!")
        return None


if __name__ == "__main__":
    manager.run()
