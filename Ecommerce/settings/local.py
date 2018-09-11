from .base import *


DATABASES = {
    'default': {
        'NAME': 'INFO',
        'ENGINE': 'sql_server.pyodbc',
        'HOST': 'localhost',
        'USER': 'userinfo',
        'PASSWORD': 'userpss',
        'OPTIONS': {
            'driver': 'SQL Server Native Client 10.0',
        },
      }

}
