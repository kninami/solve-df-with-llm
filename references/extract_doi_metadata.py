#!/usr/bin/env python3

from __future__ import annotations

import csv
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parent
OUTPUT_PATH = ROOT / "doi_metadata.csv"
DOI_RE = re.compile(r"10\.\d{4,9}/[-._;()/:A-Za-z0-9]+", re.IGNORECASE)
URL_RE = re.compile(r"https?://\S+")
YEAR_RE = re.compile(r"\b(?:19|20)\d{2}\b|undated|n\.d\.", re.IGNORECASE)


def normalize_space(value: str) -> str:
    return " ".join(value.replace("\n", " ").replace("\t", " ").split())


def normalize_doi(value: str) -> str:
    match = DOI_RE.search(value)
    if not match:
        return ""
    return match.group(0).rstrip(".,;")


def normalize_url(value: str) -> str:
    match = URL_RE.search(value)
    if not match:
        return ""
    return match.group(0).rstrip(".,;")


def cleanup_text(value: str) -> str:
    cleaned = value.strip().rstrip(",")
    if cleaned.startswith("{") and cleaned.endswith("}"):
        cleaned = cleaned[1:-1]
    elif cleaned.startswith('"') and cleaned.endswith('"'):
        cleaned = cleaned[1:-1]
    cleaned = cleaned.replace(r"\_", "_")
    cleaned = cleaned.replace(r"\&", "&")
    cleaned = cleaned.replace(r"\i", "i")
    cleaned = cleaned.replace("“", '"').replace("”", '"')
    cleaned = cleaned.replace("’", "'")
    cleaned = re.sub(r"[{}]", "", cleaned)
    replacements = {
        r"\'a": "á",
        r"\'e": "é",
        r"\'i": "í",
        r"\'o": "ó",
        r"\'u": "ú",
        r"\'A": "Á",
        r"\'E": "É",
        r"\'I": "Í",
        r"\'O": "Ó",
        r"\'U": "Ú",
        r"\`a": "à",
        r"\`e": "è",
        r"\`i": "ì",
        r"\`o": "ò",
        r"\`u": "ù",
        r"\`A": "À",
        r"\`E": "È",
        r"\`I": "Ì",
        r"\`O": "Ò",
        r"\`U": "Ù",
    }
    for latex, unicode_char in replacements.items():
        cleaned = cleaned.replace(latex, unicode_char)
    return normalize_space(cleaned)


def empty_record(entry_type: str) -> dict[str, str]:
    return {
        "entry_type": entry_type,
        "citation_key": "",
        "title": "",
        "authors": "",
        "year": "",
        "container_title": "",
        "publisher": "",
        "organization": "",
        "volume": "",
        "issue": "",
        "pages": "",
        "doi": "",
        "doi_url": "",
        "url": "",
        "note": "",
        "raw_reference": "",
        "raw_bib": "",
    }


def parse_bib_fields(text: str) -> tuple[str, str, dict[str, str]]:
    header_match = re.search(r"@(\w+)\s*\{\s*([^,]+)\s*,", text, re.DOTALL)
    if not header_match:
        raise ValueError("Invalid BibTeX entry header")

    entry_type = header_match.group(1).strip().lower()
    citation_key = header_match.group(2).strip()
    body = text[header_match.end() :]
    closing_index = body.rfind("}")
    if closing_index != -1:
        body = body[:closing_index]

    fields: dict[str, str] = {}
    index = 0
    while index < len(body):
        while index < len(body) and body[index] in " \t\r\n,":
            index += 1
        if index >= len(body):
            break

        key_start = index
        while index < len(body) and (body[index].isalnum() or body[index] in "_-"):
            index += 1
        key = body[key_start:index].strip().lower()

        while index < len(body) and body[index] in " \t\r\n":
            index += 1
        if index >= len(body) or body[index] != "=":
            break
        index += 1

        while index < len(body) and body[index] in " \t\r\n":
            index += 1
        if index >= len(body):
            break

        if body[index] == "{":
            depth = 0
            value_start = index
            while index < len(body):
                char = body[index]
                if char == "{":
                    depth += 1
                elif char == "}":
                    depth -= 1
                    if depth == 0:
                        index += 1
                        break
                index += 1
            raw_value = body[value_start:index]
        elif body[index] == '"':
            value_start = index
            index += 1
            escaped = False
            while index < len(body):
                char = body[index]
                if char == '"' and not escaped:
                    index += 1
                    break
                escaped = char == "\\" and not escaped
                if char != "\\":
                    escaped = False
                index += 1
            raw_value = body[value_start:index]
        else:
            value_start = index
            while index < len(body) and body[index] not in ",\r\n":
                index += 1
            raw_value = body[value_start:index]

        fields[key] = cleanup_text(raw_value)

        while index < len(body) and body[index] in " \t\r\n":
            index += 1
        if index < len(body) and body[index] == ",":
            index += 1

    return entry_type, citation_key, fields


def format_bib_authors(raw_author: str) -> str:
    if not raw_author:
        return ""
    parts = [normalize_space(part) for part in raw_author.split(" and ")]
    return "; ".join(part for part in parts if part)


def parse_bib(path: Path) -> dict[str, str]:
    entry_type, citation_key, fields = parse_bib_fields(path.read_text(encoding="utf-8"))
    record = empty_record(entry_type)
    record.update(
        {
            "citation_key": citation_key,
            "title": fields.get("title", ""),
            "authors": format_bib_authors(fields.get("author", "")),
            "year": fields.get("year", ""),
            "container_title": fields.get("journal", "")
            or fields.get("booktitle", "")
            or fields.get("publisher", "")
            or fields.get("school", ""),
            "publisher": fields.get("publisher", ""),
            "organization": fields.get("organization", ""),
            "volume": fields.get("volume", ""),
            "issue": fields.get("number", ""),
            "pages": fields.get("pages", ""),
            "note": fields.get("note", ""),
            "url": normalize_url(fields.get("url", "")),
            "raw_bib": normalize_space(path.read_text(encoding="utf-8")),
        }
    )

    doi = normalize_doi(fields.get("doi", "") or fields.get("url", ""))
    if doi:
        record["doi"] = doi
        record["doi_url"] = f"https://doi.org/{doi}"

    return record


def split_before_url(text: str) -> str:
    url_match = URL_RE.search(text)
    if not url_match:
        return text.strip()
    return text[: url_match.start()].rstrip(" ,.;")


def clean_tail_segment(text: str) -> str:
    text = split_before_url(text)
    text = re.sub(r"\b(?:Available at:|Retrieved from|doi:)\s*$", "", text, flags=re.IGNORECASE)
    return text.strip(" ,.;")


def pick_title_and_container(rest: str) -> tuple[str, str]:
    cleaned = clean_tail_segment(rest)
    if not cleaned:
        return "", ""

    if ". In " in cleaned:
        title, container = cleaned.split(". In ", 1)
        return title.strip(" ,.;"), container.strip(" ,.;")

    if ". Available at:" in cleaned:
        parts = [part.strip(" ,.;") for part in cleaned.split(". ") if part.strip(" ,.;")]
        if len(parts) >= 2:
            return parts[0], parts[1]

    parts = [part.strip(" ,.;") for part in cleaned.split(". ") if part.strip(" ,.;")]
    if len(parts) >= 2:
        return parts[0], parts[1]

    comma_parts = [part.strip(" ,.;") for part in cleaned.split(",") if part.strip(" ,.;")]
    if len(comma_parts) >= 2:
        return comma_parts[0], comma_parts[1]

    return cleaned, ""


def normalize_txt_authors(value: str) -> str:
    authors = value.strip(" ,.;")
    authors = re.sub(r"\s*&\s*", " and ", authors)
    authors = re.sub(r"\s+and\s+", "; ", authors)
    authors = re.sub(r";\s*", "; ", authors)
    return normalize_space(authors)


def parse_txt(path: Path) -> dict[str, str]:
    raw = normalize_space(path.read_text(encoding="utf-8"))
    normalized = raw.replace("“", '"').replace("”", '"').replace("’", "'")
    record = empty_record("text_reference")
    record["raw_reference"] = raw
    record["url"] = normalize_url(normalized)

    doi = normalize_doi(normalized)
    if doi:
        record["doi"] = doi
        record["doi_url"] = f"https://doi.org/{doi}"

    if normalized.startswith("http"):
        record["entry_type"] = "url_reference"
        record["url"] = record["url"] or normalized.rstrip(".,;")
        return record

    patterns = [
        re.compile(
            r'^(?P<authors>.+?)\s*\((?P<year>\d{4}|undated|n\.d\.)\)\s*[,.]?\s*(?P<rest>.+)$',
            re.IGNORECASE,
        ),
        re.compile(
            r"^(?P<authors>.+?),\s*(?P<year>\d{4}|undated|n\.d\.)[,.]\s*(?P<rest>.+)$",
            re.IGNORECASE,
        ),
        re.compile(
            r"^(?P<authors>.+?)\s+(?P<year>\d{4}|undated|n\.d\.)\s*,\s*(?P<rest>.+)$",
            re.IGNORECASE,
        ),
    ]

    for pattern in patterns:
        match = pattern.match(normalized)
        if not match:
            continue

        record["authors"] = normalize_txt_authors(match.group("authors"))
        record["year"] = match.group("year")
        title, container = pick_title_and_container(match.group("rest"))
        record["title"] = title
        record["container_title"] = container

        lowered = match.group("rest").lower()
        if "chapter" in lowered and not container:
            record["container_title"] = clean_tail_segment(match.group("rest"))
        elif "available at:" in lowered and not container:
            record["container_title"] = "Web resource"

        if doi:
            record["entry_type"] = "doi_text_reference"
        elif record["url"]:
            record["entry_type"] = "web_reference"
        else:
            record["entry_type"] = "citation_text_reference"
        return record

    if record["url"] and not record["doi"]:
        year_match = YEAR_RE.search(normalized)
        if year_match:
            record["year"] = year_match.group(0)
        before_url = split_before_url(normalized)
        if before_url and before_url != normalized:
            record["title"] = before_url.strip(" ,.;")
        record["entry_type"] = "web_reference"
        return record

    year_match = YEAR_RE.search(normalized)
    if year_match:
        record["year"] = year_match.group(0)
        before_year = normalized[: year_match.start()].strip(" ,.;")
        after_year = normalized[year_match.end() :].lstrip(" ,.;")
        if before_year:
            record["authors"] = normalize_txt_authors(before_year)
        if after_year:
            title, container = pick_title_and_container(after_year)
            record["title"] = title
            record["container_title"] = container

    elif normalized:
        title, container = pick_title_and_container(normalized)
        record["title"] = title
        record["container_title"] = container

    if doi:
        record["entry_type"] = "doi_text_reference"
    elif record["url"]:
        record["entry_type"] = "web_reference"

    return record


def merge_records(reference_id: str, paths: list[Path]) -> dict[str, str]:
    bib_path = next((path for path in paths if path.suffix.lower() == ".bib"), None)
    txt_path = next((path for path in paths if path.suffix.lower() == ".txt"), None)

    primary_source = bib_path.name if bib_path else txt_path.name
    merged = empty_record("unknown_reference")
    merged["reference_id"] = reference_id
    merged["source_file"] = primary_source or ""
    merged["available_files"] = "; ".join(path.name for path in sorted(paths))

    if txt_path:
        txt_record = parse_txt(txt_path)
        merged.update({key: value for key, value in txt_record.items() if value})

    if bib_path:
        bib_record = parse_bib(bib_path)
        merged.update({key: value for key, value in bib_record.items() if value})

    if not merged.get("doi") and merged.get("url"):
        doi = normalize_doi(merged["url"])
        if doi:
            merged["doi"] = doi
            merged["doi_url"] = f"https://doi.org/{doi}"

    return merged


def main() -> None:
    grouped: dict[str, list[Path]] = {}
    for path in sorted(ROOT.glob("DFCite-*.*")):
        if path.suffix.lower() not in {".txt", ".bib"}:
            continue
        grouped.setdefault(path.stem, []).append(path)

    rows = [merge_records(reference_id, paths) for reference_id, paths in sorted(grouped.items())]

    fieldnames = [
        "reference_id",
        "source_file",
        "available_files",
        "entry_type",
        "citation_key",
        "title",
        "authors",
        "year",
        "container_title",
        "publisher",
        "organization",
        "volume",
        "issue",
        "pages",
        "doi",
        "doi_url",
        "url",
        "note",
        "raw_reference",
        "raw_bib",
    ]

    with OUTPUT_PATH.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)

    doi_count = sum(1 for row in rows if row["doi"])
    print(f"Wrote {len(rows)} references to {OUTPUT_PATH.name} ({doi_count} with DOI)")


if __name__ == "__main__":
    main()
