### This is Day 12.

> Task of the Day: Build and Implement an MCP server to handle complex tasks.

---

This day revolved around three main tools for the MCP server: **A Database Reader tool**, **A Web Search tool** and a **A Python code Sandbox tool**

- For the Database Reader tool, I used `sqlite3` lib to create the database and the tool will then be able to execute `SELECT` statements only, on the database, for security.
- For the Web Search tool, I used Tavily and the `TavilyClient` object it provides to perform the search from a query that will be passed by the agent given access to the MCP.
- For the Python Code Sandbox, I used typical python libs for managing environments which include `os`,`sys`,`subprocess` and a `tempfile` lib to create and store the code passed from the MCP client.

I learned and got to understand the following today:

- sqlite3(much like pyscopg for PostgreSQL) requires a connector. This connector may be a file, for sqlite in this case, or a connection url for a remote DB.
- a method called `cursor`, I'll say is the navigator used for a sqlite DB
- revision for methods I had seen before: `.startswith()`, `.strip()`, `.upper()`
- list comprehension provided by python makes a lot easier and helps to loop and assign on the same line. Emphasis on this gave a lot of clarity.
- the `.get()` method used on dictionaries is a gamechanger as it doesn't return an error if the key doesn't exist, and can also be passed a default arg in case the key isn't found, which makes the code easier to look at and less bothersome to run
- `.execute(query: str)` method used on the `cursor` object to run a query
- the `zip()` function maos two similar objects on a 1:1 relation
- `json.dumps()` is used when converting a JSON or dict obj to a string. The `dumps` actually stands for **dump s** where **s** stands for _string_. The JSON or dict obj is passed to the function and then an `indent: int` can also be passed to tell the function to add line breaks or spaces before the line(paragraphing), which is known as _pretty printing_

Today touched on previously studied concepts so I barely had any challenges. Now all that remains is running it on an actual LLM and building my own MCP client with, I believe Langchain, to have more control over the execution and monitor it closely.

This was Day 12. Unto the next. Godspeed!
