from groq import Groq
from config import GROQ_API_KEY, LLM_MODEL

_client = None


def _get_client():
    global _client
    if _client is None:
        if not GROQ_API_KEY:
            raise RuntimeError(
                "GROQ_API_KEY is not set. Copy .env.example to .env and add your key."
            )
        _client = Groq(api_key=GROQ_API_KEY)
    return _client


def generate_response(query, retrieved_chunks):
    if not retrieved_chunks:
        return (
            "I couldn't find anything relevant in the loaded uga doc. "
            "Try rephrasing your question — or check that your ingestion pipeline is working."
        )

    context = ""

    for chunk in retrieved_chunks:
        context += (
            f"Game: {chunk['game']}\n"
            f"Rule: {chunk['text']}\n\n"
        )

    system_prompt = """
You are UGA BOT.

Answer questions using ONLY the provided uga doc context.

If the answer cannot be found in the context, say:
"I couldn't find that information in the loaded Rag documents."

Do not use outside knowledge.
Do not make assumptions.
Always mention which doc the answer comes from when possible.
"""

    user_prompt = f"""
Context:

{context}

Question:
{query}
"""

    client = _get_client()
    response = client.chat.completions.create(
        model=LLM_MODEL,
        messages=[
            {
                "role": "system",
                "content": system_prompt
            },
            {
                "role": "user",
                "content": user_prompt
            }
        ]
    )

    return response.choices[0].message.content