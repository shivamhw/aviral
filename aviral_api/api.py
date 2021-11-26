from aviral_api.base import api_caller
from aviral_api import urls, exceptions


class AviralAPI(api_caller):

    def login(self, username : str, password : str) -> dict:
        username = username.lower()
        response = self._post_call(urls.aviral_login_url, {"username": username, "password": password})
        if response["user_group"] == None:
            raise exceptions.WrongLoginError("Sahi details daal le bhai")
        return response

    def get_subjectwise_marks(self, token: str, session : str) -> dict:
        response = self._get_call(urls.aviral_marks_url, {"Authorization" : token, "session" : session})
        return response

    def get_semesterwise_marks(self, token: str) -> list[dict]:
        response = self._get_call(urls.aviral_semester_result_url, {"Authorization" : token})
        return response

    def get_userdata(self, token : str, session : str) -> dict:
        response = self._get_call(urls.aviral_user_details_url, {"Authorization" : token, "session" : session})
        return response
    
    def get_sessions(self) -> dict:
        response = self._get_call(urls.aviral_sessions_url)
        return response

    def get_mtech_specialization(self, token : str) -> dict:
        response = self._get_call(urls.aviral_mtech_specialization_url, {"Authorization" : token})
        return response