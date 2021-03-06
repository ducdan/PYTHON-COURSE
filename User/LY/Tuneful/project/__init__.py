# -*- coding: utf-8 -*-
__version__ = '0.1'

from flask import Flask

app = Flask('project')
app.config['SECRET_KEY'] = 'talamaday'
app.config.from_pyfile('config.cfg')
app.debug = True

from project.controllers import *
from project.models import *
