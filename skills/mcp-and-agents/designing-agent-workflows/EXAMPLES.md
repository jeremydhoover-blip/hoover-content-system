# Examples

## Example 1: Code refactoring workflow

Input:
- Goal: Refactor a function to improve performance
- Complexity: Multi-step with validation
- Risk: Could break existing functionality

Output:
```md
# Workflow: Safe Function Refactoring

## Goal
Refactor a function to improve performance while preserving existing behavior.

## Success criteria
The workflow succeeds when:
- [ ] Refactored function passes all existing tests
- [ ] Performance benchmark shows improvement
- [ ] No regressions in dependent code

## State
Track these values across steps:
- `target_function`: string — function name to refactor
- `original_code`: string — backup of original implementation
- `test_results_before`: object — baseline test results
- `test_results_after`: object — post-refactor test results

---

## Steps

### Step 1: Identify and backup
**Input**: Function name from user
**Action**: 
- Locate function definition
- Store original code in `original_code`
- Identify all tests for this function
**Output**: `original_code` populated, test list identified
**Next**: Step 2

**On failure**:
- Function not found: Ask user to verify function name

---

### Step 2: Run baseline tests
**Input**: Test list from Step 1
**Action**: Execute all relevant tests
**Output**: `test_results_before` with pass/fail status
**Next**: Decision 1

**On failure**:
- Tests fail to run: Report environment issue, abort workflow

---

### Decision 1: Baseline tests pass?
**Evaluate**: All tests in `test_results_before` pass
**Branches**:
- IF all pass → Step 3
- IF any fail → Abort ("Cannot refactor: existing tests fail. Fix tests first.")

---

### Step 3: Analyze and plan refactoring
**Input**: `original_code`
**Action**:
- Identify performance bottlenecks
- Generate refactoring plan
- List specific changes to make
**Output**: Refactoring plan document
**Next**: Human Checkpoint 1

**On failure**:
- No improvements identified: Report "No refactoring opportunities found", end workflow

---

### Human Checkpoint 1: Approve refactoring plan
**Present to user**:
- Current code
- Proposed changes
- Rationale for each change
**User options**: Approve | Modify | Cancel

---

### Step 4: Apply refactoring
**Input**: Approved refactoring plan
**Action**: Modify function code according to plan
**Output**: Refactored code written to file
**Next**: Step 5

**On failure**:
- Syntax error in refactored code: Revert to `original_code`, report error

---

### Step 5: Run post-refactor tests
**Input**: Same test list from Step 1
**Action**: Execute all relevant tests
**Output**: `test_results_after` with pass/fail status
**Next**: Decision 2

**On failure**:
- Tests fail to run: Revert to `original_code`, report error

---

### Decision 2: All tests still pass?
**Evaluate**: All tests in `test_results_after` pass
**Branches**:
- IF all pass → Step 6
- IF any fail → Step 7 (rollback)

---

### Step 6: Run performance benchmark
**Input**: Refactored function
**Action**: Execute performance benchmark
**Output**: Timing comparison (before vs after)
**Next**: Decision 3

---

### Decision 3: Performance improved?
**Evaluate**: Refactored version faster than original
**Branches**:
- IF faster → End (SUCCESS)
- IF same or slower → Human Checkpoint 2

---

### Human Checkpoint 2: Accept despite no improvement?
**Present to user**: "No performance improvement. Keep refactored code anyway?"
**User options**: Keep | Revert

---

### Step 7: Rollback
**Input**: `original_code`
**Action**: Restore original function implementation
**Output**: Original code restored
**Next**: End (FAILURE: "Tests failed after refactoring")

---

## Termination conditions
- SUCCESS: Tests pass AND (performance improved OR user accepts)
- FAILURE: Tests fail after refactoring (auto-rollback applied)
- ABORT: User cancels OR baseline tests already failing
```

---

## Example 2: Data import workflow

Input:
- Goal: Import data from CSV to database
- Steps: Validate, transform, load
- Risks: Data corruption, duplicate imports

Output:
```md
# Workflow: CSV Data Import

## Goal
Import data from CSV file into database with validation and deduplication.

## Success criteria
- [ ] All valid rows imported
- [ ] Invalid rows logged with reasons
- [ ] No duplicate records created
- [ ] Import audit trail created

## State
- `file_path`: string — source CSV file
- `total_rows`: int — row count in file
- `valid_rows`: array — rows passing validation
- `invalid_rows`: array — rows failing validation with reasons
- `imported_count`: int — successfully imported rows
- `import_id`: string — unique identifier for this import batch

---

## Steps

### Step 1: Load and count
**Input**: `file_path` from user
**Action**: Read CSV, count rows
**Output**: `total_rows` populated
**Next**: Step 2

**On failure**:
- File not found: Ask user to verify path
- Invalid CSV format: Report parse error with line number

---

### Step 2: Validate rows
**Input**: CSV data
**Action**: For each row:
- Check required fields present
- Validate data types
- Check business rules
**Output**: `valid_rows` and `invalid_rows` populated
**Next**: Decision 1

**On failure**:
- Validation rule error: Report which rule failed

---

### Decision 1: Enough valid rows?
**Evaluate**: `valid_rows.length / total_rows >= 0.8` (80% threshold)
**Branches**:
- IF >= 80% valid → Human Checkpoint 1
- IF < 80% valid → Abort ("Too many invalid rows: {invalid_count}/{total_rows}. Fix source data.")

---

### Human Checkpoint 1: Review validation results
**Present to user**:
- Valid: {valid_count} rows
- Invalid: {invalid_count} rows
- Sample of invalid rows with reasons
**User options**: Proceed | Download invalid report | Cancel

---

### Step 3: Check for duplicates
**Input**: `valid_rows`
**Action**: Query database for existing records matching keys
**Output**: Rows marked as new or duplicate
**Next**: Decision 2

---

### Decision 2: Duplicates found?
**Evaluate**: Any rows match existing database records
**Branches**:
- IF no duplicates → Step 4
- IF duplicates found → Human Checkpoint 2

---

### Human Checkpoint 2: Handle duplicates
**Present to user**: "{dup_count} rows match existing records"
**User options**: 
- Skip duplicates (import new only)
- Update duplicates (overwrite)
- Cancel import

---

### Step 4: Import data
**Input**: Rows to import (based on duplicate decision)
**Action**: 
- Begin database transaction
- Insert rows in batches of 100
- Track progress
**Output**: `imported_count` updated
**Next**: Step 5

**On failure**:
- Database error: Rollback transaction, report error

---

### Step 5: Create audit record
**Input**: Import results
**Action**: Log import summary with `import_id`
**Output**: Audit record created
**Next**: End (SUCCESS)

---

## Termination conditions
- SUCCESS: All valid rows imported, audit created
- FAILURE: Database error (transaction rolled back)
- ABORT: User cancels OR too many invalid rows
```

---

## Example 3: Edge case — Workflow with external dependency

Input:
- Goal: Generate report using external API
- Complexity: API may be unavailable or rate-limited
- Requirement: Must handle API failures gracefully

Output:
```md
# Workflow: External API Report Generation

## Goal
Generate report by fetching data from external API and formatting results.

## Success criteria
- [ ] Report generated with available data
- [ ] API failures handled gracefully
- [ ] User informed of any data gaps

## State
- `api_status`: enum (available, degraded, unavailable)
- `data_sources`: array — list of API endpoints to call
- `fetched_data`: object — data retrieved from APIs
- `failed_sources`: array — APIs that failed
- `retry_count`: int — current retry attempt

## Configuration
- `max_retries`: 3
- `retry_delay`: [2s, 5s, 10s]
- `api_timeout`: 30s

---

## Steps

### Step 1: Check API health
**Input**: API base URL
**Action**: Call health endpoint
**Output**: `api_status` set
**Next**: Decision 1

---

### Decision 1: API available?
**Evaluate**: `api_status`
**Branches**:
- IF available → Step 2
- IF degraded → Human Checkpoint 1
- IF unavailable → Decision 2

---

### Human Checkpoint 1: Proceed with degraded API?
**Present**: "API is experiencing issues. Proceed? Some data may be missing."
**Options**: Proceed | Wait and retry | Cancel

---

### Decision 2: Use cached data?
**Evaluate**: Cache exists and is < 24 hours old
**Branches**:
- IF cache valid → Step 4 (use cache)
- IF no cache → Abort ("API unavailable and no cache. Try again later.")

---

### Step 2: Fetch data from APIs
**Input**: `data_sources` list
**Action**: For each source:
```
WHILE retry_count < max_retries:
    response = call_api(source, timeout=api_timeout)
    IF response.success:
        store in fetched_data
        BREAK
    ELSE:
        retry_count++
        wait(retry_delay[retry_count])
        
IF not success:
    add to failed_sources
```
**Output**: `fetched_data` and `failed_sources` populated
**Next**: Decision 3

---

### Decision 3: All sources fetched?
**Evaluate**: `failed_sources.length`
**Branches**:
- IF 0 failures → Step 3
- IF some failures → Human Checkpoint 2
- IF all failed → Use cache or abort

---

### Human Checkpoint 2: Continue with partial data?
**Present**: "{failed_count} data sources unavailable: {source_names}"
**Options**: Continue with partial data | Retry failed sources | Cancel

---

### Step 3: Generate report
**Input**: `fetched_data`
**Action**: Format data into report structure
**Output**: Report document
**Next**: Step 4

---

### Step 4: Finalize
**Input**: Report
**Action**: 
- Save report
- Update cache with fresh data
- Note any data gaps in report footer
**Output**: Final report saved
**Next**: End (SUCCESS)

---

## Termination conditions
- SUCCESS: Report generated (may have data gaps noted)
- FAILURE: All APIs failed AND no valid cache
- ABORT: User cancels
```
