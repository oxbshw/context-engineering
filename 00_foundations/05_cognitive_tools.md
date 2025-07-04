# Cognitive Tools: Extending the Context Engineering Framework

> "The mind is not a vessel to be filled, but a fire to be kindled." — Plutarch

## From Biology to Cognition

Our journey through context engineering has followed a biological metaphor:

```
┌──────────┐     ┌──────────┐     ┌──────────┐     ┌──────────┐
│          │     │          │     │          │     │          │
│  Atoms   │────►│ Molecules│────►│  Cells   │────►│  Organs  │
│          │     │          │     │          │     │          │
└──────────┘     └──────────┘     └──────────┘     └──────────┘
    │                │                │                │
    ▼                ▼                ▼                ▼
┌──────────┐     ┌──────────┐     ┌──────────┐     ┌──────────┐
│          │     │          │     │          │     │          │
│  Prompts │     │ Few-shot │     │  Memory  │     │Multi-agent│
│          │     │          │     │          │     │          │
└──────────┘     └──────────┘     └──────────┘     └──────────┘
```
## Cognitive Tools? 
> “Cognitive tools” encapsulate reasoning operations within the LLM itself — [IBM Zurich](https://www.arxiv.org/pdf/2506.12115)

## **[Eliciting Reasoning in Language Models with Cognitive Tools - IBM Zurich June 2025](https://www.arxiv.org/pdf/2506.12115)**


![image](https://github.com/user-attachments/assets/cd06c3f5-5a0b-4ee7-bbba-2f9f243f70ae)

> **These cognitive tools (structured prompt templates as tool calls) break down the problem by identifying the main concepts at hand, extracting relevant information in the question, and highlighting meaningful properties, theorems, and techniques that
might be helpful in solving the problem.**

![image](https://github.com/user-attachments/assets/f7ce8605-6fa3-494f-94cd-94e6b23032b6)

Now, we'll extend this framework by drawing parallels to human cognition. Just as human minds use cognitive tools to process information efficiently, we can create similar structures for LLMs:

```
┌──────────────────────────────────────────────────────────────────────┐
│                      COGNITIVE TOOLS EXTENSION                       │
├──────────┬───────────────────┬──────────────────────────────────────┤
│          │                   │                                      │
│ HUMAN    │ Heuristics        │ Mental shortcuts that simplify       │
│ COGNITION│                   │ complex problems                     │
│          │                   │                                      │
├──────────┼───────────────────┼──────────────────────────────────────┤
│          │                   │                                      │
│ LLM      │ Prompt Programs   │ Structured prompt patterns that      │
│ PARALLEL │                   │ guide model reasoning                │
│          │                   │                                      │
└──────────┴───────────────────┴──────────────────────────────────────┘

┌──────────────────────────────────────────────────────────────────────┐
│                                                                      │
├──────────┬───────────────────┬──────────────────────────────────────┤
│          │                   │                                      │
│ HUMAN    │ Schemas           │ Organized knowledge structures       │
│ COGNITION│                   │ that help categorize information     │
│          │                   │                                      │
├──────────┼───────────────────┼──────────────────────────────────────┤
│          │                   │                                      │
│ LLM      │ Context Schemas   │ Standardized formats that            │
│ PARALLEL │                   │ structure information for models     │
│          │                   │                                      │
└──────────┴───────────────────┴──────────────────────────────────────┘

┌──────────────────────────────────────────────────────────────────────┐
│                                                                      │
├──────────┬───────────────────┬──────────────────────────────────────┤
│          │                   │                                      │
│ HUMAN    │ Priming           │ Activation of certain associations   │
│ COGNITION│                   │ that influence subsequent thinking   │
│          │                   │                                      │
├──────────┼───────────────────┼──────────────────────────────────────┤
│          │                   │                                      │
│ LLM      │ Recursive         │ Self-referential prompting that      │
│ PARALLEL │ Prompting         │ shapes model behavior patterns       │
│          │                   │                                      │
└──────────┴───────────────────┴──────────────────────────────────────┘
```

## Prompt Programs: Algorithmic Thinking for LLMs (Reasoning Tool Calls)

A prompt program is a structured, reusable prompt pattern designed to guide an LLM's reasoning process—similar to how heuristics guide human thinking.

### From Ad-hoc Prompts to Programmatic Patterns

Let's compare an ad-hoc prompt with a simple prompt program (reasoning tool calls):

```
┌───────────────────────────────────────────────────────────────┐
│ AD-HOC PROMPT                                                 │
├───────────────────────────────────────────────────────────────┤
│ "Summarize this article about climate change in 3 paragraphs. │
│  Make it easy to understand."                                 │
└───────────────────────────────────────────────────────────────┘

┌───────────────────────────────────────────────────────────────┐
│ PROMPT PROGRAM                                                │
├───────────────────────────────────────────────────────────────┤
│ program Summarize(text, paragraphs=3, complexity="simple") {  │
│   // Define the task                                          │
│   task = `Summarize the following text in ${paragraphs}       │
│           paragraphs. Use ${complexity} language.`;           │
│                                                               │
│   // Define the process                                       │
│   process = ```                                               │
│     1. Identify the main topic and key points                 │
│     2. Organize points by importance                          │
│     3. Create a coherent summary with:                        │
│        - First paragraph: Main topic and context              │
│        - Middle paragraph(s): Key supporting details          │
│        - Final paragraph: Conclusions or implications         │
│   ```;                                                        │
│                                                               │
│   // Define the output format                                 │
│   format = "A ${paragraphs}-paragraph summary using           │
│             ${complexity} language.";                         │
│                                                               │
│   // Construct the complete prompt                            │
│   return `${task}\n\nProcess:\n${process}\n\n                │
│           Format:\n${format}\n\nText to summarize:\n${text}`; │
│ }                                                             │
└───────────────────────────────────────────────────────────────┘
```

The prompt program approach offers several advantages:
1. **Reusability**: The same pattern can be applied to different texts
2. **Parameterization**: Easily customize length, complexity, etc.
3. **Transparency**: Clear structure makes the prompt's intent explicit
4. **Consistency**: Produces more predictable results across runs

### Simple Prompt Program Template

Here's a basic template for creating your own prompt programs:

```
program [Name]([parameters]) {
  // Define the task
  task = `[Clear instruction using parameters]`;
  
  // Define the process
  process = ```
    1. [First step]
    2. [Second step]
    3. [Additional steps as needed]
  ```;
  
  // Define the output format
  format = "[Expected response structure]";
  
  // Construct the complete prompt
  return `${task}\n\nProcess:\n${process}\n\nFormat:\n${format}\n\n[Input]`;
}
```

In practice, this template can be implemented in various ways:
- As pseudocode in your documentation
- As actual JavaScript/Python functions that generate prompts
- As YAML templates with variable substitution
- As JSON schemas for standardized prompt construction

## Prompt Template (Reasoning Tool Calls)

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

## Context Schemas: Structured Information Patterns

Just as human minds use schemas to organize knowledge, we can create context schemas for LLMs—standardized ways of structuring information to improve model understanding.

### Basic Schema Structure

```
┌───────────────────────────────────────────────────────────────┐
│ CONTEXT SCHEMA                                                │
├───────────────────────────────────────────────────────────────┤
│ {                                                             │
│   "$schema": "context-engineering/schemas/v1.json",           │
│   "title": "Analysis Request Schema",                         │
│   "description": "Standard format for requesting analysis",   │
│   "type": "object",                                           │
│   "properties": {                                             │
│     "task": {                                                 │
│       "type": "string",                                       │
│       "description": "The analysis task to perform"           │
│     },                                                        │
│     "context": {                                              │
│       "type": "object",                                       │
│       "properties": {                                         │
│         "background": { "type": "string" },                   │
│         "constraints": { "type": "array" },                   │
│         "examples": { "type": "array" }                       │
│       }                                                       │
│     },                                                        │
│     "data": {                                                 │
│       "type": "string",                                       │
│       "description": "The information to analyze"             │
│     },                                                        │
│     "output_format": {                                        │
│       "type": "string",                                       │
│       "enum": ["bullet_points", "paragraphs", "table"]        │
│     }                                                         │
│   },                                                          │
│   "required": ["task", "data"]                                │
│ }                                                             │
└───────────────────────────────────────────────────────────────┘
```

### From Schema to Prompt

Schemas can be translated into actual prompts by filling in the structured template:

```
# Analysis Request

## Task
Identify the main themes and supporting evidence in the provided text.

## Context
### Background
This is a speech given at a climate conference in 2023.

### Constraints
- Focus on scientific claims
- Ignore political statements
- Maintain neutrality

### Examples
- Theme: Rising Sea Levels
  Evidence: "Measurements show a 3.4mm annual rise since 2010"

## Data
[The full text of the speech would go here]

## Output Format
bullet_points
```

This structured approach helps the model understand exactly what information is being provided and what is expected in return.

## Recursive Prompting: Self-Referential Improvement

Recursive prompting is similar to cognitive priming—it establishes patterns that influence subsequent model behavior. The key insight is having the model reflect on and improve its own outputs.

### Basic Recursive Pattern

```
┌───────────────────────────────────────────────────────────────┐
│ RECURSIVE PROMPTING FLOW                                      │
│                                                               │
│  ┌─────────────┐      ┌─────────────┐      ┌─────────────┐    │
│  │             │      │             │      │             │    │
│  │  Initial    │─────►│  Self-      │─────►│  Improved   │    │
│  │  Response   │      │  Reflection │      │  Response   │    │
│  │             │      │             │      │             │    │
│  └─────────────┘      └─────────────┘      └─────────────┘    │
│        ▲                                          │           │
│        └──────────────────────────────────────────┘           │
│                                                               │
└───────────────────────────────────────────────────────────────┘
```

### Simple Implementation

```python
def recursive_prompt(question, model, iterations=2):
    """Apply recursive prompting to improve responses."""
    
    # Initial response
    response = model.generate(f"Question: {question}\nAnswer:")
    
    for i in range(iterations):
        # Self-reflection prompt
        reflection_prompt = f"""
        Question: {question}
        
        Your previous answer: 
        {response}
        
        Please reflect on your answer:
        1. What information might be missing?
        2. Are there any assumptions that should be questioned?
        3. How could the explanation be clearer or more accurate?
        
        Now, provide an improved answer:
        """
        
        # Generate improved response
        response = model.generate(reflection_prompt)
    
    return response
```

This simple recursive pattern can dramatically improve response quality by encouraging the model to critique and refine its own thinking.

## Putting It All Together: Cognitive Architecture

These cognitive tools can be combined into a complete architecture that mirrors human thinking processes:

```
┌───────────────────────────────────────────────────────────────────────────┐
│                      COGNITIVE ARCHITECTURE                               │
│                                                                           │
│  ┌─────────────────┐                                                      │
│  │                 │                                                      │
│  │  Input Parser   │  Understands user intent using schema recognition    │
│  │                 │                                                      │
│  └─────────────────┘                                                      │
│         │                                                                 │
│         ▼                                                                 │
│  ┌─────────────────┐                                                      │
│  │                 │                                                      │
│  │  Prompt Program │  Selects and applies appropriate reasoning pattern   │
│  │  Selector       │                                                      │
│  │                 │                                                      │
│  └─────────────────┘                                                      │
│         │                                                                 │
│         ▼                                                                 │
│  ┌─────────────────┐                                                      │
│  │                 │                                                      │
│  │  Working Memory │  Maintains state and context across steps            │
│  │                 │                                                      │
│  └─────────────────┘                                                      │
│         │                                                                 │
│         ▼                                                                 │
│  ┌─────────────────┐                                                      │
│  │                 │                                                      │
│  │  Recursive      │  Applies self-improvement through reflection         │
│  │  Processor      │                                                      │
│  │                 │                                                      │
│  └─────────────────┘                                                      │
│         │                                                                 │
│         ▼                                                                 │
│  ┌─────────────────┐                                                      │
│  │                 │                                                      │
│  │  Output         │  Formats final response according to schema          │
│  │  Formatter      │                                                      │
│  │                 │                                                      │
│  └─────────────────┘                                                      │
│                                                                           │
└───────────────────────────────────────────────────────────────────────────┘
```

This architecture can be implemented as a complete system using the tools and patterns we've discussed.

## Key Takeaways

1. **Prompt Programs** structure reasoning like human heuristics
2. **Context Schemas** organize information like mental knowledge structures
3. **Recursive Prompting** creates self-improvement loops similar to cognitive reflection
4. **Cognitive Architecture** combines these tools into complete systems

These cognitive extensions to our context engineering framework allow us to create more sophisticated, yet understandable, approaches to working with LLMs.

## Exercises for Practice

1. Convert one of your frequently used prompts into a prompt program
2. Create a simple schema for a common task you perform with LLMs
3. Implement basic recursive prompting to improve response quality
4. Combine these approaches into a mini cognitive architecture

## Next Steps

In the next sections, we'll explore practical implementations of these cognitive tools:
- Jupyter notebooks demonstrating prompt programs in action
- Templates for creating your own schemas
- Examples of complete cognitive architectures

[Continue to Next Section →](06_advanced_applications.md)

---

## Deeper Dive: From Our Research to Your Applications

The cognitive tools described above are simplified representations of more advanced research concepts. For those interested in exploring further:

- **Prompt Programs** are practical implementations of what researchers call "programmatic prompting" or "structured prompting frameworks"
- **Context Schemas** represent a simplified version of knowledge representation systems and ontological frameworks
- **Recursive Prompting** is related to self-reflection, metacognition, and recursive self-improvement in AI systems

These simplified frameworks make advanced concepts accessible while preserving their practical utility.
