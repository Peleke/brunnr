# Reddit DOM Selectors & Extraction Scripts

JavaScript snippets for extracting data from Reddit pages via Playwright MCP's `browser_evaluate` and `browser_run_code`. Reddit's DOM changes frequently — update these when extraction breaks.

> **Last verified**: 2026-02-12 (new Reddit / sh.reddit.com layout)

---

## Search Results Page

Navigate to: `https://www.reddit.com/r/{subreddit}/search/?q={query}&sort=top&t=year`

### Extract Search Results

Pass to `browser_evaluate`:

```javascript
// Extract post cards from search results
(() => {
  const posts = [];
  // Target the search result post containers
  const postElements = document.querySelectorAll('search-telemetry-tracker, [data-testid="search-result-link"], faceplate-tracker[source="search"]');

  // Fallback: grab all article-like containers with links to reddit posts
  const candidates = postElements.length > 0
    ? postElements
    : document.querySelectorAll('a[href*="/comments/"]');

  const seen = new Set();

  candidates.forEach(el => {
    try {
      // Find the nearest post container
      const container = el.closest('[data-testid="search-result-link"]')
        || el.closest('faceplate-tracker')
        || el.closest('div[data-fullname]')
        || el;

      // Extract permalink
      const linkEl = container.querySelector('a[href*="/comments/"]') || container;
      const href = linkEl?.getAttribute('href') || linkEl?.href || '';
      const url = href.startsWith('http') ? href : `https://www.reddit.com${href}`;

      // Deduplicate
      const postId = href.match(/comments\/([a-z0-9]+)/)?.[1];
      if (!postId || seen.has(postId)) return;
      seen.add(postId);

      // Title — look for heading elements or link text
      const titleEl = container.querySelector('a[id*="post-title"]')
        || container.querySelector('[slot="title"]')
        || container.querySelector('h2, h3')
        || linkEl;
      const title = titleEl?.textContent?.trim() || '';

      // Author
      const authorEl = container.querySelector('a[href*="/user/"]');
      const author = authorEl?.textContent?.trim()?.replace(/^u\//, '') || '';

      // Upvotes — Reddit renders these in various elements
      const voteEl = container.querySelector('faceplate-number[pretty]')
        || container.querySelector('[id*="vote-score"]')
        || container.querySelector('shreddit-post')
        || container.querySelector('[score]');
      let upvotes = 0;
      if (voteEl) {
        const raw = voteEl.getAttribute('pretty')
          || voteEl.getAttribute('score')
          || voteEl.textContent?.trim();
        upvotes = parseVoteString(raw);
      }

      // Comment count
      const commentEl = container.querySelector('a[href*="/comments/"] span')
        || container.querySelector('[data-testid="comment-count"]');
      let comments = 0;
      if (commentEl) {
        const match = commentEl.textContent?.match(/(\d+)/);
        comments = match ? parseInt(match[1], 10) : 0;
      }

      // Timestamp
      const timeEl = container.querySelector('time, faceplate-timeago');
      const timestamp = timeEl?.getAttribute('datetime')
        || timeEl?.getAttribute('ts')
        || timeEl?.textContent?.trim()
        || '';

      // Subreddit (may differ from search target if cross-posted)
      const subEl = container.querySelector('a[href*="/r/"]');
      const subreddit = subEl?.textContent?.trim() || '';

      posts.push({ title, author, url, upvotes, comments, timestamp, subreddit, postId });
    } catch (e) {
      // Skip malformed entries
    }
  });

  function parseVoteString(str) {
    if (!str) return 0;
    str = str.trim().toLowerCase();
    if (str.endsWith('k')) return Math.round(parseFloat(str) * 1000);
    if (str.endsWith('m')) return Math.round(parseFloat(str) * 1000000);
    return parseInt(str.replace(/,/g, ''), 10) || 0;
  }

  return posts;
})()
```

### Filter Results

After extraction, apply in the skill logic (not in JS):
- Skip posts with `upvotes < engagement_threshold` (default: 10)
- Rank by `comments` descending (more comments = more potential quotes)
- Select top N (default: 10 per subreddit)

---

## Thread Page (Post + Comments)

Navigate to the thread URL from search results.

### Scroll and Load Comments

Reddit lazy-loads comments. Use `browser_run_code` to scroll incrementally:

```javascript
// Scroll to load comments — run via browser_run_code
// Scrolls 700px at a time with 750ms pauses
// Returns the final scroll height for verification
(async () => {
  const scrollStep = 700;
  const pauseMs = 750;
  const maxScrolls = 20; // Safety cap: 20 * 700 = 14000px

  let scrolls = 0;
  let lastHeight = document.body.scrollHeight;

  while (scrolls < maxScrolls) {
    window.scrollBy(0, scrollStep);
    await new Promise(r => setTimeout(r, pauseMs));

    const newHeight = document.body.scrollHeight;
    // Stop if we've reached the bottom (no new content loaded)
    if (newHeight === lastHeight) {
      // One more try in case of slow load
      await new Promise(r => setTimeout(r, 1500));
      if (document.body.scrollHeight === lastHeight) break;
    }
    lastHeight = document.body.scrollHeight;
    scrolls++;
  }

  // Scroll back to top so snapshot is from the beginning
  window.scrollTo(0, 0);
  return { scrolls, finalHeight: document.body.scrollHeight };
})()
```

### Extract Post Metadata

Pass to `browser_evaluate`:

```javascript
// Extract the original post's metadata
(() => {
  const post = {};

  // Title
  const titleEl = document.querySelector('[id*="post-title"]')
    || document.querySelector('shreddit-post [slot="title"]')
    || document.querySelector('h1');
  post.title = titleEl?.textContent?.trim() || '';

  // Author
  const authorEl = document.querySelector('shreddit-post a[href*="/user/"]')
    || document.querySelector('[data-testid="post-author"]');
  post.author = authorEl?.textContent?.trim()?.replace(/^u\//, '') || '';

  // Post body text (self-post)
  const bodyEl = document.querySelector('[id*="post-rtjson-content"]')
    || document.querySelector('shreddit-post [slot="text-body"]')
    || document.querySelector('[data-testid="post-content"]');
  post.body = bodyEl?.textContent?.trim() || '';

  // Upvotes on the post itself
  const voteEl = document.querySelector('shreddit-post faceplate-number[pretty]')
    || document.querySelector('shreddit-post [score]');
  const raw = voteEl?.getAttribute('pretty') || voteEl?.getAttribute('score') || '0';
  post.upvotes = parseVoteString(raw);

  // Comment count
  const commentEl = document.querySelector('[id*="comment-count"]')
    || document.querySelector('shreddit-post [slot="commentCount"]');
  const cMatch = commentEl?.textContent?.match(/(\d+)/);
  post.commentCount = cMatch ? parseInt(cMatch[1], 10) : 0;

  // Timestamp
  const timeEl = document.querySelector('shreddit-post time, shreddit-post faceplate-timeago');
  post.timestamp = timeEl?.getAttribute('datetime') || timeEl?.getAttribute('ts') || '';

  // Subreddit
  const subEl = document.querySelector('shreddit-post a[href*="/r/"]');
  post.subreddit = subEl?.textContent?.trim() || '';

  // URL
  post.url = window.location.href;

  function parseVoteString(str) {
    if (!str) return 0;
    str = str.trim().toLowerCase();
    if (str.endsWith('k')) return Math.round(parseFloat(str) * 1000);
    if (str.endsWith('m')) return Math.round(parseFloat(str) * 1000000);
    return parseInt(str.replace(/,/g, ''), 10) || 0;
  }

  return post;
})()
```

### Extract Comments

Pass to `browser_evaluate`:

```javascript
// Extract all visible comments with metadata
(() => {
  const comments = [];

  // Target shreddit comment trees
  const commentEls = document.querySelectorAll('shreddit-comment');

  // Fallback for older/different layouts
  const targets = commentEls.length > 0
    ? commentEls
    : document.querySelectorAll('[data-testid="comment"], .Comment');

  targets.forEach((el, index) => {
    try {
      // Comment text — look for the paragraph content
      const contentEl = el.querySelector('[id*="comment-content"]')
        || el.querySelector('[slot="comment"]')
        || el.querySelector('[data-testid="comment"] p')
        || el.querySelector('p');
      const text = contentEl?.textContent?.trim() || '';

      // Skip empty or very short comments (likely "[deleted]" or reactions)
      if (!text || text.length < 20) return;

      // Author
      const author = el.getAttribute('author')
        || el.querySelector('a[href*="/user/"]')?.textContent?.trim()?.replace(/^u\//, '')
        || '';

      // Depth (nesting level)
      const depth = parseInt(el.getAttribute('depth') || '0', 10);

      // Upvotes
      const voteEl = el.querySelector('faceplate-number[pretty]')
        || el.querySelector('[score]');
      const raw = voteEl?.getAttribute('pretty') || voteEl?.getAttribute('score') || '0';
      const upvotes = parseVoteString(raw);

      // Timestamp
      const timeEl = el.querySelector('time, faceplate-timeago');
      const timestamp = timeEl?.getAttribute('datetime')
        || timeEl?.getAttribute('ts')
        || timeEl?.textContent?.trim()
        || '';

      // Permalink — construct from thing_id or comment ID
      const thingId = el.getAttribute('thingid') || el.getAttribute('id') || '';
      const permalink = thingId
        ? `${window.location.href.split('?')[0]}${thingId}/`
        : window.location.href;

      // Count replies (direct children that are also comments)
      const replyCount = el.querySelectorAll(':scope > shreddit-comment').length;

      comments.push({
        text,
        author,
        depth,
        upvotes,
        timestamp,
        permalink,
        replyCount,
        index
      });
    } catch (e) {
      // Skip malformed comments
    }
  });

  function parseVoteString(str) {
    if (!str) return 0;
    str = str.trim().toLowerCase();
    if (str.endsWith('k')) return Math.round(parseFloat(str) * 1000);
    if (str.endsWith('m')) return Math.round(parseFloat(str) * 1000000);
    return parseInt(str.replace(/,/g, ''), 10) || 0;
  }

  return comments;
})()
```

---

## "Same Here" Detection

After extracting comments, count agreement replies for each top-level pain comment. Pass to `browser_evaluate` with a target comment's index:

```javascript
// Count "same here" style agreement in replies to a specific comment
// Pass parentIndex as a variable or inline it before evaluation
((parentIndex) => {
  const allComments = document.querySelectorAll('shreddit-comment');
  const parent = allComments[parentIndex];
  if (!parent) return { sameHereCount: 0, agreementReplies: [] };

  const replies = parent.querySelectorAll(':scope > shreddit-comment');
  const agreementPatterns = [
    /\bsame\b/i,
    /\bthis\b/i,
    /\bexactly\b/i,
    /\b100%\b/i,
    /\bpreach\b/i,
    /\bso much this\b/i,
    /\bcan confirm\b/i,
    /\bme too\b/i,
    /\bi feel this\b/i,
    /\bhappened to me\b/i,
    /\bsame boat\b/i,
    /\bsame experience\b/i,
    /\bgoing through this\b/i,
    /\bi thought i was the only one\b/i,
    /^\+1$/i,
    /^this\.?$/i,
    /^same\.?$/i
  ];

  const agreementReplies = [];
  replies.forEach(reply => {
    const text = reply.querySelector('[id*="comment-content"], [slot="comment"], p')
      ?.textContent?.trim() || '';
    if (text.length < 100 && agreementPatterns.some(p => p.test(text))) {
      agreementReplies.push(text);
    }
  });

  return {
    sameHereCount: agreementReplies.length,
    agreementReplies
  };
})
```

> **Usage note**: Call this as a function literal. To invoke, wrap in an IIFE with the parentIndex: `(${script})(${idx})`. Or use `browser_evaluate` with the parentIndex inlined.

---

## Pain Category Keyword Matcher

Use this client-side to auto-suggest a `pain_category` for each harvested quote. The skill operator should verify/override.

```javascript
// Auto-suggest pain category from quote text
// Returns best-match category or "uncategorized"
((quoteText) => {
  const text = quoteText.toLowerCase();

  const categories = {
    'tutorial-gap': [
      'tutorial', 'course', 'hello world', 'getting started',
      'beginner', 'after the tutorial', 'tutorial hell',
      'every tutorial', 'no tutorial', 'step by step'
    ],
    'tool-complexity': [
      'too complex', 'overcomplicated', 'overkill', 'bloated',
      'why is it so', 'steep learning curve', 'abstraction',
      'configuration', 'boilerplate', 'ceremony'
    ],
    'real-world-gap': [
      'production', 'real world', 'enterprise', 'at scale',
      'not hello world', 'actual project', 'in practice',
      'real app', 'professional', 'team environment'
    ],
    'career-transition': [
      'career', 'transition', 'switch', 'break into',
      'junior', 'entry level', 'hire', 'job market',
      'career change', 'getting into'
    ],
    'information-overload': [
      'overwhelmed', 'too many', 'which one', 'overload',
      'where do i start', 'roadmap', 'so many options',
      'decision fatigue', 'paradox of choice', 'confused by'
    ],
    'environment-setup': [
      'setup', 'install', 'configure', 'environment',
      'local dev', 'docker compose', 'works on my machine',
      'dependency', 'version', 'compatibility'
    ],
    'debugging-hell': [
      'debugging', 'debug', 'error', 'spent hours',
      'spent days', 'can\'t figure', 'stack trace',
      'cryptic', 'error message', 'silent fail'
    ],
    'missing-fundamentals': [
      'fundamentals', 'basics', 'foundation', 'underlying',
      'don\'t understand why', 'how does it actually',
      'under the hood', 'conceptually', 'mental model'
    ]
  };

  let bestCategory = 'uncategorized';
  let bestScore = 0;

  for (const [category, keywords] of Object.entries(categories)) {
    let score = 0;
    for (const kw of keywords) {
      if (text.includes(kw)) score++;
    }
    if (score > bestScore) {
      bestScore = score;
      bestCategory = category;
    }
  }

  return bestCategory;
})
```

> **Usage note**: Same invocation pattern as the "same here" detector. Pass quote text as the argument.

---

## Troubleshooting

### Selectors returning empty results

Reddit ships multiple frontends. If selectors break:

1. Use `browser_snapshot` to get the current accessibility tree
2. Look for `shreddit-comment`, `faceplate-tracker`, or `search-telemetry-tracker` custom elements
3. If none found, Reddit may have rolled out a new frontend — use `browser_evaluate` with `document.querySelectorAll('*')` filtered by tag prefix to discover new custom element names
4. Update selectors in this file accordingly

### Comment loading issues

- Reddit caps visible comments. If a thread has 500+ comments but only 20 load, use `browser_click` on "More comments" / "Continue thread" links before extracting
- Pattern for "load more" buttons: `button[id*="comment-tree-content-anchor"]`, `[data-testid="load-more-comments"]`, or links containing "more replies"

### Login-gated content

Some subreddit searches or NSFW threads require login. The skill assumes you're logged in before invoking. If `browser_evaluate` returns empty on a page that should have content, verify login state:

```javascript
// Check if logged in
(() => {
  const userMenu = document.querySelector('[id*="USER_DROPDOWN"]')
    || document.querySelector('header a[href*="/user/"]');
  return { loggedIn: !!userMenu };
})()
```
