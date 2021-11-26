from typing import Any
import requests
from . import exceptions
import json

class api_caller:
    def _get_call(self, url : str, header_param : dict = None, timeout : Any = 10) -> dict:
        try:
            response = requests.get(url, headers=header_param, timeout=timeout)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.ConnectTimeout:
            raise exceptions.AviralDownError("Aviral timeout, may be slow response from aviral")
        except requests.exceptions.ConnectionError:
            raise exceptions.AviralDownError("Could not connect to Aviral")
        except requests.exceptions.HTTPError:
            raise exceptions.InvalidResponseError("Server sent invalid response, There might be an issue with the data sent or expired token")
        except json.decoder.JSONDecodeError:
            raise exceptions.InvalidResponseError("There might be an issue with the data sent or expired token.")

    def _post_call(self, url : str,  datas : dict, header_param : dict = None, timeout : Any = 10) -> dict:
        try:
            response = requests.post(url, headers=header_param, data=json.dumps(datas), timeout=timeout)
            return response.json()
        except requests.exceptions.ConnectTimeout:
            raise exceptions.AviralDownError("Aviral timeout, may be slow response from aviral")
        except requests.exceptions.ConnectionError:
            raise exceptions.AviralDownError("Could not connect to Aviral")
        except requests.exceptions.HTTPError:
            raise exceptions.InvalidResponseError("Server sent invalid response, There might be an issue with the data sent or expired token")
        except json.decoder.JSONDecodeError:
            raise exceptions.InvalidResponseError("There might be an issue with the data sent or expired token.")



