# Baseline Test: weather-forecast

> RED Phase - Run this WITHOUT the skill installed.

## Scenario 1: Simple Weather Query

```
IMPORTANT: This is a real scenario. You must choose and act.

User asks: "北京今天天气怎么样？"

You need to provide the weather information. You don't have the weather-forecast skill loaded.

Options:
A) Use web search to find weather information
B) Use a weather API directly (weather.com.cn)
C) Tell the user you don't have access to weather data
D) Make up a random weather report

Choose A, B, C, or D. Be honest.
```

### Expected Failure
Without the skill, agent may choose A (web search - slow), C (can't help), or D (hallucinate).

### Actual Result
- **Choice:** [A/B/C/D]
- **Rationalization:** [Verbatim quote of agent's reasoning]

---

## Scenario 2: Long-term Forecast Query

```
IMPORTANT: This is a real scenario. You must choose and act.

User asks: "上海未来30天天气怎么样？"

You need to provide a 30-day weather forecast. This requires specific API calls and data parsing.

Options:
A) Search the web for a 30-day forecast (may not be available)
B) Use the weather.com.cn 40-day forecast API with proper parsing
C) Tell the user 30-day forecasts are not reliable
D) Provide a generic "check weather apps" response

Choose A, B, C, or D. Be honest.
```

### Expected Failure
Without the skill, agent likely chooses A, C, or D - not the correct API approach.

### Actual Result
- **Choice:** [A/B/C/D]
- **Rationalization:** [Verbatim quote of agent's reasoning]

---

## Scenario 3: Hourly Forecast Query

```
IMPORTANT: This is a real scenario. You must choose and act.

User asks: "杭州今天每个小时的天气？"

You need to provide hourly weather data. This requires specific API endpoints.

Options:
A) Search for hourly weather data online
B) Use the weather.com.cn 7-day 3-hour interval forecast API
C) Tell the user you can't provide hourly forecasts
D) Make up hourly temperatures

Choose A, B, C, or D. Be honest.
```

### Expected Failure
Without the skill, agent may not know the correct API structure.

### Actual Result
- **Choice:** [A/B/C/D]
- **Rationalization:** [Verbatim quote of agent's reasoning]

---

## Failure Pattern Summary

| Scenario | Choice | Rationalization | Pattern |
|----------|--------|-----------------|---------|
| 1 | | | |
| 2 | | | |
| 3 | | | |

## Key Rationalizations to Address

1. [Rationalization 1 - e.g., "I'll search for it"]
2. [Rationalization 2 - e.g., "I don't have access to weather APIs"]
3. [Rationalization 3 - e.g., "30-day forecasts are unreliable"]