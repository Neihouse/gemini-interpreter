from dotenv import load_dotenv
import os

# Load environment variables from the .env file
load_dotenv()

# Get the API key from an environment variable
api_key = os.getenv('GCP_API_KEY')

# Print a message indicating that the API key has been loaded
print(f"The API key has been loaded: {api_key}")

