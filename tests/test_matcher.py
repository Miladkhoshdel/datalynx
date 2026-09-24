import pytest

from datalynx import find_matching_record, record_exists


def test_find_matching_record_returns_first_matching_record():
    """Return the first candidate that matches every selected field."""
    first = {"id": 90, "amount": 100, "date": "2026-09-18"}
    second = {"id": 91, "amount": 100, "date": "2026-09-18"}
    records = [{"id": 89, "amount": 100, "date": "2026-09-19"}, first, second]

    assert find_matching_record(
        {"id": 1, "amount": 100, "date": "2026-09-18"},
        records,
        ["amount", "date"],
    ) is first


def test_find_matching_record_returns_none_when_fields_match_different_records():
    """Do not combine matching values from different candidates."""
    records = [
        {"amount": 100, "date": "2026-09-18"},
        {"amount": 200, "date": "2026-09-19"},
    ]

    assert find_matching_record(
        {"amount": 100, "date": "2026-09-19"}, records, ["amount", "date"]
    ) is None


def test_find_matching_record_skips_candidate_with_missing_field():
    """Skip candidates missing a selected field and continue searching."""
    match = {"id": 2, "status": "pending"}

    assert find_matching_record(
        {"status": "pending"}, [{"id": 1}, match], ["status"]
    ) is match


def test_find_matching_record_rejects_empty_fields():
    """Reject a lookup with no fields to compare."""
    with pytest.raises(ValueError, match="at least one matching field"):
        find_matching_record({"id": 1}, [{"id": 1}], [])


def test_find_matching_record_raises_when_input_record_lacks_field():
    """Raise KeyError when the input lacks a selected field."""
    with pytest.raises(KeyError, match="status"):
        find_matching_record({"id": 1}, [{"status": "pending"}], ["status"])


def test_record_exists_with_multiple_fields():
    """Require all selected fields to match within one candidate."""
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
    """Find a match using one selected field despite other differences."""
    records = [{"id": 1, "status": "pending"}]

    assert record_exists({"id": 2, "status": "pending"}, records, ["status"])


def test_record_exists_returns_false_for_empty_records():
    """Return False when there are no candidates to search."""
    assert not record_exists({"id": 1}, [], ["id"])


def test_record_exists_rejects_empty_fields():
    """Reject an existence check with no fields to compare."""
    with pytest.raises(ValueError, match="at least one matching field"):
        record_exists({"id": 1}, [{"id": 1}], [])


def test_record_exists_raises_when_input_record_lacks_field():
    """Raise KeyError when the input lacks a selected field."""
    with pytest.raises(KeyError, match="status"):
        record_exists({"id": 1}, [{"id": 1, "status": "pending"}], ["status"])


def test_record_exists_skips_candidate_that_lacks_field():
    """Ignore incomplete candidates while checking later records."""
    records = [
        {"id": 1},
        {"id": 2, "status": "pending"},
    ]

    assert record_exists({"status": "pending"}, records, ["status"])


def test_record_exists_accepts_duplicate_fields():
    """Allow repeated field names without changing the match result."""
    records = [{"id": 1, "status": "pending"}]

    assert record_exists(
        {"id": 2, "status": "pending"},
        records,
        ["status", "status"],
    )
