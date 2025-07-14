
# PubMed Paper Filter CLI

This project is a Python-based command-line tool that searches for research papers from the PubMed database using a user-provided query. It filters papers that include at least one non-academic author affiliated with a pharmaceutical or biotech company and exports the results into a structured CSV file.

---

## How the Code is Organized

The project follows a modular structure:

```
backend-take-home/
├── cli/
│   └── main.py                # CLI entry point using argparse
│
├── get_papers/
│   ├── __init__.py
│   ├── pubmed.py              # Handles PubMed API integration (esearch and efetch)
│   ├── filters.py             # Contains logic to filter non-academic authors
│   └── utils.py               # Handles writing filtered results to a CSV
│
├── tests/
│   ├── test_filters.py        # Unit tests for author filtering logic
│   └── test_pubmed.py         # Unit tests for PubMed fetch functionality
│
├── pyproject.toml             # Poetry configuration for dependencies and CLI setup
├── poetry.lock                # Auto-generated lock file for exact dependency versions
├── README.md                  # Project documentation
└── .gitignore
```

---

## How to Install Dependencies and Execute the Program

### Prerequisites

- [Python 3.8+](https://www.python.org/)
- [Poetry](https://python-poetry.org/docs/#installation)

### Setup

1. Clone the repository:
```bash
git clone https://github.com/Isha-upadhyay/Backened_TakeHome_Task_Aganitha
cd Backened_TakeHome_Task_Aganitha
```

2. Install dependencies with Poetry:
```bash
poetry install
```

3. Run the command-line tool:
```bash
poetry run get-papers-list "your PubMed query" -f output.csv -d
```

### Example:
```bash
poetry run get-papers-list "covid AND cancer" -f papers.csv -d
```

- `"covid AND cancer"` → PubMed search query  
- `-f papers.csv` → Save results to `papers.csv`  
- `-d` → Show debug info

---

## Tools and Libraries Used

The following tools and libraries were used to build this program:

### Python Standard Library

- [`argparse`](https://docs.python.org/3/library/argparse.html): Used for parsing command-line arguments.
- [`unittest`](https://docs.python.org/3/library/unittest.html): Used for unit testing.

### Third-party Libraries

- [`requests`](https://pypi.org/project/requests/): Used for making HTTP calls to the PubMed API.
- [`Poetry`](https://python-poetry.org/): Used for dependency management, packaging, and defining the CLI interface.

### External APIs

- [`NCBI Entrez / PubMed API`](https://www.ncbi.nlm.nih.gov/books/NBK25501/): Used to search and fetch metadata from PubMed.

No LLMs, AI services, or proprietary APIs were used.

---

## Output

The tool outputs a CSV file with the following columns:

- PubmedID
- Title
- Publication Date
- Non-academic Author(s)
- Company Affiliation(s)
- Corresponding Author Email

Each row in the CSV corresponds to one paper that includes at least one author affiliated with a pharma or biotech organization.

---

## License

This project is released under the MIT License.

---

## Maintainer

**Isha Upadhyay**  
Email: ishaupadhyay3542870@gmail.com  
GitHub: [https://github.com/Isha-upadhyay](https://github.com/Isha-upadhyay)
