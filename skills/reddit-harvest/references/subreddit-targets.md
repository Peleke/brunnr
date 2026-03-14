# Subreddit Targets

Priority subreddits for pain-quote harvesting, organized by domain. DevOps is primary — start there. Expand to secondary/tertiary as the content pipeline demands.

---

## DevOps / Infrastructure (Primary)

These are the first subreddits to harvest. The brand thesis ("I finished the tutorial. Now what?") hits hardest here.

| Subreddit | Members (approx) | Why It's High-Value | Best Pain Queries |
|-----------|------------------|---------------------|-------------------|
| r/devops | 300K+ | Core audience. Practitioners venting about tooling, process, learning gaps. | "tutorial", "production", "where do I start", "career" |
| r/kubernetes | 250K+ | K8s is the #1 complained-about tool in DevOps education. Gold mine. | "learning curve", "yaml", "networking", "debugging" |
| r/docker | 200K+ | First DevOps tool most people learn. Beginner pain is concentrated here. | "beginner", "compose", "networking", "works on my machine" |
| r/terraform | 100K+ | State management, modules, team workflows — rich specific pain. | "state", "modules", "best practices", "team" |
| r/aws | 350K+ | Cloud-first pain. IAM, networking, cost. Huge audience. | "confusing", "expensive", "certification", "networking" |
| r/sysadmin | 500K+ | Old-school ops transitioning to DevOps. Career-transition pain. | "devops", "automation", "learning", "career change" |
| r/homelab | 350K+ | Hobbyists hitting production-grade problems for the first time. | "how do you", "setup", "docker", "kubernetes" |
| r/selfhosted | 300K+ | Self-starters trying to run real infrastructure. Config & debug pain. | "struggling", "setup", "alternative", "networking" |
| r/ansible | 50K+ | Automation-specific pain. Configuration management is a common gap. | "playbook", "best practice", "learning", "complex" |

### DevOps Search Priority Order

Run searches in this order to maximize yield per session:

1. **r/devops** — broadest, highest general pain density
2. **r/kubernetes** — deepest, most specific pain
3. **r/terraform** — state management is a proven gold theme
4. **r/aws** — massive audience, IAM/networking pain
5. **r/docker** — beginner-heavy, tutorial-gap pain
6. **r/sysadmin** — career-transition pain
7. **r/homelab + r/selfhosted** — real-world gap pain (hobbyists hitting production problems)
8. **r/ansible** — niche but specific

---

## Programming / Learning (Secondary)

Harvest these when expanding beyond DevOps or when the content pipeline needs programming-focused quotes.

| Subreddit | Members (approx) | Why It's High-Value | Best Pain Queries |
|-----------|------------------|---------------------|-------------------|
| r/learnprogramming | 4M+ | Massive beginner audience. Tutorial-hell quotes flow freely. | "tutorial hell", "stuck", "after the course", "real project" |
| r/webdev | 1M+ | Frontend/fullstack pain. Deployment, tooling complexity, framework fatigue. | "overwhelmed", "which framework", "deployment", "too many" |
| r/node | 150K+ | Node.js specific. Async pain, tooling, production gaps. | "async", "debugging", "production", "best practice" |
| r/reactjs | 400K+ | React-specific. State management, build tooling, testing gaps. | "state management", "testing", "build", "why is it" |
| r/golang | 200K+ | Go learners. Error handling, concurrency, "the Go way" confusion. | "error handling", "channels", "idiomatic", "coming from" |
| r/rust | 300K+ | Rust learners. Borrow checker, lifetime, learning curve legendarily painful. | "borrow checker", "lifetime", "learning curve", "fighting" |
| r/python | 1M+ | Broad. Best for beginner pain and "Python in production" gaps. | "beginner", "project", "production", "packaging" |

---

## Cybersecurity (Tertiary)

Third priority per the domain roadmap. Harvest when ready to build cybersec content.

| Subreddit | Members (approx) | Why It's High-Value | Best Pain Queries |
|-----------|------------------|---------------------|-------------------|
| r/netsec | 500K+ | Practitioner-level security. Deep technical pain. | "learning", "career", "where to start", "resources" |
| r/cybersecurity | 300K+ | Broad cybersec audience. Career-transition pain dominant. | "break into", "career change", "certification", "overwhelmed" |
| r/AskNetsec | 100K+ | Q&A format — direct pain statements. | "how do I", "where to start", "recommend", "frustrated" |
| r/blueteam | 30K+ | Defensive security. SOC analyst pain, tooling gaps. | "soc", "alert fatigue", "learning", "tools" |

---

## Cross-Domain (Bonus)

These subreddits surface pain that spans multiple domains:

| Subreddit | Why |
|-----------|-----|
| r/ExperiencedDevs | Mid-to-senior engineers. "I've been doing this for years and..." pain. Higher specificity. |
| r/cscareerquestions | Career-oriented pain. Less useful for repo content, but good for understanding audience motivations. |
| r/ITCareerQuestions | IT/ops career transitions. Overlaps with sysadmin → DevOps journey. |

---

## Usage Notes

- **Start narrow, expand if needed.** For a focused DevOps scan, hit r/devops + r/kubernetes + r/terraform. Only expand if quote yield is low.
- **Niche subreddits have higher signal-to-noise.** 30 upvotes on r/terraform (100K members) is more significant than 30 upvotes on r/programming (6M members). Adjust engagement scoring per the scoring rubric's community-size guidance.
- **Check subreddit rules before any future posting.** This file is for harvesting only. Some subreddits have strict self-promotion rules relevant to the content distribution phase.
- **Seasonal patterns.** Pain posts spike in January (New Year resolutions), September (back to school/new jobs), and during major tool releases (K8s versions, Terraform provider updates). Time scans accordingly.
