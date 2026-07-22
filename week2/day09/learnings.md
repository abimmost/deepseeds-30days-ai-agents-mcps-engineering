### This is Day 09 of the challenge, second day of Week 2.

> Task of the Day: Learn about the Microsoft's Agent Framework `AutoGen` and build a _coder and critic_ agent system.

The first thing I experienced this day was a difficulty; the difficulty of finding the correct package to use.
The OG package by Microsoft is called `AutoGen`. Then there is a fork of **AutoGen** called `AG2`. Then, there is the ultimate microsoft agent development framework called `Microsoft Agent Framework`.
I eliminated the last one and had a debate to pick which of the first two I should use. So I visited both their repos and found out that AutoGen was no longer receiving feature updates, just maintainence whereas AG2 had both going for it. Plus, it also had the methods I was going to need to do the day's task, so I chose it.

> Everything went smoothly from there.

**AutoGen** treats agents as conversable entities; agents can exchange messages and instructions among themselves in a manner almost resembling a loop, giving it a non-sequential nature, making its behaviour different from typical workflows.
It uses a `ConversableAgent` object to define it's agents. Key components of this object include:

- `name: str` which is the name assigned to the agent
- `system_prompt: str` which describes the role of the agent and its behaviour
- `llm_config: dict` which holds the configuration of the llm to be used for the agent
- `is_termination_msg: bool` which takes a function that returns a boolean value to tell the agent if the message signifies a task has been completed
- `human_input_mode: bool` which when set to `True`, the agents ask for user permission before performing tasks.

Then to run all this, the `.initiate_chat()` method is used on one of the agents and passed `recipient: ConversableAgent`, which is the other agent that will be on the loop and `message: str` which is the starting message that will be passed to the agent.

My next goal for this day is to configure and add the GEMINI API to this system and see how it performs and also test out other things.

This was Day 09. Unto the next. Godspeed!
