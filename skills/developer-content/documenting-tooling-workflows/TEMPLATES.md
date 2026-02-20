# Templates

## Default output: Tooling workflow documentation

Use this as the default structure:

```md
# <Workflow Name>

## Overview
<One paragraph: what this workflow accomplishes and when to use it.>

## Prerequisites

### Required tools
| Tool | Minimum version | Verify command |
|------|-----------------|----------------|
| <tool> | <version> | `<command --version>` |

### Required access
- [ ] <Account or credential 1>
- [ ] <Account or credential 2>

### Input artifacts
- <artifact 1>: <description and where to get it>

---

## Workflow diagram

```
[Start] → [Step 1] → [Decision] → [Step 2a] → [End]
                  ↘ [Step 2b] ↗
```

---

## Step-by-step instructions

### Step 1: <Action>

**Command:**
```bash
<command>
```

**Expected output:**
```
<what success looks like>
```

**Troubleshooting:**
- If `<error>`: <fix>

---

### Step 2: <Action>

<repeat pattern>

---

## Output artifacts
- <artifact>: <location and format>

## Verification
Confirm workflow succeeded:
```bash
<verification command>
```

Expected result: <description>

---

## Rollback procedure
If you need to undo this workflow:
1. <rollback step 1>
2. <rollback step 2>

---

## Common issues

| Symptom | Cause | Resolution |
|---------|-------|------------|
| <symptom> | <cause> | <fix> |
```

## Variant: CI/CD pipeline workflow

```md
# <Pipeline Name>

## Pipeline overview
- **Trigger**: <what starts this pipeline>
- **Duration**: <typical run time>
- **Artifacts produced**: <list>

## Pipeline stages

### Stage 1: <Name>
- **Purpose**: <what it does>
- **Runs on**: <runner/environment>
- **Dependencies**: <prior stages>

#### Jobs
1. **<job name>**: <description>
   - Inputs: <inputs>
   - Outputs: <outputs>
   - Timeout: <duration>

---

## Configuration

### Pipeline file
```yaml
<pipeline configuration>
```

### Required secrets
| Secret | Purpose | Where to set |
|--------|---------|--------------|
| <name> | <purpose> | <location> |

---

## Monitoring

### Success indicators
- <indicator 1>
- <indicator 2>

### Failure alerts
- <what triggers alerts>
- <who gets notified>

---

## Manual intervention points
- **<situation>**: <what to do>
```

## Variant: Multi-tool integration workflow

```md
# Integrating <Tool A> with <Tool B>

## Integration overview
- **Data flow**: <Tool A> → <format> → <Tool B>
- **Sync frequency**: <real-time | scheduled | manual>
- **Direction**: <one-way | bidirectional>

## Architecture

```
┌─────────┐     ┌─────────┐     ┌─────────┐
│ Tool A  │ ──► │ Adapter │ ──► │ Tool B  │
└─────────┘     └─────────┘     └─────────┘
                    │
                    ▼
              ┌─────────┐
              │  Logs   │
              └─────────┘
```

## Setup steps

### 1. Configure Tool A
<steps with verification>

### 2. Configure Tool B
<steps with verification>

### 3. Test integration
<end-to-end test steps>

---

## Data mapping
| Tool A field | Tool B field | Transformation |
|--------------|--------------|----------------|
| <field> | <field> | <rule> |

---

## Troubleshooting sync issues

### Data not appearing in Tool B
1. Check <first thing>
2. Verify <second thing>
3. Review logs at <location>

### Duplicate records
<diagnosis and fix>
```
