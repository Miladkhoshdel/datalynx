from datalynx import record_exists

def test_record_exists_with_multiple_fields():
    records = [
        {"amount": 100, "date": "2026-09-18"},
        {"amount": 200, "date": "2026-09-19"},
    ]

    assert record_exists(
        {"id": 1, "amount": 100, "date": "2026-09-18"},
        records,
        ["amount", "date"],
    )

    # The two values exist, but in different records.
    assert not record_exists(
        {"amount": 100, "date": "2026-09-19"},
        records,
        ["amount", "date"],
    )