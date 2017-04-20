
class BaseError(Exception):
    """Base Algolia API exception"""

    message = u"Unknown error occurred for '{url}'. Response content: '{content}'"

    def __init__(self, url, status, resource_name, content):
        self.url = url
        self.status = status
        self.resource_name = resource_name
        self.content = content

    def __str__(self):
        return self.message.format(url=self.url, content=self.content)

    def __unicode__(self):
        return self.__str__()

class CredentialError(BaseError):
    """
    Error Code: 403
    Invalid credentials
    """
    message = u"Credential error for url: '{url}'. Response content: '{content}'"

class InternalError(BaseError):
    """
    Error Code: 500
    Internal error
    """
    message = u"Internal error for url: '{url}'. Response content: '{content}'"

def exception_handler(result, name=""):
    """ Exception handler. Determines which error to raise for bad results """
    try:
        response_content = result.json()
    except Exception:
        response_content = result.text

    exception_map = { 403: CredentialError, 500: InternalError }
    exception_class = exception_map.get(result.status_code, BaseError)

    raise exception_class(result.url, result.status_code, name, response_content)

