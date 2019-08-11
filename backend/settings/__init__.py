import os

IS_BUILD = bool(os.environ.get('IS_BUILD'))
IS_PRODUCTION = os.environ.get('HOST_ENV') == 'production'

if IS_BUILD:
    from .base import *
elif IS_PRODUCTION:
    from .prod import *
else:
    from .dev import *

if True:
    try:
        from .dev_secrets import *
    except ModuleNotFoundError:
        pass