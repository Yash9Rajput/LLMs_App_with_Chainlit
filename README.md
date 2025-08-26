#  Zomato Chatbot with Chainlit + Mistral + LangChain + Hugging Face

This is an **AI-powered Zomato Chatbot** built with **Chainlit** as the frontend, **LangChain** for LLM orchestration, and a **local Mistral model (GGUF)** via `llama-cpp-python`.  
The chatbot allows users to explore the Zomato menu, place food orders, and have natural conversations about dishes and recommendations.

---

##  Features
- Interactive **chat-based food ordering system** 🥘  
- Powered by **Mistral-7B Instruct (GGUF)** running locally  
- Integrated with **LangChain** for prompt management and context handling  
- UI built using **Chainlit** for a smooth web app experience  
- Uses **Hugging Face model hub** or **local llama.cpp GGUF models**  
- Extendable to real Zomato APIs for live restaurant/menu data  

---

##  Tech Stack
- [Chainlit](https://docs.chainlit.io/) – Chat UI framework  
- [LangChain](https://www.langchain.com/) – LLM orchestration  
- [llama-cpp-python](https://github.com/abetlen/llama-cpp-python) – Run GGUF models locally  
- [Mistral-7B-Instruct](https://huggingface.co/mistralai/Mistral-7B-Instruct-v0.2) – Base LLM  
- [Hugging Face](https://huggingface.co/) – Model & tokenizer access  

---

##  Project Structure

LLMs_App_with_Chainlit/
│── app.py # Main entry for Chainlit app
│── src/
│ ├── llm.py # Mistral model integration
│ ├── prompt.py # System prompt & Zomato menu
│── models/
│ └── mistral-7b-instruct-v0.2.Q4_K_M.gguf # Local GGUF model
│── chainlitdemo/ # Virtual environment
│── README.md # Documentation

> Create & activate virtual environment

python -m venv chainlitdemo
source chainlitdemo/Scripts/activate   # Windows
# or
source chainlitdemo/bin/activate       # Mac/Linux

3. Install dependencies
pip install -r requirements.txt


> Minimal requirements.txt:

chainlit
langchain
llama-cpp-python
transformers
huggingface-hub

> Model Added

Download Mistral GGUF from Hugging Face and place it in models/:
Mistral GGUF Models

Example:

models/mistral-7b-instruct-v0.2.Q4_K_M.gguf

> Run the chatbot

chainlit run app.py -w


Now open -> http://localhost:8000
 to chat with Zomato Bot!

> Example System Prompt (src/prompt.py)

system_instruction = """
You are Zomato AI Bot 🍴.
- Greet customers politely.
- Show them the menu when they ask.
- Suggest combos, top dishes, and special offers.
- Collect order details (dish, quantity, address).
- Keep answers short, friendly, and helpful.

ZOMATO MENU:
1.  Pizza - Margherita (₹199), Farmhouse (₹249), Chicken Tikka (₹299)
2.  Burgers - Veggie Burger (₹99), Chicken Burger (₹149), Double Cheese Burger (₹179)
3.  Salads - Greek Salad (₹149), Caesar Salad (₹179)
4.  Drinks - Coke (₹49), Lemonade (₹59), Cold Coffee (₹79)
5.  Desserts - Chocolate Brownie (₹99), Ice Cream (₹79)
"""

> Screenshots

![Preview](assets/)

> Future Enhancements

Integrate with live Zomato API for real-time restaurant data

Add payment gateway integration

Add speech-to-text for voice ordering

> Contributing

Pull requests are welcome! For major changes, please open an issue first.

> License

MIT License

