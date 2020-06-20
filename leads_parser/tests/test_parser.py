import json
import os
import unittest
from leads_parser.leads_parser import LeadsParser
from helper import save_leads_data_to_file


class LeadsParserTest(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def setUp(self):
        self.test_leads_meta_name_config = 'lead_name'
        self.test_leads_meta_phone_config = 'lead_phone'
        self.test_leads_meta_email_config = 'lead_email'

        self.test_input_filename = 'lead_test.html'
        self.test_output_filename = 'test_output.json'

        self.test_input_file_path = os.path.dirname(__file__) + '/' + self.test_input_filename
        self.test_output_file_path = os.path.dirname(__file__) + '/' + self.test_output_filename

    def test_leads_parser(self):
        """
        Test function for testing LeadsParser
        Creates test output file and checks if leads details are correct
        :return:
        """
        lead_parser_client = LeadsParser(self.test_input_file_path,
                                         self.test_leads_meta_name_config,
                                         self.test_leads_meta_phone_config,
                                         self.test_leads_meta_email_config
                                         )

        test_file_content = lead_parser_client.read_leads_file_contents()
        test_leads_data = lead_parser_client.parse_leads_data(test_file_content)

        save_leads_data_to_file(self.test_output_file_path, test_leads_data)

        with open(self.test_output_file_path, "r") as test_output_file:
            leads_data = json.load(test_output_file)
            self.assertEqual(leads_data.get('name'), "Test Lead")
            self.assertEqual(leads_data.get('phone'), "111-222-3333")
            self.assertEqual(leads_data.get('email'), "testlead@gmail.com")

        # We need to Remove test json file created after test completes
        os.remove(self.test_output_file_path)
