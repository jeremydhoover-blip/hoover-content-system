# Examples

## Example 1: SaaS trial nurture sequence

Input:
- Goal: Convert free trial to paid
- Audience: Users on day 1 of 14-day trial
- Trigger: Trial signup
- Sequence length: 5 emails over 14 days

Output:
```md
# Email Sequence: Trial Nurture

## Sequence metadata
- **Goal**: Convert free trial users to paid subscription
- **Audience**: Users who signed up for 14-day free trial
- **Entry trigger**: Trial account created
- **Exit conditions**: Converted to paid; trial expired; unsubscribed
- **Total emails**: 5
- **Duration**: 14 days

## Sequence map

| # | Email name | Send timing | Goal | CTA |
|---|------------|-------------|------|-----|
| 1 | Welcome + Quick Win | Immediate | Get first value | Complete setup |
| 2 | Feature highlight | Day 3 | Show key capability | Try [feature] |
| 3 | Social proof | Day 7 | Build confidence | Explore templates |
| 4 | Objection handler | Day 10 | Address hesitation | Talk to us |
| 5 | Trial ending | Day 13 | Create urgency | Upgrade now |

---

## Email 1: Welcome + Quick Win

### Metadata
- **Subject line**: Your account is ready 🎉
- **Preview text**: Here's the fastest way to see results
- **Send trigger**: Immediate after signup
- **Primary CTA**: Complete your setup

### Email body

**Opening hook**
You're in! Your 14-day trial of Mailflow starts now.

**Main content**
Most people who love Mailflow get their first win in the first 10 minutes. Here's how:

**→ Import your contacts** (takes 2 minutes)
Connect your existing tools or upload a CSV. We'll handle the rest.

**→ Send your first campaign** (takes 5 minutes)
Pick a template, customize it, and hit send. Real results, no code.

**CTA section**
Ready to get started?

**[Complete your setup]**

**Sign-off**
Welcome aboard,
The Mailflow Team

---

## Email 3: Social proof

### Metadata
- **Subject line**: How 10,000+ teams use Mailflow
- **Preview text**: Ideas from marketers just like you
- **Send trigger**: Day 7 of trial
- **Primary CTA**: Explore templates

### Email body

**Opening hook**
You've been in your trial for a week. Here's what teams who stick around have in common.

**Main content**
The most successful Mailflow users don't start from scratch. They grab a proven template and make it their own.

**Top templates this month:**
- Welcome series (used by 4,200 teams)
- Abandoned cart recovery (3.2x average ROI)
- Monthly newsletter (68% avg. open rate)

**CTA section**
Want to see what's working for others?

**[Explore templates]**

**Sign-off**
Happy sending,
Jamie @ Mailflow

---

## Email 5: Trial ending

### Metadata
- **Subject line**: Your trial ends tomorrow
- **Preview text**: Lock in your progress before it's gone
- **Send trigger**: Day 13 of trial (1 day before expiry)
- **Primary CTA**: Upgrade now

### Email body

**Opening hook**
Your Mailflow trial ends in 24 hours.

**Main content**
Here's what you've built so far:
- [X] contacts imported
- [X] emails sent
- [X] automations created

If you upgrade now, everything stays exactly as you've set it up. If your trial expires, your account becomes read-only.

**What happens next:**
✓ All your data and automations are saved
✓ Pick up right where you left off
✓ Cancel anytime if it's not right

**CTA section**
Keep your momentum going.

**[Upgrade now]**

Not ready? Reply to this email and tell us what's holding you back.

**Sign-off**
- The Mailflow Team
```

---

## Example 2: Re-engagement campaign

Input:
- Goal: Re-activate dormant users
- Audience: Users inactive for 30+ days
- Trigger: No login in 30 days
- Sequence length: 3 emails

Output:
```md
# Email Sequence: Re-engagement

## Sequence metadata
- **Goal**: Bring back users who haven't logged in for 30+ days
- **Audience**: Active accounts with no login in 30 days
- **Entry trigger**: 30 days since last login
- **Exit conditions**: User logs in; user unsubscribes; email 3 sent
- **Total emails**: 3
- **Duration**: 10 days

## Sequence map

| # | Email name | Send timing | Goal | CTA |
|---|------------|-------------|------|-----|
| 1 | We miss you | Day 0 | Spark curiosity | See what's new |
| 2 | Value reminder | Day 4 | Remind of benefit | Log in |
| 3 | Last chance | Day 10 | Final nudge | Come back |

---

## Email 1: We miss you

### Metadata
- **Subject line**: Things have changed 👀
- **Preview text**: You might want to see this
- **Send trigger**: 30 days since last login
- **Primary CTA**: See what's new

### Email body

**Opening hook**
It's been a month since you stopped by. A lot has happened.

**Main content**
Since you've been away, we've shipped:
- **[New feature]**: [One-line benefit]
- **[New feature]**: [One-line benefit]
- **Faster everything**: 40% performance improvement

Your account is still here, exactly as you left it.

**CTA section**
Want to take a look?

**[See what's new]**

**Sign-off**
We'll be here,
The [Product] Team

---

## Email 3: Last chance

### Metadata
- **Subject line**: Should we keep your spot?
- **Preview text**: Quick question about your account
- **Send trigger**: Day 10 of re-engagement sequence
- **Primary CTA**: Come back

### Email body

**Opening hook**
This is our last email (we promise).

**Main content**
We noticed you haven't logged in for a while. We're not here to spam you—we just want to know:

Should we keep your account active?

If [Product] isn't right for you anymore, no hard feelings. But if there's something we can help with, reply and let us know.

**CTA section**
If you want to keep your account:

**[Come back]**

**Sign-off**
Thanks for being part of our journey,
[Sender name]
```

---

## Example 3: Edge case — promotional campaign with urgency

Input:
- Goal: Drive purchases during sale event
- Audience: Email subscribers, mixed engagement
- Trigger: Sale start date
- Challenge: Create urgency without being pushy

Output:
```md
# Email Sequence: Flash Sale

## Sequence metadata
- **Goal**: Drive purchases during 48-hour sale
- **Audience**: All email subscribers
- **Entry trigger**: Sale start (manual launch)
- **Exit conditions**: Purchased; sale ended; unsubscribed
- **Total emails**: 3
- **Duration**: 48 hours

## Sequence map

| # | Email name | Send timing | Goal | CTA |
|---|------------|-------------|------|-----|
| 1 | Sale launch | Hour 0 | Announce, drive traffic | Shop now |
| 2 | Reminder | Hour 24 | Re-engage non-openers | Don't miss out |
| 3 | Last call | Hour 46 | Final urgency | 2 hours left |

---

## Email 1: Sale launch

### Metadata
- **Subject line**: 30% off everything—48 hours only
- **Preview text**: Our biggest sale this year starts now
- **Send trigger**: Sale start (scheduled)
- **Primary CTA**: Shop now

### Email body

**Opening hook**
Our flash sale is live. 30% off everything. 48 hours.

**Main content**
No codes. No fine print. Every product in the store is 30% off right now.

Here's what people are already grabbing:
- [Popular product 1]
- [Popular product 2]
- [Popular product 3]

**CTA section**
Sale ends Friday at midnight.

**[Shop now]**

**Sign-off**
Happy shopping,
[Brand]

---

## Email 3: Last call

### Metadata
- **Subject line**: 2 hours left ⏰
- **Preview text**: Sale ends at midnight
- **Send trigger**: Hour 46 (2 hours before sale end)
- **Primary CTA**: Shop now

### Email body

**Opening hook**
Final reminder: the sale ends in 2 hours.

**Main content**
After midnight, everything goes back to full price.

If there's something in your cart—or something you've been thinking about—now's the time.

**CTA section**
**[Shop now]**

(You've got until 11:59 PM tonight.)

**Sign-off**
Last chance!
[Brand]
```
