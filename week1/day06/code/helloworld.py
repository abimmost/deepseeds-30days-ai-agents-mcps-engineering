import chromadb # the chromadb client itself

# libraries to help create the metadata
import uuid
import time

# Initialising the chromadb client and the path to save to
client = chromadb.PersistentClient(path="./helloworld_mem")

# Creating the collection(which is like a database table) using the initialised client
collection = client.get_or_create_collection(name="episodic_history")

# creation of the metadata to be saved
return_mem_id = str(uuid.uuid4())
return_mem_id1 = str(uuid.uuid4())
cash_mem_id = str(uuid.uuid4())

document_text = "User: 'Can I return a damaged box?' | Agent: 'Yes, under our 14-day policy, damaged arrivals qualify for a full refund.'"
document_text1 = "User: 'Can I return a undamaged box?' | Agent: 'No, under our 14-day policy, boxes in good condition remain with the client.'"
document_text2 = "User: 'Can I pay with cash?' | Agent: 'Yes, under company policy, cash payments are allowed during transactions.'"

metadata = {
    "session_id": "session_id_1234",
    "timestamp": time.time(),
    "category": "returns"
}
metadata1 = {
    "session_id": "session_id_1233",
    "timestamp": time.time(),
    "category": "payment"
}
metadata2 = {
    "session_id": "session_id_1235",
    "timestamp": time.time(),
    "category": "returns"
}



# Adding everything to the collection(table) we created
collection.add(
    documents=[document_text, document_text1, document_text2],
    metadatas=[metadata, metadata1, metadata2],
    ids=[return_mem_id, return_mem_id1, cash_mem_id]
)

print("Memory successfully stored!")

# Now we test the retrieval by querying the database
user_query = "Whay is your policy on broken goods?"

results = collection.query(
    query_texts=[user_query],
    n_results=1
)

print(f"Related answer: {results['documents'][0][0]}")
