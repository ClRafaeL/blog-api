from flask import jsonify
from .messages import MSG_INVALID_DATA, MSG_DOES_NOT_EXIST, MSG_EXCEPTION, MSG_ALREADY_EXISTS, MSG_RESOURCE_CREATED


def resp_data_invalid(resource :str, errors: dict, msg: str = MSG_INVALID_DATA):
    '''
    Responses 400 Bad Request
    '''

    if not isinstance(resource, str):
        raise ValueError('O recurso precisa ser uma string.')
    resp = jsonify({
        'resource': resource,
        'message': msg,
        'errors': errors,
    })
    resp.status_code = 400
    return resp

def resp_exception(resource :str, description :str = '', msg :str = MSG_EXCEPTION):
    '''
    Responses 500
    '''

    if not isinstance(resource, str):
        raise ValueError('O recurso precisa ser uma string.')
    resp = jsonify({
        'resource': resource,
        'message': msg,
        'description': description
    })
    resp.status_code = 500
    return resp

def resp_does_not_exist(resource :str, description :str, msg :str = MSG_DOES_NOT_EXIST):
    '''
    Responses 404 Not Found
    '''

    if not isinstance(resource, str):
        raise ValueError('O recurso precisa ser uma string.')
    resp = jsonify({
        'resource': resource,
        'message': MSG_DOES_NOT_EXIST.format(description),
    })
    resp.status_code = 404
    return resp

def resp_already_exists(resource :str, description :str, msg :str = MSG_ALREADY_EXISTS):
    '''
    Responses 400
    '''

    if not isinstance(resource, str):
        raise ValueError('O recurso precisa ser uma string.')
    resp = jsonify({
        'resource': resource,
        'message': MSG_ALREADY_EXISTS.format(description),
    })
    resp.status_code = 400
    return resp

def resp_ok(resource :str, message :str, data=None, **extras):
    '''
    Responses 200
    '''

    response = {'status': 200, 'message': message, 'resource': resource}
    if data:
        response['data'] = data
    response.update(extras)
    resp = jsonify(response)
    resp.status_code = 200

    return resp

def reso_created(resource :str, message :str, data=None, msg :str = MSG_RESOURCE_CREATED, **extras):
    '''
    Responses  201
    '''

    response = {'status': 201, 'message': message, 'resource': resource}
    if data:
        response['data'] = data
    response.update(extras)
    resp = jsonify(response)
    resp.status_code = 201

    return resp