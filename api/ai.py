from dotenv import load_dotenv
import os

# Load the environment variables from the .env file
load_dotenv()

# Get the API key from the environment variable
api_key = os.getenv('MY_API_KEY')

# Print the API key to the console
print(f"My API Key is: {api_key}")