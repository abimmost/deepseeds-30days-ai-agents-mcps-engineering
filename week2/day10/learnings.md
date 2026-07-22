### This is Day 10.

> Task of the Day: Apply Checkpointing, Time Travel and Human-In-The-Loop interruption for LangGraph Agents.

Specific tools and aspects of langgraph were explored in the code to achieve today's goal.

## Core Concepts Explored

- **Checkpointing** in langgraph is storing the graph's state, much like a DB using specific ID's to access the state and particular points along the state. For this, each state needs a unique `state_id` which was generated using `uuid.uuid4()`. Then, saved to langgraph's built-in state-saver, `MemorySaver()` which is passed to a variable. This variable is then passed to the agent system when it is being compiled/initialised.
- **Time-travel** in langgraph deals with accessing a saved state and either Replaying (`get_state_history()`) it or Branching (`update_state()`) it from a particular point.
  - With **Replaying**, the graph starts from the specific chosen point and repeats the same steps that were carried out and saved to the checkpointer during the graph's execution. This helps with debugging to find errors or problematic logic in the graph or code.
  - With **Branching**, the graph is made to take a different path of execution from the chosen point. This could come after a Replay that showed an error that occurred in the graph. The graph can then be branched from the point before where the issue started.
- **Human-In-The-Loop interruption** involves the `interrupt()` method that stops the graph mid-execution and asks for input from the user. The graph would only continue execution once the user provides their input or feedback.

---

## Technical Insights Learned from Code Implementation

Other than these three main aspects, I learned a lot while writing the code. After all the nodes and edges are added to the `StateGraph` (which is passed the model that contains the necessary arguments/context of the graph) using `add_node()` and `add_edge()` respectively and the graph is then compiled using `compile()` and the checkpointer variable is passed to it, I got into the main function and learned the following:

- `__name__` is a built-in variable that takes a value depending on how the code is being run. If the file itself is ran (`python agentgraph.py`) then the `__name__ == "__main__"` but if it is run as a module or just a function from it is borrowed in another file, then `__name__ = "agentgraph"`. So using the condition `if __name__ == "__main__"` ensures that that part of the code runs only when necessary and also helps to depict the main part of the code.
- `stream()` method applied to a graph just initializes the graph and returns a python collection of the various steps or events the graph is going to take. It can be passed the values of the StateGraph that the graph needs, the `state_id`, and a `stream_mode="values"` param that tells it to output the graph's content, not in a single turn, but every time a node executes or an action is taken.
- A `for` loop then loops through the collection of events and they execute.
- `get_state()` method gets a particular state, given the `thread_id` (`state_id`) is passed.
- A `.next` method applied to this gotten state provides the node that is going to be executed next.
- A langgraph type, `Command`, that allows for dynamically managing/modifying data updates and also routing the next step within a node.

---

## Challenges Faced

My only challenge this day was configuring the LLM that all this would run on.
Also, per naming convention in langgraph, _state_id_ is referred to as `thread_id`

---

This was Day 10. Unto the next. Godspeed!
