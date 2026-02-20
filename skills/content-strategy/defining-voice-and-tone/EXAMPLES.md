# Examples

## Example 1: Developer tools company

**Input:**
- Brand: Code deployment platform for engineering teams
- Attributes: technically credible, efficient, no-nonsense, supportive
- Audience: Senior engineers, DevOps professionals
- Competitors sound: Either too corporate/stiff or too casual/"bro-culture"

**Output:**

```md
# Voice and Tone Guidelines: DeployBot

## Voice principles

### 1. Technically precise
**We are:** Accurate, specific, using correct terminology
**We are not:** Dumbed-down, vague, or over-explaining basics

**This:**
> "Build failed: missing dependency `lodash@4.17.21` in package.json"

**Not this:**
> "Oops! Something went wrong with your code. Try checking your files."

### 2. Respectful of expertise
**We are:** Peer-level, assuming competence, direct
**We are not:** Condescending, tutorial-mode, hand-holding

**This:**
> "Configure your CI pipeline in `.deploybot.yml`"

**Not this:**
> "Don't worry if this seems complicated! We'll walk you through every little step."

### 3. Efficient
**We are:** Concise, scannable, action-oriented
**We are not:** Verbose, padded, repetitive

**This:**
> "Deployment complete. View logs →"

**Not this:**
> "Great news! Your deployment has been successfully completed. You can now view the full logs by clicking the button below."

---

## Tone spectrum

| Context | Tone | Example |
|---------|------|---------|
| Success | Confident, brief | "Deployed to production. 3 containers running." |
| Neutral | Direct, informational | "Select a branch to deploy." |
| Guidance | Clear, efficient | "Add your API key to continue." |
| Warning | Specific, actionable | "This will overwrite 12 environment variables." |
| Error | Precise, solution-oriented | "Authentication failed. Regenerate token in Settings → API." |
| Critical | Urgent, clear | "Production is unreachable. Rollback available." |

---

## Tone modulation rules

### When to be warmer
- First successful deployment (brief celebration)
- Reaching usage milestones
- Support conversations

### When to stay technical/neutral
- Configuration and setup flows
- Documentation
- System status messages

### When to be more urgent
- Security alerts
- Breaking changes
- Data loss scenarios
```

---

## Example 2: Consumer wellness app

**Input:**
- Brand: Meditation and sleep app for busy professionals
- Attributes: calm, encouraging, warm but not saccharine, evidence-based
- Audience: Stressed professionals, meditation beginners
- Competitors sound: Either too spiritual/woo or too clinical

**Output:**

```md
# Voice and Tone Guidelines: RestWell

## Voice principles

### 1. Calm, not passive
**We are:** Steady, reassuring, grounded
**We are not:** Sleepy, monotone, or overly soft

**This:**
> "Let's start with 5 minutes. That's enough to feel a difference."

**Not this:**
> "Shhh... just relax... everything is peaceful and soft..."

### 2. Encouraging, not performative
**We are:** Genuinely supportive, acknowledging effort
**We are not:** Cheerleader-tone, excessive enthusiasm, hollow praise

**This:**
> "You showed up today. That's the hardest part."

**Not this:**
> "OMG you're AMAZING!!! 🎉 You're basically a meditation MASTER now!!!"

### 3. Evidence-informed, not preachy
**We are:** Citing research when relevant, practical
**We are not:** Lecturing, guilt-inducing, pseudoscientific

**This:**
> "Studies show 10 minutes of daily meditation can reduce cortisol levels."

**Not this:**
> "You NEED to meditate every day or you'll never fix your stress problem."

---

## Tone spectrum

| Context | Tone | Example |
|---------|------|---------|
| Success | Warm, understated | "Session complete. Nice work." |
| Neutral | Calm, clear | "Choose a session length." |
| Guidance | Gentle, specific | "Find a quiet spot. Sit however feels comfortable." |
| Encouragement | Supportive, real | "Missed a few days? That's normal. Start fresh now." |
| Reminder | Light, non-judgmental | "Your evening wind-down is ready when you are." |
| Streak broken | Kind, forward-looking | "Streaks reset. What matters is you're here now." |

---

## Tone modulation rules

### When to be warmer
- After completing a session
- When a user returns after absence
- Sleep content (extra gentle)

### When to stay neutral
- Settings and account management
- Session selection
- Technical instructions

### When to be more direct
- Subscription and payment flows
- Privacy and data information
- Cancellation flows (clear, no guilt)
```

---

## Example 3: Edge case — Regulated financial product

**Input:**
- Brand: Investment platform for retail investors
- Attributes: trustworthy, clear, empowering, appropriately cautious
- Audience: First-time investors, financially anxious users
- Constraints: Must include required disclosures; cannot sound like advice

**Output:**

```md
# Voice and Tone Guidelines: ClearVest

## Voice principles

### 1. Clear, not clever
**We are:** Plain language, jargon-free where possible
**We are not:** Cute, punny, or using finance-bro slang

**This:**
> "A mutual fund pools money from many investors to buy a mix of stocks and bonds."

**Not this:**
> "Ready to get your tendies? Let's YOLO into some sick funds! 📈"

### 2. Empowering, not advising
**We are:** Educational, presenting options, respecting autonomy
**We are not:** Telling users what to do, guaranteeing outcomes

**This:**
> "Here are three portfolio options based on your risk preference. You choose what fits."

**Not this:**
> "You should definitely pick the aggressive portfolio for maximum gains!"

### 3. Honest about risk
**We are:** Transparent, showing downsides, including disclosures naturally
**We are not:** Burying risks, minimizing losses, or being alarmist

**This:**
> "All investments carry risk. Your balance can go down as well as up."

**Not this:**
> "Don't worry—historically the market always goes up eventually!"

---

## Tone spectrum

| Context | Tone | Example |
|---------|------|---------|
| Success | Calm confirmation | "Order placed. You'll see it in your portfolio shortly." |
| Neutral | Informational | "Select an account type to continue." |
| Educational | Clear, patient | "Dividends are payments companies make to shareholders." |
| Warning | Direct, specific | "Selling now locks in a $240 loss." |
| Error | Helpful, no alarm | "Transaction didn't go through. Check your available balance." |
| Market volatility | Steady, factual | "Markets are down 3% today. Your portfolio reflects current prices." |

---

## Tone modulation rules

### When to be warmer
- First investment milestone
- Educational content completion
- Customer support interactions

### When to stay strictly neutral
- Transaction confirmations
- Legal disclosures
- Tax documents

### When to be more cautious
- High-risk investment options
- Large transactions
- Irreversible actions (withdrawals, account closure)

---

## Required disclosure integration

Disclosures must appear but shouldn't disrupt flow:
- Use expandable sections for lengthy legal text
- Lead with the user benefit, follow with the disclosure
- Never hide disclosures behind interactions (must be visible)
```
