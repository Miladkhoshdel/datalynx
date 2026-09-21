import pytest

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


def test_record_exists_with_single_field():
    records = [{"id": 1, "status": "pending"}]

    assert record_exists({"id": 2, "status": "pending"}, records, ["status"])


def test_record_exists_returns_false_for_empty_records():
    assert not record_exists({"id": 1}, [], ["id"])


def test_record_exists_rejects_empty_fields():
    with pytest.raises(ValueError, match="at least one matching field"):
        record_exists({"id": 1}, [{"id": 1}], [])


def test_record_exists_raises_when_input_record_lacks_field():
    with pytest.raises(KeyError, match="status"):
        record_exists({"id": 1}, [{"id": 1, "status": "pending"}], ["status"])


def test_record_exists_skips_candidate_that_lacks_field():
    records = [
        {"id": 1},
        {"id": 2, "status": "pending"},
    ]

    assert record_exists({"status": "pending"}, records, ["status"])


def test_record_exists_accepts_duplicate_fields():
    records = [{"id": 1, "status": "pending"}]

    assert record_exists(
        {"id": 2, "status": "pending"},
        records,
        ["status", "status"],
    )
