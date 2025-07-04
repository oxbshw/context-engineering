# `conversation_examples.py`: Demonstration Conversations

This module provides example conversations that demonstrate how our toy chatbot implements context engineering principles from atomic responses to sophisticated field operations and meta-recursive capabilities.

## Conversation Scenarios

We'll explore several conversation scenarios that showcase different aspects of context engineering:

1. **Basic Conversation**: Simple prompt-response interactions (atomic layer)
2. **Context Retention**: Remembering previous topics across exchanges (cellular layer)
3. **Field Operations**: Attractor formation, resonance, and sophisticated field manipulation (field layer)
4. **Self-Repair**: Handling inconsistencies and restoring field integrity (field self-repair)
5. **Meta-Recursive**: Self-observation and continuous improvement (meta-recursive layer)

## Implementation

```python
import time
import random
import json
from typing import Dict, List, Any, Tuple

# Import our modules
from chatbot_core import ToyContextChatbot
from context_field import ContextField
from protocol_shells import (
    AttractorCoEmerge, 
    FieldResonanceScaffold, 
    RecursiveMemoryAttractor, 
    FieldSelfRepair
)

class ConversationExamples:
    """
    Examples of conversations with the context engineering chatbot,
    demonstrating various principles and capabilities.
    """
    
    def __init__(self):
        """Initialize with a chatbot instance and tracking variables."""
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
        self.chatbot = ToyContextChatbot(name="FieldBot")
        
        # Connect field and protocols to chatbot
        self.chatbot.field = self.field
        self.chatbot.protocols = self.protocols
        
        # Tracking variables
        self.conversations = {}
        self.current_conversation_id = None
    
    def run_basic_conversation(self) -> str:
        """
        Run a basic conversation to demonstrate atomic and molecular layers.
        
        Returns:
            str: Conversation ID
        """
        conversation_id = f"basic_{int(time.time())}"
        self.current_conversation_id = conversation_id
        
        # Start conversation
        self.conversations[conversation_id] = []
        
        # Add greeting
        self._add_exchange(
            "Hello there! I'm interested in learning about context engineering.",
            self.chatbot.chat("Hello there! I'm interested in learning about context engineering.")
        )
        
        # Ask about the chatbot
        self._add_exchange(
            "What can you tell me about yourself?",
            self.chatbot.chat("What can you tell me about yourself?")
        )
        
        # Ask about context engineering
        self._add_exchange(
            "How is context engineering different from prompt engineering?",
            self.chatbot.chat("How is context engineering different from prompt engineering?")
        )
        
        # Thank the chatbot
        self._add_exchange(
            "Thanks for the explanation!",
            self.chatbot.chat("Thanks for the explanation!")
        )
        
        # Add field metrics to conversation data
        self.conversations[conversation_id].append({
            "type": "metrics",
            "data": self.chatbot.show_field_state()
        })
        
        return conversation_id
    
    # Additional methods from the original implementation...
    
    def _add_exchange(self, user_message: str, bot_response: str) -> None:
        """Add a message exchange to the current conversation."""
        if self.current_conversation_id is None:
            raise ValueError("No active conversation")
        
        self.conversations[self.current_conversation_id].append({
            "type": "exchange",
            "user": user_message,
            "bot": bot_response,
            "timestamp": time.time()
        })
    
    def get_conversation(self, conversation_id: str) -> List[Dict[str, Any]]:
        """Get a conversation by ID."""
        return self.conversations.get(conversation_id, [])
    
    def print_conversation(self, conversation_id: str) -> None:
        """Print a conversation in a readable format."""
        conversation = self.get_conversation(conversation_id)
        
        print(f"=== Conversation: {conversation_id} ===\n")
        
        for item in conversation:
            if item["type"] == "exchange":
                print(f"User: {item['user']}")
                print(f"Bot: {item['bot']}")
                print()
            elif item["type"] == "metrics":
                print("=== Field Metrics ===")
                for key, value in item["data"].items():
                    if isinstance(value, dict):
                        continue  # Skip nested dictionaries for readability
                    print(f"{key}: {value}")
                print()
    
    # [Remaining methods from the original implementation...]
    
    def generate_report(self, conversation_id: str) -> str:
        """
        Generate a detailed report about a conversation.
        
        Args:
            conversation_id: ID of the conversation to report on
            
        Returns:
            str: Markdown-formatted report
        """
        conversation = self.get_conversation(conversation_id)
        if not conversation:
            return "Conversation not found."
        
        # Determine conversation type
        conv_type = conversation_id.split('_')[0]
        
        # Generate report header
        report = [
            f"# Conversation Report: {conversation_id}",
            "",
            f"**Type:** {conv_type.capitalize()} Conversation",
            f"**Exchanges:** {sum(1 for item in conversation if item['type'] == 'exchange')}",
            f"**Time:** {time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())}",
            "",
            "## Conversation Transcript",
            ""
        ]
        
        # Add transcript
        for item in conversation:
            if item["type"] == "exchange":
                report.append(f"**User:** {item['user']}")
                report.append(f"**Bot:** {item['bot']}")
                report.append("")
        
        # Add analysis based on conversation type
        if conv_type == "basic":
            report.extend(self._generate_basic_analysis(conversation))
        elif conv_type == "retention":
            report.extend(self._generate_retention_analysis(conversation))
        elif conv_type == "field":
            report.extend(self._generate_field_analysis(conversation))
        elif conv_type == "repair":
            report.extend(self._generate_repair_analysis(conversation))
        elif conv_type == "meta":
            report.extend(self._generate_meta_analysis(conversation))
        
        return "\n".join(report)
    
    # Additional analysis methods from the original implementation...

# Demo function to run all conversation examples
def run_conversation_demos():
    """Run all conversation examples and generate reports."""
    examples = ConversationExamples()
    
    print("Running Basic Conversation...")
    basic_id = examples.run_basic_conversation()
    examples.print_conversation(basic_id)
    
    print("\nRunning Context Retention Conversation...")
    retention_id = examples.run_context_retention_conversation()
    examples.print_conversation(retention_id)
    
    print("\nRunning Field Operations Conversation...")
    field_id = examples.run_field_operations_conversation()
    examples.print_conversation(field_id)
    
    print("\nRunning Self-Repair Conversation...")
    repair_id = examples.run_self_repair_conversation()
    examples.print_conversation(repair_id)
    
    print("\nRunning Meta-Recursive Conversation...")
    meta_id = examples.run_meta_recursive_conversation()
    examples.print_conversation(meta_id)
    
    # Generate and save reports
    for conv_id in [basic_id, retention_id, field_id, repair_id, meta_id]:
        report = examples.generate_report(conv_id)
        print(f"\nGenerated report for {conv_id}")
        
        # In a real implementation, we might save these reports to files
        # For this toy implementation, we'll just print a snippet
        print("\nReport Preview:")
        print("\n".join(report.split("\n")[:10]) + "\n...\n")
    
    return {
        "basic_id": basic_id,
        "retention_id": retention_id,
        "field_id": field_id,
        "repair_id": repair_id,
        "meta_id": meta_id
    }


# If run directly, execute the demos
if __name__ == "__main__":
    run_conversation_demos()
```

## Visualizing Meta-Recursive Improvement

Let's visualize how meta-recursive improvement works in our context engineering chatbot. This diagram shows the cyclical process of self-observation, self-improvement, and evolution:

```
┌─────────────────────────────────────────────────────────┐
│             META-RECURSIVE IMPROVEMENT CYCLE            │
├─────────────────────────────────────────────────────────┤
│                                                         │
│  ╭───────────────┐                                      │
│  │1. Self-       │                                      │
│  │  Observation  │                                      │
│  │  Monitor      │                                      │
│  │  performance  │                                      │
│  │  and field    │                                      │
│  │  state        │                                      │
│  ╰───────┬───────╯                                      │
│          │                                              │
│          ▼                                              │
│  ╭───────────────┐        ╭────────────────────┐        │
│  │2. Analysis    │        │  Improvement       │        │
│  │  Identify     │────►   │  Strategies:       │        │
│  │  areas for    │        │                    │        │
│  │  improvement  │        │  • Response Quality│        │
│  │               │        │  • Memory          │        │
│  │               │        │  • Flow            │        │
│  │               │        │  • Attractor Tuning│        │
│  ╰───────┬───────╯        ╰────────────────────╯        │
│          │                                              │
│          ▼                                              │
│  ╭───────────────┐                                      │
│  │3. Strategy    │                                      │
│  │  Selection    │                                      │
│  │  Choose most  │                                      │
│  │  promising    │                                      │
│  │  improvement  │                                      │
│  │  strategy     │                                      │
│  ╰───────┬───────╯                                      │
│          │                                              │
│          ▼                                              │
│  ╭───────────────┐                                      │
│  │4. Application │                                      │
│  │  Apply the    │                                      │
│  │  selected     │                                      │
│  │  improvement  │                                      │
│  │  strategy     │                                      │
│  ╰───────┬───────╯                                      │
│          │                                              │
│          ▼                                              │
│  ╭───────────────┐                                      │
│  │5. Evaluation  │                                      │
│  │  Measure the  │                                      │
│  │  effectiveness│                                      │
│  │  of the       │                                      │
│  │  improvement  │                                      │
│  ╰───────┬───────╯                                      │
│          │                                              │
│          └──────────────────┐                           │
│                             ▼                           │
│  ╭───────────────┐    ╭───────────────┐                 │
│  │7. Emergence   │◄───┤6. Evolution   │                 │
│  │  Monitor for  │    │  Incorporate  │                 │
│  │  emergent     │    │  successful   │                 │
│  │  behaviors    │    │  improvements │                 │
│  │  and novel    │    │  into baseline│                 │
│  │  capabilities │    │  capabilities │                 │
│  ╰───────────────╯    ╰───────────────╯                 │
│                                                         │
└─────────────────────────────────────────────────────────┘
```

### Understanding Meta-Recursive Improvement

Meta-recursive improvement is what allows systems to evolve beyond their initial programming. Here's how each step works:

1. **Self-Observation**: The system monitors its own performance and the state of its context field. It looks for signs of suboptimal responses, inefficient memory usage, or unstable field dynamics.

2. **Analysis**: Based on observations, the system identifies specific areas that could be improved. This might include response quality, memory management, conversation flow, or attractor dynamics.

3. **Strategy Selection**: The system selects the most promising improvement strategy from its repertoire, choosing based on the specific issues identified.

4. **Application**: The selected strategy is applied to modify the system's behavior, responses, or field operations.

5. **Evaluation**: The system measures the effectiveness of the improvement by tracking metrics like response quality, field coherence, and user satisfaction.

6. **Evolution**: Successful improvements become part of the system's baseline capabilities, raising the floor for future performance.

7. **Emergence**: As the system continues to improve itself recursively, new capabilities may emerge that weren't explicitly programmed, such as more sophisticated reasoning or domain adaptation.

### Real-World Example

In our example conversations, we can see meta-recursive improvement when:

1. The chatbot notices its responses about attractors could be more detailed
2. It chooses the "response_quality_enhancement" strategy
3. It adds new, more sophisticated responses about attractors to its repertoire
4. On subsequent questions about attractors, it provides richer, more nuanced answers
5. Over time, this improvement compounds as the chatbot continuously refines its understanding and explanations

This demonstrates how context engineering systems can grow beyond their initial capabilities through recursive self-improvement, ultimately developing emergent behaviors not explicitly programmed.
