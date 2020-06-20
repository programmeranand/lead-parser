import os
import sys

# General Configurations for File Paths and Metadata

# Input file Settings
LEADS_DATA_FOLDER = 'leads_data'
LEADS_DATA_FILENAME = 'lead.html'
LEAD_HTML_FILE_PATH = os.path.dirname(__file__) + '/' + LEADS_DATA_FOLDER + '/' + LEADS_DATA_FILENAME

# <meta> tag settings
# NOTE :- These Config are values  in name='attribute_value' inside <meta> HTML Tag
LEAD_NAME_META_TAG_CONFIG = 'lead_name'
LEAD_PHONE_META_TAG_CONFIG = 'lead_phone'
LEAD_EMAIL_META_TAG_CONFIG = 'lead_email'

# Output file Settings
OUTPUT_FILE_NAME = 'output.json'
OUTPUT_DATA_FOLDER = 'leads_data'
OUTPUT_FILE_PATH = os.path.dirname(__file__) + '/' + OUTPUT_DATA_FOLDER + '/' + OUTPUT_FILE_NAME


# LOGGING SETTINGS
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '[%(levelname)s] [%(asctime)s] [%(name)s] [%(filename)s:%(lineno)d] %(message)s'
        },
        'simple': {
            'format': '%(levelname)s %(message)s'
        }
    },
    'handlers': {
        'console': {
            'level': 'INFO',
            'class': 'logging.StreamHandler',
            'stream': sys.stdout,
            'formatter': 'verbose',
        },
    },
    'loggers': {
        '': {
            'handlers': ['console'],
            'level': 'INFO',
            'propagate': True,
        }
    }
}
