#!/usr/bin/env python
# whisker/exceptions.py


class WhiskerCommandFailed(Exception):
    pass


class ImproperlyConfigured(Exception):
    """
    Whisker is improperly configured; normally due to a missing library.
    """
    pass


class ValidationError(Exception):
    def __init__(self, message):
        super().__init__(message)
        self.message = message

    def __str__(self):
        return self.message
