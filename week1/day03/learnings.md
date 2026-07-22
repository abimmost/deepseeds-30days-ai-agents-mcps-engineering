### This is Day 3.

OpenAI Agents SDK is easy to use and not as sophisticated as I thought. Experimenting and trying out different things with Agent object and Runner agent orchestrator made me understand so much. But these can't be used alone by themselves as the agents need tools to help them to call other agents(handoff functions). Then, an endless loop to create a conversation environment, in which the messages between the user and agents are also saved to as conversation history and context for the agents.

Ohh but that was just the beginning... Since I couldn't get over my love for the Gemini API and their generous free tier and also coz I'm too broke to get an OpenAI API key(paid btw), I made the questionnable decision to use gemini models in the OPENAI AGENTS SDK. So I encountered errors, aloT. But I also learned so much:

- I first needed a way to manage environment variables so I leanred how to create and manage .env and other sensitive variables and exposed them through a module I created in the root called config. I would then call this config whenever and wherever I want to use those variables

Then I proceeded to code.

- I had to add a model field to all my Agent objects. To do this, I had to initialise a gemini client(with the my gemini api key and the base url which we would route all traffic through) and then pass this client into the configuration for the gemini model.
- I used new modules like asyncio, new objects and methods like AsyncOpenAI, function_tool, set_tracing_disabled etc

The game changer was the state['active_agent'] which is a global variable that takes the name of the agent to be returned after a tool is called. This helped ensure that the Agents actually switched after a tool call.

Most of my errors arose from using wrong object attributes for example, Runner.run_sync was Runner.run before, state["active_agent"].name was once turn_result.last_agents(which kept using the name of the previous agent instead), messages.append(f"...") was once messages.extend. These challenges with attribute methods made me appreciate the importance of intellisense which shows me the description of a function and its parameters and helped me build a more solid foundation in this gemini integration aspect.

Allat just to find out I could have used LiteLLM package to host the tunnel to write the trafiic and then leave my code unchanged. I'll probably do this in the coming few days.
Anyways, it was fun. Unto the next. Godspeed!!
