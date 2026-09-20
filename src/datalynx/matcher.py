def record_exists(record: dict, records: list[dict], fields: list[str]) -> bool:
    """Return whether any record matches on every specified field.

    Raise ValueError if no fields are provided, or KeyError if the input record
    lacks a specified field. Candidate records missing a field do not match.
    """
    if not fields:
        raise ValueError("Provide at least one matching field")

    values = {field: record[field] for field in fields}

    for candidate in records:
        matches = True

        for field, value in values.items():
            if field not in candidate or candidate[field] != value:
                matches = False
                break

        if matches:
            return True

    return False
