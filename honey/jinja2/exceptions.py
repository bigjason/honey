
class StaticFileNotFoundError(IOError):
    """Raised when a static file cannot be located in the django STATIC_ROOT
    folder.
    """
    pass
  