from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

import config

db = SQLAlchemy()
migrate = Migrate()

def create_app(config=None):
    app = Flask(__name__)

    if app.config["ENV"] == 'production':
        app.config.from_object('config.ProductionConfig')
    else:
        app.config.from_object('config.DevelopmentConfig')

    if config is not None:
        app.config.update(config)

    db.init_app(app)
    migrate.init_app(app, db)

    from .routes.main_route import main_bp
    from .routes.coin_route import coin_bp
    from .routes.tweet_route import tweet_bp
    app.register_blueprint(tweet_bp)

    app.register_blueprint(main_bp)
    app.register_blueprint(coin_bp)

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)