from flask import request
from flask_cors import cross_origin
from datetime import datetime

from core import api, db

from .collection.models import Collection, CollectionInterface


def validate_save_request():
    try:
        interface = CollectionInterface(**request.json)
        return True
    except: 
        return False
        



@api.route('/', methods=['GET'])
@cross_origin()
def index():
    return {
        'name': 'watamatic-flask-db',
        'paths': [
            'save', 
            'get-by-id',
            'last500',
            'get-after -> return all > target timestamp'
            'custom',
        ]
    }
    
    
    

@api.route('/save', methods=['POST'])
def save():
    response = {'msg': 'success', 'status': '200'}
    
    if not validate_save_request(): return {
        'msg': "received invalid request.",
        'status_code': '400'
    }
    try:
        temp = Collection(**request.json)
    except Exception as e:
        print ("error while passing request to collection")
        return {
            'msg': 'error while passing request to collection',
            'status_code': '500',
            'error': str(e)
        }

    try:
        db.session.add(temp)
        db.session.commit()
    except:
        print ("error while adding collection to database")
        return {
            'msg': 'error while adding collection to database',
            'status_code': '500'
        }
    
    return response


@api.route('/last500', methods=['GET'])
@cross_origin()
def get():
    response = {
        'msg': 'success', 
        'status_code': '200',
        'data': None
    }
    
    id = request.args.get('id', type=int)
    try: 
        response['data'] = [entry.serialized 
            for entry in Collection.query.all()[:500]
        ]
    except:
        response['msg'] = 'Error while querying collection.'
        response['status_code'] = '500.'
        
    if response['data'] is None:
        response['msg'] = 'Found no collection with id {}.'.format(id)
        
        
    return response
    
    


@api.route('/get-by-id', methods=['GET'])
def get_by_id():
    response = {
        'msg': 'success', 
        'status_code': '200',
        'data': None
    }
    
    id = request.args.get('id', type=int)
    try:    
        response['data'] = [entry.serialized 
            for entry in Collection.query.filter_by(id=id)
        ]
    except:
        response['msg'] = 'Error while querying collection.'
        response['status_code'] = '500.'
        
    if response['data'] is None:
        response['msg'] = 'Found no collection with id {}.'.format(id)
        
        
    return response
    
    
    
    
    
@api.route('/get-after', methods=['GET'])
@cross_origin
def get_after():
    response = {}
    
    
    
    return response
    
    
    
    
    
@api.route('/last500-temp-by-time', methods=['GET'])
def last500_temp_by_time ():
    
    response = {
        'msg': 'success', 
        'status_code': '200',
        'data': {
            'columns': [],
            'datasets': [{ 'data': [] }],
        }
    }
    
    try: 
        
        for entry in Collection.query.limit(500).all():
            response['data']['columns'].append(
                entry.created
                # datetime.strptime(entry.created, "%d-%b-%Y-%H:%M:%S")
            )
            response['data']['datasets'][0]['data'].append(entry.temperature)
        
    except:
        response['msg'] = 'Error while querying collection.'
        response['status_code'] = '500.'
        
    return response
    
    
    
    
    