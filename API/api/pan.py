from flask import Response, jsonify
from flask_restx import Resource, abort
from flask_jwt_extended import jwt_required, get_jwt_identity

# project resources
from errors import forbidden
from random import randrange
import re


class ValidationError(Exception):
    pass


class BackendError(Exception):
    pass


def get_pan_data(pan_number, cid):
    num = randrange(10)
    if re.match(r'^[A-Z]{5}[0-9]{4}[A-Z]$', str(pan_number)):
        pass
    else:
        abort(400, 'ValidationError')

    if num in (8, 9):
        raise BackendError

    return {
        'pan': pan_number,
        'name': 'Dinesh Kumar',
        'dob': '25-10-1990',
        'father_name': 'Hari Kumar',
        'clientid': cid
    }


def validate_pan_number(pan_number):
    """
    Validates if the given value is a valid PAN number or not, if not raise ValidationError
    """
    if re.match(r'^[A-Z]{5}[0-9]{4}[A-Z]$', str(pan_number)):
        return pan_number
    else:
        abort(400, 'ValidationError')


class PanApi(Resource):

    @jwt_required
    def get(self, pan_id: str, cid: str) -> Response:
        """
        GET response method for single documents in pan collection.

        :return: JSON object
        """
        try:
            output = get_pan_data(pan_id, cid)
            return jsonify({'result': output})
        except BackendError or ValidationError:
            raise abort(400, 'Validation Error Please check the PAN Number or Backend Error'
                             'TryAgain')


