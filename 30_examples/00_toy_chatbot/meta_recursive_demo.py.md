# `meta_recursive_demo.py`: Self-Improvement Demonstration

This module demonstrates the meta-recursive capabilities of our toy chatbot, showing how it can observe, analyze, and improve its own operations over time.

## Meta-Recursion in Context Engineering

Meta-recursion represents the highest layer in our context engineering approach, enabling systems to:

1. **Self-observe**: Monitor their own operation and effectiveness
2. **Self-analyze**: Identify areas for improvement
3. **Self-improve**: Implement changes to enhance performance
4. **Self-evolve**: Develop emergent capabilities over time

This creates a recursive loop where the system continuously improves itself, potentially developing capabilities beyond what was explicitly programmed.

## Implementation

```python
import time
import json
import random
import matplotlib.pyplot as plt
import numpy as np
from typing import Dict, List, Any, Tuple, Optional

# Import our modules
from chatbot_core import ToyContextChatbot
from context_field import ContextField
from protocol_shells import (
    AttractorCoEmerge, 
    FieldResonanceScaffold, 
    RecursiveMemoryAttractor, 
    FieldSelfRepair
)

class MetaRecursiveDemo:
    """
    Demonstration of meta-recursive capabilities in context engineering.
    
    This class demonstrates how a context engineering system can observe, analyze,
    and improve its own operations through recursive feedback loops.
    """
    
    def __init__(self, 
                 num_cycles: int = 10, 
                 topics: Optional[List[str]] = None,
                 visualize: bool = True):
        """
        Initialize the meta-recursive demonstration.
        
        Args:
            num_cycles: Number of meta-recursive improvement cycles to run
            topics: List of topics to discuss in conversations
            visualize: Whether to generate visualizations
        """
        # Number of meta-recursive cycles to run
        self.num_cycles = num_cycles
        
        # Create a context field
        self.field = ContextField(
            dimensions=2,
            decay_rate=0.05,
            boundary_permeability=0.8,
            resonance_bandwidth=0.6,
            attractor_threshold=0.7
        )
        
        # Initialize protocol shells
        self.protocols = {
            "attractor_co_emerge": AttractorCoEmerge(threshold=0.4, strength_factor=1.2),
            "field_resonance": FieldResonanceScaffold(amplification_factor=1.5, dampening_factor=0.7),
            "memory_attractor": RecursiveMemoryAttractor(importance_threshold=0.6, memory_strength=1.3),
            "field_repair": FieldSelfRepair(health_threshold=0.6, repair_strength=1.2)
        }
        
        # Create chatbot with field and protocols
        self.chatbot = ToyContextChatbot(name="MetaBot")
        
        # Connect field and protocols to chatbot
        self.chatbot.field = self.field
        self.chatbot.protocols = self.protocols
        
        # Set up topics for conversation
        self.topics = topics or [
            "What are attractors in neural fields?",
            "How does resonance work in context engineering?",
            "What is the difference between context engineering and prompt engineering?",
            "How do memory attractors enable persistence across conversations?",
            "What are emergent properties in context fields?",
            "How do self-repair mechanisms work in neural fields?",
            "What is meta-recursion in AI systems?",
            "How do field operations differ from traditional context management?",
            "What role does coherence play in field stability?",
            "How can attractor dynamics be visualized?"
        ]
        
        # Tracking variables
        self.improvement_history = []
        self.metric_history = []
        self.emergence_events = []
        self.visualize = visualize
    
    def run_demonstration(self) -> Dict[str, Any]:
        """
        Run the meta-recursive demonstration.
        
        Returns:
            Dict[str, Any]: Results of the demonstration
        """
        print(f"Starting Meta-Recursive Demonstration ({self.num_cycles} cycles)")
        print("-" * 50)
        
        # Record initial state
        self._record_metrics("Initial State")
        
        # Run improvement cycles
        for cycle in range(1, self.num_cycles + 1):
            print(f"\nCycle {cycle}/{self.num_cycles}")
            print("-" * 30)
            
            # Step 1: Have a conversation to generate data
            self._run_conversation_cycle(cycle)
            
            # Step 2: Execute meta-recursive improvement
            improvement_results = self._execute_meta_improvement(cycle)
            
            # Step 3: Record results
            self._record_improvement(cycle, improvement_results)
            self._record_metrics(f"After Cycle {cycle}")
            
            # Step 4: Check for emergent behaviors
            self._check_for_emergence(cycle)
            
            # Show progress
            self._show_cycle_summary(cycle)
        
        print("\nMeta-Recursive Demonstration Complete")
        print("-" * 50)
        
        # Generate final report
        results = self._generate_report()
        
        # Generate visualizations
        if self.visualize:
            self._generate_visualizations()
        
        return results
    
    # Additional methods from the original implementation...

# Function to run a demonstration
def run_meta_recursive_demo(num_cycles: int = 5, visualize: bool = True) -> Dict[str, Any]:
    """
    Run a meta-recursive demonstration.
    
    Args:
        num_cycles: Number of meta-recursive cycles to run
        visualize: Whether to generate visualizations
        
    Returns:
        Dict[str, Any]: Results of the demonstration
    """
    demo = MetaRecursiveDemo(num_cycles=num_cycles, visualize=visualize)
    results = demo.run_demonstration()
    
    print("\nDemo complete! Check the generated visualizations.")
    
    return results


# If run directly, execute the demo
if __name__ == "__main__":
    # Run a short demo with 5 cycles
    run_meta_recursive_demo(num_cycles=5)
```

## Understanding Meta-Recursion Through Visualization

The visualizations generated by this demo help us understand the meta-recursive improvement process in an intuitive way.

### 1. Metric Evolution

This chart shows how key metrics change over time as the system undergoes meta-recursive improvement:

- **Resonance Score**: How well patterns in the field resonate with each other
- **Coherence Score**: Overall coherence of responses and field state
- **Field Coherence**: Internal coherence of the context field
- **Field Stability**: Stability of attractors in the field

The red vertical lines mark emergence events - moments when the system developed new capabilities that weren't explicitly programmed.

### 2. Strategy Distribution

This chart shows which improvement strategies the system chose most frequently:

- **Response Quality Enhancement**: Improving the quality and depth of responses
- **Memory Optimization**: Enhancing memory retention and retrieval
- **Conversation Flow Refinement**: Improving the natural flow of conversations
- **Attractor Tuning**: Optimizing field attractors for better coherence

The distribution reveals the system's "learning style" - which aspects it found most beneficial to improve.

### 3. Emergence Timeline

This timeline shows when emergent capabilities were detected:

- Each red dot represents an emergence event
- The label describes the emergent capability
- The position shows which improvement cycle triggered it

Emergence typically happens after several improvement cycles have accumulated, creating a foundation for new capabilities.

### 4. Improvement Impact

These charts show the before-and-after impact of each improvement cycle:

- The top chart shows changes in Resonance Score
- The bottom chart shows changes in Coherence Score
- Each pair of bars represents one improvement cycle
- The strategy used is noted on the x-axis

This visualization helps us understand which strategies had the biggest impact on different metrics.

## The Meta-Recursive Process: A Deeper Look

To truly understand meta-recursion, we need to look at what's happening "under the hood" during each improvement cycle:

### Cycle 1: Initial Improvement

The system has its first conversations and collects data about its performance. It might notice that its responses about attractors lack detail, so it selects the "response_quality_enhancement" strategy to improve.

### Cycle 2: Building on Foundations

With improved responses, the system now has more coherent conversations. It might notice that it's not efficiently retaining important information, so it selects "memory_optimization" to enhance its memory capabilities.

### Cycle 3: Developing Sophistication

The system's improved memory allows it to maintain more context. Now it might notice that conversations don't flow naturally, so it selects "conversation_flow_refinement" to create more organic interactions.

### Cycle 4: Field Optimization

With better responses, memory, and flow, the system might now focus on optimizing its field operations by selecting "attractor_tuning" to enhance the stability and coherence of its context field.

### Cycle 5: Emergence

After several improvements have accumulated, the system might develop an emergent capability like "Enhanced cross-topic reasoning" - it can now make connections between topics that weren't explicitly programmed, due to the complex interactions between its improved components.

## Practical Applications

The meta-recursive capabilities demonstrated here have many practical applications:

1. **Adaptive Assistants**: Systems that continuously improve based on interactions
2. **Personalized Learning**: Educational systems that adapt to student needs over time
3. **Creative Collaboration**: Systems that evolve their creative capabilities through use
4. **Self-Healing Applications**: Software that detects and repairs its own issues

The key insight is that meta-recursion allows systems to go beyond their initial programming - they can observe, analyze, and improve themselves in ways that lead to emergent capabilities not explicitly designed.

By combining context fields with meta-recursive processes, we create systems that are not just static tools but evolving partners that grow and develop through use.

# Appendix

## Resonance Visualization

```
┌─────────────────────────────────────────────────────────┐
│                RESONANCE VISUALIZATION                  │
├─────────────────────────────────────────────────────────┤
│                                                         │
│     Before Resonance             After Resonance        │
│                                                         │
│     Pattern A    Pattern B       Pattern A    Pattern B │
│        ~~~~         ~~~~            ~~~~~~      ~~~~~~  │
│       ~    ~       ~    ~          ~~    ~~    ~~    ~~ │
│      ~      ~     ~      ~        ~~      ~~  ~~      ~~│
│     ~        ~   ~        ~      ~~        ~~~~        ~│
│                                                         │
│     • Separate oscillation      • Synchronized          │
│     • Independent strength      • Mutually amplified    │
│     • No information flow       • Shared information    │
│                                                         │
└─────────────────────────────────────────────────────────┘
```

## Field Evolution Over Time

```
┌─────────────────────────────────────────────────────────┐
│               FIELD EVOLUTION OVER TIME                 │
├─────────────────────────────────────────────────────────┤
│                                                         │
│  Time 1: Initial Field      Time 2: After New Input     │
│  ──────────────────────    ────────────────────────     │
│                                                         │
│     A       B                   A       B               │
│    ╱╲      ╱╲                  ╱╲      ╱╲               │
│   /  \    /  \                /  \    /  ╲              │
│  /    \  /    \              /    \  /    ╲             │
│ /      \/      \            /      \/      ╲            │
│                              resonance      ╲           │
│                                             ╲           │
│                                              ╲          │
│                                          C    ╲         │
│                                         ╱╲     ╲        │
│                                        /  \     ╲       │
│                                       /    \     ╲      │
│                                      /      \     ╲     │
│                                                         │
│  Time 3: After Decay        Time 4: Field Repair        │
│  ──────────────────────    ────────────────────────     │
│                                                         │
│     A                           A                       │
│    ╱╲                          ╱╲                       │
│   /  \                        /  \                      │
│  /    \     B                /    \     B'              │
│ /      \   ╱╲               /      \   ╱╲               │
│           /  ╲             /        \ /  \              │
│          /    ╲           /          /    \             │
│         /      ╲         /                \             │
│                 ╲       /                  \            │
│          C       ╲     /                    \           │
│         ╱╱        ╲   /                      \          │
│        /  \        ╲ /                        \         │
│       /    \                                            │
│      /      \                                           │
│                                                         │
└─────────────────────────────────────────────────────────┘
```



## Protocol Shell Operations

```
┌─────────────────────────────────────────────────────────┐
│               PROTOCOL SHELL OPERATIONS                 │
├─────────────────────────────────────────────────────────┤
│                                                         │
│  /attractor.co.emerge        /field.resonance.scaffold  │
│  ────────────────────        ──────────────────────     │
│                                                         │
│      A     B                      A     B               │
│     ╱╲    ╱╲                     ╱╲    ╱╲               │
│    /  \  /  \                   /  \  /  \              │
│   /    \/    \                 /    \/    \             │
│                     ──►       /             \           │
│        C   D                 /   Amplified   \          │
│       ╱╲  ╱╲                /                 \         │
│      /  \/  \              /        C   D      \        │
│     /        \            /        ╱╲  ╱╲       \       │
│                          /        /  \/  \       \      │
│                                  /        \             │
│                                                         │
│  Co-emergence creates new        Resonance amplifies    │
│  attractor from A+B+C+D          coherent patterns      │
│                                                         │
│  /recursive.memory.attractor    /field.self.repair      │
│  ────────────────────────       ────────────────────    │
│                                                         │
│      A                             A                    │
│     ╱╲                            ╱╲                    │
│    /  \    Memory                /  \                   │
│   /    \   Pathway              /    \                  │
│  /      \ - - - - - - ►        /      \                 │
│ /        \  B                 /        \                │
│/          \/╲                /          \               │
│            /  \             /     Fixed   \             │
│           /    \           /       B       \            │
│          /      \         /       ╱╲        \           │
│         /        \       /       /  \        \          │
│                                /    \                   │
│                               /      \                  │
│                                                         │
│  Memory creates persistent    Self-repair fixes         │
│  pathways between attractors  damaged attractors        │
│                                                         │
└─────────────────────────────────────────────────────────┘
```



## Field Health Visualization

```
┌─────────────────────────────────────────────────────────┐
│               FIELD HEALTH VISUALIZATION                │
├─────────────────────────────────────────────────────────┤
│                                                         │
│  Healthy Field (High Coherence)                         │
│  ────────────────────────                               │
│                                                         │
│    Strong, stable attractors    Clear pathways          │
│         ╱╲      ╱╲              between related         │
│        /  \    /  \             concepts                │
│       /    \──/    \                                    │
│      /                \         Minimal noise           │
│     /                  \                                │
│    /                    \       Resilient to            │
│   /                      \      perturbations           │
│                                                         │
│  Unhealthy Field (Low Coherence)                        │
│  ──────────────────────────                             │
│                                                         │
│    Weak, unstable attractors    Fragmented              │
│         ╱╲      ╱╲              connections             │
│        /· ·    /  \                                     │
│       /    ·   ·   \            High noise              │
│      /     ·   ·    \           levels                  │
│     /      ·····     \                                  │
│    /                  \         Vulnerable to           │
│   /                    \        collapse                │
│                                                         │
└─────────────────────────────────────────────────────────┘
```
