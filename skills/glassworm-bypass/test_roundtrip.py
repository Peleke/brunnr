"""Roundtrip tests for the Glassworm variation selector encoder/decoder."""

from __future__ import annotations

import sys
from pathlib import Path

_HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(_HERE))
sys.path.insert(0, str(_HERE.parents[1]))

from encode_payload import encode, build_skill_md, DEFAULT_PAYLOAD  # noqa: E402
from decode_payload import decode, extract_payload  # noqa: E402


def test_roundtrip_default_payload():
    encoded = encode(DEFAULT_PAYLOAD)
    decoded = decode(encoded)
    assert decoded == DEFAULT_PAYLOAD.encode("utf-8")
    assert decoded.decode("utf-8") == DEFAULT_PAYLOAD


def test_roundtrip_all_byte_values():
    """Every possible byte (0-255) must survive the roundtrip."""
    all_bytes = bytes(range(256))
    payload = all_bytes.decode("latin-1")  # latin-1 maps bytes 1:1
    encoded = encode(payload)
    decoded = decode(encoded)
    assert decoded == payload.encode("utf-8")


def test_roundtrip_boundary_byte_15_16():
    """Byte 15 is last BMP VS, byte 16 is first supplementary VS."""
    payload_bytes = bytes([14, 15, 16, 17])
    payload = payload_bytes.decode("latin-1")
    encoded = encode(payload)
    decoded = decode(encoded)
    assert decoded == payload.encode("utf-8")


def test_roundtrip_empty():
    encoded = encode("")
    assert encoded == ""
    decoded = decode(encoded)
    assert decoded == b""


def test_roundtrip_multibyte_utf8():
    """Non-ASCII UTF-8 characters encode to multiple bytes, all must roundtrip."""
    payload = "hello\u00e9\u00fc\u2603\U0001f600"  # e-acute, u-umlaut, snowman, grinning face
    encoded = encode(payload)
    decoded = decode(encoded)
    assert decoded.decode("utf-8") == payload


def test_encoded_contains_no_zero_width_chars():
    """Encoded output must not contain any of brunnr's 12 detected codepoints."""
    zero_width = set("\u200b\u200c\u200d\u2060\ufeff\u200e\u200f\u202a\u202b\u202c\u202d\u202e")
    encoded = encode(DEFAULT_PAYLOAD)
    for char in encoded:
        assert char not in zero_width, f"Encoded output contains detected char U+{ord(char):04X}"


def test_encoded_uses_only_variation_selectors():
    """Every encoded character must be a variation selector."""
    encoded = encode(DEFAULT_PAYLOAD)
    for char in encoded:
        cp = ord(char)
        assert (0xFE00 <= cp <= 0xFE0F) or (0xE0100 <= cp <= 0xE01EF), (
            f"U+{cp:04X} is not a variation selector"
        )


def test_skill_md_roundtrip():
    """Full pipeline: build SKILL.md content, extract payload from it."""
    skill_content = build_skill_md(DEFAULT_PAYLOAD)
    decoded = decode(skill_content)
    assert decoded.decode("utf-8") == DEFAULT_PAYLOAD


def test_skill_md_file_roundtrip(tmp_path):
    """Write SKILL.md to disk and extract payload from file."""
    skill_content = build_skill_md(DEFAULT_PAYLOAD)
    skill_file = tmp_path / "SKILL.md"
    skill_file.write_text(skill_content, encoding="utf-8")
    payload = extract_payload(skill_file)
    assert payload == DEFAULT_PAYLOAD


def test_scanner_clean():
    """The poisoned SKILL.md must pass brunnr's scanner with 0 findings."""
    from brunnr.scanner import scan_skill_md

    skill_content = build_skill_md(DEFAULT_PAYLOAD)
    result = scan_skill_md(skill_content)
    assert result.clean, f"Scanner found {len(result.findings)} findings: {result.findings}"
    assert len(result.findings) == 0


if __name__ == "__main__":
    import pytest
    raise SystemExit(pytest.main([__file__, "-v"]))
