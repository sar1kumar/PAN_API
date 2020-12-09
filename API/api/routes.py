from flask_restx import Api

# project resources
from auth import SignUpApi, LoginApi
from user import UsersApi, UserApi
from pan import PanApi


def create_routes(api: Api):

    api.add_resource(SignUpApi, '/auth/signup')
    api.add_resource(LoginApi, '/auth/login')

    api.add_resource(UsersApi, '/user/')
    api.add_resource(UserApi, '/user/<user_id>')

    api.add_resource(PanApi, '/pan/<pan_id>/<cid>')
