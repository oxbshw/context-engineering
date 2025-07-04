# Context Field Management

This module implements the context field, a continuous semantic substrate for a toy chatbot. The context field represents a shift from discrete token-based contexts to a continuous semantic medium with attractors, resonance, and emergent properties.

## Conceptual Overview: From Tokens to Fields

Traditional context management treats information as discrete tokens or chunks. The field approach reimagines context as a continuous semantic landscape:

```
┌─────────────────────────────────────────────────────────┐
│              CONTEXT FIELD VISUALIZATION                │
├─────────────────────────────────────────────────────────┤
│                                                         │
│                        Z (Semantic Depth)               │
│                        ▲                                │
│                        │                                │
│                        │      Attractor B               │
│                        │      ╱╲                        │
│                        │     /  \                       │
│                        │    /    \                      │
│                        │   /      \        Attractor C  │
│                        │  /        \       ╱╲           │
│                        │ /          \     /  \          │
│  Attractor A           │/            \   /    \         │
│  ╱╲                    │              \ /      \        │
│ /  \                   │               /        \       │
│/    \                  │              /          \      │
│      \                 │             /            \     │
│       \                │            /              \    │
│        \               │           /                \   │
│         \              │          /                  \  │
│          \             │         /                    \ │
│           ╰─────────────────────┼──────────────────────┼─── X (Semantic Dimension 1)
│                                /                         │
│                               /                          │
│                              /                           │
│                             /                            │
│                            /                             │
│                           /                              │
│                          /                               │
│                         /                                │
│                        Y (Semantic Dimension 2)          │
│                                                         │
└─────────────────────────────────────────────────────────┘
```

### Key Field Concepts

1. **Attractors**: Stable semantic configurations representing coherent concepts.
2. **Resonance**: Mutual reinforcement between compatible patterns.
3. **Field Operations**: Actions like injection, decay, and attractor formation.
4. **Persistence**: Patterns remaining stable over time, forming semantic memory.
5. **Emergence**: New properties arising from field dynamics.

## Implementation

Here's the implementation of the context field for the toy chatbot:

```python
import time
import json
import uuid
import math
import random
import numpy as np
from typing import Dict, List, Any, Optional, Union, Tuple, Set

class ContextField:
    """
    A continuous semantic field with attractors, resonance, and persistence.
    This class serves as the substrate for protocol shell operations.
    """
    
    def __init__(
        self,
        dimensions: int = 2,
        decay_rate: float = 0.05,
        boundary_permeability: float = 0.8,
        resonance_bandwidth: float = 0.6,
        attractor_threshold: float = 0.7
    ):
        """
        Initialize the context field.
        
        Args:
            dimensions: Number of semantic dimensions
            decay_rate: Base rate of pattern decay
            boundary_permeability: How easily new information enters
            resonance_bandwidth: How broadly patterns resonate
            attractor_threshold: Threshold for attractor formation
        """
        self.dimensions = dimensions
        self.decay_rate = decay_rate
        self.boundary_permeability = boundary_permeability
        self.resonance_bandwidth = resonance_bandwidth
        self.attractor_threshold = attractor_threshold
        
        # Field components
        self.content = {}       # Semantic content in the field
        self.patterns = {}      # Detected patterns in the field
        self.attractors = {}    # Stable attractors in the field
        self.pathways = {}      # Connections between elements
        
        # Field state tracking
        self.state_history = []     # History of field states
        self.operation_log = []     # Log of operations
        self.current_time = time.time()  # Current field time
        self.field_id = str(uuid.uuid4())  # Unique identifier
        
        # Field metrics
        self.metrics = {
            "coherence": 0.5,
            "stability": 0.7,
            "boundary_integrity": 0.9,
            "attractor_strength": 0.6,
            "overall_health": 0.0
        }
        self._update_overall_health()
        
        # Initialize empty field
        self._initialize_empty_field()
    
    def _initialize_empty_field(self):
        """Initialize an empty semantic field with visualization grid."""
        grid_size = 10
        self.field_grid = np.zeros((grid_size, grid_size))
        self.field_grid += np.random.normal(0, 0.05, (grid_size, grid_size))
        self._log_operation("initialize_field", {"dimensions": self.dimensions})
    
    def _update_overall_health(self):
        """Calculate overall health based on component metrics."""
        self.metrics["overall_health"] = (
            self.metrics["coherence"] * 0.3 +
            self.metrics["stability"] * 0.3 +
            self.metrics["boundary_integrity"] * 0.2 +
            self.metrics["attractor_strength"] * 0.2
        )
    
    def _log_operation(self, operation_type: str, parameters: Dict[str, Any]):
        """Record an operation in the field's log."""
        operation = {
            "type": operation_type,
            "timestamp": time.time(),
            "parameters": parameters
        }
        self.operation_log.append(operation)
    
    def _take_field_snapshot(self):
        """Capture the current state of the field."""
        snapshot = {
            "timestamp": time.time(),
            "content_count": len(self.content),
            "pattern_count": len(self.patterns),
            "attractor_count": len(self.attractors),
            "pathway_count": len(self.pathways),
            "metrics": self.metrics.copy()
        }
        self.state_history.append(snapshot)
    
    def inject(self, content: str, strength: float = 1.0, position: Optional[Tuple[float, ...]] = None) -> str:
        """
        Inject new content into the field.
        
        Args:
            content: The semantic content to inject
            strength: Initial strength of the content
            position: Optional position in the field
            
        Returns:
            str: ID of the injected content
        """
        content_id = str(uuid.uuid4())
        effective_strength = strength * self.boundary_permeability
        
        if position is None:
            position = tuple(random.random() * 10 for _ in range(self.dimensions))
        
        resonances = {}
        for existing_id, existing_content in self.content.items():
            resonance = self._calculate_resonance(content, existing_content["content"])
            if resonance > 0.2:
                resonances[existing_id] = resonance
        
        content_entry = {
            "content": content,
            "strength": effective_strength,
            "position": position,
            "injection_time": time.time(),
            "last_update_time": time.time(),
            "resonances": resonances
        }
        
        self.content[content_id] = content_entry
        self._update_field_grid(content_entry)
        
        self._log_operation("inject", {
            "content_id": content_id,
            "content_preview": content[:50] + "..." if len(content) > 50 else content,
            "strength": effective_strength,
            "resonances": len(resonances)
        })
        
        self._detect_patterns()
        self._check_attractor_formation()
        self._take_field_snapshot()
        
        return content_id
    
    # [Remaining methods from the original implementation...]
    
    def get_summary(self) -> Dict[str, Any]:
        """Get a summary of the current field state."""
        return {
            "field_id": self.field_id,
            "age": time.time() - self.current_time,
            "content_count": len(self.content),
            "pattern_count": len(self.patterns),
            "attractor_count": len(self.attractors),
            "pathway_count": len(self.pathways),
            "operation_count": len(self.operation_log),
            "snapshot_count": len(self.state_history),
            "metrics": self.metrics,
            "parameters": {
                "dimensions": self.dimensions,
                "decay_rate": self.decay_rate,
                "boundary_permeability": self.boundary_permeability,
                "resonance_bandwidth": self.resonance_bandwidth,
                "attractor_threshold": self.attractor_threshold
            }
        }


# Usage demonstration
if __name__ == "__main__":
    # Initialize a context field
    field = ContextField(
        dimensions=2,
        decay_rate=0.05,
        boundary_permeability=0.8,
        resonance_bandwidth=0.6,
        attractor_threshold=0.7
    )
    
    # Inject some content
    field.inject("This is a demonstration of context field operations.", strength=0.8)
    field.inject("Context fields use attractors to represent stable meaning.", strength=0.9)
    field.inject("Attractors naturally form through resonance and pattern detection.", strength=0.7)
    field.inject("Field operations include injection, decay, and attractor formation.", strength=0.8)
    field.inject("Resonance occurs when compatible patterns reinforce each other.", strength=0.7)
    
    # Apply decay to simulate time passing
    field.decay()
    
    # Display field summary
    summary = field.get_summary()
    print("Field Summary:")
    for key, value in summary.items():
        if key not in ["metrics", "parameters"]:
            print(f"  {key}: {value}")
    
    print("\nField Metrics:")
    for key, value in summary["metrics"].items():
        print(f"  {key}: {value:.2f}")
    
    # Visualize attractors
    attractor_vis = field.visualize_field("attractors")
    print(f"\nAttractors ({attractor_vis['count']}):")
    for attractor_id, attractor in attractor_vis.get("attractors", {}).items():
        print(f"  {attractor_id}: {attractor['pattern']} (strength: {attractor['strength']:.2f})")
```

## Field Visualization: Understanding Attractors and Resonance

Visualizing context fields helps us understand how attractors and resonance function within a semantic space.

### Attractors in Semantic Space

Imagine a landscape where concepts settle into valleys (attractors) based on their meaning:

```
┌─────────────────────────────────────────────────────────┐
│             FIELD VISUALIZATION: ATTRACTORS             │
├─────────────────────────────────────────────────────────┤
│                                                         │
│     Semantic Space (2D Projection)                      │
│                                                         │
│     ╭─────────────────────────────────────────────╮     │
│     │                                             │     │
│     │                          Attractor B        │     │
│     │                          "Context Field"    │     │
│     │                               ╱╲            │     │
│     │                              /  \           │     │
│     │                             /    \          │     │
│     │                            /      \         │     │
│     │                     ─────╲        /─────    │     │
│     │                           ╲      /          │     │
│     │                            ╲    /           │     │
│     │                             ╲  /            │     │
│     │  Attractor A                 \/             │     │
│     │  "Prompt Engineering"         Resonance     │     │
│     │        ╱╲                     Pathway       │     │
│     │       /  \                                  │     │
│     │      /    \                                 │     │
│     │     /      \                      Attractor C     │
│     │    /        \                     "Memory"        │
│     │   /          \                        ╱╲          │
│     │  /            \                      /  \         │
│     │ /              \                    /    \        │
│     │/                \                  /      \       │
│     │                  \                /        \      │
│     │                   \              /          \     │
│     │                    \            /            \    │
│     │                     \          /              \   │
│     │                      \        /                \  │
│     │                                                   │
│     ╰─────────────────────────────────────────────╯     │
│                                                         │
└─────────────────────────────────────────────────────────┘
```

### Key Concepts Visualized:

1. **Attractors**: Represent stable concepts like "Prompt Engineering," "Context Field," and "Memory."
2. **Basin of Attraction**: Shows the influence range of each attractor.
3. **Resonance Pathway**: Connection between related concepts.

## How Resonance Works

Resonance occurs when patterns reinforce each other like tuning forks:

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

Fields evolve as new information is added and old information decays:

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
│                                              ╲          │
│                                               ╲         │
│                                          C     ╲        │
│                                         ╱╲      ╲       │
│                                        /  \      ╲      │
│                                       /    \      ╲     │
│                                      /      \      ╲    │
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

## How Protocol Shells Operate on Fields

Protocol shells provide structured operations for manipulating the field:

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
│                     ──►       /            \            │
│        C   D                 /   Amplified  \           │
│       ╱╲  ╱╲                /                \          │
│      /  \/  \              /        C   D     \         │
│     /        \            /        ╱╲  ╱╲      \        │
│                          /        /  \/  \      \       │
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
│/          \/╲                /     Fixed\               │
│            /  \             /       B    \              │
│           /    \           /     ╱╲       \             │
│          /      \         /     /  \       \            │
│                                /    \                   │
│                               /      \                  │
│                                                         │
│  Memory creates persistent    Self-repair fixes         │
│  pathways between attractors  damaged attractors        │
│                                                         │
└─────────────────────────────────────────────────────────┘
```

## Field Health and Coherence

Context fields have measurable health metrics. High coherence means the field maintains structure despite noise or damage:

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
│      /              \         Minimal noise             │
│     /                \                                  │
│    /                  \       Resilient to              │
│   /                    \      perturbations             │
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

## Practical Applications

Here's how these concepts translate to code. This function demonstrates attractor formation:

```python
def form_attractor(field, pattern, strength=0.7):
    """Form a new attractor in the field."""
    if strength >= field.attractor_threshold:
        attractor = {
            "pattern": pattern,
            "strength": strength,
            "basin_width": 0.5 + (0.5 * strength),
            "formation_time": time.time()
        }
        attractor_id = field.add_attractor(attractor)
        field._log_operation("form_attractor", {
            "attractor_id": attractor_id,
            "pattern": pattern,
            "strength": strength
        })
        field._update_metrics_after_attractor_formation()
        return attractor_id
    return None
```

## Understanding Through Analogy

For those new to field theory:

1. **Gravitational Analogy**: Attractors are like planets with gravity wells.
2. **Social Network Analogy**: Attractors are like popular conversation topics.
3. **Musical Analogy**: Resonance is like harmony between musical notes.
4. **Ecosystem Analogy**: The field is like an ecosystem where concepts find niches.

## Visualizing Your Own Fields

To visualize context fields:

1. Map key concepts as potential attractors
2. Draw connections between related concepts
3. Identify strong attractors that should persist
4. Simulate field operations to see how the field might evolve

By visualizing these concepts, we can better understand how context fields operate and how to use them effectively.
