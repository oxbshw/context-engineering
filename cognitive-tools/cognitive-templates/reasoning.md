# Reasoning Templates

> "Logic is the anatomy of thought." — John Locke

## Overview

Reasoning templates guide language models through structured thinking processes to solve problems, generate insights, or make decisions. These templates build upon understanding templates by providing systematic approaches to processing information and reaching conclusions.

```
┌──────────────────────────────────────────────────────────────┐
│                                                              │
│  REASONING PROCESS                                           │
│                                                              │
│  Input → Structure → Apply Logic → Step-by-Step → Conclusion │
│                                                              │
└──────────────────────────────────────────────────────────────┘
```

## Basic Templates

### 1. Step-by-Step Reasoning

The fundamental template for breaking down complex reasoning into manageable steps.

```markdown
# Step-by-Step Reasoning Template

Task: Solve the following problem by breaking it down into clear, logical steps.

Problem: {{problem}}

Please follow this process:
1. **Understand**: Restate the problem and identify what you need to find.
2. **Plan**: Outline your approach to solving the problem.
3. **Execute**: Work through each step of your plan in detail.
   - Step 1: [Description of the first step]
   - Step 2: [Description of the second step]
   - Step 3: [Continue with additional steps as needed]
4. **Verify**: Check your solution against the original problem.
5. **Conclude**: State your final answer or conclusion clearly.

Show all your work and explain your reasoning at each step.
```

**Token Count**: ~130 tokens (template only)

**Usage Example**:
- For mathematical problem solving
- When working through complex logical arguments
- For any task requiring transparent reasoning

### 2. Compare and Contrast

For analytical reasoning that evaluates similarities and differences.

```markdown
# Compare and Contrast Template

Task: Analyze the similarities and differences between the following items.

Items to Compare: {{item_a}} and {{item_b}}

Please follow this structured approach:
1. **Background**: Briefly introduce both items and their context.
2. **Criteria Selection**: Identify the key dimensions for comparison.
3. **Systematic Comparison**:
   - Dimension 1: [Explain how both items relate to this dimension]
   - Dimension 2: [Explain how both items relate to this dimension]
   - Dimension 3: [Continue with additional dimensions as needed]
4. **Key Similarities**: Explicitly list the most important similarities.
5. **Key Differences**: Explicitly list the most important differences.
6. **Synthesis**: Explain what these similarities and differences reveal.
7. **Conclusion**: Summarize the most significant insights from this comparison.
```

**Token Count**: ~140 tokens (template only)

**Usage Example**:
- For comparing theories, products, or approaches
- When analyzing competing solutions
- For evaluating alternative explanations

### 3. Causal Analysis

For reasoning about cause and effect relationships.

```markdown
# Causal Analysis Template

Task: Analyze the causes and effects related to the following situation or phenomenon.

Situation: {{situation}}

Please follow this structured approach:
1. **Describe the Phenomenon**: Clearly state what needs to be explained.
2. **Identify Potential Causes**:
   - Immediate Causes: [Direct factors that led to the situation]
   - Underlying Causes: [Deeper factors that created conditions for the situation]
   - Contributory Factors: [Elements that amplified or enabled the causes]
3. **Evaluate Each Cause**:
   - Evidence: [What evidence supports this as a cause?]
   - Significance: [How important was this cause?]
   - Mechanism: [How did this cause lead to the effect?]
4. **Analyze Effects**:
   - Immediate Effects: [Direct consequences]
   - Long-term Effects: [Ongoing or future consequences]
   - Secondary Effects: [Indirect consequences]
5. **Examine Interactions**: How do these causes and effects interact with each other?
6. **Conclusion**: Summarize the most significant causal relationships.
```

**Token Count**: ~160 tokens (template only)

**Usage Example**:
- For historical analysis
- When investigating complex systems
- For understanding social or economic phenomena

## Advanced Templates

### 4. Hypothesis Testing

For systematically evaluating a hypothesis against evidence.

```markdown
# Hypothesis Testing Template

Task: Systematically evaluate the following hypothesis based on available evidence.

Hypothesis: {{hypothesis}}

Evidence: {{evidence}}

Please follow this structured approach:
1. **Clarify the Hypothesis**: Restate the hypothesis in precise terms.
2. **Identify Testable Predictions**: What should be true if the hypothesis is correct?
3. **Evaluate Evidence**:
   - Supporting Evidence: [Evidence that confirms predictions]
     - Strength: [How strongly does this evidence support the hypothesis?]
     - Reliability: [How reliable is this evidence?]
   - Contradictory Evidence: [Evidence that contradicts predictions]
     - Strength: [How strongly does this evidence oppose the hypothesis?]
     - Reliability: [How reliable is this evidence?]
   - Missing Evidence: [Evidence that should exist but isn't present]
4. **Consider Alternative Hypotheses**: What other explanations could account for the evidence?
5. **Weigh Comparative Explanatory Power**: How well does the hypothesis explain the evidence compared to alternatives?
6. **Conclusion**: Assess the overall credibility of the hypothesis.
7. **Confidence Level**: Indicate your level of confidence in this assessment.
```

**Token Count**: ~180 tokens (template only)

**Usage Example**:
- For scientific reasoning
- When evaluating theories or claims
- For evidence-based decision making

### 5. Decision Matrix

For structured decision making across multiple criteria.

```markdown
# Decision Matrix Template

Task: Evaluate options against criteria to make a structured decision.

Decision Context: {{decision_context}}
Options: {{options}}
Criteria: {{criteria}}

Please follow this structured approach:
1. **Define the Decision**: Clearly state what decision needs to be made.
2. **Establish Criteria Weights**:
   - Criterion 1: [Importance weight (1-10)]
   - Criterion 2: [Importance weight (1-10)]
   - [Continue for all criteria]
3. **Evaluate Each Option**:
   Create a matrix with options as rows and criteria as columns.
   
   | Option | Criterion 1 | Criterion 2 | ... | Total |
   |--------|-------------|-------------|-----|-------|
   | Option A | [Score] | [Score] | ... | [Sum] |
   | Option B | [Score] | [Score] | ... | [Sum] |
   
   For each cell, provide:
   - Score: [Rating (1-10)]
   - Justification: [Brief explanation]
   
4. **Calculate Weighted Scores**: Multiply each score by the criterion weight.
5. **Rank Options**: Order options based on their total weighted scores.
6. **Sensitivity Analysis**: How would the ranking change if weights were adjusted?
7. **Recommendation**: State the recommended option with justification.
```

**Token Count**: ~180 tokens (template only)

**Usage Example**:
- For choosing between alternatives
- When balancing multiple factors
- For transparent decision processes

### 6. Argument Construction

For building well-structured arguments.

```markdown
# Argument Construction Template

Task: Construct a well-reasoned argument for the following position.

Position: {{position}}

Please follow this structured approach:
1. **Thesis Statement**: Clearly articulate the main claim or position.
2. **Define Key Terms**: Clarify any ambiguous or technical terms.
3. **Establish Premises**:
   - Premise 1: [State first supporting claim]
     - Evidence: [Support for this premise]
     - Reasoning: [How this evidence supports the premise]
   - Premise 2: [State second supporting claim]
     - Evidence: [Support for this premise]
     - Reasoning: [How this evidence supports the premise]
   - [Continue with additional premises as needed]
4. **Logical Structure**: Explain how these premises lead to the conclusion.
5. **Address Counterarguments**:
   - Counterargument 1: [Potential objection]
     - Response: [Rebuttal or accommodation]
   - Counterargument 2: [Potential objection]
     - Response: [Rebuttal or accommodation]
6. **Conclusion**: Restate the thesis and summarize the supporting arguments.
```

**Token Count**: ~170 tokens (template only)

**Usage Example**:
- For persuasive writing
- When developing position papers
- For constructing logical cases

## Implementation Patterns

Here's a simple Python function to implement the Step-by-Step Reasoning template:

```python
def step_by_step_reasoning(problem, steps=None):
    """
    Create a prompt that guides through step-by-step reasoning.
    
    Args:
        problem (str): The problem to solve
        steps (list, optional): Custom steps for the reasoning process
        
    Returns:
        str: A formatted prompt for step-by-step reasoning
    """
    if steps is None:
        steps = [
            "Understand: Restate the problem and identify what you need to find.",
            "Plan: Outline your approach to solving the problem.",
            "Execute: Work through each step of your plan in detail.",
            "Verify: Check your solution against the original problem.",
            "Conclude: State your final answer or conclusion clearly."
        ]
    
    steps_text = "\n".join([f"{i+1}. **{step.split(':', 1)[0]}**:{step.split(':', 1)[1]}" 
                           for i, step in enumerate(steps)])
    
    return f"""
Task: Solve the following problem by breaking it down into clear, logical steps.

Problem: {problem}

Please follow this process:
{steps_text}

Show all your work and explain your reasoning at each step.
"""
```

## Measurement and Optimization

When using reasoning templates, measure their effectiveness by:

1. **Logical Validity**: Are the conclusions properly supported by the premises?
2. **Completeness**: Does the reasoning address all aspects of the problem?
3. **Transparency**: Is each step clearly explained and justified?
4. **Efficiency**: Does the reasoning take a direct path to the solution?
5. **Correctness**: Does the reasoning lead to the right answer or conclusion?

Optimize your templates by:
- Adjusting the level of detail based on problem complexity
- Adding domain-specific reasoning steps for specialized fields
- Customizing evaluation criteria for particular types of problems

## Combining with Other Tools

Reasoning templates work best as part of a complete cognitive workflow:

```
┌─────────────────────┐     ┌─────────────────┐     ┌─────────────────┐
│                     │     │                 │     │                 │
│ Understanding       │────►│ Reasoning       │────►│ Verification    │
│ Template            │     │ Template        │     │ Template        │
│                     │     │                 │     │                 │
└─────────────────────┘     └─────────────────┘     └─────────────────┘
```

For example, use an Understanding template to analyze a problem, apply a Reasoning template to solve it, and then use a Verification template to check the solution.

## Advanced Reasoning Patterns

For complex problems, consider these advanced patterns:

### Divide and Conquer

Break the problem into independent sub-problems, solve each separately, then combine the results.

```
┌───────────────────────────────────────────────────────────────┐
│                                                               │
│  Main Problem                                                 │
│       │                                                       │
│       ├────────────────┬────────────────┬────────────────┐    │
│       │                │                │                │    │
│       ▼                ▼                ▼                ▼    │
│  Sub-Problem 1    Sub-Problem 2    Sub-Problem 3    Sub-Problem 4 │
│       │                │                │                │    │
│       ├────────────────┼────────────────┼────────────────┘    │
│       │                │                │                     │
│       ▼                ▼                ▼                     │
│  Combine Solutions and Integrate Results                      │
│                                                               │
└───────────────────────────────────────────────────────────────┘
```

### Iterative Refinement

Start with a simple solution, then iteratively improve it.

```
┌───────────────────────────────────────────────────────────────┐
│                                                               │
│  Initial Solution                                             │
│       │                                                       │
│       ▼                                                       │
│  Identify Weaknesses                                          │
│       │                                                       │
│       ▼                                                       │
│  Improve Solution           ◄─────────────┐                   │
│       │                                    │                   │
│       ▼                                    │                   │
│  Evaluate Improvement                      │                   │
│       │                                    │                   │
│       └────────────────────────────────────┘                   │
│       │                                                        │
│       ▼                                                        │
│  Final Solution (when satisfactory)                            │
│                                                                │
└────────────────────────────────────────────────────────────────┘
```

### Analogical Reasoning

Apply reasoning patterns from a known domain to a new problem.

```
┌───────────────────────────────────────────────────────────────┐
│                                                               │
│  Target Problem                                               │
│       │                                                       │
│       ▼                                                       │
│  Identify Similar Solved Problem                              │
│       │                                                       │
│       ▼                                                       │
│  Map Elements from Solved Problem to Target Problem           │
│       │                                                       │
│       ▼                                                       │
│  Apply Similar Solution Strategy                              │
│       │                                                       │
│       ▼                                                       │
│  Adapt as Needed for Target Problem                           │
│                                                               │
└───────────────────────────────────────────────────────────────┘
```

## Next Steps

- Explore [verification.md](./verification.md) for templates that check reasoning
- See [composition.md](./composition.md) for ways to combine multiple templates
- Check out [../cognitive-programs/advanced-programs.md](../cognitive-programs/advanced-programs.md) for programmatic approaches that leverage these reasoning patterns
