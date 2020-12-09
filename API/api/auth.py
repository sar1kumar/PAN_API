from flask import Response, request, jsonify
from flask_restx import Resource
from flask_jwt_extended import create_access_token, create_refresh_token

# project resources
from users import Users
from errors import unauthorized

# external packages
import datetime


class SignUpApi(Resource):

    @staticmethod
    def post() -> Response:
        data = request.get_json()
        post_user = Users(**data)
        post_user.save()
        output = {'id': str(post_user.id)}
        return jsonify({'result': output})


class LoginApi(Resource):

    @staticmethod
    def post() -> Response:
        """
        POST response method for retrieving user web token.

        :return: JSON object
        """
        data = request.get_json()
        user = Users.objects.get(email=data.get('email'))
        auth_success = user.check_pw_hash(data.get('password'))
        if not auth_success:
            return unauthorized()
        else:
            expiry = datetime.timedelta(days=5)
            access_token = create_access_token(identity=str(user.id), expires_delta=expiry)
            refresh_token = create_refresh_token(identity=str(user.id))
            return jsonify({'result': {'access_token': access_token,
                                       'refresh_token': refresh_token,
                                       'logged_in_as': f"{user.email}"}})
