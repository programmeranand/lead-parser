from settings import LEAD_HTML_FILE_PATH,\
    LEAD_EMAIL_META_TAG_CONFIG,\
    LEAD_NAME_META_TAG_CONFIG,\
    LEAD_PHONE_META_TAG_CONFIG,\
    OUTPUT_FILE_PATH

from leads_parser.leads_parser import LeadsParser
from helper import save_leads_data_to_file


def main():
    """
    Invokes Parser for Parsing HTML file containing leads information
    """
    leads_parser_client = LeadsParser(
        LEAD_HTML_FILE_PATH,
        LEAD_NAME_META_TAG_CONFIG,
        LEAD_PHONE_META_TAG_CONFIG,
        LEAD_EMAIL_META_TAG_CONFIG
    )

    lead_file_contents = leads_parser_client.read_leads_file_contents()
    leads_details = leads_parser_client.parse_leads_data(lead_file_contents)
    save_leads_data_to_file(OUTPUT_FILE_PATH, leads_details)


if __name__ == "__main__":
    main()
