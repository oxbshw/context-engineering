# Cognitive Tools for Context Engineering

> "Give me a lever long enough and a fulcrum on which to place it, and I shall move the world." — Archimedes

## What Are Cognitive Tools?
> "Providing our “cognitive tools” to GPT-4.1
increases its pass@1 performance on AIME2024 from 26.7% to 43.3%, bringing it very close to the performance of o1-preview." — [IBM June 2025](https://www.arxiv.org/pdf/2506.12115)

<div align="center">
    
![image](https://github.com/user-attachments/assets/a6402827-8bc0-40b5-93d8-46a07154fa4e)

"The tool breaks down the problem by identifying the main concepts at hand, extracting relevant information in the question, and highlighting meaningful properties, theorems, and techniques that might be helpful in solving the problem." — [Eliciting Reasoning in Language Models with Cognitive Tools — IBM June 2025](https://www.arxiv.org/pdf/2506.12115)


</div>

Cognitive tools are structured prompt patterns that guide language models through specific reasoning operations. Like mental tools that humans use to solve problems (analogies, mental models, heuristics), these tools provide models with scaffolding for complex reasoning tasks.

```
┌──────────────────────────────────────────────────────────────┐
│                                                              │
│  CONTEXT ENGINEERING PROGRESSION                             │
│                                                              │
│  Atoms       → Molecules   → Cells       → Organs      → Cognitive Tools  │
│  (Prompts)     (Few-shot)    (Memory)      (Multi-agent)  (Reasoning Patterns) │
│                                                              │
└──────────────────────────────────────────────────────────────┘
```

## Structure
```
cognitive-tools/
├── README.md                  # Overview and quick-start guide
├── cognitive-templates/       # Reusable templates for different reasoning patterns
│   ├── understanding.md       # Templates for comprehension operations
│   ├── reasoning.md           # Templates for analytical operations
│   ├── verification.md        # Templates for checking and validation
│   └── composition.md         # Templates for combining multiple tools
│
├── cognitive-programs/        # Structured prompt programs with code-like patterns
│   ├── basic-programs.md      # Fundamental program structures (conditionals, loops)
│   ├── advanced-programs.md   # Complex program architectures (meta-programming)
│   ├── program-library.py     # Python implementation of common prompt programs
│   └── program-examples.ipynb # Interactive examples showing programs in action
│
├── cognitive-schemas/         # Structured knowledge representation formats
│   ├── user-schemas.md        # Schemas for representing user information
│   ├── domain-schemas.md      # Schemas for different knowledge domains
│   ├── task-schemas.md        # Schemas for different reasoning tasks
│   └── schema-library.yaml    # YAML library of reusable schemas
│
├── cognitive-architectures/   # Complete reasoning systems combining multiple tools
│   ├── solver-architecture.md # Architecture for problem-solving applications
│   ├── tutor-architecture.md  # Architecture for educational applications
│   ├── research-architecture.md # Architecture for information synthesis
│   └── architecture-examples.py # Implementation examples of complete architectures
│
└── integration/               # Guides for integrating with other components
    ├── with-rag.md            # Combining cognitive tools with retrieval
    ├── with-memory.md         # Integrating with memory systems
    ├── with-agents.md         # Using in multi-agent architectures
    └── evaluation-metrics.md  # Measuring cognitive tool effectiveness
```
## Why Cognitive Tools Matter

Research has shown that structuring reasoning with cognitive tools can dramatically improve model performance:

- **Performance**: Up to 16.6% improvement on mathematical reasoning benchmarks
- **Reliability**: Significant reduction in reasoning errors and hallucinations
- **Efficiency**: Better results with fewer total tokens
- **Flexibility**: Applicable across domains from mathematics to creative writing

## Quick Start

To use a cognitive tool, choose a template from `cognitive-templates/` that matches your task:

```python
# Example: Using the "understand_question" cognitive tool
from cognitive_tools.templates import understand_question

problem = "If a train travels at 60 mph for 2.5 hours, how far does it go?"
understanding = llm.generate(understand_question(problem))
print(understanding)
```

For more complex reasoning, use structured prompt programs from `cognitive-programs/`:

```python
# Example: Using a multi-step reasoning program
from cognitive_tools.programs import solve_math_problem

problem = "If a train travels at 60 mph for 2.5 hours, how far does it go?"
solution = solve_math_problem(problem, llm=my_llm_interface)
print(solution.steps)  # View step-by-step reasoning
print(solution.answer)  # View final answer
```

## Directory Structure

- `cognitive-templates/`: Reusable templates for different reasoning operations
- `cognitive-programs/`: Structured prompt programs with code-like patterns
- `cognitive-schemas/`: Knowledge representation formats for different domains
- `cognitive-architectures/`: Complete reasoning systems combining multiple tools
- `integration/`: Guides for integrating with other components (RAG, memory, etc.)

## Learning Path

1. **Start with templates**: Learn the basic cognitive operations
2. **Explore programs**: See how operations can be combined into reasoning flows
3. **Study schemas**: Understand how to structure knowledge effectively
4. **Master architectures**: Build complete reasoning systems
5. **Integrate components**: Combine with RAG, memory, and other context engineering components

## Measuring Effectiveness

Always measure the impact of cognitive tools on your specific tasks:

```python
# Example: Measuring performance improvement
from cognitive_tools.evaluation import measure_reasoning_quality

baseline_score = measure_reasoning_quality(problem, baseline_prompt)
tool_score = measure_reasoning_quality(problem, cognitive_tool_prompt)

improvement = (tool_score / baseline_score - 1) * 100
print(f"Cognitive tool improved performance by {improvement:.1f}%")
```

## Research Foundation

These tools are based on research from:

- Brown et al. (2025): "Eliciting Reasoning in Language Models with Cognitive Tools"
- Wei et al. (2023): "Chain-of-Thought Prompting Elicits Reasoning in Large Language Models"
- Huang et al. (2022): "Inner Monologue: Embodying Knowledge and Reasoning in Language Models"

## Contributing

Have a new cognitive tool pattern that works well? See [CONTRIBUTING.md](../../.github/CONTRIBUTING.md) for guidelines on submitting your templates, programs, or architectures.

## Next Steps

- See [understanding.md](./cognitive-templates/understanding.md) for basic comprehension tools
- Try [basic-programs.md](./cognitive-programs/basic-programs.md) for fundamental program structures
- Explore [solver-architecture.md](./cognitive-architectures/solver-architecture.md) for a complete problem-solving system
