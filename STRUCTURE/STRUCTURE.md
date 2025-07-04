# Context-Engineering – Structural Overview
_A pragmatic, first-principles handbook for the next generation of LLM orchestration_

> **Why this repo exists**  
> Prompt engineering = thinking about **what** you say.  
> **Context engineering** = thinking about **everything else** the model sees.  
> Our goal is to teach that "everything else" from the ground-up, with humility and a bias toward simple, working code.
> 
> As models evolve, so does our approach: from discrete tokens to continuous fields, from static prompts to resonant patterns.

---

## 1. Map of the Territory

| Folder | Role (Plain English) | First-Principles Metaphor |
|--------|----------------------|---------------------------|
| `00_foundations` | Theory & intuition. Tiny, self-contained readings. | Atoms → Molecules → Cells → Organs → Neural Systems → Fields |
| `10_guides_zero_to_hero` | Interactive guides you **run**, tweak, break. | Chemistry set |
| `20_templates` | Drop-in snippets you can copy/paste. | Lego bricks |
| `30_examples` | End-to-end mini-apps, each harder than the last. | Model organisms |
| `40_reference` | Deeper dives & evaluation cookbooks. | Textbook appendix |
| `50_contrib` | Space for community pull requests. | Open lab bench |
| `60_protocols` | Protocol shells, schemas, and frameworks. | DNA sequences |
| `70_agents` | Self-contained agent demos using protocols. | Stem-cell cultures |
| `80_field_integration` | End-to-end projects with field protocols. | Whole organisms |
| `cognitive-tools` | Advanced cognitive frameworks and architectures. | Extended neural systems |

---

## 2. Learning Path (0 → Zero → Hero)

### Foundations (Understanding the Basics)

1. **Skim `README.md` (2 min)**  
   See what "context" even means beyond prompts.

2. **Read `00_foundations/01_atoms_prompting.md` (5 min)**  
   *Atoms*: a single instruction / example.  
   Why atoms alone often underperform.

3. **Continue through the biological metaphor chain:**  
   - `02_molecules_context.md`: Few-shot packs
   - `03_cells_memory.md`: Memory & logs
   - `04_organs_applications.md`: Multi-step control flows
   - `05_cognitive_tools.md`: Mental model extensions
   - `06_advanced_applications.md`: Real-world implementations
   - `07_prompt_programming.md`: Code-like reasoning patterns
   - `08_neural_fields_foundations.md`: Context as continuous fields
   - `09_persistence_and_resonance.md`: Field dynamics and attractors
   - `10_field_orchestration.md`: Coordinating multiple fields

### Hands-On Practice (Learning by Doing)

4. **Open `10_guides_zero_to_hero/01_min_prompt.ipynb`**  
   Run, modify, observe token counts.  
   Notebook cells highlight **why** each extra line helps (or hurts).

5. **Experiment through progressive notebooks:**
   - Basic context manipulation
   - Control flow and reasoning patterns
   - Retrieval augmentation strategies
   - Prompt programming techniques
   - Schema design principles
   - Recursive context patterns
   - Neural field implementation

### Applied Skills (Building Real Solutions)

6. **Copy a template from `20_templates/`**  
   Use as starting points for your projects:
   - `minimal_context.yaml` for basic projects
   - `control_loop.py` for interactive systems
   - `scoring_functions.py` for evaluation
   - `prompt_program_template.py` for reasoning tasks
   - `schema_template.yaml` for structured data
   - `recursive_framework.py` for self-improving systems
   - `neural_field_context.yaml` for field-based approaches

7. **Study examples in `30_examples/`**  
   See complete implementations of progressively complex systems:
   - Basic conversational agents
   - Data annotation systems
   - Multi-agent orchestration
   - Cognitive assistants
   - RAG implementations
   - Neural field orchestrators

### Advanced Topics (Mastering the Craft)

8. **Explore cognitive tools and protocols:**
   - Advanced reasoning frameworks in `cognitive-tools/`
   - Protocol shells and schemas in `60_protocols/`
   - Agent demonstrations in `70_agents/`
   - Complete field integration projects in `80_field_integration/`

9. **Contribute back to the community:**
   - Review the contribution guidelines in `50_contrib/README.md`
   - Check the evaluation criteria in `40_reference/eval_checklist.md`
   - Open a PR with your improvements or extensions

---

## 3. Biological Metaphor Evolution

Our repository is organized around an extended biological metaphor that helps make abstract concepts concrete and shows how simple components build into complex systems:

```
                                   ┌───────────────────┐
                                   │  Neural Fields    │  08_neural_fields_foundations.md
                                   │  (Continuous      │  09_persistence_and_resonance.md
                                   │   Context Medium) │  10_field_orchestration.md
                                   └───────┬───────────┘
                                           │
                                           ▲
                                           │
                                   ┌───────┴───────────┐
                                   │ Neurobiological   │  05_cognitive_tools.md
                                   │ Systems           │  06_advanced_applications.md
                                   │ (Cognitive Tools) │  07_prompt_programming.md
                                   └───────┬───────────┘
                                           │
                                           ▲
                                           │
                             ┌─────────────┴─────────────┐
                             │         Organs            │  04_organs_applications.md
                             │  (Multi-Agent Systems)    │
                             └─────────────┬─────────────┘
                                           │
                                           ▲
                                           │
                             ┌─────────────┴─────────────┐
                             │         Cells             │  03_cells_memory.md
                             │   (Memory Systems)        │
                             └─────────────┬─────────────┘
                                           │
                                           ▲
                                           │
                             ┌─────────────┴─────────────┐
                             │       Molecules           │  02_molecules_context.md
                             │   (Few-Shot Examples)     │
                             └─────────────┬─────────────┘
                                           │
                                           ▲
                                           │
                             ┌─────────────┴─────────────┐
                             │         Atoms             │  01_atoms_prompting.md
                             │    (Single Prompts)       │
                             └───────────────────────────┘
```

This evolution follows the natural progression of complexity in biological systems and mirrors the development of increasingly sophisticated context engineering approaches.

---

## 4. Advanced Context Frameworks

### Protocol Shell Framework

Protocols provide structured shells for orchestrating complex context operations. Found in the `60_protocols/` directory:

```
/recursive.field{
    intent="Define field properties and operations",
    input={
        field_state=<current_state>,
        new_information=<incoming_data>
    },
    process=[
        /field.measure{resonance, coherence, entropy},
        /pattern.detect{across="field_state"},
        /attractor.form{where="pattern_strength > threshold"},
        /field.evolve{with="new_information"}
    ],
    output={
        updated_field=<new_state>,
        metrics={resonance_score, coherence_delta}
    }
}
```

These protocol shells enable:
- Declarative definition of context operations
- Recursive self-improvement patterns
- Field-based context manipulation
- Auditability through explicit process steps

### Cognitive Tool Framework

Cognitive tools provide reusable reasoning patterns that extend model capabilities. Found in the `cognitive-tools/` directory:

```
cognitive-tools/
├── cognitive-templates/     # Pattern templates for different reasoning modes
├── cognitive-programs/      # Structured prompt programs with code-like patterns
├── cognitive-schemas/       # Knowledge representation formats
├── cognitive-architectures/ # Complete reasoning systems
└── integration/            # Guides for integrating with other components
```

This framework supports:
- Modular reasoning components
- Domain-specific reasoning patterns
- Integration with retrieval and memory systems
- Evaluation metrics for reasoning quality

### Neural Field Framework

Neural fields represent context as a continuous medium rather than discrete tokens. Implemented across:

```
00_foundations/08_neural_fields_foundations.md  # Conceptual foundation
00_foundations/09_persistence_and_resonance.md  # Field dynamics
00_foundations/10_field_orchestration.md        # Multi-field coordination
20_templates/neural_field_context.yaml          # Implementation template
30_examples/05_neural_field_orchestrator/       # Complete example
```

Key concepts include:
- Context as a continuous semantic field
- Information persistence through resonance
- Attractor formation and dynamics
- Field orchestration for complex tasks

---

## 5. Quiet Karpathy Guidelines (Style DNA)  

*Keep it atomic → build up.*  
1. **Minimal first pass** – start with the smallest viable context.  
2. **Iterative add-on** – add only what the model demonstrably lacks.  
3. **Measure everything** – token cost, latency, quality score, field resonance.  
4. **Delete ruthlessly** – pruning beats padding.  
5. **Code > slides** – every concept has a runnable cell.
6. **Recursive thinking** – contexts that evolve themselves.

---

## 6. Repository Structure in Detail

```
Context-Engineering/
├── LICENSE                          # MIT license
├── README.md                        # Quick-start overview
├── structure.md                     # This structural map
├── context.json                     # Original schema configuration
├── context_v2.json                  # Extended schema with field protocols
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
│   └── 10_field_orchestration.md    # Coordinating multiple fields
│
├── 10_guides_zero_to_hero/          # Hands-on tutorials
│   ├── 01_min_prompt.ipynb          # Minimal prompt experiments
│   ├── 02_expand_context.ipynb      # Context expansion techniques
│   ├── 03_control_loops.ipynb       # Flow control mechanisms
│   ├── 04_rag_recipes.ipynb         # Retrieval-augmented patterns
│   ├── 05_prompt_programs.ipynb     # Structured reasoning programs
│   ├── 06_schema_design.ipynb       # Schema creation patterns
│   ├── 07_recursive_patterns.ipynb  # Self-referential contexts
│   └── 08_neural_fields.ipynb       # Working with field-based contexts
│
├── 20_templates/                    # Reusable components
│   ├── minimal_context.yaml         # Base context structure
│   ├── control_loop.py              # Orchestration template
│   ├── scoring_functions.py         # Evaluation metrics
│   ├── prompt_program_template.py   # Program structure template
│   ├── schema_template.yaml         # Schema definition template
│   ├── recursive_framework.py       # Recursive context template
│   ├── neural_field_context.yaml    # Field-based context template
│   ├── field_resonance_measure.py   # Field property measurement
│   └── context_audit.py             # Context analysis tool
│
├── 30_examples/                     # Practical implementations
│   ├── 00_toy_chatbot/              # Simple conversation agent
│   ├── 01_data_annotator/           # Data labeling system
│   ├── 02_multi_agent_orchestrator/ # Agent collaboration system
│   ├── 03_cognitive_assistant/      # Advanced reasoning assistant
│   ├── 04_rag_minimal/              # Minimal RAG implementation
│   └── 05_neural_field_orchestrator/ # Field-based orchestration
│
├── 40_reference/                    # Deep-dive documentation
│   ├── token_budgeting.md           # Token optimization strategies
│   ├── retrieval_indexing.md        # Retrieval system design
│   ├── eval_checklist.md            # PR evaluation criteria
│   ├── cognitive_patterns.md        # Reasoning pattern catalog
│   ├── schema_cookbook.md           # Schema pattern collection
│   ├── neural_field_theory.md       # Comprehensive field theory
│   ├── symbolic_residue_guide.md    # Guide to residue tracking
│   └── protocol_reference.md        # Protocol shell reference
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
│   │   └── field.resonance.scaffold.shell  # Field resonance
│   ├── digests/                     # Simplified protocol documentation
│   └── schemas/                     # Protocol schemas
│       ├── fractalRepoContext.v1.json     # Repository context
│       ├── fractalConsciousnessField.v1.json # Field schema
│       └── protocolShell.v1.json           # Shell schema
│
├── 70_agents/                       # Agent demonstrations
│   ├── README.md                    # Agent overview
│   ├── 01_residue_scanner/          # Symbolic residue detection
│   └── 02_self_repair_loop/         # Self-repair protocol
│
├── 80_field_integration/            # Complete field projects
│   ├── README.md                    # Integration overview
│   ├── 00_protocol_ide_helper/      # Protocol development tools
│   └── 01_context_engineering_assistant/ # Field-based assistant
│
├── cognitive-tools/                 # Advanced cognitive framework
│   ├── README.md                    # Overview and quick-start guide
│   ├── cognitive-templates/         # Templates for reasoning
│   │   ├── understanding.md         # Comprehension operations
│   │   ├── reasoning.md             # Analytical operations
│   │   ├── verification.md          # Checking and validation
│   │   └── composition.md           # Combining multiple tools
│   │
│   ├── cognitive-programs/          # Structured prompt programs
│   │   ├── basic-programs.md        # Fundamental program structures
│   │   ├── advanced-programs.md     # Complex program architectures
│   │   ├── program-library.py       # Python implementations
│   │   └── program-examples.ipynb   # Interactive examples
│   │
│   ├── cognitive-schemas/           # Knowledge representations
│   │   ├── user-schemas.md          # User information schemas
│   │   ├── domain-schemas.md        # Domain knowledge schemas
│   │   ├── task-schemas.md          # Reasoning task schemas
│   │   └── schema-library.yaml      # Reusable schema library
│   │
│   ├── cognitive-architectures/     # Complete reasoning systems
│   │   ├── solver-architecture.md   # Problem-solving systems
│   │   ├── tutor-architecture.md    # Educational systems
│   │   ├── research-architecture.md # Information synthesis
│   │   └── architecture-examples.py # Implementation examples
│   │
│   └── integration/                 # Integration patterns
│       ├── with-rag.md              # Integration with retrieval
│       ├── with-memory.md           # Integration with memory
│       ├── with-agents.md           # Integration with agents
│       └── evaluation-metrics.md    # Effectiveness measurement
│
└── .github/                         # GitHub configuration
    ├── CONTRIBUTING.md              # Contribution guidelines
    ├── workflows/ci.yml             # CI pipeline configuration
    ├── workflows/eval.yml           # Evaluation automation
    └── workflows/protocol_tests.yml # Protocol testing
```

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

---

## 8. License & Attribution

MIT. No gate-keeping: copy, remix, redistribute.  
A respectful nod to Andrej Karpathy for coining the framing.  
All errors are ours; improvements are welcome.
