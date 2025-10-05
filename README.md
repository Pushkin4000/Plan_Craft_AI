
## Plan Craft AI

**Plan Craft AI** is an intelligent project planning assistant built with **LangChain**, **Groq LLM**, and **Streamlit**.
It generates project ideas and detailed step-by-step execution plans for any given technology.

In the **agentic branch**, the system is extended to search the web for related **GitHub repositories** and **YouTube tutorials**, combining live web data with AI reasoning.


### Features

* **AI-Powered Project Generation** – Enter any technology (for example, LSTM, YOLO, or Blockchain) and receive a suitable project idea.
* **Automatic Step-by-Step Planning** – Produces a clear set of steps to execute the generated project.
* **Groq LLM (gpt-oss-120b)** – The main large language model used for reasoning and text generation.
* **Optional Ollama Integration** – A local LLM option for users who prefer privacy or offline operation.
* **Streamlit Interface** – Simple, interactive web interface for users.
* **Agentic Branch (Experimental)** – Adds web-search capability to find GitHub repositories and YouTube tutorials related to the chosen technology.

---

### Project Structure

```
├── langchain_groq_chain.ipynb        # Core logic using Groq LLM for project and procedure generation
├── langchain_helpz.py                # Helper functions connecting LangChain logic to the Streamlit app
├── streamlit_app.py                  # Streamlit frontend for user interaction
├── langchain_ollama_test.ipynb       # Optional Ollama test file for local/private setups
├── agentic_branch/                   # Agentic version with web search and tutorial discovery
│   ├── web_agent.py                  # Web agent for GitHub and YouTube search
│   └── utils.py                      # Helper utilities for search and parsing
└── README.md                         # Documentation
```

---

### Installation

#### 1. Clone the repository

```bash
git clone https://github.com/<your-username>/PlanCraftAI.git
cd PlanCraftAI
```

#### 2. Create and activate a virtual environment

```bash
python -m venv .venv
source .venv/bin/activate   # macOS/Linux
.venv\Scripts\activate      # Windows
```

#### 3. Install dependencies

```bash
pip install -r requirements.txt
```

If `requirements.txt` is not present, use:

```txt
streamlit
langchain
langchain-groq
requests
beautifulsoup4
```

---

### Environment Setup

Before running the app, set your **Groq API key**.

**macOS/Linux:**

```bash
export GROQ_API_KEY="your_api_key_here"
```

**Windows (PowerShell):**

```powershell
setx GROQ_API_KEY "your_api_key_here"
```

If you want to use the **local Ollama model**, make sure Ollama is installed and the model is available locally (for example, `ollama run qwen2.5`).

---

### Running the Application

Start the Streamlit interface:

```bash
streamlit run streamlit_app.py
```

Open the URL shown in the terminal (usually `http://localhost:8501`).

---

### How It Works

#### Main Branch

1. **Backend (LangChain + Groq)**

   * A `SequentialChain` combines two LangChain `LLMChain`s:

     * `proj_chain`: Generates a one-word project name for the given technology.
     * `proj_full`: Generates a comma-separated list of steps for that project.
   * The Groq LLM (`gpt-oss-120b`) handles all text generation.

2. **Frontend (Streamlit)**

   * The user enters a technology name.
   * The app calls `langchain_helpz.techo()`, which runs the LangChain pipeline.
   * The resulting project name and procedural steps are displayed in a clean, formatted output.

#### Agentic Branch

1. Uses an **agent-based approach** that enables:

   * Real-time web searches for relevant GitHub repositories.
   * Retrieval of YouTube tutorials related to the selected technology.
2. Returns results in a unified response combining:

   * The AI-generated project idea and steps.
   * Real examples and resources from the web.

---

### Example Usage

**Input:**

```
LSTM
```

**Output (Main Branch):**

```
Project Name: LSTMAnalyzer
Procedure:
1. Install the LSTMAnalyzer library
2. Import the necessary libraries
3. Load and preprocess the dataset
4. Split data into training and testing sets
5. Build and train the LSTM model
6. Visualize and analyze the results
```

**Output (Agentic Branch):**

```
Project Name: LSTMAnalyzer
Top GitHub Repositories:
- github.com/user1/lstm-stock-predictor
- github.com/user2/lstm-sentiment-analysis

YouTube Tutorials:
- "LSTM Explained with Code" – YouTube.com/watch?v=xxxx
- "LSTM Stock Prediction in Python" – YouTube.com/watch?v=yyyy
```

---

### Switching Between Branches

**Main (Groq-based app):**

```bash
git checkout main
```

**Agentic (web-enabled version):**

```bash
git checkout agentic
```

---

### Technologies Used

| Component                     | Description                                                  |
| ----------------------------- | ------------------------------------------------------------ |
| **Python 3.13**               | Core programming language                                    |
| **LangChain**                 | Framework for chaining LLM prompts and logic                 |
| **Groq LLM (gpt-oss-120b)**   | Main reasoning and text generation model                     |
| **Ollama**                    | Local/private LLM option                                     |
| **Streamlit**                 | Web-based user interface                                     |
| **Requests / BeautifulSoup4** | Web scraping for GitHub and YouTube results (agentic branch) |

---

### Author

**Pushkin Ranjan**
GitHub: [https://github.com/Pushkin4000](https://github.com/Pushkin4000)
Email: [[pushkinranjan4000@gmail.com](mailto:pushkinranjan4000@gmail.com)]

---

### License

This project is licensed under the **MIT License**.
You are free to use, modify, and distribute it with proper attribution.

---

Would you like me to generate a matching **`requirements.txt`** for this version (including optional agentic dependencies)? It’ll make your repo more complete for users installing from GitHub.
