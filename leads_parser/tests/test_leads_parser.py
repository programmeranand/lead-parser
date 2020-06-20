import json
import os
import unittest

from helper import save_leads_data_to_file
from leads_parser.leads_parser import LeadsParser


class LeadsParserTest(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def setUp(self):
        """
        TestRunner Configurations
        Configures :-
            <meta> Tag name attribute values :- Name, email, phone
            Test Input file Paths
            Test Output file Paths
        """
        self.test_leads_meta_name_config = 'lead_name'
        self.test_leads_meta_phone_config = 'lead_phone'
        self.test_leads_meta_email_config = 'lead_email'

        self.test_input_filename = 'lead_test.html'
        self.test_invalid_input_filename = 'lead_test_2.html'
        self.test_output_filename = 'test_output.json'
        self.test_invalid_output_filename = 'test_invalid_output.json'

        self.test_input_file_path = os.path.dirname(__file__) + '/' + self.test_input_filename
        self.test_invalid_input_file_path = os.path.dirname(__file__) + '/' + self.test_invalid_input_filename

        self.test_output_file_path = os.path.dirname(__file__) + '/' + self.test_output_filename
        self.test_invalid_output_file_path = os.path.dirname(__file__) + '/' + self.test_invalid_output_filename

    def test_leads_parser_with_valid_metadata_in_html(self):
        """
        Tests Leads parser with the test file provided
        Creates test output file and checks if leads details are correct
        :return:
        """
        # Invoke Parser client
        lead_parser_client = LeadsParser(self.test_input_file_path,
                                         self.test_leads_meta_name_config,
                                         self.test_leads_meta_phone_config,
                                         self.test_leads_meta_email_config
                                         )

        # Read HTML file and Parse data
        test_file_content = lead_parser_client.read_leads_html_file_contents()
        test_leads_data = lead_parser_client.parse_leads_data(test_file_content)

        save_leads_data_to_file(self.test_output_file_path, test_leads_data)

        with open(self.test_output_file_path, "r") as test_output_file:
            leads_data = json.load(test_output_file)
            self.assertEqual(leads_data.get('name'), "Test Lead")
            self.assertEqual(leads_data.get('phone'), "111-222-3333")
            self.assertEqual(leads_data.get('email'), "testlead@gmail.com")

        # We need to Remove test json file created after test completes
        # Comment this last line in order to see output file after test case completes
        os.remove(self.test_output_file_path)

    def test_leads_parser_with_invalid_metadata_in_html(self):
        """
        Tests Leads Parser with invalid test file (HTML file with no valid <meta> having none of leads name, phone, email)
        :return:
        """
        # Invoke Parser Client
        lead_parser_client = LeadsParser(self.test_invalid_input_file_path,
                                         self.test_leads_meta_name_config,
                                         self.test_leads_meta_phone_config,
                                         self.test_leads_meta_email_config
                                         )

        # Read HTML file and Parse data
        # Here we are Checking if Log Statements Actually appear if in case of missing data within HTML File
        test_file_content = lead_parser_client.read_leads_html_file_contents()
        with self.assertLogs('leads_parser.leads_parser', level="INFO") as logger:
            test_leads_data = lead_parser_client.parse_leads_data(test_file_content)
            self.assertEqual(f"[LeadsParser] Leads Name Does not Exist"
                             f" due to invalid config: {self.test_leads_meta_name_config}", logger.records[0].msg)
            self.assertEqual(f"[LeadsParser] Leads Phone Does not Exist"
                             f" due to invalid config: {self.test_leads_meta_phone_config}", logger.records[1].msg)
            self.assertEqual(f"[LeadsParser] Leads Email Does not Exist"
                             f" due to invalid config: {self.test_leads_meta_email_config}", logger.records[2].msg)

            save_leads_data_to_file(self.test_invalid_output_file_path, test_leads_data)

        with open(self.test_invalid_output_file_path, "r") as test_output_file:
            leads_data = json.load(test_output_file)
            self.assertEqual(leads_data.get('name'), "")
            self.assertEqual(leads_data.get('phone'), "")
            self.assertEqual(leads_data.get('email'), "")

        # We need to Remove test json file created after test completes
        # Comment this last line in order to see output file after test case completes
        os.remove(self.test_invalid_output_file_path)
