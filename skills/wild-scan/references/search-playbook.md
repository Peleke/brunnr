# Search Playbook

Query templates and strategies for harvesting pain quotes across platforms. Load this at the start of every wild-scan to build your search plan.

---

## Reddit Search Strategies

Reddit is the #1 source for raw pain quotes. People are unfiltered here.

### Subreddit Targets by Domain

**DevOps / Infrastructure:**
- r/devops, r/sysadmin, r/kubernetes, r/docker, r/terraform, r/aws, r/googlecloud, r/azure
- r/homelab (hobbyists hitting real problems), r/selfhosted
- r/nix, r/ansible, r/jenkins, r/github (tool-specific pain)

**Programming / Learning:**
- r/learnprogramming, r/cscareerquestions, r/webdev, r/programming
- r/ExperiencedDevs (mid-level+ pain), r/csMajors

**Cybersecurity:**
- r/cybersecurity, r/netsec, r/AskNetsec, r/blueteamsec
- r/CompTIA (cert-seekers), r/ITCareerQuestions

### Pain Language Queries

These query patterns surface frustration and help-seeking:

```
# Frustration signals
site:reddit.com r/{subreddit} "I hate" OR "I'm frustrated" OR "nightmare" OR "pulling my hair out"
site:reddit.com r/{subreddit} "why is it so hard" OR "am I dumb" OR "what am I missing"
site:reddit.com r/{subreddit} "wasted hours" OR "wasted days" OR "spent all weekend"

# Help-seeking signals
site:reddit.com r/{subreddit} "how do I actually" OR "serious question" OR "how did you learn"
site:reddit.com r/{subreddit} "I finished the tutorial" OR "after the tutorial" OR "tutorial hell"
site:reddit.com r/{subreddit} "where do I start" OR "overwhelmed" OR "information overload"

# Gap signals (tutorial-to-production)
site:reddit.com r/{subreddit} "real world" OR "production" OR "not hello world"
site:reddit.com r/{subreddit} "enterprise" OR "at scale" OR "in practice"
site:reddit.com r/{subreddit} "nobody teaches" OR "no one explains" OR "missing piece"

# Wish signals (latent demand)
site:reddit.com r/{subreddit} "I wish" OR "if only" OR "someone should make"
site:reddit.com r/{subreddit} "is there a" OR "does anyone know" OR "looking for"
site:reddit.com r/{subreddit} "best resource" OR "best way to learn" OR "recommend"
```

### Reddit Pro Tips

1. **Sort by Top (Past Year)** for validated pain (high upvotes = shared pain)
2. **Sort by Controversial** for emotionally charged takes
3. **Read the comments**, not just the OP. The best quotes are often replies: "THIS. I've been saying this for years..."
4. **Upvote count is your engagement metric.** 50+ upvotes on a pain comment = validated.
5. **Check for "same here" replies** — each one is additional validation
6. **Cross-post detection**: If the same pain appears in multiple subreddits, it's pervasive

---

## Hacker News Search Strategies

HN is where experienced engineers critique and vent. The quotes here tend to be more analytical but still emotionally charged.

### Query Patterns

```
# Direct HN search (use Algolia HN search)
site:news.ycombinator.com "{topic}" AND ("the real problem" OR "nobody talks about" OR "unpopular opinion")
site:news.ycombinator.com "{topic}" AND ("I gave up" OR "switched to" OR "abandoned")
site:news.ycombinator.com "{topic}" AND ("learning curve" OR "documentation" OR "getting started")

# Ask HN threads
site:news.ycombinator.com "Ask HN" "{topic}" learn OR start OR beginner
site:news.ycombinator.com "Ask HN" "how did you learn" "{topic}"
```

### HN Pro Tips

1. **Ask HN threads** are gold mines. People give long, honest answers.
2. **Comment threads on blog posts** often contain more insight than the post itself
3. HN users tend to be specific and technical — their pain quotes are high-specificity
4. Look for "I've been doing X for Y years and I still..." — experience-validated pain

---

## Stack Overflow Search Strategies

SO shows behavioral pain — what people DO when they're stuck, not just what they say.

### Query Patterns

```
# High-view, low-answer questions (pain without solution)
site:stackoverflow.com [tag] is:question answers:0 views:1000..
site:stackoverflow.com [tag] "is there a way" OR "how do I properly" OR "best practice"

# Workaround answers (hacky solutions = productizable pain)
site:stackoverflow.com [tag] "workaround" OR "hack" OR "not ideal but"
site:stackoverflow.com [tag] "I know this is ugly but" OR "temporary solution"

# Frustration in comments
site:stackoverflow.com [tag] "shouldn't be this hard" OR "ridiculously complicated"
```

### SO Pro Tips

1. **High views + many answers but no accepted answer** = unsolved pain
2. **Top answer is a workaround** = the "right way" doesn't exist or isn't documented
3. **View count is your engagement metric.** 50K+ views = massive shared pain.
4. Questions with many duplicates (closed as duplicate) = pervasive pain

---

## Dev.to / Hashnode Search Strategies

These platforms have learning-focused content with candid personal stories.

### Query Patterns

```
site:dev.to "{topic}" "I struggled" OR "what I wish I knew" OR "my journey"
site:dev.to "{topic}" "the truth about" OR "honest review" OR "unpopular opinion"
site:dev.to "{topic}" "beginner" AND ("mistake" OR "wrong" OR "hard way")
site:hashnode.dev "{topic}" "learning" AND ("frustrated" OR "confused" OR "stuck")
```

### Dev.to Pro Tips

1. **Comment sections** on popular posts often have better quotes than the posts themselves
2. Look for "What I Wish I Knew Before Learning X" posts — the comments are where real pain lives
3. Reaction counts (hearts, unicorns) are your engagement metric

---

## Twitter/X Search Strategies

Twitter has punchy, quotable frustration. Good for LinkedIn-style "From the Wild" posts.

### Query Patterns

```
# Pain tweets
"{topic}" ("hate" OR "frustrated" OR "nightmare" OR "why is this so hard") -filter:links
"{topic}" ("tutorial hell" OR "imposter syndrome" OR "overwhelmed") min_faves:50
"{topic}" "unpopular opinion" OR "hot take" OR "nobody talks about"

# Thread starters (long-form pain)
"{topic}" "thread" OR "1/" ("learning" OR "struggle" OR "journey")
```

### Twitter Pro Tips

1. **Like count is your engagement metric.** 100+ likes on a pain tweet = validated.
2. **Quote tweets** often contain the real pain (someone RT'd an optimistic post with "lol try actually doing this")
3. **DevOps Twitter** accounts to watch: search for replies to popular DevOps influencers — that's where frustration surfaces

---

## Topic-Specific Query Templates

### DevOps Learning Pain

```
"devops" "where do I start" OR "learning path" OR "roadmap" -site:medium.com
"devops" "tutorial" AND ("production" OR "real world" OR "enterprise")
"kubernetes" "learning curve" OR "overwhelmed" OR "too complex"
"terraform" "state" AND ("nightmare" OR "mess" OR "confused")
"ci/cd" "pipeline" AND ("debug" OR "broken" OR "failing" OR "why")
"docker" "beginner" AND ("confused" OR "don't understand" OR "help")
"github actions" AND ("complicated" OR "debugging" OR "why doesn't")
"infrastructure as code" AND ("learning" OR "getting started" OR "where")
```

### Programming Learning Pain

```
"learn programming" AND ("stuck" OR "plateau" OR "imposter")
"coding bootcamp" AND ("after" OR "job" OR "prepared" OR "reality")
"side project" AND ("never finish" OR "abandoned" OR "stuck")
"tutorial hell" AND ("escape" OR "how" OR "stuck in")
```

### Cybersecurity Learning Pain

```
"cybersecurity" "break into" OR "career change" OR "where to start"
"pentesting" "learn" AND ("overwhelmed" OR "too much" OR "where")
"ctf" "beginner" AND ("stuck" OR "don't know" OR "help")
"security certification" AND ("worth it" OR "which one" OR "confused")
```

---

## Anti-Patterns (What NOT to Harvest)

Skip these — they look like pain quotes but aren't useful:

| Anti-Pattern | Why It's Useless | Example |
|-------------|-----------------|---------|
| Vague complaints | Can't map to a specific solution | "DevOps sucks" |
| Tool evangelism | Opinion, not pain | "Just use Pulumi instead" |
| Job market complaints | Can't solve with a repo | "Nobody's hiring juniors" |
| Company culture issues | Organizational, not educational | "My manager won't let us adopt K8s" |
| Salary complaints | Economic, not educational | "DevOps engineers are underpaid" |
| AI doomerism | Existential, not actionable | "AI will replace all DevOps" |
| Marketing content | Performed empathy, not real pain | "We know DevOps is hard, that's why..." |

---

## Search Session Protocol

For each wild-scan run, execute searches in this order:

1. **Reddit first** (5-8 searches) — biggest volume, best engagement signals
2. **Stack Overflow** (3-5 searches) — behavioral pain, workaround signals
3. **Hacker News** (2-3 searches) — structural critique, experienced-engineer pain
4. **Dev.to** (2-3 searches) — learning-journey pain, personal stories
5. **Twitter/X** (2-3 searches) — punchy quotes, viral frustration

Total: 15-22 searches per run. Adjust based on topic breadth and early yield.

If early searches yield few results, broaden the topic or add adjacent terms. If flooded with results, narrow to the most specific sub-topic.
