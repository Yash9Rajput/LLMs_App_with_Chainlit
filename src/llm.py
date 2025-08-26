#from openai import OpenAI

#from transformers import pipeline

from llama_cpp import Llama
#from src.prompt import system_instruction

#client = OpenAI()

# generator = pipeline(
#     "text-generation",
#     model=r"C:\Users\asus\Documents\LLMs_App_with_Chainlit\models\mistral-7b-instruct-v0.2.Q4_K_M.gguf"
# )

llm = Llama(
    model_path="D:/models/mistral/mistral-7b-instruct-v0.2.Q4_K_M.gguf",
    n_ctx=4096,   # context window
    n_threads=8   # adjust based on your CPU cores
)

# messages = [
#     {"role": "system", "content":system_instruction}
# ]

# def ask_order(message , model = "gpt-3.5-turbo" , temperature = 0):
#     response = client.chat.completions.create(
#         model = model,
#         messages = messages,
#         temperature = temperature
#     )

#     return response.choices[0].message.content



# def ask_order(message, temperature=0.7, max_tokens=256):
#     # Combine messages into one prompt
#     prompt = ""
#     for m in message:
#         if m["role"] == "system":
#             prompt += f"System: {m['content']}\n"
#         elif m["role"] == "user":
#             prompt += f"User: {m['content']}\n"
#         elif m["role"] == "assistant":
#             prompt += f"Assistant: {m['content']}\n"

#     prompt += "Assistant:"

#     # Generate reply from local Hugging Face model
#     response = generator(
#         prompt,
#         max_length=len(prompt.split()) + max_tokens,
#         temperature=temperature,
#         do_sample=True
#     )[0]["generated_text"]

#     # Only return text after the last "Assistant:"
#     reply = response.split("Assistant:")[-1].strip()
#     return reply


def ask_order(prompt: str):
    output = llm(prompt, max_tokens=512, stop=["User:", "System:"])
    return output["choices"][0]["text"].strip()