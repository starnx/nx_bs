from sql_manager import db, User


def create_userinfo(username, password, email=None):
    current_userinfo = User(username=username, password=password, email=email)
    db.session.add(current_userinfo)
    db.session.commit()
    print("%s 创建成功" % current_userinfo)


def drop_userinfo(username):
    will_drop_data = User.query.filter_by(username=username).first()
    if will_drop_data:
        db.session.delete(will_drop_data)
        db.session.commit()
        print("数据删除成功")
        print(User.query.all())
    else:
        print("用户不存在!!!")


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


def found_userinfo(username):
    userdata = User.query.filter_by(username="张三").first()
    if userdata:
        username = userdata.username
        password = userdata.password
        email = userdata.email
        print("---用户名:{}---密码:{}---邮箱:{}---".format(username, password, email))
        return userdata
    else:
        print("用户不存在!!!")
        return None


if __name__ == "__main__":
    # 创建数据库
    # db.create_all()
    # 销毁数据库
    # db.drop_all()
    # 添加数据
    # create_userinfo("张三", 123123)
    # 删除数据
    # drop_userinfo("李四")
    # 修改数据
    # reset_userinfo("123", "张三", 123123, "123@qq.com")
    # 查询数据(最好用filter,而不是get)
    found_userinfo("张三")
