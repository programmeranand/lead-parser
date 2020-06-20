import json


def save_leads_data_to_file(output_file_path, leads_data):
    """
    Saves Leads data into a JSON file
    :param leads_data: leads data to be saved
    :param output_file_path: output file location
    """
    output_file = open(output_file_path, "w")
    json.dump(leads_data, output_file, indent=4)
