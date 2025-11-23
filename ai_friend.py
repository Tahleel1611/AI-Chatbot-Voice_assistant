from transformers import BlenderbotTokenizer, BlenderbotForConditionalGeneration
import time
from typing import Optional

# Load the BlenderBot model and tokenizer
tokenizer = BlenderbotTokenizer.from_pretrained("facebook/blenderbot-400M-distill")
model = BlenderbotForConditionalGeneration.from_pretrained("facebook/blenderbot-400M-distill")

# Conversation history to maintain context
conversation_history = []

def ask_ai_friend(prompt: str, max_retries: int = 3, retry_delay: float = 1.0) -> str:
    """
    Generate AI response using BlenderBot with error handling and retry mechanism.
    
    Args:
        prompt: The user's input message
        max_retries: Maximum number of retry attempts on failure (default: 3)
        retry_delay: Delay in seconds between retries (default: 1.0)
    
    Returns:
        str: AI-generated response or error message
    """
    if not prompt or not prompt.strip():
        return "I didn't catch that. Could you please repeat?"
    
    for attempt in range(max_retries):
        try:
            # Add current prompt to conversation history
            conversation_context = " ".join(conversation_history[-5:])  # Use last 5 exchanges for context
            full_prompt = f"{conversation_context} {prompt}" if conversation_context else prompt
            
            # Tokenize and generate response
            inputs = tokenizer(full_prompt, return_tensors="pt", truncation=True, max_length=128)
            outputs = model.generate(**inputs, max_length=128, num_beams=5, early_stopping=True)
            response = tokenizer.decode(outputs[0], skip_special_tokens=True)
            
            # Update conversation history
            conversation_history.append(prompt)
            conversation_history.append(response)
            
            # Keep history manageable (last 10 exchanges)
            if len(conversation_history) > 20:
                conversation_history.pop(0)
                conversation_history.pop(0)
            
            return response
            
        except RuntimeError as e:
            if "out of memory" in str(e).lower():
                # Clear conversation history to free memory
                conversation_history.clear()
                return "I'm experiencing memory issues. Let's start fresh. What can I help you with?"
            elif attempt < max_retries - 1:
                time.sleep(retry_delay)
                continue
            else:
                return "I'm having trouble processing that right now. Could you try rephrasing?"
        
        except Exception as e:
            if attempt < max_retries - 1:
                time.sleep(retry_delay)
                continue
            else:
                return "I apologize, but I'm experiencing technical difficulties. Please try again later."
    
    return "I'm unable to respond at the moment. Please try again."

def clear_conversation_history() -> None:
    """Clear the conversation history."""
    global conversation_history
    conversation_history.clear()

def get_conversation_history() -> list:
    """Get the current conversation history."""
    return conversation_history.copy()
