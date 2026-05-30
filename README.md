# 🧠 Context Management with AI Agents

A Python-based project demonstrating **context-aware AI agents** using OpenAI Agents SDK and Google Gemini API.  
The system manages multiple real-world contexts like **Banking, Student Profile, and Library Book System** using structured data models.

---

## 📌 Project Overview

This project demonstrates how AI agents can:

- Maintain **context-specific memory**
- Use **structured data (Pydantic models)**
- Call **tools dynamically**
- Work with multiple independent domains
- Run asynchronously using Python asyncio

Each agent operates with its own context:
- 🏦 Bank Account Agent
- 🎓 Student Profile Agent
- 📚 Library Book Agent

---

## ⚙️ Tech Stack

- Python 3.12+
- OpenAI Agents SDK
- Google Gemini API (via OpenAI-compatible endpoint)
- Pydantic (data modeling)
- Rich (console output formatting)
- dotenv (environment management)
- asyncio (asynchronous execution)

---

## 📂 Project Structure

```
context-management/
│── app.py              # Main agent execution file
│── connection.py       # Gemini API + model configuration
│── pyproject.toml      # Project dependencies
│── uv.lock             # Dependency lock file
│── .env                # API key storage (not included in repo)
```

---

## 🧠 How It Works

### 1️⃣ Context Models (Pydantic)

Each domain has its own structured context:

- BankAccount
- StudentProfile
- LibraryBook

These models define the **data structure passed into agents**.

---

### 2️⃣ Function Tools

Each agent uses a tool:

- `get_bank_info`
- `get_student_info`
- `get_book_info`

These tools access the **RunContextWrapper** to fetch contextual data.

---

### 3️⃣ AI Agents

Three separate agents are created:

- 🏦 `bank_agent` → Bank account queries
- 🎓 `student_agent` → Student information queries
- 📚 `Library_agent` → Book availability queries

Each agent is instructed to always use tools for responses.

---

### 4️⃣ Execution Flow

1. Load Gemini API key from `.env`
2. Initialize model using OpenAI-compatible endpoint
3. Pass context into each agent
4. Run agents asynchronously using `Runner.run()`
5. Display results using `rich.print`

---

## 🚀 Example Output

```
Bank Info:
The user info is BankAccount(account_number='ACC-789456', customer_name='Hafsa Rahman', account_balance=975500.50, account_type='savings')

Student Info:
The user info is StudentProfile(student_id='STU-247', student_name='Hafsa Rahman', current_semester=4, total_courses=5)

Book Info:
The user info is LibraryBook(book_id='BOOK-123', book_title='Python Programming', auther_name='John Smith', is_available=True)
```

---

## 🔑 Environment Setup

Create a `.env` file:

```
GEMINI_API_KEY=your_api_key_here
```

---

## ▶️ Installation & Run

### 1️⃣ Install dependencies
```bash
pip install -r requirements.txt
```

or (if using uv)
```bash
uv sync
```

---

### 2️⃣ Run the project
```bash
python app.py
```

---

## 🧩 Key Features

- 🧠 Context-aware AI agents
- 🔄 Multiple independent agent systems
- 📦 Structured data handling using Pydantic
- ⚡ Async execution with asyncio
- 🔧 Tool-based agent architecture
- 🤖 Gemini + OpenAI-compatible integration

---

## 📌 Learning Outcomes

This project helps understand:

- Context management in AI systems
- Tool calling with agents
- Structured data modeling
- Multi-agent architecture
- Async Python execution
- LLM integration patterns

---

## 🚀 Future Improvements

- Add database storage (PostgreSQL / MongoDB)
- Add web UI using Streamlit or FastAPI
- Expand agents (Finance, Healthcare, Education)
- Add memory persistence across sessions
- Add conversation history tracking

---

## 👩‍💻 Author

**Hafsa Rahman**  
Software Engineering Student  
Interested in AI, Data Science & Full Stack Development

---

## ⭐ License

This project is for educational purposes only.
