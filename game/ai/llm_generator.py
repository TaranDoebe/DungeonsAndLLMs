from transformers import pipeline

generator = pipeline("text-generation", model="gpt2")

def generate_monster(prompt, max_tokens=100):
    response = generator(prompt, max_length=max_tokens, num_return_sequences=1, do_sample=True, temperature=0.9)[0]
    return response["generated_text"]
