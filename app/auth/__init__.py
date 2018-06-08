# -*- coding: utf-8 -*-
# Author: hkey
from flask import Blueprint
auth = Blueprint('auth', __name__)
from . import views

