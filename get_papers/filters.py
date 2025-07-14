from typing import List, Tuple

# Heuristics: if affiliation doesn't contain these academic keywords, it's likely non-academic
ACADEMIC_KEYWORDS = [
    "university", "institute", "school", "college", "faculty",
    "hospital", "center", "centre", "department", "clinic", "research foundation"
]

def is_non_academic(affiliation: str) -> bool:
    aff_lower = affiliation.lower()
    return not any(keyword in aff_lower for keyword in ACADEMIC_KEYWORDS)

def extract_non_academic_authors(authors: List[str], affiliations: List[str]) -> Tuple[List[str], List[str]]:
    non_academic_authors = []
    company_names = []

    for i, aff in enumerate(affiliations):
        if is_non_academic(aff):
            author = authors[i] if i < len(authors) else f"Author_{i}"
            non_academic_authors.append(author)
            company_names.append(aff)

    return non_academic_authors, company_names
