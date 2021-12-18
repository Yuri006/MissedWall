from flask import Flask, render_template, request, redirect, url_for, make_response
from wall_db import *

app = Flask(__name__)
global main_db
main_db = MainDB('wall.db')


@app.route('/admin')
def admin():
    return render_template('admin_panel.html')


@app.route('/login')
def login():
    if (request.cookies.get('username') is not None) and (request.cookies.get('password') is not None):
        return redirect(
            '/cgi-bin/login?username=' + request.cookies.get('username') + '&password=' + request.cookies.get(
                'password'))
    return render_template('login_page.html')


@app.route('/wall')
def main_wall():
    return render_template('wall.html', number_of_user=main_db.number_of_user())


@app.route('/registration')
def reg():
    return render_template('reg.html')


@app.route('/forgot')
def forgot():
    return render_template('forgot.html')


@app.route('/')
def index():
    return render_template('Index.html')


@app.route('/cgi-bin/<action>')
def cgi(action):
    if action == 'login':
        name = request.args.get('username')
        password = request.args.get('password')
        correct = main_db.check_password(name, password)
        if not correct:
            resp = make_response(redirect('/wall'))
            resp.set_cookie('username', name, max_age=60 * 60 * 24 * 365 * 2)
            resp.set_cookie('password', password, max_age=60 * 60 * 24 * 365 * 2)
            return resp
        else:
            if (request.cookies.get('username') is not None) and (request.cookies.get('password') is not None):
                resp = make_response(redirect('/login'))
                resp.set_cookie('username', request.cookies.get('username'), max_age=0)
                resp.set_cookie('password', request.cookies.get('password'), max_age=0)
                return resp
            return redirect('/login')
    elif action == 'user_check':
        nick = request.args.get('nick')
        if not main_db.check_name(nick):
            return '1'
        return '0'


@app.errorhandler(404)
def page_not_found(error):
    return render_template('404page.html'), 404


if __name__ == '__main__':
    # app.templates_auto_reload = True
    # app.jinja_env.auto_reload = True
    app.run()
