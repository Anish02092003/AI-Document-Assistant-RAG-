import os

key = os.getenv("OPENAI_API_KEY")
print("KEY FOUND:", key is not None)
print("KEY VALUE:", key)
