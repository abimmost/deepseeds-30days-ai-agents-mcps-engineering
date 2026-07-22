### This is Day 15.

> Task of the Day: Study and Build with the Google ADK and compare to other Agent Development Frameworks.

Day 15 involved studying tool definition, session state management and deployment for the Google ADK framework and agents built with it. The python library is `google-adk`.

Setting up an agent in python using Google ADK first requires building it using the path structure of a python module; a dedicated folder with the agent's name, an `__init__.py` and `agent.py`. Then for the code that is the core of the agent, written in `agent.py`:

- Agents in Google ADK are instances of its `Agent` object and this object can be passed parameters to configure it like their name, instruction, model and tools.
- It uses a **Runner**(`InMemoryRunner`) to initialize and begin execution of the workflow and also manage context between agents.
- Concerning tool definition, the ADK comes with some prebuilt tools like `google_search` but others can be created as functions and then passed as tools, like in other frameworks.
- `InMemorySaver`, the runner for the agents uses a `thread_id` to keep track of the turns and chats to efficiently manage and pass context, which is great for session management, but only in testing. In production, databases are preferred.

Agents and workflows can be tested using the `adk web` command which opens up a uvicorn server on a local port where the developer can interact with his creation through a UI.
The command then used to deploy the agent is `agent-cli`, which involves scaffloding before deployment.
In production, GCP and Vertex AI are the best options for deployment and require configuration before they can go live.

Passing built-in tools and user-defined tools in the same Agent object can lead to errors so we wrap user-defined tools inside a `AgentTool` object.

---

#### Drawbacks

- I didn't deploy the agent on either GCP or Vertex AI and I didn't know how to configure the agents to work together with them.

I hope to change this in the future.
This was Day 15. Unto the next. Godspeed!
