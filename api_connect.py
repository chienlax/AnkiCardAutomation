import google.generativeai as genai
import os

def setup_gemini_api():
    """
    Sets up the Gemini API using the API key from environment variables.

    Returns:
        genai.GenerativeModel: The initialized Gemini Pro model, or None if setup fails.
    """
    try:
        # 1. Get API key from environment variable (recommended)
        api_key = os.environ.get("GOOGLE_API_KEY")  # Make sure you set this!

        if not api_key:
            print("Error: GOOGLE_API_KEY environment variable not set.")
            print("Please follow the setup instructions to set your API key.")
            return None

        # 2. Configure Gemini API with the API key
        genai.configure(api_key=api_key)

        # 3. Initialize the Gemini Pro model (or your desired model)
        model = genai.GenerativeModel('models/gemini-2.0-flash-thinking-exp')

        print("Gemini API setup successful!")
        return model

    except Exception as e:
        print(f"Error setting up Gemini API: {e}")
        return None

def test_gemini_connection(model):
    """
    Tests the connection to the Gemini API with a simple prompt.

    Args:
        model: The initialized Gemini model from setup_gemini_api().
    """
    if not model:
        print("Gemini model not initialized. Cannot test connection.")
        return

    try:
        # Simple test prompt
        response = model.generate_content("Hello Gemini, are you there?")
        print("\n--- Gemini API Test Response ---")
        print(response.text)
        print("--- End of Test Response ---")
        print("\nGemini API connection test successful!")

    except Exception as e:
        print(f"Error testing Gemini connection: {e}")


if __name__ == "__main__":
    print("Setting up Gemini API...")
    gemini_model = setup_gemini_api()

    if gemini_model:
        print("\nTesting Gemini API connection...")
        test_gemini_connection(gemini_model)
    else:
        print("\nGemini API setup failed. Please check the errors above.")