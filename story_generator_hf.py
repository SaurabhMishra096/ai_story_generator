from transformers import AutoTokenizer, AutoModelForCausalLM, pipeline
import re

model_name = "distilgpt2"

tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name)

generator = pipeline('text-generation', model=model, tokenizer=tokenizer)

def clean_story(text, prompt):
    """Clean up and extract only the generated story after the prompt."""
    if text.startswith(prompt):
        text = text[len(prompt):]
    lines = text.strip().splitlines()
    story_lines = [line.strip("-• ") for line in lines if line.strip()]
    return " ".join(story_lines).strip()

def format_prompt(user_msg):
    """Prompt format for story generation."""
    return f"Write a detailed and imaginative short story based on the following idea:\n\n{user_msg}\n\nStory:\n"

def generate_story(prompt, max_new_tokens=300, temperature=0.8):
    formatted_prompt = format_prompt(prompt)
    result = generator(
        formatted_prompt,
        max_new_tokens=max_new_tokens,
        num_return_sequences=1,
        temperature=temperature,
        top_k=50,
        top_p=0.95,
        return_full_text=True
    )
    raw_text = result[0]['generated_text']
    return clean_story(raw_text, formatted_prompt)
