# DataLynx

DataLynx checks whether a record matches any record in a list on the fields you choose, and can return the first matching record. All selected fields must match in the **same** record.

## Requirements

- Python 3.10 or newer

## Installation

Install the package from [PyPI](https://pypi.org/project/datalynx/) with pip:

```bash
python -m pip install datalynx
```

To install a local checkout instead, run this from the project directory:

```bash
python -m pip install .
```

## Usage

```python
from datalynx import find_matching_record, record_exists

records = [
    {"id": 90, "amount": 100, "date": "2026-09-18"},
    {"id": 91, "amount": 200, "date": "2026-09-19"},
]
incoming = {"id": 1, "amount": 100, "date": "2026-09-18"}

found = record_exists(incoming, records, ["amount", "date"])
print(found)  # True

match = find_matching_record(incoming, records, ["amount", "date"])
print(match)  # {"id": 90, "amount": 100, "date": "2026-09-18"}
```

The `id` values can differ because `id` is not in the selected fields. If no single record matches every selected field, `record_exists` returns `False` and `find_matching_record` returns `None`.

## API

### `record_exists(record, records, fields) -> bool`

- `record`: the dictionary to look for.
- `records`: a list of dictionaries to search.
- `fields`: a nonempty list of keys to compare.

The function returns `True` on the first full match and `False` if none is found. An empty `fields` list raises `ValueError`. If `record` lacks a selected field, it raises `KeyError`; a candidate that lacks a selected field simply does not match.

### `find_matching_record(record, records, fields) -> dict | None`

Uses the same matching and error rules as `record_exists`. Returns the first matching dictionary from `records`, or `None` if there is no match. The returned value is the original dictionary, not a copy.

## Development

Install the development dependencies from a local checkout and run the tests:

```bash
python -m pip install -e ".[dev]"
python -m pytest
```

## License

DataLynx is licensed under the [MIT License](LICENSE).
