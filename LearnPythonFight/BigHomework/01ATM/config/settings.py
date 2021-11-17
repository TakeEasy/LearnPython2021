import os
import sys

BASE_PATH = os.path.dirname(
    os.path.dirname(__file__)
)

USER_DATA_PATH = os.path.join(
    BASE_PATH, 'db', 'user_info'
)

LOGGIN_DIC = os.path.join(
    BASE_PATH, 'log', 'atm.log'
)


logfile_dir = os.path.join(BASE_PATH, 'log')
# print(logfile_dir)

# ****************注意2: log文件名
logfile_name = 'atm.log'

# 如果不存在定义的日志目录就创建一个
#if not os.path.isdir(logfile_dir):
#    os.mkdir(logfile_dir)

# log文件的全路径
logfile_path = os.path.join(logfile_dir, logfile_name)



standard_format = '%(asctime)s - %(threadName)s:%(thread)d - 日志名字:%(name)s - %(filename)s:%(lineno)d -' \
                  '%(levelname)s - %(message)s'

simple_format = '[%(levelname)s][%(asctime)s][%(filename)s:%(lineno)d]%(message)s'

test_format = '%(asctime)s] %(message)s'

# 3、日志配置字典
LOGGING_DIC = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'standard': {
            'format': standard_format
        },
        'simple': {
            'format': simple_format
        },
        'test': {
            'format': test_format
        },
    },
    'filters': {},
    # handlers是日志的接收者，不同的handler会将日志输出到不同的位置
    'handlers': {
        # 打印到终端的日志
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',  # 打印到屏幕
            'formatter': 'simple'
        },
        'default': {
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',  # 保存到文件
            # 'maxBytes': 1024*1024*5,  # 日志大小 5M
            'maxBytes': 1000,
            'backupCount': 5,
            'filename': LOGGIN_DIC,  # os.path.join(os.path.dirname(os.path.dirname(__file__)),'log','a2.log')
            'encoding': 'utf-8',
            'formatter': 'standard',

        },
        # 打印到文件的日志,收集info及以上的日志
        'other': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',  # 保存到文件
            'filename': LOGGIN_DIC,  # os.path.join(os.path.dirname(os.path.dirname(__file__)),'log','a2.log')
            'encoding': 'utf-8',
            'formatter': 'test',

        },
    },
    # loggers是日志的产生者，产生的日志会传递给handler然后控制输出
    'loggers': {
        # logging.getLogger(__name__)拿到的logger配置
        'user': {
            'handlers': ['console', 'other'],  # 这里把上面定义的两个handler都加上，即log数据既写入文件又打印到屏幕
            'level': 'DEBUG',  # loggers(第一层日志级别关限制)--->handlers(第二层日志级别关卡限制)
            'propagate': False,  # 默认为True，向上（更高level的logger）传递，通常设置为False即可，否则会一份日志向上层层传递
        },
        'bank': {
            'handlers': ['console', ],  # 这里把上面定义的两个handler都加上，即log数据既写入文件又打印到屏幕
            'level': 'DEBUG',  # loggers(第一层日志级别关限制)--->handlers(第二层日志级别关卡限制)
            'propagate': False,  # 默认为True，向上（更高level的logger）传递，通常设置为False即可，否则会一份日志向上层层传递
        },
        'admin': {
            'handlers': ['default', ],  # 这里把上面定义的两个handler都加上，即log数据既写入文件又打印到屏幕
            'level': 'DEBUG',  # loggers(第一层日志级别关限制)--->handlers(第二层日志级别关卡限制)
            'propagate': False,  # 默认为True，向上（更高level的logger）传递，通常设置为False即可，否则会一份日志向上层层传递
        },
    },
}

if __name__ == '__main__':
    print(BASE_PATH)
    print(USER_DATA_PATH)
