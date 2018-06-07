# -*- coding: utf-8 -*-
# Author: hkey
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import Required

class NameForm(FlaskForm):
    '''通过 flask-wtf 定义表单类'''
    name = StringField('What is your name ?', validators=[Required()])  # 文本框
    submit = SubmitField('Submit')  # 按钮