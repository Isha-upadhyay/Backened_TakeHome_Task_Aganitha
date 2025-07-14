# PubMed Paper Filter CLI

This project provides a command-line interface (CLI) tool to fetch research papers from the PubMed database based on a user-defined query, identify authors affiliated with non-academic organizations such as pharmaceutical or biotech companies, and export the results in a structured CSV format.

The tool is built with modular and production-grade Python practices using Poetry for dependency management and packaging.

---

## Features

- Fetches PubMed paper IDs using `esearch` API based on a query.
- Retrieves paper metadata (title, authors, affiliations, email) using `efetch` API.
- Identifies non-academic authors by analyzing affiliations.
- Filters out university/hospital-based academic authors.
- Outputs results to a CSV file for further analysis.
- Modular codebase with CLI exposed as `get-papers-list`.
- Poetry-managed environment for easy packaging and installation.

---

## Use Case

This tool is useful for:
- Competitive intelligence in biotech and pharma sectors.
- Identifying research contributions from private organizations.
- Academic analysis of industry collaboration in biomedical literature.

---

## Installation

Ensure you have [Poetry](https://python-poetry.org/docs/) installed.

Clone the repository and install dependencies:

```bash
git clone https://github.com/Isha-upadhyay/Backened_TakeHome_Task_Aganitha
cd Backened_TakeHome_Task_Aganitha
poetry install
