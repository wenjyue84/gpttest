import openai

openai.api_key = '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'

def generate_text(prompt, max_tokens=100):
    """
    Generate text using OpenAI's GPT-3 engine.

    Parameters:
    prompt (str): The text prompt to base the generation on.
    max_tokens (int): The maximum length of the generated text.

    Returns:
    str: The generated text.
    """
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=max_tokens
    )
    return response.choices[0].text.strip()

if __name__ == "__main__":
    user_prompt = input("Enter a prompt: ")
    generated_text = generate_text(user_prompt)
    print(generated_text)
