### This is Day 04 of the challenge and today we'll be learning about Langgraph, the python agent orchestrator by langchain.

We'll begin with simple concepts like State, Nodes and Edges which are the core of Langgraph.

- State serves as the memory of the graph. It is a dictionary or pydantic model that holds the activity throughout the flow/execution of a graph
- Nodes are points(on the graph) or fuctions that perform a specific action. Each Node reads the State, performs it's task and then returns an updated state.
- Edges are what connect nodes to each other. They can be direct or conditional. This is what helps Nodes to pass the State between each other.

For today's mini task, I'll be building a Simple Research Agent graph which flows as follows: search -> summarize -> fact-check -> respond

Thus, 4 nodes. A Node in Langgraph is just a function. This function, for example, the search function will contain the logic to read the query(from the State), pass to the LLM to perform the search, then save the LLM search results to the State once more. Not every Node needs LLM interaction.

A workflow(graph) is initialised with a Stategraph object from the Langgraph.graph module, which receives the State dict or model as argument.
`workflow = Stategraph(ResearchState)`

Then, various methods are applied to it to create the flow like

- add_node, which creates a node by taking a function and assigns it a name
- add_edge, which takes the names of two nodes as argument, which forms a direct link between them
- START/END, which are used as the first arg, at the first edge, and used as the last arg on the last edge respectively.
- add_conditional_edge, which takes the name of a node, and then a decision/route funtion that uses a condition to check which node to proceed to, and then moves the workflow in that direction.

compile() to package the workflow for execution

So that's pretty much it for today. Make sure to visit the [code](code/main.py).
Unto the next. Godspeed!
