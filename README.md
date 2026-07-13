# 🤖 Q&A Chatbot with Groq & LangChain

A simple and interactive AI-powered Q&A chatbot built using **Streamlit**, **LangChain**, and **Groq LLMs**. The application allows users to ask questions, choose different Groq models, and customize the response using temperature and token settings.

---

## 🚀 Features

* 💬 Interactive chatbot interface using Streamlit
* ⚡ Fast responses powered by Groq LLMs
* 🧠 Prompt engineering with LangChain
* 🎛️ Adjustable temperature and maximum token settings
* 🔄 Multiple Groq model selection
* 🔐 Secure API key input from the sidebar
* 📊 LangSmith tracing support for debugging and monitoring

---

## 🛠️ Tech Stack

* Python
* Streamlit
* LangChain
* Groq API
* LangSmith
* python-dotenv

---

## 📂 Project Structure

```text
Q-A-Chatbot-Groq/
│
├── app.py                # Main Streamlit application
├── requirements.txt      # Project dependencies
├── .env                  # Environment variables (not uploaded)
├── .gitignore
├── README.md
└── venv/                 # Virtual environment (ignored)
```

---

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/your-username/Q-A-Chatbot-Groq.git
cd Q-A-Chatbot-Groq
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

### 3. Activate the virtual environment

**Windows**

```bash
venv\Scripts\activate
```

**Linux / macOS**

```bash
source venv/bin/activate
```

### 4. Install the required packages

```bash
pip install -r requirements.txt
```

---

## 🔑 Environment Variables

Create a `.env` file in the project root.

```env
GROQ_API_KEY=your_groq_api_key
LANGCHAIN_API_KEY=your_langsmith_api_key
```

---

## ▶️ Run the Application

```bash
streamlit run app.py
```

The application will open automatically in your browser.

---

## 🖥️ How to Use

1. Launch the application.
2. Enter your Groq API key in the sidebar.
3. Select a Groq language model.
4. Adjust the temperature and maximum token settings.
5. Type your question.
6. Receive an AI-generated response.

---

## 📸 Demo

```
<p align="center">
  <img src="readme_images\chatbot_demo.png" alt="Description" width="500">
</p>

```

---

## 📚 Concepts Used

* Prompt Templates
* LangChain Expression Language (LCEL)
* Output Parsers
* Large Language Models (LLMs)
* Streamlit User Interface
* Environment Variable Management
* LangSmith Tracing

---

## 🔮 Future Improvements

* Conversational memory
* Chat history
* Streaming responses
* PDF Question Answering (RAG)
* Website Question Answering
* Multiple LLM provider support (OpenAI, Gemini, Groq)
* File upload support

---

## 🤝 Contributing

Contributions are welcome. Feel free to fork the repository, create a feature branch, and submit a pull request.

---

## 📄 License

This project is licensed under the MIT License.

---

## 👨‍💻 Author

**Amrit Raj**

* M.Tech in Robotics & AI, IIT Bhubaneswar
* Passionate about Artificial Intelligence, Generative AI, Machine Learning, and Robotics.

If you found this project helpful, consider giving it a ⭐ on GitHub.
