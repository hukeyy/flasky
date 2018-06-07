# -*- coding: utf-8 -*-
# Author: hkey
from flask import render_template, session, redirect, url_for, current_app
from . import main
from .forms import NameForm
from .. import db
from ..models import User
from ..email import send_mail

@main.route('/', methods=['GET', 'POST'])
def index():
    form = NameForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.name.data).first()    # 查询数据库是否有该用户
        if user is None:    # 如果没有该用户，就保存到数据库中
            user = User(username=form.name.data)
            db.session.add(user)
            session['known'] = False    # 通过session保存 known为False，通过web渲染需要
            if current_app.config['FLASKY_ADMIN']:  # 如果配置变量有flasky管理员就发送邮件
                # 异步发送邮件
                send_mail(current_app.config['FLASKY_ADMIN'], 'New User', 'mail/new_user', user=user)
        else:
            session['known'] = True
        session['name'] = form.name.data
        form.name.data = ''
        return redirect(url_for('.index'))  # 通过redirect避免用户刷新重复提交
    return render_template('index.html', form=form, name=session.get('name'),
                           known=session.get('known', False))