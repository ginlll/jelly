# coding:utf8

from flask import Blueprint,request
from jelly.functions import get_status, get_grid_str, get_hash_str
from jelly.dbop import get_bombs, initial_level, update_level
from jelly.configs import GRID_LENGTH

blueprint = Blueprint('user', __name__) 

@blueprint.route('/start-level', methods=['GET'])
def start():
    n = GRID_LENGTH
    grid_str = get_grid_str()
    hash_str = get_hash_str(grid_str)
    grid_str_output = ''
    for i in range(n):
        grid_str_output += grid_str[i*n:i*n+n] + '\n'
    return hash_str + '\n' + grid_str_output

@blueprint.route('/move', methods=['GET'])
def move():
    n = GRID_LENGTH 
    session_id = request.args.get("sessionId")
    row0 = request.args.get("row0")
    col0 = request.args.get("col0")
    row1 = request.args.get("row1")
    col1 = request.args.get("col1")
    row0 = int(row0) if row0.isdigit() else None
    col0 = int(col0) if col0.isdigit() else None
    row1 = int(row1) if row1.isdigit() else None
    col1 = int(col1) if col1.isdigit() else None
    bombs = get_bombs(session_id)
    next_bombs = get_status(bombs, row0, col0, row1, col1)
    next_bombs_output = ''
    for i in range(n):
        next_bombs_output += next_bombs[i*n:i*n+n] + '<br>'
    return next_bombs_output