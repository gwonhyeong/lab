from flask_restx import Namespace, fields


class UserNs:
    impl = Namespace('user', description='user namespace')
    userinfo = impl.model('userinfo', {
        'email': fields.String(required=True, description='user email address'),
        'username': fields.String(required=True, description='user username'),
        'public_id': fields.String(description='user Identifier')
    })
    user = impl.model('user', {
        'email': fields.String(required=True, description='user email address'),
        'username': fields.String(required=True, description='user username'),
        'password': fields.String(required=True, description='user password'),
        'public_id': fields.String(description='user Identifier')
    })
    '''
    sample = impl.model('sample', {
        'sample': fields.String(required=True, description='sample')
    })
    '''


class AuthNs:
    impl = Namespace('auth', description='auth namespace')
    auth = impl.model('auth', {
        'email': fields.String(required=True, description='user email address'),
        'password': fields.String(required=True, description='user password'),
    })
