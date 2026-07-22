### This is Day 16.

> Task of the Day: Study the Vercel AI SDK and use it to render components for agents.

The Vercel AI SDK is a TypeScript/JS toolkit that provides hooks and streaming capabilities that help an agent return UI components based on a user's goals.

There's no native Python package, but using a python backend like FastAPI, we can communicate to this language-foreign lib through emitted SSEs(Single-Server Events) that obey Vercel Data Stream Protocol.

Communication is done mainly through SSEs where the client(JS frontend) intercepted through the `useChat` hook that captures the agent's output in real time from the server(FastAPI) backend like its response state, tool calls and response output.
The Vercel AI SDK then uses that to render a component configured by the dev when a particular state or output is perceived.

The agent also passes its text responses to `useChat()` in chunks, through the backend, immediately as it gets them. This gives a streaming expereience on the frontend and doesn't wait for the entire response to be generated first.

> The data passed over these SSEs are sent and received as JSON objects.

It uses prefixes like `0:{...}` for tokens, `9:{...}` for tool calls and `a:{...}` for results.

---

#### Darwbacks

- I saw and used SSEs, intentionally, for my first time today so it was really an issue to understand it.
  But SSEs are just requests made using HTTP/1.1 or HTTP/2 protocol and they are the most common form of web communication, which I would have used many times before today. It is recommended communication protocol for platforms that deal with real-time data and interaction.

- A UI dependent on Vercel AI SDK was not implemented due to a deficiency in TypeScript. Only a FastAPI backend was implemented.

- My original intention was to build and serve a Langgraph workflow but I ended up using Langchain instead.
  I hope to change this in the future.

This was Day 16. Unto the next. Godspeed!
