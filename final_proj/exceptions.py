from werkzeug.exceptions import default_exceptions, HTTPException, InternalServerError


class InvalidUsage(HTTPException):
    def __init__(self, description, code):
        HTTPException.__init__(self)

        # set defaults
        self.description = "Something wrong happened"
        self.code = 400

        if description is not None:
            self.description = description
        
        if code is not None:
            self.code = code


class NoPokemonNameError(HTTPException):
    code = 400
    description = 'No pokemon name was inputed'


class InvalidPokemonNameError(HTTPException):
    code = 400
    description = 'Invalid pokemon name'


class NoQuoteError(HTTPException):
    code = 400
    description = 'Not quotes found'


class YoutubeError(HTTPException):
    code = 400
    description = 'Something wrong happened while trying to download the youtube video'


