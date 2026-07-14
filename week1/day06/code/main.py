import uuid
import time
import chromadb

class EpisodicMemoryRetriever:
    def __init__(self, db_path="./mem_store"):
        self.client = chromadb.PersistentClient(path=db_path)
        self.collection = self.client.get_or_create_collection("episodic_mem")

    def save_interaction(self, session_id: str, user_text: str, agent_text: str, category: str = "general") -> None:
        """Formats and saves a conversation turn"""
        document_text = f"User: {user_text} | Agent: {agent_text}"

        memory_id = str(uuid.uuid4())        
        metadata = {
            "session_id": session_id,
            "timestamp": time.time(),
            "category": category
        }

        self.collection.add(
            documents=[document_text],
            metadatas=[metadata],
            ids=[memory_id]
        )
        print(f"Saved memory {memory_id[:6]}...")

    def retrieve_interaction(self, user_query: str) -> list:
        """Retrieves related available interactions from the database"""
        results = self.collection.query(
            query_texts=[user_query],
            n_results=2
        )

        if not results['documents'] or not results['documents'][0]:
            return ["No related past conversations found"]
        
        return results['documents'][0]
    
    def generate_agent_prompt(self, user_message: str) -> str:
        """Creating the system prompt for the agent"""
        past_interactions = self.retrieve_interaction(user_message)

        prompt = f"""
Use the past conversations to personalize your tone and grasp details about the user(if provided): {past_interactions}

Then, output your response in format:

Current user message: {user_message}
Agent response:
"""
        return prompt
    

agent_mem = EpisodicMemoryRetriever()

agent_mem.save_interaction(
    session_id="user_john_101",
    user_text="My order #54321 was shattered when it arrived.",
    agent_text="I am so sorry to hear that! I have issued a replacement shipment for order #54321.",
    category="damaged_item"
)

new_user_message = "What's the status of my replacement order?"

prompt_to_send_to_llm = agent_mem.generate_agent_prompt(new_user_message)

print(f"Prompt: {prompt_to_send_to_llm}")