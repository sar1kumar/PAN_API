from flask import Response, request, jsonify
from flask_restx import Resource
from flask_jwt_extended import jwt_required, get_jwt_identity

# project resources
from users import Users
from errors import forbidden


class UsersApi(Resource):

    @jwt_required
    def get(self) -> Response:
        """
        GET response method for acquiring all user data.
        JSON Web Token is required.
        Authorization is required: Access(admin=true)

        :return: JSON object
        """
        authorized: bool = Users.objects.get(id=get_jwt_identity()).access.admin

        if authorized:
            output = Users.objects()
            return jsonify({'result': output})
        else:
            return forbidden()


class UserApi(Resource):

    @jwt_required
    def get(self, user_id: str) -> Response:
        """
        GET response method for acquiring single user data.
        JSON Web Token is required.
        Authorization is required: Access(admin=true) or UserId = get_jwt_identity()

        :return: JSON object
        """
        authorized: bool = Users.objects.get(id=get_jwt_identity()).access.admin

        if authorized:
            output = Users.objects.get(id=user_id)
            return jsonify({'result': output})
        else:
            return forbidden()

    @jwt_required
    def put(self, user_id: str) -> Response:
        """
        PUT response method for updating a user.
        JSON Web Token is required.
        Authorization is required: Access(admin=true) or UserId = get_jwt_identity()

        :return: JSON object
        """
        authorized: bool = Users.objects.get(id=get_jwt_identity()).access.admin

        if authorized:
            data = request.get_json()
            put_user = Users.objects(id=user_id).update(**data)
            output = {'id': str(put_user.id)}
            return jsonify({'result': output})
        else:
            return forbidden()

    @jwt_required
    def post(self) -> Response:
        """
        POST response method for creating user.
        JSON Web Token is required.
        Authorization is required: Access(admin=true)

        :return: JSON object
        """
        authorized: bool = Users.objects.get(id=get_jwt_identity()).access.admin

        if authorized:
            data = request.get_json()
            post_user = Users(**data).save()
            output = {'id': str(post_user.id)}
            return jsonify({'result': output})
        else:
            return forbidden()

    @jwt_required
    def delete(self, user_id: str) -> Response:
        """
        DELETE response method for deleting user.
        JSON Web Token is required.
        Authorization is required: Access(admin=true)

        :return: JSON object
        """
        authorized: bool = Users.objects.get(id=get_jwt_identity()).access.admin

        if authorized:
            output = Users.objects(id=user_id).delete()
            return jsonify({'result': output})
        else:
            return forbidden()
