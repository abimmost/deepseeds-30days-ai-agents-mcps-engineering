### This is Day 08 of the challenge, officially commencing Week 2.

> Task of the Day: Learn **Crewai** fundamentals and build a content creation and research agent workflow.

This day was enjoyably smooth. **Crewai** is so easy to learn.
Like many other agenr frameworks, Crewai uses classes and objects to create and configure agents. For Day 08, I used:

- **Agent**: which creates an agent object. The key params for this object are the `role: str`(a phrase that resembles a job title), `goal: str`(this will describe its purpose) and `backstory: str`(to give it some context and give it the personality and tone to be used.)
- **Task**: creates a task for an agent. Core params include `description: str`(description of the task), `expected_output: str`(the format in which the Agent should return data after the Task is done) and `agent: list`(which takes the name of the agent that performs the task)
- **Crew**: This is the orchestration layer. The Agents and Tasks created here are passed to `agents: list` and `tasks: list` params respectively, to form the _crew_. Then a `process` param that takes the order in which the flow is executed, in my case, a sequential flow(`Process.sequential`).

There are two other params that appear often, which are `verbose: bool` and `allow_delegation: bool`; the first appears in both **Agent** and **Crew** classes, while the second appears only in **Agent**.

- _verbose_ set to `True` tells the agent to print out its thinking process, while `False` tells it not to.
- _allow_delegation_ set to `True` gives the agent permission to call other agents mid-task execution to ask them for help or in case it needs certain information it can't get. This could wind up causing **infinite loops** if used improperly.

Then, to finally test out the crew or agent workflow, the method `.kickoff()` is used on the object to start it. Inputs can be passed into it using an `input: dict` param.

## Challenges

CrewAI needs an LLM connected to it(preferably OPENAI API) to run. I didn't configure one and thus, my code ran with a multitude of errors, all resulting from the lack of an LLM. I plan to incorprate one in the coming days.

That was Day 08. Unto the next. Godspeed!
