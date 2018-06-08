# -*- coding: utf-8 -*-
# Author: hkey
from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail
from flask_login import LoginManager
from config import config

# 由于尚未初始化所需的程序实例，所以没有初始化扩展，创建扩展类时没有向构造函数传入参数。
bootstrap = Bootstrap()
mail = Mail()
db = SQLAlchemy()
login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'auth.login'


def create_app(config_name):
    '''工厂函数'''
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)   # 通过config.py统一接口
    bootstrap.init_app(app)     # 该init_app是bootstrap实例的方法调用，与上面毫无关系
    mail.init_app(app)          # 同上
    db.init_app(app)            # 同上
    login_manager.init_app(app)

    # 附加路由和自定义错误页面，将蓝本注册到工厂函数
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    # 附加认证蓝本
    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint, url_prefix='/auth')

    return app