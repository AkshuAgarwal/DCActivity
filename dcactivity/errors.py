from discord import DiscordException, InvalidArgument

class DCActivityException(DiscordException):
    """Base Exception class for DCActivity Raised Errors."""
    pass

class APIException(DCActivityException):
    """Exception that is raised in case of some errors dur to API while requesting Invite Link."""
    pass

class InvalidChannel(InvalidArgument):
    """Exception that is raised when library encounters invalid channel as the input."""
    pass

class InvalidApplicationID(InvalidArgument):
    """Exception that is raised when library encounters invalid Application ID as the input."""
    pass
