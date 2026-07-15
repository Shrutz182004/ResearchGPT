# 📚 ResearchGPT

An AI-powered Research Paper Analysis Platform built using **Python, Streamlit, Google Gemini, and NLP**. ResearchGPT helps users quickly understand research papers by generating summaries, extracting key contributions, answering questions, and demonstrating the impact of prompt engineering.

---

## 🚀 Features

- 📄 Upload Research Papers (PDF)
- 📝 AI-Powered Research Paper Summarization
- ⭐ Key Contribution Extraction
- 💬 Chat with Your Research Paper
- 🧠 Prompt Engineering Comparison (Basic vs Advanced Prompts)
- 📊 Document Statistics (Pages, Words, Characters, Reading Time)

---

## 🛠️ Tech Stack

- Python
- Streamlit
- Google Gemini API
- PyMuPDF
- NLTK
- spaCy

---

## 📂 Project Structure

```
ResearchGPT/
│── app.py
│── requirements.txt
│── README.md
│── services/
│   ├── gemini_service.py
│   ├── pdf_service.py
│   └── preprocessing_service.py
└── assets/
```

---

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/ResearchGPT.git
cd ResearchGPT
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

**Linux/macOS**

```bash
source venv/bin/activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

### 5. Create a `.env` file

```env
GOOGLE_API_KEY=YOUR_GEMINI_API_KEY
```

### 6. Run the application

```bash
streamlit run app.py
```

---

## 🎯 Future Improvements

- Export Summary as PDF
- Download Chat History
- Multi-document Support
- Citation Generation
- Research Paper Recommendations

---

## 👩‍💻 Developer

**Shruti Singh**

B.Tech – Computer Science & Engineering (AI & ML)

---

## 📄 License

This project is intended for educational and internship purposes.