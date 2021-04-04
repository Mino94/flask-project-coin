class Config(object):
    DEBUG = False
    TESTING = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite+pysqlite:///coin_db.sqlite3'


class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'sqlite+pysqlite:///coin_db.sqlite3'
