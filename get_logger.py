import os
import logging.config
from pathlib import Path

proj_dir = Path(__file__).parent.parent


def setup_logging():
    log_conf = {
        'version': 1,
        'formatters': {
            'standard': {
                'format': '%(asctime)s [%(name)s], %(lineno)d %(levelname)s:  %(message)s',
                'datefmt': '%Y-%m-%d %H-%M-%S',
            },
        },
        'handlers': {
            'console': {
                'class': 'logging.StreamHandler',
                'formatter': 'standard',
                'stream': 'ext://sys.stdout',
            },
            'file_handler': {
                'class': 'logging.handlers.TimedRotatingFileHandler',  # класс для ротации
                'when': 'D',  # единицца ротации
                'interval': 1,  # через сколько единиц будет проходить ротации
                'backupCount': 30,  # сколько файлов хранить
                'filename': f"{Path(proj_dir, 'logs', 'pat_send_data.log')}",
                'formatter': 'standard',
                'level': 'INFO',
                'encoding': 'utf-8',
            }
        },
        'root': {
            'handlers': ['console',],
            'level': 'INFO',
        },
        'loggers': {
            'PYKIS': {
                'handlers': ['console',],
                'level': 'DEBUG',
                'propagate': False,
            },
            'PACSAPI': {
                'handlers': ['console', 'file_handler',],
                'level': 'DEBUG',
                'propagate': False,
            },
            'PG_EXEC': {
                'handlers': ['console', ],
                'level': 'DEBUG',
                'propagate': False,
            },
        },
    }

    logging.config.dictConfig(log_conf)

# вызываем настройки логгера
setup_logging()


def get_logger(name: str):
    return logging.getLogger(name)
