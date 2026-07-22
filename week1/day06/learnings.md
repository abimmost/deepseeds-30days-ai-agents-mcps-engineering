### This is Day 06 and what a day it was. Today, the task was to learn about the different types of memory agents use and to implement one of those types for an agent. It was hell... but my skills are mad cold so there was no way I was conceding.

The different types of agent memory are: working, episodic, procedural and semantic memory.

- **working memory** entails the context window with the user's immediate prompt
- **episodic memory** entails past prompts and conversation history, usually stored and accessed in a database
- **procedural memory** entails configured skills and function definitions
- **semantic memory** entails text, context or knowledge from external sources like a website or document and are usually accessed through RAG pipelines

> The highlight of the day was to build an episodic memory storage for agents. Because episodic memory requires a vector database, I had to understand first, what a vector database actually does and how to build mine.

- A vector database is a type of data storage that saves entries/data as vector embeddings. A vector embedding is simply the data to be stored which is coverted to a string of numbers, and these numbers retain the meaning of the original data.
- To find data in a vector db, a method called semantic search is used. This type of search involves searching by meaning - the meaning assigned to the data saved as embeddings. So a wrd/query is provided which will then be turned into a vector too. Then the meaning given to this query is compared to the meaning of the other entries in the database.
- The way the search is done is by using a math method called Cosine Similarity, which calculates the angle between two vectors. In this case, the provided query and an entry in the database. The smaller the angle, the better the match. Thus, we say it finds the closest 'n' neighbors, where 'n' is the number of similar matches desired.

I enjoyed the learning part. The coding part on the other hand... Well, we move.
For this, I had to build my own vector database and I had to choose between using `numpy` to build one from the ground-up, or use `chroma_db` library which has methods and logic pre-packaged for this specific task already.

> So I chose `chroma_db`, duh...

Initialising a `chroma_db` vector db first requires a chroma_db client to be created. Within this client, the path(mine is local) to where the database will be stored is passed as `db_path`.
Then a collection/collections using that client.
A collection is like a database table. It has various pre-defined columns but the ones I made use of were `documents`(which holds the text/data to be saved),`metadatas`(which can be configured to have details like timestamp and session_id),and `ids`(which is an id).

> The metadata is essential as keywords like category or type can be passed which strengthen the meaning of that entry.

So like in a regular database table, putting data into each of these 3 in the same instance forms a row. An `ids` is always required, while `documents` and `metadatas` are optional. These are added using a `.add()` method on the `collection` created for the database.
Then to get data or search the database for matches, a `.query()` method is used. The **query** or **word** to be searched is required along with the number of results(**n_results**) you want.
Also, to convert data into embeddings, a tool is used called an **embedding model**. This could be the default model provided by `chroma_db` or a third-party model working through an API or as a local model.

I learned all this through practice in my [hello world](code/helloworld.py) file.

Then I stepped into [the actual task](code/main.py) and it made a joke of me. I wanted to touch on classes and objects in python a bit so I created a class to handle everything about the memory. I'm glad the only thing I had to learn here was the use of the `self` within the function definitions of my class.

> (When an instance of the class(object) is created, the instance is passed to the defined methods as an argument, when that method is called, to make sure that all operations performed belong to that object.)

For my difficulties, I had an issue with conditions involving `not` and then comparisons with `and` and `or`. I had to dry-run the conditions to fully grasp what was going on, but I understood at the end.

I plan to give an LLM or agent access to this memory class and see how it performs.
Crazy day today. Unto the next. Godspeed!
