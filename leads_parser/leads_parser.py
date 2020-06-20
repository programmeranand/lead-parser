import codecs
import logging

from bs4 import BeautifulSoup

logger = logging.getLogger(__name__)


class LeadsParser(object):
    def __init__(self, file_path: str,
                 lead_name: str, lead_phone: str, lead_email: str):
        self.file_path = file_path
        self.lead_name_meta_config = lead_name
        self.lead_phone_meta_config = lead_phone
        self.lead_email_meta_config = lead_email

    def read_leads_html_file_contents(self):
        """
        Reads HTML file
        """
        file = codecs.open(self.file_path, "r")
        return file.read()

    def parse_leads_data(self, leads_contents):
        """
        Parses Leads HTML file contents using BeautifulSoup Python Library
        Algorithm :
            1. Reads HTML file into BeautifulSoup parsable format
            2. Searches <meta> Tags in given HTML File with provided config to fetch name, email and phone
                e.g <meta name='lead_name', content='Test Lead'> only tags like these are fetched
                    from BeautifulSoup Parser

                2.1 lead_name_meta_config: refers to value in name='lead_name' attribute provided inside the <meta> Tag
                2.2 lead_phone_meta_config: refers to value in phone='lead_phone' attribute provided inside the <meta> Tag
                2.3 lead_email_meta_config: refers to value in email='lead_email' attribute provided inside the <meta> Tag

            3. Creates a Python Dictionary containing name, email and Phone of leads

        NOTE :- 1.1 Algorithm Assumes HTML file is Provided with all valid <meta> tags containing all leads details
                1.2 If HTML file is provided with missing <meta> tags containing necessary leads details required,
                    then JSON file is produced with empty fields

        :param leads_contents: HTML File Contents
        :return: Python Dictionary containing parsed HTML details
        """

        # Assigning Empty values here to handle Invalid HTML file cases
        lead_name = ''
        lead_email = ''
        lead_phone = ''
        get_soup = BeautifulSoup(leads_contents, 'lxml')

        # Fetch Leads Name from Parsed Data
        try:
            lead_name = get_soup.find(
                'meta', attrs={'name': self.lead_name_meta_config}).get('content')
        except Exception:
            logger.exception(f'[LeadsParser] Leads Name Does not Exist'
                             f' due to invalid config: {self.lead_name_meta_config}')

        # Fetch Leads Phone from Parsed Data
        try:
            lead_phone = get_soup.find(
                'meta', attrs={'name': self.lead_phone_meta_config}).get('content')
        except Exception:
            logger.exception(f'[LeadsParser] Leads Phone Does not Exist'
                             f' due to invalid config: {self.lead_phone_meta_config}')

        # Fetch Leads Email from Parsed Data
        try:
            lead_email = get_soup.find(
                'meta', attrs={'name': self.lead_email_meta_config}).get('content')
        except Exception:
            logger.exception(f'[LeadsParser] Leads Email Does not Exist due'
                             f' to invalid config: {self.lead_email_meta_config}')

        # Store all required data inside Dictionary
        leads_parsed_data = {
            'name': lead_name,
            'phone': lead_phone,
            'email': lead_email
        }
        return leads_parsed_data
