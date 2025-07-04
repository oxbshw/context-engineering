# Context Expansion Techniques: From Prompts to Layered Context
=============================================================
This notebook presents hands-on strategies for evolving basic prompts into layered, information-rich contexts that enhance LLM performance. The focus is on practical context engineering: how to strategically add and structure context layers, and systematically measure the effects on both token usage and output quality.

Key concepts covered:
1. Transforming minimal prompts into expanded, context-rich structures
2. Principles of context layering and compositional prompt engineering
3. Quantitative measurement of token usage as context grows
4. Qualitative assessment of model output improvements
5. Iterative approaches to context refinement and optimization

Usage:
```python
# In Jupyter or Colab:
%run 02_context_expansion.py
# or
# Step through notebook cells, modifying context layers and observing effects
```

Notes:
- Each section is modular—experiment by editing and running different context layers
- Track how additional context alters both cost (token count) and performance (output quality)
- Use as a practical foundation for developing advanced context engineering protocols

---

## Setup and Prerequisites

```python
import os
import json
import time
import tiktoken  # OpenAI's tokenizer
import numpy as np
import matplotlib.pyplot as plt
from typing import Dict, List, Tuple, Any, Optional, Union

# Load environment variables
import dotenv
dotenv.load_dotenv()

# API client configuration
USE_OPENAI = True  # Set to False to use another provider

if USE_OPENAI:
    from openai import OpenAI
    client = OpenAI()
    MODEL = "gpt-3.5-turbo"  # Can be changed to gpt-4 or other models
else:
    # Add alternative API client setup here
    pass

# Token counter setup
tokenizer = tiktoken.encoding_for_model(MODEL) if USE_OPENAI else None

def count_tokens(text: str) -> int:
    """Count tokens in a string using the appropriate tokenizer."""
    if tokenizer:
        return len(tokenizer.encode(text))
    # Fallback for non-OpenAI models
    return len(text.split()) * 1.3  # Rough approximation

def measure_latency(func, *args, **kwargs) -> Tuple[Any, float]:
    """Measure execution time of a function."""
    start_time = time.time()
    result = func(*args, **kwargs)
    return result, time.time() - start_time
```

---

## 1. Understanding Context Expansion

```python
def calculate_metrics(prompt: str, response: str, latency: float) -> Dict[str, float]:
    """Calculate key metrics for a prompt-response pair."""
    prompt_tokens = count_tokens(prompt)
    response_tokens = count_tokens(response)
    
    token_efficiency = response_tokens / prompt_tokens if prompt_tokens > 0 else 0
    latency_per_1k = (latency / prompt_tokens) * 1000 if prompt_tokens > 0 else 0
    
    return {
        "prompt_tokens": prompt_tokens,
        "response_tokens": response_tokens,
        "token_efficiency": token_efficiency,
        "latency": latency,
        "latency_per_1k": latency_per_1k
    }

def generate_response(prompt: str) -> Tuple[str, float]:
    """Generate a response from the LLM and measure latency."""
    if USE_OPENAI:
        start_time = time.time()
        response = client.chat.completions.create(
            model=MODEL,
            messages=[{"role": "user", "content": prompt}],
            temperature=0.7,
            max_tokens=500
        )
        return response.choices[0].message.content, time.time() - start_time
    else:
        pass
```

---

## 2. Experiment: Context Expansion Techniques

```python
base_prompt = "Write a paragraph about climate change."

expanded_prompts = {
    "base": base_prompt,
    "with_role": """You are an environmental scientist. 
Write a paragraph about climate change.""",
    "with_examples": """Write a paragraph about climate change.

Example 1:
Climate change refers to long-term shifts in temperatures and weather patterns. Human activities have been the main driver of climate change since the 1800s.

Example 2:
Global climate change is evident in the increasing frequency of extreme weather events, rising sea levels, and shifting wildlife populations.""",
    "with_constraints": """Write a paragraph about climate change.
- Include at least one scientific fact
- Mention both causes and effects
- End with a call to action""",
    "with_audience": """Write a paragraph about climate change for high school students 
just beginning to learn about environmental science.""",
    "comprehensive": """You are an environmental scientist.

Write a paragraph about climate change for high school students just beginning to learn about environmental science.

Guidelines:
- Include at least one scientific fact
- Mention both causes and effects
- End with a call to action

Example tone:
"Ocean acidification occurs when seawater absorbs CO2 from the atmosphere, causing pH levels to drop. Since the Industrial Revolution, ocean pH has decreased by 0.1 units."
"""
}

results = {}
responses = {}

for name, prompt in expanded_prompts.items():
    print(f"Testing prompt: {name}")
    response, latency = generate_response(prompt)
    responses[name] = response
    results[name] = calculate_metrics(prompt, response, latency)
```

---

## 3. Visualizing and Analyzing Results

```python
prompt_types = list(results.keys())
prompt_tokens = [results[k]['prompt_tokens'] for k in prompt_types]
response_tokens = [results[k]['response_tokens'] for k in prompt_types]
latencies = [results[k]['latency'] for k in prompt_types]

fig, axes = plt.subplots(2, 2, figsize=(14, 10))

axes[0, 0].bar(prompt_types, prompt_tokens, label='Prompt Tokens', alpha=0.7, color='blue')
axes[0, 0].bar(prompt_types, response_tokens, bottom=prompt_tokens, label='Response Tokens', alpha=0.7, color='green')
axes[0, 0].set_title('Token Usage by Prompt Type')
axes[0, 0].legend()

axes[0, 1].bar(prompt_types, [results[k]['token_efficiency'] for k in prompt_types], color='purple', alpha=0.7)
axes[0, 1].set_title('Token Efficiency (Response/Prompt)')

axes[1, 0].bar(prompt_types, latencies, color='red', alpha=0.7)
axes[1, 0].set_title('Response Latency')

axes[1, 1].bar(prompt_types, [results[k]['latency_per_1k'] for k in prompt_types], color='orange', alpha=0.7)
axes[1, 1].set_title('Latency per 1k Tokens')

plt.tight_layout()
plt.show()
```

---

## 4. Qualitative Analysis

```python
for name, response in responses.items():
    print(f"\n=== Response for {name} prompt ===\n")
    print(response)
    print("\n" + "=" * 80 + "\n")
```

---

## 5. Context Expansion Patterns

```python
def create_expanded_context(
    base_prompt: str, 
    role: Optional[str] = None,
    examples: Optional[List[str]] = None,
    constraints: Optional[List[str]] = None,
    audience: Optional[str] = None,
    tone: Optional[str] = None,
    output_format: Optional[str] = None
) -> str:
    """Create an expanded context from a base prompt with optional components."""
    context_parts = []
    
    if role:
        context_parts.append(f"You are {role}.")
    
    context_parts.append(base_prompt)
    
    if audience:
        context_parts.append(f"Your response should be suitable for {audience}.")
    
    if tone:
        context_parts.append(f"Use a {tone} tone in your response.")
    
    if output_format:
        context_parts.append(f"Format your response as {output_format}.")
    
    if constraints:
        context_parts.append("Requirements:")
        for constraint in constraints:
            context_parts.append(f"- {constraint}")
    
    if examples:
        context_parts.append("Examples:")
        for i, example in enumerate(examples, 1):
            context_parts.append(f"Example {i}:\n{example}")
    
    return "\n\n".join(context_parts)
```

---

## 6. Advanced Context Expansion: Layer Optimization

```python
def test_layered_contexts(base_prompt: str, context_layers: Dict[str, str]) -> Dict[str, Dict]:
    """Test different combinations of context layers to find optimal configurations."""
    layer_results = {}
    
    # Test base prompt alone
    base_response, base_latency = generate_response(base_prompt)
    layer_results["base"] = calculate_metrics(base_prompt, base_response, base_latency)
    
    # Test each layer individually added to base
    for layer_name, layer_content in context_layers.items():
        combined_prompt = f"{base_prompt}\n\n{layer_content}"
        response, latency = generate_response(combined_prompt)
        layer_results[f"base+{layer_name}"] = calculate_metrics(combined_prompt, response, latency)
    
    # Test all layers combined
    all_layers = "\n\n".join(context_layers.values())
    full_prompt = f"{base_prompt}\n\n{all_layers}"
    full_response, full_latency = generate_response(full_prompt)
    layer_results["all_layers"] = calculate_metrics(full_prompt, full_response, full_latency)
    
    return layer_results
```

---

## 7. Context Compression Techniques

```python
def compress_context(context: str, technique: str = 'summarize') -> str:
    """Apply different compression techniques to reduce token usage while preserving meaning."""
    if technique == 'summarize':
        prompt = f"""Summarize the following context in a concise way that preserves all key information:
{context}"""
        compressed, _ = generate_response(prompt)
        return compressed
    
    elif technique == 'keywords':
        prompt = f"""Extract the most important keywords and phrases from this context:
{context}
Format your response as a comma-separated list."""
        keywords, _ = generate_response(prompt)
        return keywords
    
    elif technique == 'bullet':
        prompt = f"""Convert this context into a concise list of bullet points that
captures all essential information:
{context}"""
        bullets, _ = generate_response(prompt)
        return bullets
    
    else:
        return context
```

---

## 8. Context Pruning: Deleting What Doesn't Help

```python
def evaluate_response_quality(prompt: str, response: str, criteria: List[str]) -> float:
    """Use the LLM to evaluate the quality of a response based on specific criteria."""
    criteria_list = "\n".join([f"- {c}" for c in criteria])
    eval_prompt = f"""Rate the quality of the following response to a prompt. 
Prompt: {prompt}
Response: {response}
Evaluate based on these criteria:
{criteria_list}
Provide an overall score from 0.0 to 1.0."""
    
    evaluation, _ = generate_response(eval_prompt)
    # Extract quality score from evaluation
    return float(re.findall(r"(\d+\.\d+)", evaluation)[-1]) if re.findall(r"(\d+\.\d+)", evaluation) else 0.5
```

---

## 9. Context Expansion with Retrieval

```python
def retrieve_relevant_info(query: str, knowledge_base: List[Dict[str, str]]) -> List[str]:
    """Retrieve relevant information from a knowledge base based on a query."""
    query_terms = set(query.lower().split())
    relevant_info = []
    
    for item in knowledge_base:
        content = item['content'].lower()
        title = item['title'].lower()
        
        if any(term in content or term in title for term in query_terms):
            relevant_info.append(item['content'])
    
    return relevant_info[:3]  # Return top 3 matches

def create_rag_context(base_prompt: str, query: str, knowledge_base: List[Dict[str, str]]) -> str:
    """Create a retrieval-augmented context by combining a base prompt with relevant information."""
    relevant_info = retrieve_relevant_info(query, knowledge_base)
    
    if not relevant_info:
        return base_prompt
    
    context_block = "Relevant information:\n\n" + "\n\n".join(relevant_info)
    return f"{base_prompt}\n\n{context_block}"
```

---

## 10. Conclusion: Context Expansion Best Practices

Based on our experiments, here are the key best practices for effective context expansion:

1. Start minimal: Begin with the simplest prompt that might work
2. Measure impact: Track token usage, latency, and quality metrics
3. Layer strategically: Add context in distinct, modular layers
4. Compress when possible: Use summarization or bullet points
5. Prune ruthlessly: Remove context layers that don't improve quality
6. Use templates: Create reusable templates for different patterns
7. Consider retrieval: For large knowledge bases, use retrieval
8. Balance specificity vs. generality: Optimize for quality and efficiency

### Template for Context Expansion Decision-Making

```plaintext
1. Define core objective
   ↓
2. Create minimal prompt
   ↓
3. Measure baseline performance
   ↓
4. Identify potential context layers
   ↓
5. Test each layer individually
   ↓
6. Combine promising layers
   ↓
7. Measure impact on token usage, quality, and latency
   ↓
8. Prune unnecessary layers
   ↓
9. Compress remaining context
   ↓
10. Final optimization
```

The goal is to create the most effective context that optimizes for both quality and efficiency.

---

In the next notebook (`03_control_loops.ipynb`), we'll explore building sophisticated control flow mechanisms for multi-step LLM interactions.
```
