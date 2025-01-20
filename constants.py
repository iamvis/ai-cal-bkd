# from dotenv import load_dotenv
# import os
# load_dotenv()



# SERVER_URL = 'localhost'
# PORT = '8900'
# ENV='dev'
# GEMINI_API_KEY= os.getenv('GEMINI_API_KEY')



from dotenv import load_dotenv
import os

# Load environment variables from a .env file (useful for local development)
load_dotenv()

# Use Render-provided PORT or default to 8900 for local development
SERVER_URL = '0.0.0.0'  # Bind to all available network interfaces for deployment
PORT = os.getenv('PORT', '8900')  # Default to 8900 for local testing

# Load API key securely from environment
GEMINI_API_KEY = os.getenv('GEMINI_API_KEY')

# Print for debugging (optional, remove in production)
print(f"Running on {SERVER_URL}:{PORT}")
print(f"GEMINI_API_KEY Loaded: {'Yes' if GEMINI_API_KEY else 'No'}")
