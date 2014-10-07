class OAuthToolkitError(Exception):
    """
    Base class for exceptions
    """
    def __init__(self, error=None, *args, **kwargs):
        super(OAuthToolkitError, self).__init__(*args, **kwargs)
        self.oauthlib_error = error


class FatalClientError(OAuthToolkitError):
    """
    Class for critical errors
    """
    pass
