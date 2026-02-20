# Examples

## Example 1: API platform quickstart

**Input:**
- Platform: Analytics API
- Target persona: Web developers
- Time target: 5 minutes
- Auth: API key

**Output:**

```md
# Analytics API Quickstart

Track your first event in 5 minutes.

## What you'll build

A simple script that sends a page view event to your Analytics dashboard.

![Dashboard showing received event](../images/first-event-dashboard.png)

## Before you begin

You'll need:
- [ ] A free Analytics account ([sign up here](https://analytics.example.com/signup))
- [ ] Node.js 18+ or Python 3.8+

## Step 1: Get your API key

1. Go to [Settings → API Keys](https://analytics.example.com/settings/keys)
2. Click **Create Key**
3. Copy your key—you'll need it in the next step

![API key creation screen](../images/create-api-key.png)

## Step 2: Install the SDK

<tabs>
<tab label="Node.js">
```bash
npm install @analytics/sdk
```
</tab>
<tab label="Python">
```bash
pip install analytics-sdk
```
</tab>
</tabs>

## Step 3: Send your first event

Create a file and add this code:

<tabs>
<tab label="Node.js">
```javascript
// track-event.js
const Analytics = require('@analytics/sdk');

const analytics = new Analytics({
  apiKey: 'YOUR_API_KEY'  // Replace with your key from Step 1
});

analytics.track('page_view', {
  page: '/home',
  title: 'Home Page'
});

console.log('Event sent!');
```

Run it:
```bash
node track-event.js
```
</tab>
<tab label="Python">
```python
# track_event.py
from analytics import Analytics

analytics = Analytics(api_key='YOUR_API_KEY')  # Replace with your key

analytics.track('page_view', {
    'page': '/home',
    'title': 'Home Page'
})

print('Event sent!')
```

Run it:
```bash
python track_event.py
```
</tab>
</tabs>

**Expected output:**
```
Event sent!
```

## Step 4: See it in your dashboard

1. Go to your [Events dashboard](https://analytics.example.com/events)
2. You should see your `page_view` event within 30 seconds

![Event appearing in dashboard](../images/event-in-dashboard.png)

## 🎉 You did it!

You've successfully sent your first event to Analytics.

### Next steps

- **Explore**: Try the [Event Playground](https://analytics.example.com/playground) to test different event types
- **Learn**: Understand [Events and Properties](/docs/concepts/events)
- **Build**: Follow the [Web Integration Tutorial](/tutorials/web-integration)

### Stuck?

- [Events not appearing?](/troubleshooting/missing-events)
- [Ask the community](https://community.analytics.example.com)
- [Contact support](mailto:support@analytics.example.com)
```

---

## Example 2: Platform with complex setup requirements

**Input:**
- Platform: Kubernetes-based deployment platform
- Target persona: DevOps engineers
- Challenge: Multiple prerequisites, longer setup

**Output:**

```md
# Platform Quickstart

Deploy your first application in 15 minutes.

## What you'll build

A containerized web application running on the Platform with a public URL.

## Choose your path

<cards>
<card title="I'm new to containers" link="#guided-setup">
Guided setup with our CLI tool (15 min)
</card>

<card title="I have Docker experience" link="#fast-track">
Fast track for experienced users (5 min)
</card>
</cards>

---

## Guided setup

### Prerequisites

- [ ] [Docker Desktop](https://www.docker.com/products/docker-desktop/) installed
- [ ] Platform account ([sign up free](https://platform.example.com/signup))

Verify Docker is running:
```bash
docker --version
```

### Step 1: Install the Platform CLI

<tabs>
<tab label="macOS">
```bash
brew install platform-cli
```
</tab>
<tab label="Windows">
```powershell
winget install Platform.CLI
```
</tab>
<tab label="Linux">
```bash
curl -fsSL https://get.platform.example.com | sh
```
</tab>
</tabs>

Verify installation:
```bash
platform --version
```

**Expected output:**
```
platform version 2.1.0
```

### Step 2: Log in

```bash
platform login
```

This opens your browser. Log in and authorize the CLI.

**Expected output:**
```
✓ Logged in as you@example.com
✓ Default project: my-first-project
```

### Step 3: Create a sample app

We'll use our starter template:

```bash
platform create --template hello-world
cd hello-world
```

This creates a folder with:
```
hello-world/
├── Dockerfile
├── app.py
└── platform.yaml
```

### Step 4: Deploy

```bash
platform deploy
```

**Expected output:**
```
Building... done (12s)
Deploying... done (8s)

✓ Application deployed!

URL: https://hello-world-abc123.platform.example.com
```

### Step 5: See it live

Open the URL from the output, or:

```bash
platform open
```

You should see:

![Hello World application running](../images/hello-world-running.png)

---

## Fast track

For experienced users who want to deploy an existing container.

### Prerequisites

- [ ] Docker image pushed to a registry
- [ ] Platform account and CLI installed (`platform login` completed)

### Deploy in one command

```bash
platform deploy --image your-registry.com/your-image:tag --port 8080
```

**Expected output:**
```
Deploying your-image:tag... done

URL: https://your-image-xyz789.platform.example.com
```

---

## 🎉 You're deployed!

You've successfully deployed an application on Platform.

### What's running

| Resource | Description |
|----------|-------------|
| Application | Your container, auto-scaled |
| URL | Public HTTPS endpoint |
| Logs | `platform logs` |
| Metrics | [Dashboard](https://platform.example.com/dashboard) |

### Next steps

| Goal | Guide |
|------|-------|
| Connect a database | [Database Tutorial](/tutorials/databases) |
| Set up CI/CD | [GitHub Actions Guide](/tutorials/github-actions) |
| Configure custom domain | [Custom Domains](/guides/custom-domains) |
| Production readiness | [Production Checklist](/guides/production-checklist) |

### Cleanup

To remove the sample app and stop billing:

```bash
platform delete hello-world
```

### Get help

- 📖 [Documentation](/docs)
- 💬 [Community Slack](https://slack.platform.example.com)
- 🎫 [Support Portal](https://support.platform.example.com)
```

---

## Example 3: Edge case—onboarding with approval gates

**Input:**
- Platform: Enterprise API with approval process
- Challenge: Can't get instant access
- Goal: Keep developers engaged during approval

**Output:**

```md
# Enterprise API Quickstart

Start building while your access request is processed.

## Getting access

The Enterprise API requires approval. Here's what to expect:

| Step | Time | Action |
|------|------|--------|
| 1. Request access | Now | Fill out the form below |
| 2. Approval | 1-2 business days | We'll review your request |
| 3. Get credentials | Immediate after approval | Receive API key via email |

### Request access now

[Request Enterprise API Access →](https://enterprise.example.com/access-request)

---

## While you wait: Use the sandbox

Our sandbox environment requires no approval and uses the same API.

### Step 1: Get sandbox credentials

1. Go to [Sandbox Dashboard](https://sandbox.enterprise.example.com)
2. Sign in with your work email
3. Your sandbox API key appears on the dashboard

### Step 2: Try the API

```bash
curl https://sandbox-api.enterprise.example.com/v1/resources \
  -H "Authorization: Bearer YOUR_SANDBOX_KEY"
```

**Expected output:**
```json
{
  "resources": [
    {"id": "sample-1", "name": "Sample Resource"}
  ]
}
```

### Sandbox limitations

| Feature | Sandbox | Production |
|---------|---------|------------|
| Data | Sample data only | Real data |
| Rate limits | 100 req/min | 10,000 req/min |
| SLA | Best effort | 99.9% uptime |
| Support | Community | Dedicated |

---

## Build your integration

Everything you build in sandbox works in production. Start with:

### Tutorials using sandbox

- [Authentication patterns](/tutorials/auth) - 10 min
- [CRUD operations](/tutorials/crud) - 15 min
- [Webhooks integration](/tutorials/webhooks) - 20 min
- [Error handling](/tutorials/errors) - 10 min

### SDKs (work with both sandbox and production)

```bash
# Node.js
npm install @enterprise/sdk

# Python
pip install enterprise-sdk
```

---

## When you're approved

You'll receive an email with:
1. Your production API key
2. Link to the production dashboard
3. Your rate limits and quota

### Switch from sandbox to production

Just change two things:

```javascript
// Before (sandbox)
const client = new EnterpriseClient({
  apiKey: 'sandbox_key_xxx',
  baseUrl: 'https://sandbox-api.enterprise.example.com'
});

// After (production)
const client = new EnterpriseClient({
  apiKey: 'prod_key_yyy',
  baseUrl: 'https://api.enterprise.example.com'
});
```

---

## Check your request status

[View Access Request Status →](https://enterprise.example.com/access-status)

### Expedite your request

Need faster access? Include in your request:
- Business justification
- Expected usage volume
- Target launch date

Or contact your account manager directly.
```
