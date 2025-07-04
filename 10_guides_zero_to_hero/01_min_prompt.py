# Minimal Prompt Exploration: Fundamentals of Context Engineering

This notebook introduces the core principles of context engineering by exploring minimal, atomic prompts and their direct impact on LLM output and behavior.

Key concepts covered:
1. Constructing atomic prompts for maximum clarity and control
2. Measuring effectiveness through token count and model response quality
3. Iterative prompt modification for rapid feedback cycles
4. Observing context drift and minimal prompt boundaries
5. Foundations for scaling from atomic prompts to protocolized shells

## Experiment 1: The Atomic Prompt

Let's start with the most basic unit: a single instruction.

```python
# Initialize our LLM interface
llm = SimpleLLM()

atomic_prompt = "Write a short poem about programming."
tokens = llm.count_tokens(atomic_prompt)

print(f"\nAtomic Prompt: '{atomic_prompt}'")
print(f"Token Count: {tokens}")
print("\nGenerating response...")
response = llm.generate(atomic_prompt)
print(f"\nResponse:\n{response}")
```

## Experiment 2: Adding Constraints

Now let's add constraints to our atomic prompt and observe the difference.

```python
prompts = [
    "Write a short poem about programming.",  # Original
    "Write a short poem about programming in 4 lines.",  # Added length constraint
    "Write a short haiku about programming using only simple words."  # Format and vocabulary constraints
]

results = []
for i, prompt in enumerate(prompts):
    tokens = llm.count_tokens(prompt)
    print(f"\nPrompt {i+1}: '{prompt}'")
    print(f"Token Count: {tokens}")
    
    start_time = time.time()
    response = llm.generate(prompt)
    end_time = time.time()
    
    results.append({
        "prompt": prompt,
        "tokens": tokens,
        "response": response,
        "latency": end_time - start_time
    })
    
    print(f"Latency: {results[-1]['latency']:.4f} seconds")
    print(f"Response:\n{response}")
```

## Experiment 3: Measuring the ROI Curve

Let's explore the relationship between prompt complexity and output quality.

```python
# In a real notebook, you would define subjective quality scores for each response
# For this demo, we'll use placeholder values
quality_scores = [3, 6, 8]  # Placeholder subjective scores on a scale of 1-10

# Plot tokens vs. quality
plt.figure(figsize=(10, 6))
tokens_list = [r["tokens"] for r in results]
plt.plot(tokens_list, quality_scores, marker='o', linestyle='-', color='blue')
plt.xlabel('Tokens in Prompt')
plt.ylabel('Output Quality (1-10)')
plt.title('Token-Quality ROI Curve')
plt.grid(True)

# Add annotations
for i, (x, y) in enumerate(zip(tokens_list, quality_scores)):
    plt.annotate(f"Prompt {i+1}", (x, y), textcoords="offset points", 
                 xytext=(0, 10), ha='center')

print("[A plot would display here in a Jupyter environment]")
```

## Experiment 4: Minimal Context Enhancement

Now we'll add minimal context to improve output quality while keeping token count low.

```python
enhanced_prompt = """Task: Write a haiku about programming.

A haiku is a three-line poem with 5, 7, and 5 syllables per line.
Focus on the feeling of solving a difficult bug."""

tokens = llm.count_tokens(enhanced_prompt)
print(f"\nEnhanced Prompt:\n'{enhanced_prompt}'")
print(f"Token Count: {tokens}")

response = llm.generate(enhanced_prompt)
print(f"\nResponse:\n{response}")
```

## Experiment 5: Measuring Consistency

Let's test how consistent the outputs are with minimal vs. enhanced prompts.

```python
def measure_consistency(prompt: str, n_samples: int = 3) -> Dict[str, Any]:
    """Generate multiple responses and measure consistency metrics."""
    responses = []
    total_tokens = 0
    
    for _ in range(n_samples):
        response = llm.generate(prompt)
        responses.append(response)
        total_tokens += llm.count_tokens(prompt)
    
    # In a real notebook, you would implement proper consistency metrics
    # such as semantic similarity between responses
    consistency_score = 0.5  # Placeholder value
    
    return {
        "prompt": prompt,
        "responses": responses,
        "total_tokens": total_tokens,
        "consistency_score": consistency_score
    }

basic_results = measure_consistency(prompts[0])
enhanced_results = measure_consistency(enhanced_prompt)

print(f"\nBasic Prompt Consistency Score: {basic_results['consistency_score']}")
print(f"Enhanced Prompt Consistency Score: {enhanced_results['consistency_score']}")
```

## Conclusion

Key insights from our experiments:
1. Even small additions to prompts can significantly impact output quality
2. There's an ROI curve where token count and quality find an optimal balance
3. Adding minimal but strategic context improves consistency
4. The best prompts are clear, concise, and provide just enough context

## Next Steps

1. Try these experiments with a real LLM API
2. Implement proper consistency and quality metrics
3. Explore the concept of 'molecules' - combining multiple instructions
4. Experiment with few-shot examples in the context window

## Exercise for the Reader

1. Connect this notebook to a real LLM API (OpenAI, Anthropic, etc.)
2. Test the same prompts with different model sizes
3. Create your own token-quality curve for a task you care about
4. Find the "minimum viable context" for your specific use case

See 02_expand_context.ipynb for more advanced context engineering techniques!
