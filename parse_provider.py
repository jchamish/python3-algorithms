import re

"""
The Requirements
Write a function parse_provider_data(raw_string) that returns a dictionary/object.

Name: Should be {"first": "...", "last": "..."}.

Specialty: A string (e.g., "Therapist").

NPI: A 10-digit unique identifier.

The "Messy" Input Examples
The input strings are inconsistent and may contain noise:

"NPI:1234567890;NAME:John Doe;SPEC:Therapist" (Standard semicolon-delimited)

"NAME:Jane Smith|NPI:0987654321|SPEC:Psychologist" (Pipe-delimited)

"SPEC:Counselor;NPI:1122334455;NAME:Dr. Robert 'Bob' Brown" (Contains titles and nicknames)

Constraints & Edge Cases
NPI Validation: The NPI must be exactly 10 digits. If it's missing or invalid, return an error or None.

Name Cleaning: Remove professional titles like "Dr." or "MD" and ignore nicknames in quotes.

Extensibility: Your solution should easily handle a new delimiter (like a comma) without rewriting the whole logic.
"""


def parse_provider_data(raw_string):
    normalized = raw_string.replace('|', ';').replace(',',';')

    # Extract parts using a dict
    parts = {}
    for item in normalized.split(';'):
        if ':' in item:
            key, val = item.split(':', 1)
            parts[key.strip().upper()] = val.strip()
        
    full_name = parts.get('NAME', "")
    clean_name = re.sub(r"Dr\.\s*|MD\s*|'.*?'", "", full_name).strip()
    first_name, last_name = clean_name.split(' ', 1)
    npi: str = parts.get('NPI', "")

    if len(npi) < 10:
        return None

    return {
        "first_name": first_name,
        "last_name": last_name,
        "npi": npi,
        "specialty": parts.get('SPEC')
    }

###


KV_PATTERN = re.compile(r'(?P<key>NAME|NPI|SPEC)s\*:\s*(?P<vale>[^;|]+)')
CLEAN_NAME_PATTERN = re.compile(r"(?i)\b(Dr|MD|PhD|Esq)\b\.?['\"].*?['\"]")

from typing import Dict

def parse_provider_data_v2(raw_string: str) -> Dict:

    raw_parts = {match.group('key').upper():match.group('value').strip()
                 for match in KV_PATTERN.finditer(raw_string)}

    # 2. Extract and Validate NPI (Must be 10 digits)
    npi = raw_parts.get('NPI', "")
    if not (npi.isdigit() and len(npi) == 10):
        npi = None  # Or raise a custom ValidationError for a Senior-level approach
        
    # 3. Clean the Name
    full_name = raw_parts.get('NAME', "")
    # Remove titles and nicknames using our pre-compiled cleaner
    clean_name = CLEAN_NAME_PATTERN.sub("", full_name).strip()
    
    # Simple split for first/last logic
    name_parts = clean_name.split()
    first_name = name_parts[0] if name_parts else ""
    last_name = name_parts[-1] if len(name_parts) > 1 else ""

    return {
        "first_name": first_name,
        "last_name": last_name,
        "npi": npi,
        "specialty": raw_parts.get('SPEC', "Unknown"),
        "is_valid": npi is not None
    }





t = ["NPI:1234567890;NAME:John Doe;SPEC:Therapist",
"NAME:Jane Smith|NPI:0987654321|SPEC:Psychologist",
"SPEC:Counselor;NPI:1122334455;NAME:Dr. Robert 'Bob' Brown"]

for elm in t:
    print(f"parsed: {parse_provider_data_v2(elm)}")




