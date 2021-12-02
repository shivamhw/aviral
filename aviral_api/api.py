from typing import Optional
from aviral_api.base import api_caller
from aviral_api import urls, exceptions


class AviralAPI(api_caller):

    def login(self, username : str, password : str) -> dict:
        username = username.lower()
        response = self._post_call(urls.aviral_login_url, {"username": username, "password": password})
        if response["user_group"] == None:
            raise exceptions.WrongLoginError("Sahi details daal le bhai")
        return response

    def get_subjectwise_marks(self, user: dict, session : str = None) -> dict:
        token = user.get("jwt_token")
        if session is None:
            session = user.get("session_id")
        if token is None:
            raise exceptions.UserNotLoggedInError("Invalid Token, Try to login first")
        if session is None:
            raise exceptions.InvalidSessionError("No session specified")
        response = self._get_call(urls.aviral_marks_url, {"Authorization" : token, "session" : session})
        return response

    def get_semesterwise_marks(self, user: dict) -> dict:
        token = user.get("jwt_token")
        if token is None:
            raise exceptions.UserNotLoggedInError("Invalid Token, Try to login first")
        response = self._get_call(urls.aviral_semester_result_url, {"Authorization" : token})
        return response

    def get_userdata(self, user: dict, session : str = None) -> dict:
        token = user.get("jwt_token")
        if session is None:
            session = user.get("session_id")
        if token is None:
            raise exceptions.UserNotLoggedInError("Invalid Token, Try to login first")
        if session is None:
            raise exceptions.InvalidSessionError("No session specified")
        response = self._get_call(urls.aviral_user_details_url, {"Authorization" : token, "session" : session})
        return response
    
    def get_sessions(self) -> dict:
        response = self._get_call(urls.aviral_sessions_url)
        return response

    def get_mtech_specialization(self, user : dict) -> dict:
        token = user.get("jwt_token")
        if token is None:
            raise exceptions.UserNotLoggedInError("Invalid Token, Try to login first")
        response = self._get_call(urls.aviral_mtech_specialization_url, {"Authorization" : token})
        return response