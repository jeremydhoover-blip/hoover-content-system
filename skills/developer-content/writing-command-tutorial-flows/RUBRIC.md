# Rubric

## Pass criteria
All must be true:

### Structure requirements
- [ ] Tutorial states learning goal in first paragraph
- [ ] Time estimate and difficulty level are provided
- [ ] Prerequisites are explicit and checkable
- [ ] Each step has a clear action verb in heading
- [ ] Each step shows the command and expected output

### Flow requirements
- [ ] Steps are in dependency order (no forward references)
- [ ] Steps build incrementally (each depends on previous)
- [ ] Checkpoints exist at critical milestones (minimum 1 per 3 steps)
- [ ] Final verification step confirms end state

### Completeness requirements
- [ ] All placeholders are explained with replacement instructions
- [ ] Expected output is realistic and shows success indicators
- [ ] Troubleshooting covers at least 2 common failure points
- [ ] Cleanup section provided if tutorial creates resources

### Usability requirements
- [ ] Commands are copy-pasteable (no smart quotes, no truncation)
- [ ] Commands work in stated shell (bash, PowerShell, etc.)
- [ ] Optional or conditional steps are clearly marked
- [ ] Time estimates are realistic for stated difficulty level

### Pedagogical requirements
- [ ] Steps explain why, not just what
- [ ] Complexity increases progressively
- [ ] User understands what they've built at the end
- [ ] Next steps point to related learning

## Fail criteria
Fail if any are true:

- Step depends on something not yet done
- Command has syntax error or missing required arguments
- Expected output doesn't match what command actually produces
- Placeholder is used without explanation
- Step says "run this command" without showing output
- Checkpoint verifies wrong thing or is missing for destructive operation
- Troubleshooting entries are generic ("if it doesn't work, try again")
- Tutorial creates persistent resources with no cleanup section
- Time estimate is wildly inaccurate (>2x actual time)
- Steps skip over environment-specific requirements (OS, shell)
