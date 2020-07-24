# encoding: utf-8

class gapipyError(Exception):
    pass


class InvalidRequestError(gapipyError):
    # invalid parameter, bad request
    pass


class NotPermittedError(gapipyError):
    # invalid credentials, no permission
    pass


class LimitExceededError(gapipyError):
    # quota, rate limit, ...
    pass


class ServerError(gapipyError):
    # internal server error / backend error
    pass