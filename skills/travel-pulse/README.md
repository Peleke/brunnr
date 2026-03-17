# Travel Pulse

Travel risk intelligence for 195 countries. Computes a SafeGo Score (0-100) from 6 data sources via the [Travel Advisory API](https://www.traveladvisory.io).

## Setup

### 1. Get an API key

Sign up at [traveladvisory.io](https://www.traveladvisory.io) (free tier: 250 requests/month, no credit card).

### 2. Set the environment variable

```bash
export TRAVEL_ADVISORY_API_KEY="ta_live_your_key_here"
```

Or add it to your shell profile (`~/.zshrc`, `~/.bashrc`).

### 3. Install the skill

```bash
brunnr install travel-pulse
```

### 4. Use it

```
> Is Colombia safe to travel to?
> Compare Thailand vs Vietnam
> SafeGo score for Japan
```

## What it does

The agent calls `GET /v1/advisory/{COUNTRY_CODE}` with your API key, then computes a SafeGo Score from the response:

| Source | Weight | Derived from |
|--------|--------|-------------|
| Advisory | 35% | `advisory.level` (1-4) |
| Safety | 20% | `restrictions.*`, regional area levels |
| Health | 15% | Health keywords in `advisory.reasons` |
| Freedom | 15% | `trend.freedom_status` |
| Economic | 10% | Economic keywords in `advisory.reasons`, `entry_exit` |
| Climate | 5% | Climate keywords in `advisory.reasons` |

The raw weighted score gets capped by the advisory level (L2 caps at 70, L3 at 40, L4 at 15), then adjusted for trend direction, do-not-travel zones, and state of emergency.

### Grades

| Grade | Score | Meaning |
|-------|-------|---------|
| A | 80-100 | Low risk |
| B | 60-79 | Moderate risk |
| C | 40-59 | Elevated risk |
| D | 20-39 | High risk |
| F | 0-19 | Extreme risk |

## Modes

- **Single country**: full report with score breakdown, key risks, regional breakdown, travel logistics
- **Comparison**: side-by-side table for up to 5 countries with recommendation
- **Regional drill-down**: expanded regional breakdown for a specific country

## Rate limits

Free tier: 250 requests/month. Each country lookup costs 1 request. A 5-country comparison costs 5. The skill reports remaining budget after every API call.

## Requirements

- `curl` (used to call the API)
- `TRAVEL_ADVISORY_API_KEY` environment variable
