from rest_framework.exceptions import APIException


class OwnerDoctorError(APIException):
    status_code = 403
    default_detail = {
        'error': ['You do not have access to this.']}