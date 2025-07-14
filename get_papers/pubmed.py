import requests
import xml.etree.ElementTree as ET
from typing import List, Dict

BASE_URL = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/"

def fetch_pubmed_ids(query: str, max_results: int = 20) -> List[str]:
    url = f"{BASE_URL}esearch.fcgi"
    params = {
        "db": "pubmed",
        "term": query,
        "retmode": "json",
        "retmax": max_results
    }
    response = requests.get(url, params=params)
    response.raise_for_status()
    data = response.json()
    return data["esearchresult"].get("idlist", [])

def fetch_pubmed_details(pubmed_ids: List[str]) -> List[Dict]:
    url = f"{BASE_URL}efetch.fcgi"
    params = {
        "db": "pubmed",
        "id": ",".join(pubmed_ids),
        "retmode": "xml"
    }
    response = requests.get(url, params=params)
    response.raise_for_status()
    root = ET.fromstring(response.content)

    results = []
    for article in root.findall(".//PubmedArticle"):
        pmid = article.findtext(".//PMID")
        title = article.findtext(".//ArticleTitle")
        pub_date = article.findtext(".//PubDate/Year") or "Unknown"

        authors = []
        affiliations = []
        emails = []

        for author in article.findall(".//Author"):
            aff = author.findtext(".//AffiliationInfo/Affiliation")
            if aff:
                affiliations.append(aff)
                if "@" in aff:
                    emails.append(aff.split()[-1])
            last = author.findtext("LastName") or ""
            fore = author.findtext("ForeName") or ""
            full_name = f"{fore} {last}".strip()
            authors.append(full_name)

        results.append({
            "PubmedID": pmid,
            "Title": title,
            "Publication Date": pub_date,
            "All Authors": authors,
            "Affiliations": affiliations,
            "Emails": emails
        })

    return results
