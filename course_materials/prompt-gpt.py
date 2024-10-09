import openai
import jsonlines
from openai import OpenAI
import openai


api_key = "###"
client = OpenAI(api_key=api_key)
def read_jsonl_file(file_path):
    """Reads a JSONL file and returns the content as a list of dictionaries."""
    data = []
    with jsonlines.open(file_path) as reader:
        for obj in reader:
            data.append(obj)
    return data

def estimate_token_count(messages):
    """Estimates the number of tokens in the conversation history."""
    # Rough estimate: 1 token ≈ 4 characters
    total_tokens = 0
    for message in messages:
        total_tokens += len(message["content"]) // 4
    return total_tokens

def prune_conversation_history(conversation_history, max_tokens=100000):
    """Prunes the conversation history if it exceeds the max token limit."""
    while estimate_token_count(conversation_history) > max_tokens:
        print("attempt to prune...")
        # Remove the oldest user message and assistant response
        conversation_history = conversation_history[2:]  # Removing 2 messages at a time (user and assistant)
    return conversation_history

def send_to_gpt4(conversation_history, data, model="gpt-4o"):
    """Feeds the conversation history and data to GPT-4 and returns the response."""
    try:
        # Send the data to GPT-4 using the conversation history and client completion instance
        response = client.chat.completions.create(
            model=model,
            messages=conversation_history + [
                {"role": "assistant", "content": str(data)}  # Feed the data here
            ],
        )
        return response.choices[0].message.content
        
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

def add_to_conversation(conversation_history, user_input, assistant_response):
    """Adds user input and GPT-4 response to the conversation history."""
    # Add user input
    conversation_history.append({"role": "user", "content": user_input})
    # Add assistant response
    conversation_history.append({"role": "assistant", "content": assistant_response})
    
    return conversation_history

if __name__ == "__main__":
    # Path to your JSONL file
    file_path = 'bitcoin_client_data.jsonl'
    
    # Load the JSONL data once
    jsonl_data = read_jsonl_file(file_path)

    # Initialize the conversation history with the system message
    conversation_history = [
        {"role": "system", "content": "You are a Blockchain programming teacher assisting with developing a bitcoin client using the provided data."}
    ]

    # Welcome message for the chatbot
    print("Welcome to the Bitcoin Client Development Chatbot! Type your queries or 'exit' to quit.")
    
    while True:
        # Get user input for each interaction
        user_input = input("\nYou: ")

        # Check if the user wants to exit
        if user_input.lower() == 'exit':
            print("Goodbye!")
            break

        # Prune the conversation history to ensure it doesn't exceed the token limit
        conversation_history = prune_conversation_history(conversation_history)

        # Send the conversation history and new user input along with the JSONL data to GPT-4
        gpt4_response = send_to_gpt4(conversation_history, jsonl_data)
        
        # Print GPT-4's response
        if gpt4_response:
            print("\nGPT-4 Response:\n", gpt4_response)

            # Update the conversation history with the user input and GPT-4's response
            conversation_history = add_to_conversation(conversation_history, user_input, gpt4_response)