# Examples

## Example 1: Python SDK quickstart documentation

**Input:**
- SDK: Cloud Storage SDK for Python
- Service: Object storage with bucket and blob operations
- Auth methods: Service account JSON, environment variable
- Target audience: Backend developers, intermediate

**Output:**

```md
# Cloud Storage SDK for Python

## Overview
The Cloud Storage SDK for Python provides programmatic access to object storage services, enabling bucket management, file uploads, and access control.

## Prerequisites
- Python 3.8 or later
- pip package manager
- Service account with Storage Admin role

## Installation

### pip
```python
pip install cloud-storage-sdk>=2.0.0
```

## Authentication

### Option 1: Service account JSON file
```python
from cloud_storage import StorageClient

# Path to your service account key file
client = StorageClient.from_service_account_json(
    "path/to/service-account.json"
)
```

### Option 2: Environment variable
```python
import os
from cloud_storage import StorageClient

# Expects STORAGE_CREDENTIALS environment variable
# containing path to service account JSON
client = StorageClient.from_env()
```

## Quickstart

### Upload a file
```python
from cloud_storage import StorageClient

# Initialize client (uses STORAGE_CREDENTIALS env var)
client = StorageClient.from_env()

# Get bucket reference
bucket = client.bucket("my-bucket")

# Upload local file to bucket
blob = bucket.blob("data/report.csv")
blob.upload_from_filename("./local-report.csv")

print(f"Uploaded to: {blob.public_url}")
```

**What this code does:**
1. Creates authenticated client using environment credentials
2. References existing bucket by name
3. Creates blob object with destination path
4. Uploads local file to blob location
5. Prints public URL of uploaded file

## Error handling

### Common errors
| Error code | Cause | Resolution |
|------------|-------|------------|
| `BucketNotFound` | Bucket name doesn't exist or access denied | Verify bucket name and service account permissions |
| `QuotaExceeded` | Storage quota limit reached | Request quota increase or delete unused files |
| `InvalidCredentials` | Service account JSON invalid or expired | Regenerate service account key |

### Error handling pattern
```python
from cloud_storage import StorageClient
from cloud_storage.exceptions import (
    BucketNotFound, 
    QuotaExceeded,
    StorageError
)

client = StorageClient.from_env()

try:
    bucket = client.bucket("my-bucket")
    blob = bucket.blob("data/report.csv")
    blob.upload_from_filename("./local-report.csv")
except BucketNotFound:
    # Handle missing bucket - create or check name
    print("Bucket does not exist. Creating...")
    bucket = client.create_bucket("my-bucket")
except QuotaExceeded as e:
    # Handle quota - log and alert
    print(f"Quota exceeded: {e.current_usage}/{e.limit}")
except StorageError as e:
    # Catch-all for other storage errors
    print(f"Storage operation failed: {e.message}")
```
```

---

## Example 2: JavaScript SDK with async/await patterns

**Input:**
- SDK: Payment Gateway SDK for Node.js
- Service: Payment processing with charges and refunds
- Auth methods: API key
- Target audience: Full-stack developers, need production patterns

**Output:**

```md
# Payment Gateway SDK for Node.js

## Overview
The Payment Gateway SDK processes payments, manages refunds, and handles subscription billing through a unified API.

## Prerequisites
- Node.js 18.x or later
- npm or yarn
- API key from merchant dashboard

## Installation

### npm
```bash
npm install @payments/gateway-sdk
```

### yarn
```bash
yarn add @payments/gateway-sdk
```

## Authentication

### API key authentication
```javascript
import { PaymentClient } from '@payments/gateway-sdk';

// REQUIRED: Replace with your API key from merchant dashboard
// WARNING: Never commit API keys to version control
const client = new PaymentClient({
  apiKey: process.env.PAYMENT_API_KEY,
  environment: 'sandbox' // Use 'production' for live transactions
});
```

## Quickstart

### Create a charge
```javascript
import { PaymentClient } from '@payments/gateway-sdk';

const client = new PaymentClient({
  apiKey: process.env.PAYMENT_API_KEY,
  environment: 'sandbox'
});

async function createCharge() {
  const charge = await client.charges.create({
    amount: 2500,        // Amount in cents ($25.00)
    currency: 'usd',
    source: 'tok_visa',  // Token from client-side SDK
    description: 'Order #1234',
    metadata: {
      orderId: '1234',
      customerId: 'cust_abc'
    }
  });

  console.log(`Charge created: ${charge.id}`);
  console.log(`Status: ${charge.status}`);
  return charge;
}

// Expected output:
// Charge created: ch_1234567890
// Status: succeeded
```

**What this code does:**
1. Initializes client with API key from environment
2. Calls charges.create with amount in smallest currency unit
3. Passes payment source token (generated client-side)
4. Attaches metadata for your records
5. Returns charge object with ID and status

## Operations

### Charges

#### Create a charge
```javascript
const charge = await client.charges.create({
  amount: 2500,
  currency: 'usd',
  source: 'tok_visa',
  description: 'Payment description'
});
```

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| amount | integer | yes | Amount in smallest currency unit (cents for USD) |
| currency | string | yes | Three-letter ISO currency code |
| source | string | yes | Payment source token from client SDK |
| description | string | no | Arbitrary description for your records |
| metadata | object | no | Key-value pairs for your reference |

**Returns:** Charge object with `id`, `status`, `amount`, `created` timestamp

#### Retrieve a charge
```javascript
const charge = await client.charges.retrieve('ch_1234567890');
```

### Refunds

#### Create a refund
```javascript
const refund = await client.refunds.create({
  charge: 'ch_1234567890',
  amount: 1000,  // Partial refund of $10.00
  reason: 'requested_by_customer'
});
```

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| charge | string | yes | ID of charge to refund |
| amount | integer | no | Amount to refund in cents. Defaults to full charge. |
| reason | string | no | One of: `duplicate`, `fraudulent`, `requested_by_customer` |

## Error handling

### Common errors
| Error code | Cause | Resolution |
|------------|-------|------------|
| `card_declined` | Card issuer declined transaction | Prompt customer for different payment method |
| `insufficient_funds` | Card has insufficient funds | Prompt for different card or lower amount |
| `invalid_api_key` | API key is incorrect or revoked | Verify key in merchant dashboard |
| `rate_limit_exceeded` | Too many requests | Implement exponential backoff |

### Error handling pattern
```javascript
import { PaymentClient, PaymentError, CardError, RateLimitError } from '@payments/gateway-sdk';

async function processPayment(amount, source) {
  try {
    const charge = await client.charges.create({
      amount,
      currency: 'usd',
      source
    });
    return { success: true, chargeId: charge.id };
  } catch (error) {
    if (error instanceof CardError) {
      // Card was declined - return user-friendly message
      return { 
        success: false, 
        userMessage: 'Your card was declined. Please try a different card.',
        code: error.declineCode
      };
    }
    if (error instanceof RateLimitError) {
      // Implement retry with backoff
      await sleep(error.retryAfter * 1000);
      return processPayment(amount, source);
    }
    if (error instanceof PaymentError) {
      // Log for investigation, return generic message
      console.error(`Payment failed: ${error.code} - ${error.message}`);
      return { 
        success: false, 
        userMessage: 'Payment could not be processed. Please try again.' 
      };
    }
    throw error; // Re-throw unexpected errors
  }
}
```

## Advanced usage

### Idempotent requests
```javascript
// REQUIRED for production: Prevents duplicate charges on retry
const charge = await client.charges.create(
  {
    amount: 2500,
    currency: 'usd',
    source: 'tok_visa'
  },
  {
    idempotencyKey: `order_${orderId}_${Date.now()}`
  }
);
```
```

---

## Example 3: Edge case—SDK with breaking changes and migration

**Input:**
- SDK: Analytics SDK v3 (upgrade from v2)
- Context: Major version with breaking changes
- Target audience: Existing v2 users

**Output:**

```md
# Analytics SDK v3 Migration Guide

## Overview
Version 3.0 introduces a new event batching system and changes to the initialization API. This guide helps you upgrade from v2.x.

## Breaking changes summary

| v2.x | v3.x | Migration action |
|------|------|------------------|
| `Analytics.init(key)` | `Analytics.create({ apiKey: key })` | Update initialization |
| `track(event, props)` | `track({ name: event, properties: props })` | Change to object parameter |
| Automatic batching | Explicit `flush()` required | Add flush calls or enable auto-flush |
| `userId` in init | `identify()` method | Separate identification from init |

## Step-by-step migration

### Step 1: Update initialization

**Before (v2.x):**
```javascript
import Analytics from 'analytics-sdk';

Analytics.init('YOUR_API_KEY', {
  userId: 'user_123',
  debug: true
});
```

**After (v3.x):**
```javascript
import { Analytics } from 'analytics-sdk';

// NOTE: userId is no longer set in init - use identify() instead
const analytics = Analytics.create({
  apiKey: process.env.ANALYTICS_KEY,
  debug: process.env.NODE_ENV !== 'production',
  autoFlush: true,           // NEW: Enable automatic batching
  flushInterval: 10000       // NEW: Flush every 10 seconds
});

// Identify user separately
analytics.identify('user_123', {
  email: 'user@example.com',
  plan: 'premium'
});
```

### Step 2: Update track calls

**Before (v2.x):**
```javascript
Analytics.track('Button Clicked', {
  buttonId: 'signup',
  page: '/home'
});
```

**After (v3.x):**
```javascript
analytics.track({
  name: 'Button Clicked',
  properties: {
    buttonId: 'signup',
    page: '/home'
  },
  // OPTIONAL: Override timestamp for historical events
  timestamp: new Date()
});
```

### Step 3: Handle batching

**If you disabled autoFlush:**
```javascript
// Manually flush before user leaves page
window.addEventListener('beforeunload', () => {
  analytics.flush();
});

// Or flush after critical events
await analytics.track({ name: 'Purchase Completed', ... });
await analytics.flush(); // Ensure event is sent immediately
```

## Troubleshooting migration issues

| Symptom | Cause | Solution |
|---------|-------|----------|
| Events not appearing in dashboard | Auto-flush disabled, no manual flush | Enable `autoFlush: true` or add `flush()` calls |
| `userId` undefined in events | Forgot to call `identify()` | Add `analytics.identify()` after initialization |
| "Invalid event format" error | Using old `track(name, props)` signature | Update to object parameter format |
| Duplicate events after upgrade | Both v2 and v3 installed | Remove v2 from dependencies |
```
