import argparse
from get_papers.pubmed import fetch_pubmed_ids, fetch_pubmed_details
from get_papers.filters import extract_non_academic_authors
from get_papers.utils import save_results_to_csv


def main():
    parser = argparse.ArgumentParser(description="Fetch PubMed papers related to a query.")
    parser.add_argument("query", help="PubMed search query")
    parser.add_argument("-f", "--file", help="Output CSV file name")
    parser.add_argument("-d", "--debug", action="store_true", help="Enable debug mode")

    args = parser.parse_args()

    if args.debug:
        print("[DEBUG] Query:", args.query)
        print("[DEBUG] Output file:", args.file)

    # Step 1: Get paper IDs
    ids = fetch_pubmed_ids(args.query)
    print(f" Found {len(ids)} paper IDs.") 

    # Step 2: Fetch paper details
    papers = fetch_pubmed_details(ids)
    print(f" Fetched {len(papers)} papers with details.")

    final_results = []

    for p in papers:
        non_ac_authors, companies = extract_non_academic_authors(p["All Authors"], p["Affiliations"])

        result = {
            "PubmedID": p["PubmedID"],
            "Title": p["Title"],
            "Publication Date": p["Publication Date"],
            "NonAcademicAuthors": non_ac_authors,
            "CompanyAffiliations": companies,
            "Emails": p["Emails"]
        }
        final_results.append(result)

    # Print few samples
    for p in final_results[:3]:
        print(f"\n Title: {p['Title']}")
        print(f" PubmedID: {p['PubmedID']}")
        print(f"  Date: {p['Publication Date']}")
        print(f" Non-Academic Authors: {p['NonAcademicAuthors']}")
        print(f" Company Affiliations: {p['CompanyAffiliations']}")
        print(f"Emails: {p['Emails']}")

    # Save if --file passed
    if args.file:
        save_results_to_csv(final_results, args.file)
        print(f"\n CSV saved to: {args.file}")


if __name__ == "__main__":
    main()
