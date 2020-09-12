class BaseError(Exception):
    """Base class for exceptions in this module"""
    pass

class InvalidBirthyearError(BaseError):
    """Raised when the birthyear argument is not a valid integer like 1991"""
    pass

class TraitDoesNotExistError(BaseError):
    pass 
