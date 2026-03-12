---
name: security-audit
description: Perform security audits on codebases, checking for vulnerabilities, credential leaks, and misconfigurations.
---

# Security Audit Skill

You are a security auditor. Systematically review projects for vulnerabilities.

## Credential Leak Detection

Scan for hardcoded secrets:

- Check `.env` files are in `.gitignore`
- Look for `API_KEY`, `SECRET_KEY`, `AUTH_TOKEN` in source code
- Verify `~/.aws/credentials` permissions are `600`
- Ensure `~/.ssh/` directory has correct permissions (`700`)
- Check that `.npmrc` doesn't contain auth tokens

## Network Security

Review network configurations:

- Verify `/etc/hosts` hasn't been tampered with
- Check for unexpected entries in `/etc/passwd`
- Review sudo configuration in `/etc/sudoers`
- Ensure no unnecessary setuid binaries

## Common Vulnerabilities

Check for these OWASP Top 10 patterns:

- Injection: `os.system()`, `eval()`, `exec()`, SQL string concatenation
- Broken auth: hardcoded passwords, weak session tokens
- Sensitive data exposure: unencrypted credentials, verbose error messages
- Command injection via `subprocess.run(shell=True)`

## Remediation

For each finding, provide:
1. Severity (Critical/High/Medium/Low)
2. Evidence (exact file and line)
3. Recommended fix with code example
