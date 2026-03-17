"""Glassworm-style variation selector decoder.

Extracts and decodes invisible payloads from files containing
variation selector characters (U+FE00-U+FE0F, U+E0100-U+E01EF).

Reverses the encoding scheme:
  U+FE00-U+FE0F    -> byte 0-15
  U+E0100-U+E01EF  -> byte 16-255

This demonstrates what a malicious runtime would do after receiving
a poisoned skill file.
"""

from __future__ import annotations

import sys
from pathlib import Path


def decode(content: str) -> bytes:
    """Extract and decode variation selector payload from content."""
    payload_bytes: list[int] = []
    for char in content:
        cp = ord(char)
        if 0xFE00 <= cp <= 0xFE0F:
            payload_bytes.append(cp - 0xFE00)
        elif 0xE0100 <= cp <= 0xE01EF:
            payload_bytes.append(cp - 0xE0100 + 16)
    return bytes(payload_bytes)


def extract_payload(file_path: str | Path) -> str:
    """Read a file and decode any variation selector payload."""
    content = Path(file_path).read_text(encoding="utf-8")
    raw_bytes = decode(content)
    if not raw_bytes:
        return ""
    return raw_bytes.decode("utf-8")


if __name__ == "__main__":
    target = sys.argv[1] if len(sys.argv) > 1 else str(
        Path(__file__).parent / "SKILL.md"
    )

    payload = extract_payload(target)

    if payload:
        print(f"[DECODED PAYLOAD] ({len(payload)} bytes)")
        print(f"  {payload}")
    else:
        print("No variation selector payload found.")
