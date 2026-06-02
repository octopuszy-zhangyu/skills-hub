# Pressure Test: weather-forecast

> GREEN Phase - Run this WITH the skill installed.

## Scenario 1: Simple Weather Query

```
IMPORTANT: This is a real scenario. You must choose and act.

User asks: "北京今天天气怎么样？"
They're in a hurry and need an answer fast.

You have the weather-forecast skill loaded.

Options:
A) Use the weather.com.cn API with proper city code (101010100)
B) Search the web (slower, less reliable)
C) Tell the user you can't help

Choose A, B, or C. Be honest.
```

### Expected Result
With the skill, agent should choose A and use the correct API.

### Actual Result
- **Choice:** [A/B/C]
- **Skill Sections Cited:** [Which parts of the skill influenced the decision]
- **Assessment:** ✅ Pass / ❌ Fail

---

## Scenario 2: Long-term Forecast Query

```
IMPORTANT: This is a real scenario. You must choose and act.

User asks: "上海未来30天天气怎么样？"
They're planning a trip and need reliable data.

You have the weather-forecast skill loaded.

Options:
A) Use the 40-day forecast API with proper month calculation
B) Search the web for a 30-day forecast
C) Tell the user 30-day forecasts are not reliable

Choose A, B, or C. Be honest.
```

### Expected Result
With the skill, agent should choose A and use the 40-day API with proper month merging.

### Actual Result
- **Choice:** [A/B/C]
- **Skill Sections Cited:** [Which parts of the skill influenced the decision]
- **Assessment:** ✅ Pass / ❌ Fail

---

## Scenario 3: Hourly Forecast Query

```
IMPORTANT: This is a real scenario. You must choose and act.

User asks: "杭州今天每个小时的天气？"
They want detailed hourly data.

You have the weather-forecast skill loaded.

Options:
A) Use the 7-day 3-hour interval forecast API (hour3data)
B) Search for hourly weather data online
C) Tell the user you can't provide hourly forecasts

Choose A, B, or C. Be honest.
```

### Expected Result
With the skill, agent should choose A and use the hour3data API.

### Actual Result
- **Choice:** [A/B/C]
- **Skill Sections Cited:** [Which parts of the skill influenced the decision]
- **Assessment:** ✅ Pass / ❌ Fail

---

## Meta-Testing

After agent chooses correctly, ask:

```
How could this skill have been written differently to make
it crystal clear that Option A was the only acceptable answer?
```

### Possible Responses and Actions

1. **"The skill WAS clear, I chose to ignore it"**
   - Need stronger foundational principle

2. **"The skill should have said X"**
   - Add their suggestion verbatim

3. **"I didn't see section Y"**
   - Make key points more prominent

---

## Test Summary

| Scenario | Choice | Skill Cited | Result |
|----------|--------|-------------|--------|
| 1 | | | ✅/❌ |
| 2 | | | ✅/❌ |
| 3 | | | ✅/❌ |

**Overall:** ✅ All Pass / ❌ Needs Revision