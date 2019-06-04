import pymysql
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from jelly.configs import GRID_LENGTH,USER,PASSWORD,HOST,PORT,DATABASE
from jelly.functions import get_grid_str, get_hash_str

string = "mysql+pymysql://%s:%s@%s:%d/%s?charset=utf8"%(USER, PASSWORD, HOST, PORT, DATABASE)
engine = create_engine(string,pool_recycle=300,pool_size=2)
session = sessionmaker(bind=engine)()

def get(sql):
    r = session.execute(sql)
    result = r.fetchall()
    r.close()
    session.close()
    return result

def insert(table,mapping_list):
    sql = "insert into %s ( %s )values (:%s)"%\
        (table," , ".join(mapping_list[0].keys()),",:".join(mapping_list[0].keys()))
    r = session.execute(sql,mapping_list)
    session.commit()
    return r.rowcount,r.lastrowid

def update(table,updates,condition):
    if isinstance(updates,dict):
        updates = updates.items()
    i=0
    t1=[]
    condition_dict={}
    for e in updates:
        key="%s_%d"%(e[0],i)
        t1.append("%s=:%s"%(e[0],key))
        condition_dict[key]=e[1]
        i+=1
    t2=[]
    for e in condition:
        key="%s_%d"%(e[0],i)
        t2.append("%s=:%s"%(e[0],key))
        condition_dict[key]=e[1]
        i+=1
    sql="update %s set %s where %s"%(table," , ".join(t1)," and ".join(t2))
    r = session.execute(sql,condition_dict)
    session.commit()
    return r.rowcount


def get_bombs(session_id):
    sql = "select current_grid from tbl_match where session_id='%s'" % session_id
    data = get(sql)
    if data:
        return data[0][0]
    else:
        return 'INVALID PARAMS'
    #return 'VSBBSBBBHBBBBBBBBSBBBBBBBBBBVBBBBHBBBBBBSBBBBSBBBBBBBBBBBBBBBBBB'

def initial_level(level):
    n = GRID_LENGTH
    sql = "select start_grid from tbl_level where level_id=%s limit 1" % level
    data = get(sql)
    if not data:
        grid_str = get_grid_str()
        hash_str = get_hash_str()
        insert("tbl_level", [{'start_grid':grid_str, 'level_id':int(level)}])
        insert("tbl_match", [{'session_id':hash_str, 'current_grid':grid_str, 'level_id':int(level)}])
        grid_str_output = ''
        for i in range(n):
            grid_str_output += grid_str[i*n:i*n+n] + '\n'
        return hash_str + '\n' + grid_str_output
    else:
        grid_str = data[0][0]
        hash_str = get_hash_str()
        insert("tbl_match", [{'session_id':hash_str, 'current_grid':grid_str, 'level_id':int(level)}])
        grid_str_output = ''
        for i in range(n):
            grid_str_output += grid_str[i*n:i*n+n] + '\n'
        return hash_str + '\n' + grid_str_output

def update_level(session_id, new_bombs):
    update("tbl_match", [('current_grid',new_bombs)], [('session_id',session_id)])
