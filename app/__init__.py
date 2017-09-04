from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def create_app(config_name):
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'M*qaEYfBjdOg*Ja#'
    # 按照你们数据库配置来修改此项 mysql://用户名:密码@服务器地址:端口号/数据库名称
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:wycg55967568w@localhost:3306/loan'
    app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True

    db.init_app(app)

    from .index import app as index
    app.register_blueprint(index, url_prefix='/index')

    from .check_identity import app as check
    app.register_blueprint(check, url_prefix='/check')

    from .credit_calculation import app as credit
    app.register_blueprint(credit, url_prefix='/credit')

    from .standard_investment import app as investment
    app.register_blueprint(investment, url_prefix='/investment')

    return app
