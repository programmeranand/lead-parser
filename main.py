from helper import save_leads_data_to_file
from leads_parser.leads_parser import LeadsParser
from settings import (LEAD_EMAIL_META_TAG_CONFIG, LEAD_HTML_FILE_PATH,
                      LEAD_NAME_META_TAG_CONFIG, LEAD_PHONE_META_TAG_CONFIG,
                      OUTPUT_FILE_PATH)


def main():
    """
    Invokes Parser for Parsing HTML file containing leads information
    **NOTE** :- The Parser Assumes <meta> tags are present with correct name attributes in the HTML file Provided
    """
    # Invoke Parser client
    leads_parser_client = LeadsParser(
        LEAD_HTML_FILE_PATH,
        LEAD_NAME_META_TAG_CONFIG,
        LEAD_PHONE_META_TAG_CONFIG,
        LEAD_EMAIL_META_TAG_CONFIG
    )

    # Read HTML file and Parse contents
    lead_file_contents = leads_parser_client.read_leads_html_file_contents()
    leads_details = leads_parser_client.parse_leads_data(lead_file_contents)

    # Save the Parsed Data into Output file path configured
    save_leads_data_to_file(OUTPUT_FILE_PATH, leads_details)


if __name__ == "__main__":
    main()
