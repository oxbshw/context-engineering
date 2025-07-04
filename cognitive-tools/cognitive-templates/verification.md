# Verification Templates

> "Trust, but verify." — Russian proverb

## Overview

Verification templates help language models check their own work, catch errors, and ensure the quality of their outputs. These templates are crucial for increasing reliability, reducing hallucinations, and improving overall accuracy.

```
┌──────────────────────────────────────────────────────────────┐
│                                                              │
│  VERIFICATION PROCESS                                        │
│                                                              │
│  Solution → Check Logic → Test Assumptions → Correct → Final │
│                                                              │
└──────────────────────────────────────────────────────────────┘
```

## Basic Templates

### 1. Solution Verification

The fundamental template for checking a solution or answer.

```markdown
# Solution Verification Template

Task: Verify the correctness of the following solution.

Problem: {{problem}}
Proposed Solution: {{solution}}

Please follow this verification process:
1. **Restate the Problem**: Confirm understanding of what was asked.
2. **Check Methodology**: Is the approach used appropriate for this problem?
3. **Verify Calculations**: Check all mathematical operations for accuracy.
4. **Check Logic**: Examine the reasoning for logical errors or gaps.
5. **Test with Examples**: Test the solution with specific examples or edge cases.
6. **Check Constraints**: Ensure all constraints from the original problem are satisfied.
7. **Final Assessment**: State whether the solution is:
   - Correct: The solution is completely accurate
   - Partially Correct: The solution has minor errors (specify)
   - Incorrect: The solution has major flaws (specify)

If errors are found, explain them clearly and suggest corrections.
```

**Token Count**: ~160 tokens (template only)

**Usage Example**:
- For mathematical solutions
- When checking logical arguments
- For any output where accuracy is crucial

### 2. Fact Checking

For verifying factual claims and statements.

```markdown
# Fact Checking Template

Task: Verify the accuracy of the following statement(s).

Statement(s): {{statements}}

Please follow this verification process:
1. **Break Down Claims**: Identify each distinct factual claim.
2. **Assess Knowledge Base**: Determine if you have reliable information about each claim.
3. **Verify Each Claim**:
   - Claim 1: [Restate the claim]
     - Assessment: [Accurate / Inaccurate / Partially Accurate / Uncertain]
     - Explanation: [Provide relevant facts and context]
     - Confidence: [High / Medium / Low]
   - Claim 2: [Continue for each claim]
4. **Check for Omissions**: Identify any relevant context that's missing.
5. **Overall Assessment**: Summarize the overall accuracy.
6. **Knowledge Limitations**: Note any claims you cannot verify with confidence.

Provide corrections for any inaccurate information.
```

**Token Count**: ~150 tokens (template only)

**Usage Example**:
- For checking historical or scientific claims
- When verifying information in summaries
- For any output containing factual assertions

### 3. Consistency Check

For ensuring internal consistency in content.

```markdown
# Consistency Check Template

Task: Check the following content for internal consistency.

Content: {{content}}

Please follow this verification process:
1. **Identify Key Elements**: Note the main claims, definitions, and arguments.
2. **Create Consistency Map**:
   - Element 1: [Description]
   - Element 2: [Description]
   - [Continue for all important elements]
3. **Check for Contradictions**:
   - Between Elements: Compare each element with others for compatibility
   - Within Elements: Check each element for internal contradictions
4. **Temporal Consistency**: Ensure events and developments follow a logical timeline.
5. **Terminology Consistency**: Verify that terms are used consistently throughout.
6. **Logical Flow**: Check that conclusions follow from premises.
7. **Final Assessment**: Summarize any inconsistencies found.

For each inconsistency, explain the contradiction and suggest a resolution.
```

**Token Count**: ~160 tokens (template only)

**Usage Example**:
- For long-form content
- When checking complex arguments
- For any output that builds on multiple premises

## Advanced Templates

### 4. Comprehensive Error Analysis

For detailed examination of potential errors across multiple dimensions.

```markdown
# Comprehensive Error Analysis Template

Task: Perform a thorough error analysis on the following content.

Content: {{content}}
Context: {{context}}

Please examine for these error types:
1. **Factual Errors**:
   - Incorrect statements: [Identify and correct]
   - Outdated information: [Identify and update]
   - Misattributed statements: [Identify and correct]

2. **Logical Errors**:
   - False equivalences: [Identify]
   - Non sequiturs: [Identify]
   - Circular reasoning: [Identify]
   - Hasty generalizations: [Identify]

3. **Mathematical/Computational Errors**:
   - Calculation mistakes: [Identify and correct]
   - Formula application errors: [Identify and correct]
   - Unit conversion issues: [Identify and correct]

4. **Contextual Errors**:
   - Misunderstanding of context: [Clarify]
   - Inappropriate assumptions: [Identify]
   - Missing relevant information: [Supply]

5. **Linguistic Errors**:
   - Ambiguous statements: [Clarify]
   - Incorrect terminology: [Correct]
   - Inconsistent language: [Standardize]

6. **Structural Errors**:
   - Organizational problems: [Identify]
   - Missing components: [Identify]
   - Redundancies: [Identify]

For each error found, explain:
- What the error is
- Why it's problematic
- How it should be corrected

Conclude with an overall assessment of the content's accuracy and reliability.
```

**Token Count**: ~240 tokens (template only)

**Usage Example**:
- For critical review of important content
- When maximum accuracy is required
- For peer review or editorial processes

### 5. Alternative Perspective Analysis

For checking bias and exploring alternative viewpoints.

```markdown
# Alternative Perspective Analysis Template

Task: Analyze the following content from alternative perspectives to check for bias or blind spots.

Content: {{content}}

Please follow this process:
1. **Identify the Content's Perspective**: What worldview, assumptions, or values underlie the content?

2. **Explore Alternative Perspectives**:
   - Perspective A: [Description of a different viewpoint]
     - How would this perspective view the content?
     - What would it critique or question?
     - What additional considerations would it raise?
   
   - Perspective B: [Description of another different viewpoint]
     - How would this perspective view the content?
     - What would it critique or question?
     - What additional considerations would it raise?
   
   - [Continue with additional relevant perspectives]

3. **Identify Blind Spots**: What important considerations are missing from the original content?

4. **Check for Unstated Assumptions**: What does the content take for granted that might be questioned?

5. **Balance Assessment**: Is the content fair and balanced, or does it favor certain perspectives?

6. **Recommendations**: Suggest modifications that would make the content more comprehensive and balanced.

This analysis helps ensure that the content accounts for diverse viewpoints and avoids unintentional bias.
```

**Token Count**: ~220 tokens (template only)

**Usage Example**:
- For policy analysis
- When checking for cultural or ideological bias
- For any content addressing controversial topics

### 6. Implementation Verification

For checking that a solution can actually be implemented.

```markdown
# Implementation Verification Template

Task: Verify that the following solution can be practically implemented.

Proposed Solution: {{solution}}
Implementation Context: {{context}}

Please follow this verification process:
1. **Feasibility Assessment**:
   - Technical feasibility: Can this be built with available technology?
   - Resource requirements: What resources (time, money, skills) would be needed?
   - Scalability: Would the solution work at the required scale?

2. **Constraints Check**:
   - Technical constraints: Does the solution respect technical limitations?
   - Regulatory constraints: Does it comply with relevant regulations?
   - Operational constraints: Can it be implemented within operational parameters?

3. **Risk Analysis**:
   - Implementation risks: What could go wrong during implementation?
   - Operational risks: What could go wrong once implemented?
   - Mitigation strategies: How could these risks be addressed?

4. **Dependency Analysis**:
   - External dependencies: What does this solution depend on?
   - Critical path: Which dependencies are on the critical path?
   - Vulnerability points: Where could dependencies cause problems?

5. **Testing Approach**:
   - Validation methods: How could the implementation be tested?
   - Success criteria: How would success be measured?
   - Failure scenarios: How would failures be detected and addressed?

6. **Overall Assessment**: Is the solution implementable as described? What modifications would improve implementability?

This verification ensures that solutions are not just theoretically sound but practically viable.
```

**Token Count**: ~240 tokens (template only)

**Usage Example**:
- For engineering solutions
- When evaluating project proposals
- For any solution that requires practical implementation

## Implementation Patterns

Here's a simple Python function to implement the Solution Verification template:

```python
def verify_solution(problem, solution):
    """
    Create a prompt that verifies a proposed solution.
    
    Args:
        problem (str): The original problem
        solution (str): The proposed solution to verify
        
    Returns:
        str: A formatted prompt for solution verification
    """
    return f"""
Task: Verify the correctness of the following solution.

Problem: {problem}
Proposed Solution: {solution}

Please follow this verification process:
1. **Restate the Problem**: Confirm understanding of what was asked.
2. **Check Methodology**: Is the approach used appropriate for this problem?
3. **Verify Calculations**: Check all mathematical operations for accuracy.
4. **Check Logic**: Examine the reasoning for logical errors or gaps.
5. **Test with Examples**: Test the solution with specific examples or edge cases.
6. **Check Constraints**: Ensure all constraints from the original problem are satisfied.
7. **Final Assessment**: State whether the solution is:
   - Correct: The solution is completely accurate
   - Partially Correct: The solution has minor errors (specify)
   - Incorrect: The solution has major flaws (specify)

If errors are found, explain them clearly and suggest corrections.
"""
```

## Self-Correction Loop

One of the most powerful applications of verification templates is the self-correction loop:

```
┌─────────────────────────────────────────────────────────────────────┐
│                                                                     │
│  Initial Solution                                                   │
│       │                                                             │
│       ▼                                                             │
│  Apply Verification Template                                        │
│       │                                                             │
│       ▼                                                             │
│  Errors Found?                                                      │
│       │                                                             │
│       ├─────────────Yes─────────────┐                               │
│       │                             │                               │
│       ▼                             ▼                               │
│  No   │                        Apply Corrections                    │
│       │                             │                               │
│       ▼                             ▼                               │
│  Final Verified Solution ◄──────────┘                               │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
```

Implementation example:

```python
def self_correction_loop(problem, max_iterations=3):
    """
    Implement a self-correction loop for problem solving.
    
    Args:
        problem (str): The problem to solve
        max_iterations (int): Maximum number of correction iterations
        
    Returns:
        dict: The final solution and verification history
    """
    # Initial solution
    solution = llm.generate(f"Solve this problem: {problem}")
    
    history = [{"type": "solution", "content": solution}]
    iteration = 0
    
    while iteration < max_iterations:
        # Verify the current solution
        verification = llm.generate(verify_solution(problem, solution))
        history.append({"type": "verification", "content": verification})
        
        # Check if corrections are needed
        if "Correct: The solution is completely accurate" in verification:
            break
        
        # Generate corrected solution
        correction_prompt = f"""
        Based on the verification feedback below, provide a corrected solution to the original problem.
        
        Original Problem: {problem}
        
        Previous Solution: {solution}
        
        Verification Feedback: {verification}
        
        Please provide a fully corrected solution that addresses all issues identified in the verification.
        """
        
        corrected_solution = llm.generate(correction_prompt)
        history.append({"type": "correction", "content": corrected_solution})
        
        # Update solution for next iteration
        solution = corrected_solution
        iteration += 1
    
    return {
        "problem": problem,
        "final_solution": solution,
        "verification_history": history,
        "iterations": iteration
    }
```

## Measurement and Optimization

When using verification templates, measure their effectiveness by:

1. **Error Detection Rate**: What percentage of injected errors are caught?
2. **False Positive Rate**: How often are correct elements incorrectly flagged?
3. **Correction Quality**: How effective are the suggested corrections?
4. **Iteration Efficiency**: How many iterations to reach a correct solution?

Optimize your templates by:
- Adding domain-specific verification steps for specialized fields
- Tuning the level of scrutiny based on the importance of accuracy
- Focusing on common error types for particular tasks

## Combining with Other Tools

Verification templates complete the cognitive workflow:

```
┌─────────────────────┐     ┌─────────────────┐     ┌─────────────────┐
│                     │     │                 │     │                 │
│ Understanding       │────►│ Reasoning       │────►│ Verification    │
│ Template            │     │ Template        │     │ Template        │
│                     │     │                 │     │                 │
└─────────────────────┘     └─────────────────┘     └─────────────────┘
          ▲                                                │
          │                                                │
          └────────────────────────────────────────────────┘
                        (Correction Loop)
```

This creates a complete cognitive system that can:
1. Understand a problem
2. Generate a solution
3. Verify and correct the solution
4. Iterate until a satisfactory result is achieved

## Next Steps

- Explore [composition.md](./composition.md) for ways to combine multiple templates
- See how these templates can be integrated into complete cognitive programs in [../cognitive-programs/basic-programs.md](../cognitive-programs/basic-programs.md)
- Learn about complete cognitive architectures in [../cognitive-architectures/solver-architecture.md](../cognitive-architectures/solver-architecture.md)
