import csv
from typing import List, Dict

def save_results_to_csv(papers: List[Dict], filename: str) -> None:
    with open(filename, mode="w", newline="", encoding="utf-8") as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=[
            "PubmedID",
            "Title",
            "Publication Date",
            "Non-academic Author(s)",
            "Company Affiliation(s)",
            "Corresponding Author Email"
        ])
        writer.writeheader()

        for paper in papers:
            writer.writerow({
                "PubmedID": paper["PubmedID"],
                "Title": paper["Title"],
                "Publication Date": paper["Publication Date"],
                "Non-academic Author(s)": "; ".join(paper["NonAcademicAuthors"]),
                "Company Affiliation(s)": "; ".join(paper["CompanyAffiliations"]),
                "Corresponding Author Email": "; ".join(paper["Emails"])
            })
