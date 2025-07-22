import os
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")

async def translate_to_official_speech(text: str) -> str:
    client = openai.OpenAI()

    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {
              "role": "system",
              "content": (
                "You are a workplace communication assistant. Your task is to rephrase informal, rude, emotional, or chaotic speech into clear, professional business language. "
                "Avoid greetings (like 'Dear...'), closings (like 'Best regards'), and placeholders (like '[Your Name]'). Just rewrite the core message as if it were said by a competent and polite employee. "
                "Always keep the output in the same language as the input. Do not translate or change the language."
              )
            },
            {
              "role": "user",
              "content": (
                f"Here is a raw message:\n{text}\n\n"
                "Rewrite this as a professional internal message — formal, constructive, and neutral in tone. "
                "If the original is aggressive or messy, clean it up but keep the intent. "
                "No need to add artificial structure like greetings or signatures — just the message body."
              )
            }
        ],
        temperature=0.3,
    )

    return response.choices[0].message.content.strip()