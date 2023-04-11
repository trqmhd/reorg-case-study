## Getting Started

This project contains all of endpoints and data migration scripts related to Open Payment Search Tool.

### Prerequisites

Kindly ensure you have the following installed:

- [ ] [Python 3.9+](https://www.python.org/downloads/release/python-365/)
- [ ] [Pip](https://pip.pypa.io/en/stable/installing/)
- [ ] [Virtualenv](https://virtualenv.pypa.io/en/stable/installation/)


### Project Structure

    payment-search-tool-api
    ├── app.py
    ├── config.py
    ├── static
        ├── index.html
    ├── __init__.py
    ├── model.py
    ├── README.md
    ├── update_data.py
    ├── insert_data.py
    ├── route
        ├── export.py
        ├── typeahead.py
        ├── search.py
    ├── .env.template
    ├── requirements.txt
    ├── utils.py
    ├── .gitignore
    ├── test
        ├── test_typeahead.py


### How to Run
1. Clone the repository

2. Create a virtual environment inside project folder
```bash
    python -m venv venv
```

3. Activate the virtual environment
```bash
    source venv/bin/activate
```

5. Install Require Libraries
```bash
    pip install -r requirements.txt
```

6. Then Run the Flask application    
```bash
    python app.py
```