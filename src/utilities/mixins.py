import redis

from abc import ABC, abstractmethod


class AbstractHttpBase(ABC):
    """
    Abstract class which help child classes make http calls.
    Child classes must declare properties:
        - base_url: Base url of Application/Service
        - header: Header to pass in HTTP Requests
        - paths: relative path of urls
    """

    @property
    @abstractmethod
    def base_url(self):
        pass

    @property
    @abstractmethod
    def header(self):
        pass

    @property
    @abstractmethod
    def paths(self):
        pass

    @property
    def __method_dispatcher(self):
        return {
            "get": requests.get,
            "post": requests.post,
            "put": requests.put,
            "delete": requests.delete,
            "patch": requests.patch,
            "head": requests.head,
        }

    def get_status_and_response(self, method, path, data={}, headers={}):
        method = self.__method_dispatcher.get(method.lower())
        assert method, f"{method} not found"

        if not headers:
            headers = self.header

        url = f"{self.base_url}{path}"
        response = method(url, data=json.dumps(data), headers=headers)
        return response.status_code, response.json()
