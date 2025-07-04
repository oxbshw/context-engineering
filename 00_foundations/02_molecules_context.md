# Molecules: Combining Prompts with Examples

> "The whole is greater than the sum of its parts." — Aristotle

## From Atoms to Molecules

In the previous section, we explored **atomic prompts** — single instructions that form the basic unit of LLM interaction. Now we'll combine these atoms into **molecules**: structured contexts that include examples and patterns for the model to follow.

```
MOLECULE = [INSTRUCTION] + [EXAMPLES] + [CONTEXT] + [NEW INPUT]
```

This molecular approach leverages a powerful capability of LLMs: **few-shot learning**.

## Few-Shot Learning: Teaching by Example

Few-shot learning provides examples of input-output behavior to help the model recognize and continue patterns.

```
Input: "Paris"
Output: "Paris is the capital of France."

Input: "Tokyo"
Output: "Tokyo is the capital of Japan."

Input: "Ottawa"
Output: ?
```

The model recognizes the pattern and completes it: "Ottawa is the capital of Canada."

## The Molecular Advantage: Measurable Improvements

Compare the atomic and molecular approaches to sentiment classification:

```
ATOMIC:
"Classify this review as positive or negative:
'The service was terrible and the food was cold.'"

MOLECULAR:
Classify the sentiment of reviews.

Review: 'The food was amazing!'
Sentiment: Positive

Review: 'Waited 30 minutes and the food was cold.'
Sentiment: Negative

Review: 'The service was terrible and the food was cold.'
Sentiment:
```

**Benefits of the molecular approach:**

* Higher accuracy (10–30% improvements across tasks)
* Greater output consistency
* Improved adherence to formatting
* Better handling of edge cases

## Designing Effective Molecular Templates

Common molecular prompt structures:

```
PREFIX-SUFFIX
<instruction>
Input: <example1>
Output: <result1>
Input: <new_input>
Output:

INPUT-OUTPUT PAIRS
<instruction>
Input: <example1>
Output: <result1>
Input: <example2>
Output: <result2>
Input: <new_input>
Output:

CHAIN-OF-THOUGHT
<instruction>
Input: <example1>
Thinking: <step-by-step>
Output: <result1>
Input: <new_input>
Thinking:
```

* **Prefix-Suffix**: Best for straightforward completions
* **Input-Output Pairs**: Ideal for structured outputs
* **Chain-of-Thought**: Best for complex reasoning

## The Science of Example Selection

Not all examples are equally effective. Choose examples that:

```
✓ Cover a variety of cases
✓ Include edge cases to clarify boundaries
✓ Progress from simple to complex
✓ Reflect frequent or recent inputs
✓ Include near misses to define boundaries clearly
```

## Measuring Molecular Efficiency

As more examples are added, accuracy improves—up to a point:

```
Accuracy
  ▲                     ● 4-shot
  │               ● 3-shot
  │         ● 2-shot
  │   ● 1-shot
  │ ● 0-shot
  └────────────────────────► Tokens Used
```

**Key insight:** Diminishing returns. More examples increase token count and cost, but the marginal gains shrink.

## Finding the Molecular Sweet Spot

Optimal example count varies by task type:

```
Task Type             | Recommended Examples
----------------------|---------------------
Classification        | 1–3 per class
Generation            | 2–5 diverse cases
Structured Extraction | 2–4 full-field examples
Reasoning             | 2–3 with chain-of-thought
Translation           | 3–5, increasing complexity
```

## Dynamic Molecule Construction

Advanced systems dynamically select examples based on the query:

```
User Query
   │
   ▼
Query Analysis ──▶ Retrieve Relevant Examples ──▶ Build Molecular Context ──▶ LLM
```

This process:

1. Analyzes the user input
2. Retrieves relevant examples from a database
3. Constructs a tailored molecular prompt
4. Feeds the optimized context to the model

## Putting It Into Practice: Python Example

```python
def create_molecular_context(instruction, examples, new_input,
                            format_type="input-output"):
    """
    Construct a molecular context from examples.

    Args:
        instruction (str): The task instruction
        examples (List[Dict]): Example input/output pairs
        new_input (str): The input to evaluate
        format_type (str): Template type (input-output, chain-of-thought)

    Returns:
        str: Complete molecular context
    """
    context = f"{instruction}\n\n"

    if format_type == "input-output":
        for ex in examples:
            context += f"Input: {ex['input']}\nOutput: {ex['output']}\n\n"
    elif format_type == "chain-of-thought":
        for ex in examples:
            context += f"Input: {ex['input']}\nThinking: {ex['thinking']}\nOutput: {ex['output']}\n\n"

    context += f"Input: {new_input}\nOutput:"
    return context
```

## Key Takeaways

1. Molecular contexts combine instructions and examples to boost performance.
2. Few-shot learning helps models identify patterns.
3. Template format affects clarity and reliability.
4. Thoughtful example selection is critical.
5. Diminishing returns mean balance matters.
6. Dynamic construction maximizes relevance.

## Exercises

1. Measure performance on a classification task using 0, 1, 3, and 5 examples.
2. Compare different template types for the same task.
3. Build a function to select examples dynamically by similarity.
4. Find the "minimum viable molecule" for a key workflow.

## Coming Next: Cells and Memory

In the next section, we'll explore **cells** — context structures that maintain memory and state across interactions.

[Continue to 03\_cells\_memory.md →](03_cells_memory.md)

---

## Deeper Dive: Prompt vs. Context Engineering

Prompt engineering focuses on crafting good instructions. Context engineering goes further:

```
CONTEXT ENGINEERING LAYERS

Model Behavior
▲
│ Training, fine-tuning, alignment
Instructions
▲
│ Prompts, constraints
Examples
▲
│ Few-shot learning
Retrieved Data
▲
│ RAG, tools, APIs
State & Memory
▲
│ Session history, persistent variables
```

Context engineering offers deeper control for creating robust, intelligent applications.
