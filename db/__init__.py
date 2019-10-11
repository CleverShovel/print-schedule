from peewee import *
from configparser import ConfigParser

config = ConfigParser()
config.read('./config.ini')
db_config = config['DATABASE']

db = MySQLDatabase(db_config['db_name'], user=db_config['user'], password=db_config['password'],
                   host=db_config['host'], port=int(db_config['port']))
