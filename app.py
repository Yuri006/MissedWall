from flask import Flask, render_template, request, redirect, url_for, make_response
from wall_db import *

app = Flask(__name__)


@app.route('/admin')
def admin():
    return render_template('admin_panel.html')


@app.route('/login')
def login():
    return render_template('login_page.html')


'''
@app.route('/wall')
def main_wall():
    return render_template('wall.html')


@app.route('/registration')
def reg():
    return render_template('reg.html')
'''


@app.route('/')
def index():
    return render_template('Index.html')


@app.route('/cgi-bin/')
def cgi():
    name = request.args.get('username')
    password = request.args.get('password')
    res = make_response('')
    res.set_cookie('username', name, max_age=60 * 60 * 24 * 365 * 2)
    res.set_cookie('password', password, max_age=60 * 60 * 24 * 365 * 2)
    print(name, password)
    return render_template('Index.html')


@app.route('/cookie/')
def getcookie():
    name = request.cookies.get('name')
    return '<h1>welcome ' + name + '</h1>'


@app.errorhandler(404)
def page_not_found(error):
    return render_template('404page.html'), 404


@app.route('/cookie/')
def cookie():
    if not request.cookies.get(''):
        res = make_response("Setting a cookie")

    else:
        res = make_response("Value of cookie foo is {}".format(request.cookies.get('foo')))
    return res


if __name__ == '__main__':
    main_db = MainDB()
    # app.templates_auto_reload = True
    # app.jinja_env.auto_reload = True
    app.run()
