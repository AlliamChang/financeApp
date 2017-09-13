# encoding:utf-8

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def create_app(config_name):
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'M*qaEYfBjdOg*Ja#'
    # 按照你们数据库配置来修改此项 mysql://用户名:密码@服务器地址:端口号/数据库名称
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://p2p:p2p@120.27.199.164:3306/loan'
    app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

    db.init_app(app)

    from .index import app as index
    app.register_blueprint(index, url_prefix='/index')

    from .check_identity import app as check
    app.register_blueprint(check, url_prefix='/check')

    # from .credit_calculation import app as credit
    # app.register_blueprint(credit, url_prefix='/credit')

    from .standard_investment import app as investment
    app.register_blueprint(investment, url_prefix='/investment')

    from .loan_borrow import app as loan
    app.register_blueprint(loan, url_prefix='/loan')

    from .profile_management import app as profile
    app.register_blueprint(profile, url_prefix='/profile')

    from .activation import app as activation
    app.register_blueprint(activation, url_prefix='/activation')

    from .credit import app as credit
    app.register_blueprint(credit, url_prefix='/credit')

    return app
