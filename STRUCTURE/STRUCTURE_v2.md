# Context-Engineering – Structural Overview v2
_A pragmatic, first-principles handbook for the next generation of LLM orchestration_

> **Why this repo exists**  
> Prompt engineering = thinking about **what** you say.  
> **Context engineering** = thinking about **everything else** the model sees.  
> 
> In our evolution from prompt engineering to context engineering to **field theory**:
> - We began with discrete tokens and simple prompts
> - We advanced to stateful context management and complex orchestration
> - We now explore emergent symbolic mechanisms and neural field dynamics
> 
> Our goal is to teach all of this from the ground up, with humility and a bias toward simple, working code, while embracing the latest research on how LLMs actually reason and process information.

---

## 1. Map of the Territory

| Folder | Role (Plain English) | First-Principles Metaphor | Key Concepts |
|--------|----------------------|---------------------------|-------------|
| `00_foundations` | Theory & intuition. Tiny, self-contained readings. | Atoms → Molecules → Cells → Organs → Neural Systems → Fields | Progressive complexity from basic prompts to emergent field dynamics |
| `10_guides_zero_to_hero` | Interactive guides you **run**, tweak, break. | Chemistry set | Hands-on experiments with measurable outcomes |
| `20_templates` | Drop-in snippets you can copy/paste. | Lego bricks | Reusable components for rapid implementation |
| `30_examples` | End-to-end mini-apps, each harder than the last. | Model organisms | Complete systems demonstrating principles in action |
| `40_reference` | Deeper dives & evaluation cookbooks. | Textbook appendix | Comprehensive resources and evaluation frameworks |
| `50_contrib` | Space for community pull requests. | Open lab bench | Collaborative experimentation zone |
| `60_protocols` | Protocol shells, schemas, and frameworks. | DNA sequences | Structured definitions for field operations |
| `70_agents` | Self-contained agent demos using protocols. | Stem-cell cultures | Specialized components with emergent properties |
| `80_field_integration` | End-to-end projects with field protocols. | Whole organisms | Complete systems with field-based architectures |
| `cognitive-tools` | Advanced cognitive frameworks and architectures. | Extended neural systems | Structured reasoning operations and tools |

---

## 2. Learning Path: From Basics to Field Theory

### 2.1. Foundations Track (Understanding the Basics)

1. **Skim `README.md` (2 min)**  
   See what "context" even means beyond prompts.

2. **Read `00_foundations/01_atoms_prompting.md` (5 min)**  
   *Atoms*: a single instruction / example.  
   Why atoms alone often underperform.

3. **Continue through the biological metaphor chain:**  
   - `02_molecules_context.md`: Few-shot packs and examples
   - `03_cells_memory.md`: Memory & logs for persistence
   - `04_organs_applications.md`: Multi-step control flows and orchestration
   - `05_cognitive_tools.md`: Mental model extensions for reasoning

### 2.2. Advanced Track (Diving Deeper)

4. **Explore advanced applications and patterns:**
   - `06_advanced_applications.md`: Real-world implementations
   - `07_prompt_programming.md`: Code-like reasoning patterns
   - `08_neural_fields_foundations.md`: Context as continuous fields
   - `09_persistence_and_resonance.md`: Field dynamics and attractors
   - `10_field_orchestration.md`: Coordinating multiple fields
   - `11_emergence_and_attractor_dynamics.md`: Emergent properties
   - `12_symbolic_mechanisms.md`: Symbolic reasoning in LLMs

### 2.3. Hands-On Practice (Learning by Doing)

5. **Start with `10_guides_zero_to_hero/01_min_prompt.ipynb`**  
   Run, modify, observe token counts.  
   Notebook cells highlight **why** each extra line helps (or hurts).

6. **Explore more complex patterns:**
   - `02_expand_context.ipynb`: Adding context effectively
   - `03_control_loops.ipynb`: Building flow control
   - `04_rag_recipes.ipynb`: Retrieval-augmented generation
   - `05_protocol_bootstrap.ipynb`: Working with field protocols
   - `06_protocol_token_budget.ipynb`: Measuring efficiency

7. **Advance to field-based approaches:**
   - `07_streaming_context.ipynb`: Real-time context management
   - `08_emergence_detection.ipynb`: Detecting emergent patterns
   - `09_residue_tracking.ipynb`: Following symbolic residue
   - `10_attractor_formation.ipynb`: Creating stable field patterns

### 2.4. Implementation Track (Building Real Systems)

8. **Experiment with `20_templates/`**  
   Copy a YAML or Python snippet into your own repo.  
   Tune "token_budget" or "resonance_score" like adjusting pH.

9. **Examine `30_examples/` implementations:**
   - `00_toy_chatbot/`: Simple but complete context management
   - `01_data_annotator/`: Specialized context for data labeling
   - `02_multi_agent_orchestrator/`: Complex agent coordination
   - `03_vscode_helper/`: IDE integration for context engineering
   - `04_rag_minimal/`: Streamlined retrieval architecture

10. **Explore field-based examples:**
    - `05_streaming_window/`: Real-time context management
    - `06_residue_scanner/`: Symbolic residue detection
    - `07_attractor_visualizer/`: Visualizing field dynamics
    - `08_field_protocol_demo/`: Protocol-based field operations
    - `09_emergence_lab/`: Detecting and measuring emergence

### 2.5. Advanced Integration (Field Theory in Practice)

11. **Dive into field protocols with `60_protocols/`:**
    - Protocol shells for defining field operations
    - Schemas for structured field representations
    - Digests for understanding protocol functions

12. **Study agent implementations in `70_agents/`:**
    - `01_residue_scanner/`: Detecting symbolic residue
    - `02_self_repair_loop/`: Self-healing field protocols
    - `03_attractor_modulator/`: Managing attractor dynamics
    - `04_boundary_adapter/`: Dynamic boundary tuning
    - `05_field_resonance_tuner/`: Optimizing field resonance

13. **Explore integrated systems in `80_field_integration/`:**
    - `00_protocol_ide_helper/`: Development tools for protocols
    - `01_context_engineering_assistant/`: Field-based assistant
    - `02_recursive_reasoning_system/`: Recursive reasoning architecture
    - `03_emergent_field_laboratory/`: Experimental field environments
    - `04_symbolic_reasoning_engine/`: Symbolic mechanism integration

14. **Understand cognitive tools in `cognitive-tools/`:**
    - Cognitive templates for structured reasoning
    - Cognitive programs for complex operations
    - Cognitive schemas for knowledge representation
    - Cognitive architectures for complete systems
    - Integration patterns for connecting with other components

---

## 3. Conceptual Foundations

### 3.1. Biological Metaphor Evolution

Our biological metaphor has evolved from simple components to complex, field-based systems:

```
Atoms         → Individual instructions or constraints
Molecules     → Instructions with examples (few-shot learning)
Cells         → Context with memory that persists across interactions
Organs        → Coordinated systems of context cells working together
Neural Systems → Cognitive tools extending reasoning capabilities
Neural Fields  → Context as continuous medium with emergent properties
```

### 3.2. Field Theory Concepts

As we advance to neural field theory, we incorporate several key concepts:

1. **Continuity**: Context as continuous semantic landscape rather than discrete tokens
2. **Resonance**: How information patterns interact and reinforce each other
3. **Persistence**: How information maintains influence over time
4. **Attractor Dynamics**: Stable patterns that organize the field
5. **Boundary Dynamics**: How information enters and exits the field
6. **Symbolic Residue**: Fragments of meaning that persist and influence the field
7. **Emergence**: How new patterns and behaviors arise from field interactions

### 3.3. Emergent Symbolic Mechanisms

Research has identified an emergent three-stage architecture for symbolic reasoning in LLMs:

1. **Symbol Abstraction**: Heads in early layers convert input tokens to abstract variables based on relations
2. **Symbolic Induction**: Heads in intermediate layers perform sequence induction over abstract variables
3. **Retrieval**: Heads in later layers predict next tokens by retrieving values associated with abstract variables

These mechanisms support our field-based approach to context engineering by providing a mechanistic understanding of how LLMs actually process and reason with information.

### 3.4. Cognitive Tools Framework

To enhance reasoning capabilities, we incorporate a cognitive tools framework:

1. **Tool-Based Approach**: Modular, predetermined cognitive operations executed sequentially
2. **Key Operations**:
   - **Recall Related**: Retrieving relevant knowledge to guide reasoning
   - **Examine Answer**: Self-reflection on reasoning and answers
   - **Backtracking**: Exploring alternative reasoning paths when blocked
3. **Integration**: These tools can be combined with field-based approaches for more powerful systems

---

## 4. Quiet Karpathy Guidelines (Style DNA)  

*Keep it atomic → build up.*  
1. **Minimal first pass** – start with the smallest viable context.  
2. **Iterative add-on** – add only what the model demonstrably lacks.  
3. **Measure everything** – token cost, latency, quality score, field resonance.  
4. **Delete ruthlessly** – pruning beats padding.  
5. **Code > slides** – every concept has a runnable cell.
6. **Recursive thinking** – contexts that evolve themselves.

---

## 5. Repository Structure in Detail

```
Context-Engineering/
├── LICENSE                          # MIT license
├── README.md                        # Quick-start overview
├── structure.md                     # Original structural map
├── STRUCTURE_v2.md                  # Enhanced structural map with field theory
├── context.json                     # Original schema configuration
├── context_v2.json                  # Extended schema with field protocols
├── context_v3.json                  # Neural field extensions
├── context_v3.5.json                # Symbolic mechanism integration
├── CITATIONS.md                     # Research references and bridges
│
├── 00_foundations/                  # First-principles theory
│   ├── 01_atoms_prompting.md        # Atomic instruction units
│   ├── 02_molecules_context.md      # Few-shot examples/context
│   ├── 03_cells_memory.md           # Stateful conversation layers
│   ├── 04_organs_applications.md    # Multi-step control flows
│   ├── 05_cognitive_tools.md        # Mental model extensions
│   ├── 06_advanced_applications.md  # Real-world implementations
│   ├── 07_prompt_programming.md     # Code-like reasoning patterns
│   ├── 08_neural_fields_foundations.md # Context as continuous fields
│   ├── 09_persistence_and_resonance.md # Field dynamics and attractors
│   ├── 10_field_orchestration.md    # Coordinating multiple fields
│   ├── 11_emergence_and_attractor_dynamics.md # Emergent properties
│   └── 12_symbolic_mechanisms.md    # Symbolic reasoning in LLMs
│
├── 10_guides_zero_to_hero/          # Hands-on tutorials
│   ├── 01_min_prompt.ipynb          # Minimal prompt experiments
│   ├── 02_expand_context.ipynb      # Context expansion techniques
│   ├── 03_control_loops.ipynb       # Flow control mechanisms
│   ├── 04_rag_recipes.ipynb         # Retrieval-augmented patterns
│   ├── 05_protocol_bootstrap.ipynb  # Field protocol bootstrap
│   ├── 06_protocol_token_budget.ipynb # Protocol efficiency
│   ├── 07_streaming_context.ipynb   # Real-time context
│   ├── 08_emergence_detection.ipynb # Detecting emergence
│   ├── 09_residue_tracking.ipynb    # Tracking symbolic residue
│   └── 10_attractor_formation.ipynb # Creating field attractors
│
├── 20_templates/                    # Reusable components
│   ├── minimal_context.yaml         # Base context structure
│   ├── control_loop.py              # Orchestration template
│   ├── scoring_functions.py         # Evaluation metrics
│   ├── prompt_program_template.py   # Program structure template
│   ├── schema_template.yaml         # Schema definition template
│   ├── recursive_framework.py       # Recursive context template
│   ├── field_protocol_shells.py     # Field protocol templates
│   ├── symbolic_residue_tracker.py  # Residue tracking tools
│   ├── context_audit.py             # Context analysis tool
│   ├── shell_runner.py              # Protocol shell runner
│   ├── resonance_measurement.py     # Field resonance metrics
│   ├── attractor_detection.py       # Attractor analysis tools
│   ├── boundary_dynamics.py         # Boundary operation tools
│   └── emergence_metrics.py         # Emergence measurement
│
├── 30_examples/                     # Practical implementations
│   ├── 00_toy_chatbot/              # Simple conversation agent
│   ├── 01_data_annotator/           # Data labeling system
│   ├── 02_multi_agent_orchestrator/ # Agent collaboration system
│   ├── 03_vscode_helper/            # IDE integration 
│   ├── 04_rag_minimal/              # Minimal RAG implementation
│   ├── 05_streaming_window/         # Real-time context demo
│   ├── 06_residue_scanner/          # Symbolic residue demo
│   ├── 07_attractor_visualizer/     # Field visualization
│   ├── 08_field_protocol_demo/      # Protocol demonstration
│   └── 09_emergence_lab/            # Emergence experimentation
│
├── 40_reference/                    # Deep-dive documentation
│   ├── token_budgeting.md           # Token optimization strategies
│   ├── retrieval_indexing.md        # Retrieval system design
│   ├── eval_checklist.md            # PR evaluation criteria
│   ├── cognitive_patterns.md        # Reasoning pattern catalog
│   ├── schema_cookbook.md           # Schema pattern collection
│   ├── patterns.md                  # Context pattern library
│   ├── field_mapping.md             # Field theory fundamentals
│   ├── symbolic_residue_types.md    # Residue classification
│   ├── attractor_dynamics.md        # Attractor theory and practice
│   ├── emergence_signatures.md      # Detecting emergence
│   └── boundary_operations.md       # Boundary management guide
│
├── 50_contrib/                      # Community contributions
│   └── README.md                    # Contribution guidelines
│
├── 60_protocols/                    # Protocol shells and frameworks
│   ├── README.md                    # Protocol overview
│   ├── shells/                      # Protocol shell definitions
│   │   ├── attractor.co.emerge.shell      # Attractor co-emergence
│   │   ├── recursive.emergence.shell      # Recursive field emergence
│   │   ├── recursive.memory.attractor.shell # Memory persistence
│   │   ├── field.resonance.scaffold.shell  # Field resonance
│   │   ├── field.self_repair.shell        # Self-repair mechanisms
│   │   └── context.memory.persistence.attractor.shell # Context persistence
│   ├── digests/                     # Simplified protocol documentation
│   └── schemas/                     # Protocol schemas
│       ├── fractalRepoContext.v3.5.json    # Repository context
│       ├── fractalConsciousnessField.v1.json # Field schema
│       ├── protocolShell.v1.json           # Shell schema
│       ├── symbolicResidue.v1.json         # Residue schema
│       └── attractorDynamics.v1.json       # Attractor schema
│
├── 70_agents/                       # Agent demonstrations
│   ├── README.md                    # Agent overview
│   ├── 01_residue_scanner/          # Symbolic residue detection
│   ├── 02_self_repair_loop/         # Self-repair protocol
│   ├── 03_attractor_modulator/      # Attractor dynamics
│   ├── 04_boundary_adapter/         # Dynamic boundary tuning
│   └── 05_field_resonance_tuner/    # Field resonance optimization
│
├── 80_field_integration/            # Complete field projects
│   ├── README.md                    # Integration overview
│   ├── 00_protocol_ide_helper/      # Protocol development tools
│   ├── 01_context_engineering_assistant/ # Field-based assistant
│   ├── 02_recursive_reasoning_system/    # Recursive reasoning
│   ├── 03_emergent_field_laboratory/     # Field experimentation
│   └── 04_symbolic_reasoning_engine/     # Symbolic mechanisms
│
├── cognitive-tools/                 # Advanced cognitive framework
│   ├── README.md                    # Overview and quick-start guide
│   ├── cognitive-templates/         # Templates for reasoning
│   │   ├── understanding.md         # Comprehension operations
│   │   ├── reasoning.md             # Analytical operations
│   │   ├── verification.md          # Checking and validation
│   │   ├── composition.md           # Combining multiple tools
│   │   └── emergence.md             # Emergent reasoning patterns
│   │
│   ├── cognitive-programs/          # Structured prompt programs
│   │   ├── basic-programs.md        # Fundamental program structures
│   │   ├── advanced-programs.md     # Complex program architectures
│   │   ├── program-library.py       # Python implementations
│   │   ├── program-examples.ipynb   # Interactive examples
│   │   └── emergence-programs.md    # Emergent program patterns
│   │
│   ├── cognitive-schemas/           # Knowledge representations
│   │   ├── user-schemas.md          # User information schemas
│   │   ├── domain-schemas.md        # Domain knowledge schemas
│   │   ├── task-schemas.md          # Reasoning task schemas
│   │   ├── schema-library.yaml      # Reusable schema library
│   │   └── field-schemas.md         # Field representation schemas
│   │
│   ├── cognitive-architectures/     # Complete reasoning systems
│   │   ├── solver-architecture.md   # Problem-solving systems
│   │   ├── tutor-architecture.md    # Educational systems
│   │   ├── research-architecture.md # Information synthesis
│   │   ├── architecture-examples.py # Implementation examples
│   │   └── field-architecture.md    # Field-based architectures
│   │
│   └── integration/                 # Integration patterns
│       ├── with-rag.md              # Integration with retrieval
│       ├── with-memory.md           # Integration with memory
│       ├── with-agents.md           # Integration with agents
│       ├── evaluation-metrics.md    # Effectiveness measurement
│       └── with-fields.md           # Integration with field protocols
│
└── .github/                         # GitHub configuration
    ├── CONTRIBUTING.md              # Contribution guidelines
    ├── workflows/ci.yml             # CI pipeline configuration
    ├── workflows/eval.yml           # Evaluation automation
    └── workflows/protocol_tests.yml # Protocol testing
```

---

## 6. Implementation Patterns

### 6.1. Context Structure Patterns

| Pattern | Description | Use Case |
|---------|-------------|----------|
| **Atomic Prompt** | Single instruction with constraints | Simple, well-defined tasks |
| **Few-Shot Examples** | Instruction with examples | Pattern demonstration |
| **Chain-of-Thought** | Reasoning steps explicit in prompt | Complex reasoning tasks |
| **Stateful Context** | Context with memory | Multi-turn conversations |
| **Multi-Agent** | Multiple specialized agents | Complex, multi-step tasks |
| **Field-Based** | Context as continuous field | Emergent reasoning needs |

### 6.2. Field Operation Patterns

| Pattern | Description | Implementation |
|---------|-------------|----------------|
| **Attractor Formation** | Creating stable semantic patterns | `attractor_detection.py` |
| **Resonance Amplification** | Strengthening pattern interactions | `resonance_measurement.py` |
| **Boundary Tuning** | Controlling information flow | `boundary_dynamics.py` |
| **Residue Integration** | Managing symbolic fragments | `symbolic_residue_tracker.py` |
| **Emergence Detection** | Identifying novel patterns | `emergence_metrics.py` |
| **Self-Repair** | Automatic context healing | `field.self_repair.shell` |

### 6.3. Cognitive Tool Patterns

| Pattern | Description | Implementation |
|---------|-------------|----------------|
| **Recall Related** | Retrieving relevant knowledge | `cognitive-programs/basic-programs.md` |
| **Examine Answer** | Self-reflection and verification | `cognitive-templates/verification.md` |
| **Backtracking** | Exploring alternative paths | `cognitive-programs/advanced-programs.md` |
| **Decomposition** | Breaking problems into parts | `cognitive-templates/reasoning.md` |
| **Integration** | Combining multiple results | `cognitive-templates/composition.md` |

---

## 7. How to Contribute

Open a PR in `50_contrib/`.  
Checklist lives in `40_reference/eval_checklist.md`—run it before submitting.

When contributing:
1. Follow the Karpathy style guidelines
2. Include runnable code examples
3. Measure token usage and performance
4. Maintain the biological metaphor consistency
5. Add tests for any new functionality
6. Consider field dynamics and symbolic mechanisms

### 7.1. Contribution Focus Areas

We especially welcome contributions in these areas:

1. **Field Dynamics Tools**: Tools for measuring and visualizing field properties
2. **Symbolic Mechanism Experiments**: Demonstrations of emergent symbolic processing
3. **Cognitive Tool Implementations**: New cognitive operations and patterns
4. **Protocol Shell Developments**: Novel protocol shells for field operations
5. **Integration Examples**: Combining multiple approaches in practical applications
6. **Evaluation Metrics**: Better ways to measure context effectiveness

---

## 8. License & Attribution

MIT. No gate-keeping: copy, remix, redistribute.  
A respectful nod to Andrej Karpathy for coining the framing.  
Research acknowledgments in CITATIONS.md.  
All errors are ours; improvements are welcome.

---

## 9. Roadmap

### 9.1. Near-Term Priorities

1. **Symbolic Mechanism Integration**: Better leverage of emergent symbolic mechanisms
2. **Field Visualization Tools**: Tools for understanding field dynamics
3. **Protocol Shell Expansion**: More protocol shells for field operations
4. **Evaluation Framework Enhancement**: Improved metrics for field-based systems
5. **Cognitive Tool Integration**: Better integration with field-based approaches

### 9.2. Long-Term Vision

1. **Self-Evolving Context Systems**: Contexts that improve themselves
2. **Field Theory Formalization**: More rigorous mathematical foundation
3. **Unified Framework**: Integrating symbolic mechanisms, field theory, and cognitive tools
4. **Cross-Model Compatibility**: Ensuring techniques work across different model architectures
5. **Automated Context Optimization**: Tools for automatic context tuning
