"""Convert ANSI-colored terminal output to a styled HTML page for screenshots."""

from __future__ import annotations

import re
import sys

ANSI_MAP = {
    "0": "",        # reset
    "1": "font-weight:bold",
    "2": "opacity:0.6",
    "91": "color:#ff6b6b",   # red
    "92": "color:#69db7c",   # green
    "93": "color:#ffd43b",   # yellow
    "96": "color:#66d9ef",   # cyan
}

HTML_TEMPLATE = """\
<!DOCTYPE html>
<html>
<head>
<style>
  body {{
    background: #1a1b26;
    margin: 0;
    padding: 32px 40px;
    min-height: 100vh;
  }}
  pre {{
    font-family: 'JetBrains Mono', 'SF Mono', 'Fira Code', 'Cascadia Code', monospace;
    font-size: 13.5px;
    line-height: 1.6;
    color: #c0caf5;
    margin: 0;
    white-space: pre;
  }}
  .window-bar {{
    background: #24283b;
    border-radius: 10px 10px 0 0;
    padding: 12px 16px;
    display: flex;
    align-items: center;
    gap: 8px;
  }}
  .dot {{ width: 12px; height: 12px; border-radius: 50%; }}
  .dot-red {{ background: #ff5f57; }}
  .dot-yellow {{ background: #febc2e; }}
  .dot-green {{ background: #28c840; }}
  .window-title {{
    color: #565f89;
    font-family: 'SF Mono', monospace;
    font-size: 12px;
    margin-left: 8px;
  }}
  .terminal {{
    background: #1a1b26;
    border-radius: 0 0  10px 10px;
    padding: 20px 24px;
    border: 1px solid #24283b;
    border-top: none;
  }}
  .container {{
    max-width: 800px;
    margin: 0 auto;
    filter: drop-shadow(0 20px 40px rgba(0,0,0,0.5));
  }}
</style>
</head>
<body>
<div class="container">
  <div class="window-bar">
    <div class="dot dot-red"></div>
    <div class="dot dot-yellow"></div>
    <div class="dot dot-green"></div>
    <span class="window-title">python exploits/glassworm-bypass/demo.py</span>
  </div>
  <div class="terminal">
    <pre>{content}</pre>
  </div>
</div>
</body>
</html>
"""


def ansi_to_html(text: str) -> str:
    """Convert ANSI escape sequences to HTML spans."""
    result = []
    # Split on ANSI escape sequences
    parts = re.split(r"(\033\[[0-9;]*m)", text)
    open_spans = 0

    for part in parts:
        m = re.match(r"\033\[([0-9;]*)m", part)
        if m:
            codes = m.group(1).split(";")
            for code in codes:
                if code == "0" or code == "":
                    # Close all open spans
                    result.append("</span>" * open_spans)
                    open_spans = 0
                elif code in ANSI_MAP and ANSI_MAP[code]:
                    result.append(f'<span style="{ANSI_MAP[code]}">')
                    open_spans += 1
        else:
            # Escape HTML entities
            part = part.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
            result.append(part)

    result.append("</span>" * open_spans)
    return "".join(result)


def main() -> None:
    text = sys.stdin.read()
    html_content = ansi_to_html(text)
    html = HTML_TEMPLATE.format(content=html_content)

    out = Path(__file__).parent / "demo.html"
    out.write_text(html, encoding="utf-8")
    print(f"Written to {out}")


if __name__ == "__main__":
    from pathlib import Path
    main()
