"""Paragraph-aware text splitting with a maximum chunk length."""

from collections.abc import Iterator


def split_paragraphs(text: str, max_chars: int = 1500) -> list[str]:
    """Split text at paragraph boundaries without exceeding ``max_chars``."""
    if max_chars < 1:
        raise ValueError("max_chars must be a positive integer")

    paragraphs = (part.strip() for part in text.split("\n\n"))
    chunks: list[str] = []
    current = ""

    def split_long_paragraph(paragraph: str) -> Iterator[str]:
        for offset in range(0, len(paragraph), max_chars):
            yield paragraph[offset : offset + max_chars]

    for paragraph in paragraphs:
        if not paragraph:
            continue
        parts = split_long_paragraph(paragraph) if len(paragraph) > max_chars else (paragraph,)
        for part in parts:
            candidate = f"{current}\n\n{part}" if current else part
            if len(candidate) <= max_chars:
                current = candidate
            else:
                if current:
                    chunks.append(current)
                current = part

    if current:
        chunks.append(current)
    return chunks

