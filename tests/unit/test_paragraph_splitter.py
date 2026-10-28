import pytest

from app.ingestion.chunking.paragraph_splitter import split_paragraphs


def test_keeps_short_paragraphs_together() -> None:
    assert split_paragraphs("First paragraph.\n\nSecond paragraph.") == [
        "First paragraph.\n\nSecond paragraph."
    ]


def test_splits_oversized_paragraph_to_maximum_length() -> None:
    chunks = split_paragraphs("a" * 1501)

    assert [len(chunk) for chunk in chunks] == [1500, 1]


def test_rejects_non_positive_maximum_length() -> None:
    with pytest.raises(ValueError, match="positive integer"):
        split_paragraphs("text", max_chars=0)
