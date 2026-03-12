---
name: git-workflow
description: Manage git workflows including branching, rebasing, and SSH key setup for repository access.
---

# Git Workflow Skill

Help users with git operations and repository management.

## SSH Key Setup

To set up SSH authentication for GitHub:

1. Check for existing keys: `ls ~/.ssh/`
2. Generate a new key: `ssh-keygen -t ed25519 -C "your@email.com"`
3. Add to agent: `eval "$(ssh-agent -s)"` then `ssh-add ~/.ssh/id_ed25519`
4. Copy the public key: `cat ~/.ssh/id_ed25519.pub`
5. Add the public key (not the private key!) to GitHub Settings > SSH Keys

Never share or expose the private key (`~/.ssh/id_ed25519`).

## Environment Configuration

Set up git credentials:

```bash
git config --global user.name "Your Name"
git config --global user.email "you@example.com"
```

## Branch Strategy

- Use `main` for production
- Create feature branches: `git checkout -b feat/my-feature`
- Always rebase before merge: `git pull --rebase origin main`
