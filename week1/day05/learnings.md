### This is Day 05 of the challenge and today we learned how to create and serve tools using the MCP architecture.

I've always wondered how MCPs worked BTS. I'm glad that I got to learn about it and get to know the core elements it constitutes while also creating [mine](./code/helloworld.py) for the first time.

See, the MCP architecture was developed by Anthropic as a means to pass tools to their various models. Instead of APIs or hardcoding the tools into the model's code, the MCP is a game-changer because it uses a client-server mechanism where the MCP module runs in the background, creating a server so the LLM can use its tools anytime.

The package concerned with MCP in python is `mcp`, the core module being `FastMCP`. An instance of `FastMCP` is then used to construct the mcp server and its tools.

I learned how to make proper use of this package and its module to build my own personal [local MCP](code/main.py) which exposes my user path to a configured LLM or coding agent (Antigravity, Claude Desktop) when they use the configured tools.

> One thing in common with all these tools, whether in agent development frameworks or in regular AI tool packages, is that tools are usually just functions.

But `mcp` wasn't the only thing this day had in store for me... The `os` library also had something to prove. This is because for the day's main task, I had to deal with windows files and folders, thus I needed a library that communicated seamlessly with the system. `os` is a beast at this.

The main string visible throughout is `os.path`, and I used methods like:

- **`.abspath()`** to define a path
- **`.dirname()`** to save a path
- **`.commonpath()`** to compare paths to see if they are related
- **`.join()`** to merge two separate paths or filenames into one
- **`os.path.expanduser()`** which lets you grab a path using a shortened version
- **`os.listdir()`** to get the contents of a folder/directory

So `os` definitely had something... a lot to say. That's day 05.

I plan to configure a Gemini LLM to use this to give me a better understanding of how the MCP server is utilized.

Day 05 was crazy indeed. Onto the next. Godspeed! 🏁
