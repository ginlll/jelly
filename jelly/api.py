# coding:utf8

from flask import Blueprint,request
from jelly.functions import get_status, get_grid_str, get_hash_str
from jelly.dbop import get_bombs, initial_level, update_level
from jelly.configs import GRID_LENGTH

blueprint = Blueprint('user', __name__) 

@blueprint.route('/start-level', methods=['GET'])
def start():
    try:
        n = GRID_LENGTH
        level = request.args.get("level")
        if not level.isdigit():
            return 'INVALID PARAMS'
        final_str_output = initial_level(level)
        return final_str_output
    except Exception as e:
        #return e
        return 'INVALID PARAMS'
@blueprint.route('/move', methods=['GET'])
def move():
    try:
        n = GRID_LENGTH 
        session_id = request.args.get("sessionId")
        row0 = request.args.get("row0")
        col0 = request.args.get("col0")
        row1 = request.args.get("row1")
        col1 = request.args.get("col1")
        row0 = int(row0)
        col0 = int(col0)
        row1 = int(row1)
        col1 = int(col1)
        bombs = get_bombs(session_id)
        next_bombs = get_status(bombs, row0, col0, row1, col1)
        update_level(session_id, next_bombs)
        next_bombs_output = ''
        for i in range(n):
            next_bombs_output += next_bombs[i*n:i*n+n] + '\n' # <br> in explorer
        return next_bombs_output
    except Exception as e:
        #return e
        return 'INVALID PARAMS'