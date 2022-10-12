
from dbhelpers import conn_exe_close
from apihelpers import get_display_results, verify_endpoints_info
from flask import Flask, request, make_response
import dbcreds
import json

app = Flask(__name__)

@app.post('/api/painting')
def add_painting():
    invalid = verify_endpoints_info(request.json,['artist','name','image_url'])
    if(invalid != None):
        return make_response(json.dumps(invalid,default=str),400)
    results_json = get_display_results('call add_painting(?,?,?)',
    [request.json.get('artist'),request.json.get('name'),request.json.get('image_url')])
    return results_json

@app.get('/api/painting')
def all_paintings():
    invalid = verify_endpoints_info(request.args,['artist'])
    if(invalid != None):
        return make_response(json.dumps(invalid,default=str),400)
    results_json = get_display_results('call all_paintings(?)',[request.args.get('artist')])
    return results_json


if(dbcreds.production_mode == True):
    print('Running in production mode')
    app.run(debug=True)
else:
    from flask_cors import CORS
    CORS(app)
    print('Running in Testing mode')
    app.run(debug=True)
app.run(debug=True)
