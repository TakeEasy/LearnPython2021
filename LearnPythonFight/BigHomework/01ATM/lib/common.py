import hashlib
import logging.config
from config import settings


def get_pwd_md5(password):
    md5_obj = hashlib.md5()
    md5_obj.update(password.encode('utf-8'))
    salt = '55555555'
    md5_obj.update(salt.encode('utf-8'))
    return md5_obj.hexdigest()


def login_auth(func):
    from core import src
    from functools import wraps
    @wraps(func)
    def wrapper(*args, **kwargs):
        if src.login_user:
            res = func(*args, **kwargs)
            return res
        else:
            print('请先登录')
            src.login()

    return wrapper


def get_logger(log_type):
    logging.config.dictConfig(settings.LOGGIN_DIC)
    logger = logging.getLogger(log_type)
    return logger
