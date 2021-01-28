class Config(object):
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    TIMEOUT_COUNT=60
    DBCONFIG ={
      'DBNAME' : 'dbname',
      'DBUSER' : 'laxmikant',
      'DBPASSWORD' : '*******',
      'DBHOST' : 'localhost'
    }

class ProductionConfig(Config):
    dbcredentials = {'DBUSER' : 'produser', 'DBPASSWORD':'******'}
    DBCONFIG = Config.DBCONFIG.copy()
    DBCONFIG.update(dbcredentials)

class DevelopmentConfig(Config):
    dbcredentials = {'DBUSER' : 'devuser', 'DBPASSWORD':'******'}
    DBCONFIG = Config.DBCONFIG.copy()
    DBCONFIG.update(dbcredentials)