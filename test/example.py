# from flask import Flask
# app = Flask(__name__)

# # 简单的访问
# @app.route('/')
# def index():
#     return "Index Page"

# @app.route('/hello')
# def hello():
#     return "Hello Wrold!"

# # 带参数的访问
# @app.route('/user/<username>')
# def show_user_profile(username):
#     return "User %s" % username

# @app.route('/post/<int:post_id>')
# def show_post(post_id):
#     return 'Post %d' % post_id

# # 构造 URL
# from flask import Flask, url_for
# app = Flask(__name__)

# @app.route('/')
# def index(): pass

# @app.route('/login')
# def login():pass

# @app.route('/user/<username>')
# def profile(username):pass

# with app.test_request_context():
#     print(url_for('index'))
#     print(url_for('login'))
#     print(url_for('login', next='/'))
#     print(url_for('profile', username='John Doe'))


# # http的访问方法
# from flask import Flask, request
# app = Flask(__name__)

# @app.route('/login', methods=['GET', 'POST'])
# def login():
#     if request.method == 'POST':
#         return 'methods:Post'
#     else:
#         return 'methods:Get'


# 模板渲染方法
from flask import Flask, render_template
app = Flask(__name__)


@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)


if __name__ == "__main__":
    # app.run(host='0.0.0.0', debug=True)
    app.debug = True
    app.run()
