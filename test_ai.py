import os
import time
from dotenv import load_dotenv
from google import genai

load_dotenv()

client = genai.Client(api_key=os.environ.get("GEMINI_API_KEY"))

for attempt in range(3):

    try:
        response = client.models.generate_content(
            model="gemini-3.5-flash-lite",
            contents="Explain K-Means clustering in 3 simple bullet points for a college student."
        )

        print("\nGemini response:\n")
        print(response.text)
        break

    except Exception as e:

        print(f"\nAttempt {attempt + 1} failed:")
        print(e)

        if attempt < 2:
            print("Retrying in 5 seconds...")
            time.sleep(5)
        else:
            print("All attempts failed.")
