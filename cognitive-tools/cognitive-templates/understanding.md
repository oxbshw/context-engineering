# Understanding Templates

> "The beginning of wisdom is the definition of terms." — Socrates

## Overview

Understanding templates help language models comprehend and analyze information before attempting to solve a problem or generate content. These templates serve as the foundation for effective reasoning by ensuring the model has properly interpreted the task, context, and requirements.

```
┌──────────────────────────────────────────────────────────────┐
│                                                              │
│  UNDERSTANDING PROCESS                                       │
│                                                              │
│  Input → Analyze → Structure → Clarify → Ready for Reasoning │
│                                                              │
└──────────────────────────────────────────────────────────────┘
```

## Basic Templates

### 1. Question Analysis

The most fundamental understanding template helps break down a question or problem into its core components.

```markdown
# Question Analysis Template

Task: Analyze and break down the following question before attempting to answer it.

Question: {{question}}

Please provide:
1. **Question Type**: What kind of question is this? (e.g., factual, conceptual, analytical)
2. **Core Task**: What specific action or thinking is required?
3. **Key Components**: What are the main elements that need to be addressed?
4. **Implicit Assumptions**: What unstated assumptions might be relevant?
5. **Knowledge Domains**: What fields of knowledge are relevant?
6. **Constraints**: Are there any explicit or implicit constraints?
7. **Restatement**: Restate the question in your own words for clarity.

Once you've completed this analysis, you'll be better prepared to address the question effectively.
```

**Token Count**: ~120 tokens (template only)

**Usage Example**:
- For complex questions where understanding the requirements is crucial
- When precision in interpretation matters
- Before tackling multi-step problems

### 2. Information Extraction

For extracting structured information from text.

```markdown
# Information Extraction Template

Task: Extract and organize the key information from the following text.

Text: {{text}}

Please extract:
1. **Main Topic**: What is the central subject?
2. **Key Facts**: List the most important factual statements.
3. **Entities**: Identify people, organizations, locations, dates, etc.
4. **Relationships**: How are these entities related to each other?
5. **Numerical Data**: Extract any numbers, statistics, or measurements.
6. **Claims**: What assertions or arguments are made?
7. **Evidence**: What support is provided for these claims?

Organize this information in a clear, structured format.
```

**Token Count**: ~110 tokens (template only)

**Usage Example**:
- For processing research papers or articles
- When summarizing complex documents
- Before synthesizing information from multiple sources

### 3. Problem Decomposition

For breaking down complex problems into solvable parts.

```markdown
# Problem Decomposition Template

Task: Decompose the following problem into smaller, manageable components.

Problem: {{problem}}

Please provide:
1. **Problem Type**: What category of problem is this?
2. **Goal State**: What does a successful solution look like?
3. **Given Information**: What information is explicitly provided?
4. **Unknown Variables**: What needs to be determined?
5. **Constraints**: What limitations or conditions must be satisfied?
6. **Sub-Problems**: Break down the main problem into smaller parts.
7. **Dependencies**: How do these sub-problems relate to each other?
8. **Solution Approach**: Suggest a high-level strategy for solving the problem.

This decomposition will provide a structured approach to solving the problem.
```

**Token Count**: ~120 tokens (template only)

**Usage Example**:
- For mathematical or logical problems
- When faced with multi-step reasoning tasks
- Before attempting complex analyses

## Advanced Templates

### 4. Conceptual Mapping

For understanding relationships between concepts within a domain.

```markdown
# Conceptual Mapping Template

Task: Create a conceptual map of the ideas and relationships in the following text.

Text: {{text}}

Please provide:
1. **Core Concepts**: Identify the central ideas or concepts.
2. **Concept Definitions**: Briefly define each concept.
3. **Hierarchical Relationships**: Which concepts are subcategories of others?
4. **Causal Relationships**: Which concepts influence or cause others?
5. **Contrasting Concepts**: Which concepts stand in opposition to each other?
6. **Complementary Concepts**: Which concepts support or enhance each other?
7. **Missing Concepts**: Are there any implied but unstated concepts?

Represent these relationships in a structured format that shows how the concepts interconnect.
```

**Token Count**: ~120 tokens (template only)

**Usage Example**:
- For theoretical or abstract content
- When analyzing complex systems
- Before synthesizing disparate information

### 5. Multi-Perspective Analysis

For understanding different viewpoints on a topic.

```markdown
# Multi-Perspective Analysis Template

Task: Analyze the following topic from multiple perspectives.

Topic: {{topic}}

Please provide:
1. **Perspective Identification**: What major viewpoints exist on this topic?
2. **Core Arguments**: What are the main arguments from each perspective?
3. **Evidence Base**: What evidence supports each perspective?
4. **Underlying Values**: What values or assumptions underlie each perspective?
5. **Areas of Agreement**: Where do the perspectives converge?
6. **Key Disagreements**: What are the fundamental points of contention?
7. **Synthesis Possibilities**: How might these perspectives be integrated?

This analysis will provide a balanced understanding of the different ways to view this topic.
```

**Token Count**: ~120 tokens (template only)

**Usage Example**:
- For controversial or complex topics
- When balanced understanding is crucial
- Before forming a nuanced position

### 6. Requirement Analysis

For clearly understanding task requirements.

```markdown
# Requirement Analysis Template

Task: Analyze the requirements for the following task or project.

Task Description: {{task_description}}

Please provide:
1. **Primary Objective**: What is the main goal?
2. **Deliverables**: What specific outputs are required?
3. **Quality Criteria**: How will success be measured?
4. **Constraints**: What limitations must be worked within?
5. **Dependencies**: What external factors impact this task?
6. **Stakeholders**: Who is involved or affected?
7. **Priorities**: Which aspects are most important?
8. **Ambiguities**: What aspects need clarification?

This analysis will ensure all requirements are properly understood before proceeding.
```

**Token Count**: ~120 tokens (template only)

**Usage Example**:
- For project planning
- When tasked with creating specific outputs
- Before beginning any complex task

## Implementation Patterns

Here's a simple Python function to implement the Question Analysis template:

```python
def understand_question(question):
    """
    Create a prompt that analyzes and breaks down a question.
    
    Args:
        question (str): The question to analyze
        
    Returns:
        str: A formatted prompt for question analysis
    """
    return f"""
Task: Analyze and break down the following question before attempting to answer it.

Question: {question}

Please provide:
1. **Question Type**: What kind of question is this? (e.g., factual, conceptual, analytical)
2. **Core Task**: What specific action or thinking is required?
3. **Key Components**: What are the main elements that need to be addressed?
4. **Implicit Assumptions**: What unstated assumptions might be relevant?
5. **Knowledge Domains**: What fields of knowledge are relevant?
6. **Constraints**: Are there any explicit or implicit constraints?
7. **Restatement**: Restate the question in your own words for clarity.

Once you've completed this analysis, you'll be better prepared to address the question effectively.
"""
```

## Measurement and Optimization

When using understanding templates, measure their effectiveness by:

1. **Accuracy**: Does the understanding correctly identify all key elements?
2. **Comprehensiveness**: Are all important aspects of the input covered?
3. **Clarity**: Is the structured understanding clear and unambiguous?
4. **Utility**: Does the understanding improve subsequent reasoning?

Optimize your templates by:
- Removing unnecessary components that don't improve understanding
- Adding specific components needed for your particular domain
- Adjusting the level of detail based on the complexity of your inputs

## Combining with Other Tools

Understanding templates work best when combined with other cognitive tools:

```
┌─────────────────────┐     ┌─────────────────┐     ┌─────────────────┐
│                     │     │                 │     │                 │
│ Understanding       │────►│ Reasoning       │────►│ Verification    │
│ Template            │     │ Template        │     │ Template        │
│                     │     │                 │     │                 │
└─────────────────────┘     └─────────────────┘     └─────────────────┘
```

For example, use the Question Analysis template first, then pass the structured understanding to a problem-solving template, and finally verify the solution with a verification template.

## Next Steps

- Explore [reasoning.md](./reasoning.md) for templates that build on understanding
- See [composition.md](./composition.md) for ways to combine multiple templates
- Check out [../cognitive-programs/basic-programs.md](../cognitive-programs/basic-programs.md) for programmatic approaches that use these templates
