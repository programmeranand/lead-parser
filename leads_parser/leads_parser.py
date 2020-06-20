from bs4 import BeautifulSoup
import codecs


class LeadsParser(object):
    def __init__(self, file_path: str,
                 lead_name: str, lead_phone: str, lead_email: str):
        self.file_path = file_path
        self.lead_name_meta_config = lead_name
        self.lead_phone_meta_config = lead_phone
        self.lead_email_meta_config = lead_email

    def read_leads_file_contents(self):
        """
        Reads HTML file
        """
        file = codecs.open(self.file_path, "r")
        return file.read()

    def parse_leads_data(self, leads_contents):
        """
        Parses Leads HTML file contents using BeautifulSoup Library
        Algorithm :
            1. Reads HTML file into BeautifulSoup parsable format
            2. Searches All <meta> Tags in given HTML File with provided config to fetch name, email and phone

                2.1 lead_name_meta_config: refers to value in name='lead_name' pair provided inside the <meta> Tag
                2.2 lead_phone_meta_config: refers to value in phone='lead_phone' pair provided inside the <meta> Tag
                2.3 lead_email_meta_config: refers to value in email='lead_email' pair provided inside the <meta> Tag

            3. Creates a Python Dictionary containing name, email and Phone of leads
        :param leads_contents:
        :return: Python Dictionary containing parsed HTML details
        """
        get_soup = BeautifulSoup(leads_contents, 'lxml')
        lead_name = get_soup.find(
            'meta', attrs={'name': self.lead_name_meta_config}).get('content')
        lead_phone = get_soup.find(
            'meta', attrs={'name': self.lead_phone_meta_config}).get('content')
        lead_email = get_soup.find(
            'meta', attrs={'name': self.lead_email_meta_config}).get('content')
        leads_parsed_data = {
            'name': lead_name,
            'phone': lead_phone,
            'email': lead_email
        }
        return leads_parsed_data
