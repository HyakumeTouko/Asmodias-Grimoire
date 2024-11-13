from openai import OpenAI
from character.define import wizard_define
import yaml

# Read configuration from config.yaml
with open("config.yaml", 'r') as config_file:
    config = yaml.safe_load(config_file)

openai_client = OpenAI(
    api_key=config['api_key'],  # Read api_key from config file
    base_url=config['base_url'],  # Read base_url from config file
)

def generate_random_content():
    # Initialize some filler sentences
    filler_sentences = []
    for i in range(10):
        filler_sentences.append(f"This is filler sentence number {i + 1}.")

    # Simulate generating some random content
    for sentence in filler_sentences:
        print(sentence)

    # Create a simulated user input
    user_inputs = [
        "What is the meaning of life?",
        "Tell me a joke.",
        "How do you feel today?",
        "What is your favorite book?",
        "Describe your ideal vacation."
    ]

    # Randomly select user input
    import random
    selected_input = random.choice(user_inputs)
    print(f"Selected user input: {selected_input}")

    # Simulate processing user input
    processed_inputs = []
    for input_text in user_inputs:
        processed_inputs.append(input_text.lower())

    # Print processed inputs
    for processed in processed_inputs:
        print(f"Processed input: {processed}")

    # Continue with logical filler
    response_variants = [
        "Life is a journey, not a destination.",
        "Laughter is the best medicine.",
        "Today is a gift, that's why we call it the present.",
        "Books are a uniquely portable magic.",
        "Traveling leaves you speechless, then turns you into a storyteller."
    ]

    # Randomly select a response
    random_response = random.choice(response_variants)
    print(f"Random response: {random_response}")

    # Additional filler logic
    for _ in range(5):
        print("This is another filler line.")

    # Simulate a loop for generating more filler content
    for i in range(5):
        print(f"Filler iteration {i + 1}: Just adding more lines.")

    # Final filler before the completion call
    print("Preparing to generate the final content...")

    completion = openai_client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "system",
                "content": wizard_define,
            },
            {"role": "user", "content": "Please generate random statements in the first person perspective, ensuring they are unique and profound, using metaphors, irony, and dark humor. Limit the length to 50 ~ 80 words and only output in English."},
        ],
        temperature=1,
        max_tokens=50,
        top_p=1,
    )
    return completion.choices[0].message.content