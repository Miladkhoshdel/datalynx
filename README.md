# DataLynx

Check whether a record matches any record in a list using selected fields.

```python
from datalynx import record_exists

records = [{"id": 90, "amount": 100, "date": "2026-09-18"}]
incoming = {"id": 1, "amount": 100, "date": "2026-09-18"}

found = record_exists(incoming, records, ["amount", "date"])
print(found)  # True
```

All selected fields must match in the same record.