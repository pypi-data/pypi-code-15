class SDKError(IOError):
    def __init__(self, *args, **kwargs):
        self.status_code = kwargs.get("status_code")
        self.details = None

        error = kwargs.get("error")
        e = kwargs.get("exception")

        if error is not None:
            self.status_code = error["code"]
            self.message = error["message"]
            self.details = error.get("details")

        elif e is not None:
            self.message = e.message

        self.result = kwargs.get("result", None)

    def __str__(self):
        return "{}: {}".format(self.message, self.details)
