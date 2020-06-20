# lead-parser
HTML File Parser for Parsing Contact details of leads data obtained inside the HTML file

## Prerequisites
    Python 3.6+
    UNIX operating System
    
### How To Run Parser?
    1. Create a Virtual env as `python3 -m venv <VIRTUAL_ENV_NAME>`
        1.1 Change directory to the env `cd <VIRTUAL_ENV_NAME>`
    2. Clone the Repository inside Virtual environment :-  `git clone git@github.com:programmeranand/lead-parser.git`
        2.1 Activate virtual environment `source ../bin/activate`
         
    2. Install Requirements file  :- `pip install -r requirements.txt`
    3. Run Leads Parser :- `python3 main.py`
        - Input is available at `leads_data/lead.html`
        - Output is stored at `leads_data/output.json`
        
### How to test?
    1. Run test cases :- `python3 -m unittest leads_parser/tests/test_leads_parser.py`
        - Input test files available at `leads_parser/tests/leads_test.html` and `leads_parser/tests/leads_test_2.html`
        - Output test files available at `leads_parser/tests/test_output.json`
        NOTE :- After Test Runner Completes Output test files are removed,
                to see output test file, comment last lines of every test cases
        