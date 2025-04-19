from google import genai

client = genai.Client(api_key="go get your own API###")  # Replace with your actual API key

while True:
    user_prompt = input("What would you like to ask Gemini? (type 'exit' to quit): ")
    
    if user_prompt.lower() in ['exit', 'quit']:
        print("Goodbye!")
        break

    response = client.models.generate_content(
        model="gemini-2.0-flash",
        contents=user_prompt
    )
    
    print(response.text)
