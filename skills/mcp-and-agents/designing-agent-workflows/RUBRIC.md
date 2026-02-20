# Rubric

Pass if all are true:
- Workflow goal is stated in one clear sentence
- Success criteria are measurable and verifiable
- Every step has defined input, action, output, and next step
- Every decision point has explicit conditions for all branches
- State variables are declared with type and purpose
- Every step has failure handling defined
- Human checkpoints exist before irreversible or high-risk actions
- Termination conditions are explicit (success, failure, abort)
- No dead ends (every path leads to termination or loops with exit condition)
- Loop constructs have explicit termination conditions (max iterations, success condition)

Fail if any are true:
- Workflow goal is vague or missing
- Success criteria are subjective (e.g., "works well")
- Step missing input, action, output, or next step
- Decision point with undocumented branch (ELSE case missing)
- State implicitly assumed but not declared
- Step without failure handling
- Irreversible action without human checkpoint
- Infinite loop possible (no termination condition)
- Dead end where workflow stops without success/failure status
