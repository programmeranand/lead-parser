import os

# Input file Settings
LEADS_DATA_FOLDER = 'leads_data'
LEADS_DATA_FILENAME = 'lead.html'
LEAD_HTML_FILE_PATH = os.path.dirname(__file__) + '/' + LEADS_DATA_FOLDER + '/' + LEADS_DATA_FILENAME

# <meta> tag settings
LEAD_NAME_META_TAG_CONFIG = 'lead_name'
LEAD_PHONE_META_TAG_CONFIG = 'lead_phone'
LEAD_EMAIL_META_TAG_CONFIG = 'lead_email'

# Output file Settings
OUTPUT_FILE_NAME = 'output.json'
OUTPUT_DATA_FOLDER = 'leads_data'
OUTPUT_FILE_PATH = os.path.dirname(__file__) + '/' + OUTPUT_DATA_FOLDER + '/' + OUTPUT_FILE_NAME
