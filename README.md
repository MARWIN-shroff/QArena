# 🚀 QArena

**QArena** is an AI-powered end-to-end unit testing agent designed to automate test generation, execution, and result analysis for modern software applications.

The goal of this project is to reduce the manual effort involved in writing and maintaining end-to-end tests by leveraging AI-driven reasoning and automation.

---

## Architecture Diagram
```
User / CI
   │
   ▼
[Test Generator Agent]
   │   → creates test cases
   ▼
[Test Executor Agent]
   │   → runs pytest
   ▼
[Result Analyzer Agent]
   │   → explains failures
   ▼
UI / Logs / CI Feedback
```

## ✨ Features

- 🧠 **Automated Test Generation**
  - Generates test cases based on application behavior and user flows

- 🤖 **Agentic Test Execution**
  - Executes tests automatically across environments

- 📊 **AI-Based Result Analysis**
  - Analyzes failures and provides insights into potential causes

- 🔄 **CI/CD Ready**
  - Designed to integrate with modern CI pipelines

---

## 🛠 Tech Stack

- **Python 3.10+**
- **Streamlit** – lightweight UI
- **PyTest** – test execution
- **Open-source LLMs / Rule-based AI (initial phase)**

> The project is designed to be **100% cost-free** using open-source tools.

---

## 📁 Project Structure


```
qarena/
│
├── agent/
│   ├── test_generator.py    # AI logic to generate test cases
│   ├── test_executor.py     # Executes generated tests
│   └── result_analyzer.py   # Analyzes test outcomes and failures
│
├── ui/
│   └── app.py               # Streamlit-based user interface
│
├── tests/
│   └── sample_app_tests.py  # Sample / demo tests
│
├── requirements.txt         # Python dependencies
├── README.md
└── .gitignore
```

## 🚧 Project Status

🔨 **In Active Development**

Planned improvements:
- Smarter test generation
- Failure root-cause detection
- CI/CD integration
- Multi-language support

---

## 🤝 Contributing

Contributions are welcome!  
Feel free to open issues or submit pull requests.

---

## 📜 License

MIT License




