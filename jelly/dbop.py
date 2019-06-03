import pymysql
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmake
from configs import USER,PASSWORD,HOST,PORT,DATABASE

string = "mysql+pymysql://%s:%s@%s:%d/%s?charset=utf8"%(USER, PASSWORD, HOST, PORT, DATABASE)
engine = create_engine(string,pool_recycle=300,pool_size=2)
session = sessionmaker(bind=engine)



def get_bombs(session_id):
    return 'VSBBSBBBHBBBBBBBBSBBBBBBBBBBVBBBBHBBBBBBSBBBBSBBBBBBBBBBBBBBBBBB'

def initial_level():
    pass

def update_level():
    pass
