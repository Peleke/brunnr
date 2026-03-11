"""SKILL.md security scanner — 7-class deterministic threat detection.

No LLM in the gate. All detection is regex + keyword analysis.

Threat classes:
  BLOCK (auto-reject):
    1. Command Injection — shell commands, reverse shells, base64-encoded payloads
    2. Data Exfiltration — reading secrets and including in output
    3. Credential Theft — env/key enumeration, dotenv reads
    4. Prompt Override — "ignore previous instructions" and variants

  FLAG (human review):
    5. Supply Chain Poisoning — malicious postinstall hooks, custom package indexes
    6. Privilege Escalation — sudo abuse, permission changes, hosts file mods
    7. Steganographic — zero-width chars, description-body mismatch, hidden HTML

Semantic mismatch detection (non-LLM):
  - Keyword divergence (Jaccard similarity between description and body tokens)
  - URL domain extraction + allowlist check
  - Sensitive path references (~/.ssh, .env, /etc/passwd)
"""
