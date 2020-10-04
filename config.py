class DefaultConfig:
    DEBUG = False
    TESTING = False
    DB_SERVER = 'localhost'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
