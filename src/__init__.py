import os

from flask import Flask

def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'src.sqlite'),
    )
    app.jinja_env.auto_reload = True
    app.config["TEMPLATES_AUTO_RELOAD"] = True

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        app.config.from_mapping(test_config)

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    from . import db
    db.init_app(app)

    from . import auth
    app.register_blueprint(auth.bp)

    from . import page
    app.register_blueprint(page.bp)
    app.add_url_rule('/', endpoint='index')

    from . import review
    app.register_blueprint(review.bp)
    app.add_url_rule('/', endpoint='review')

    from . import beer
    app.register_blueprint(beer.bp)
    app.add_url_rule('/', endpoint='beer')

    return app
