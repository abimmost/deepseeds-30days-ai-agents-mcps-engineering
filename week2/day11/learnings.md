### This is Day 11.

> Task of the Day: Study Agent Planning Strategies(Plan-and-Execute, Hierachichal, LATS - Language Agent Tree Search) and implement the Plan-and-Execute strategy for a complex research task

---

### What each strategy means:

- Plan-and-Execute: The agents generates a complete plan of the objective and then executes step-by-step
- Hierachical: A planner agent takes the main objective, breaks it down into sub-tasks and assigns it to multiple worker agents.
- LATS - Language Agent Tree Search: The agent explores multiple plans and picks the best

In implementing the Plan-and-Execute Strategy, I used `Langgraph`.
Today was just a revision of concepts and I got to strenghthen my Langgraph abilities.

But here are some things that still got me invested on this day:

- I got to actually plan and reason how to write complex code and build agent workflows.
- Used Pydantic `BaseModel` models to create templates for the tasks to be stored and their attributes
- Actually added an LLM this time(gemini) using langchain_google_genai library alongside the `ChatGoogleGenerativeAI` type for LLM definition.
- Used the `.with_structured_output()` method on the defined LLM and passed the model holding all the tasks(which I defined as `Plan`)` to ensure the LLM returns data in the format suggested by the model.

My only challenge this day was not having the time to actually program the code/workflow to carry out specific tasks and optimize it for better performance. Which led me not to run it to test it's performance. I'll get that when next I'm back here.

This was Day 11. Unto the next. Godspeed!
