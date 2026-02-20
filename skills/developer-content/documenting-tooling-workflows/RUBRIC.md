# Rubric

Pass if all are true:
- Workflow has clear start state and end state defined
- Prerequisites include version-pinned tools with verification commands
- Every step includes the command, expected output, and at least one troubleshooting tip
- Decision points document all branches and criteria for choosing
- Destructive operations have rollback procedures
- Output artifacts are named with location and format specified
- A verification step confirms overall workflow success
- Common failure modes are documented with resolutions
- Tool version requirements specify minimum versions, not just "latest"
- Workflow diagram or sequence is included for 4+ step workflows

Fail if any are true:
- Step documented without expected output
- Prerequisite tool listed without version or verification command
- Destructive operation without rollback procedure
- Decision point with undocumented branch
- Workflow ends without verification step
- Assumed knowledge (e.g., "configure the tool as usual") without specifics
- Version requirement says "latest" without minimum version
