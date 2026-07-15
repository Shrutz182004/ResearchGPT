import streamlit as st
from streamlit_option_menu import option_menu

from services.pdf_service import extract_text_from_pdf
from services.preprocessing_service import preprocess_text
from services.gemini_service import generate_summary
from services.gemini_service import extract_key_contributions
from services.gemini_service import answer_question
from services.gemini_service import basic_summary
from services.gemini_service import advanced_summary 

# ==========================================================
# PAGE CONFIG
# ==========================================================
st.set_page_config(
    page_title="ResearchGPT - AI Research Assistant",
    page_icon="📚",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ==========================================================
# CUSTOM CSS
# ==========================================================

st.markdown("""
<style>

.block-container{
    padding-top:2rem;
    padding-bottom:2rem;
}

section[data-testid="stSidebar"]{
    background:#F8FAFC;
    border-right:1px solid #E5E7EB;
}

.hero{
background:linear-gradient(135deg,#2563EB,#4F46E5);
padding:40px;
border-radius:18px;
color:white;
margin-bottom:25px;
box-shadow:0px 12px 35px rgba(0,0,0,0.15);
}

.hero h1{
font-size:48px;
margin-bottom:10px;
}

.hero p{
font-size:19px;
opacity:.95;
}

.card{
background:white;
padding:25px;
border-radius:15px;
border:1px solid #E5E7EB;
box-shadow:0px 6px 20px rgba(0,0,0,.05);
transition:0.3s;
height:170px;
}

.card:hover{
transform:translateY(-6px);
box-shadow:0px 15px 35px rgba(0,0,0,.12);
}

.metric-card{
background:white;
padding:20px;
border-radius:15px;
text-align:center;
box-shadow:0 5px 15px rgba(0,0,0,.08);
}

.footer{
text-align:center;
color:gray;
padding:20px;
font-size:14px;
}

</style>
""", unsafe_allow_html=True)

# ==========================================================
# SIDEBAR
# ==========================================================

with st.sidebar:

    st.markdown("## 📚 ResearchGPT")
    st.caption("AI Research Assistant")

    page = option_menu(
        menu_title=None,
        options=[
            "Home",
            "Upload Paper",
            "Summary",
            "Key Contributions",
            "Ask Questions",
            "Prompt Comparison",
            "About"
        ],
        icons=[
            "house-fill",
            "cloud-upload-fill",
            "file-earmark-text-fill",
            "stars",
            "chat-dots-fill",
            "diagram-3-fill",
            "info-circle-fill"
        ],
        default_index=0,
    )

    st.divider()

    st.success("🤖 Powered by Google Gemini")

    st.caption("Version 1.0")

    st.divider()

    st.markdown("""
### 🛠 Tech Stack

- Python
- Streamlit
- Google Gemini
- PyMuPDF
- NLTK
- spaCy
""")

    st.divider()

    st.caption("Developed by Shruti Singh")

# ==========================================================
# HOME
# ==========================================================

if page == "Home":

    st.markdown("""
<div class="hero">

<h1>📚 ResearchGPT</h1>

<p>
Transform complex research papers into actionable insights using
<b>Google Gemini</b>, <b>Natural Language Processing</b>, and
<b>Large Language Models</b>.

<br><br>

📄 Upload PDFs • 📝 AI Summary • ⭐ Key Contributions •
💬 Chat with Papers • 🧠 Prompt Engineering Comparison

</p>

</div>
""", unsafe_allow_html=True)

    st.markdown("## 🚀 Features")

    col1, col2 = st.columns(2)

    # ==========================
    # LEFT COLUMN
    # ==========================

    with col1:

        st.markdown("""
<div class="card">

<h3>📄 Upload Research Papers</h3>

Upload any research paper in PDF format.

Supports multi-page research articles.

</div>
""", unsafe_allow_html=True)

        st.write("")

        st.markdown("""
<div class="card">

<h3>📝 AI Summary</h3>

Generate concise AI-powered summaries in seconds.

</div>
""", unsafe_allow_html=True)

        st.write("")

        st.markdown("""
<div class="card">

<h3>⭐ Key Contributions</h3>

Automatically identify the most important research contributions.

</div>
""", unsafe_allow_html=True)

    # ==========================
    # RIGHT COLUMN
    # ==========================

    with col2:

        st.markdown("""
<div class="card">

<h3>💬 Chat with Research Paper</h3>

Ask intelligent questions and receive context-aware answers.

</div>
""", unsafe_allow_html=True)

        st.write("")

        st.markdown("""
<div class="card">

<h3>🧠 Prompt Engineering Comparison</h3>

Compare basic and advanced prompts to understand how prompt design improves AI responses.

</div>
""", unsafe_allow_html=True)

    st.write("")
    st.divider()

    # ==========================
    # PLATFORM OVERVIEW
    # ==========================

    st.subheader("🚀 ResearchGPT at a Glance")

    m1, m2, m3, m4 = st.columns(4)

    with m1:
        st.markdown("""
<div class="metric-card">

<h1>📄</h1>

Unlimited PDF Support

</div>
""", unsafe_allow_html=True)

    with m2:
        st.markdown("""
<div class="metric-card">

<h1>⚡</h1>

5–15 sec AI Response

</div>
""", unsafe_allow_html=True)

    with m3:
        st.markdown("""
<div class="metric-card">

<h1>🤖</h1>

Gemini 3.1 Flash Lite

</div>
""", unsafe_allow_html=True)

    with m4:
        st.markdown("""
<div class="metric-card">

<h1>💬</h1>

Interactive AI Chat

</div>
""", unsafe_allow_html=True)
    st.write("")

    # ==========================
    # HOW IT WORKS
    # ==========================

    st.divider()
    st.subheader("⚙️ How It Works")

    st.markdown("""
<div class="card">
    <h3>① Upload Research Paper</h3>
    <p>📄 Upload any research paper in PDF format.</p>
</div>

<div style="text-align:center;font-size:30px;padding:8px;">
⬇️
</div>

<div class="card">
    <h3>② AI Extracts & Analyzes Content</h3>
    <p>🤖 Uses NLP and Google Gemini to understand the uploaded paper.</p>
</div>

<div style="text-align:center;font-size:30px;padding:8px;">
⬇️
</div>

<div class="card">
    <h3>③ Generate AI Summary & Key Contributions</h3>
    <p>📝 Instantly creates concise summaries and extracts the paper's key findings.</p>
</div>

<div style="text-align:center;font-size:30px;padding:8px;">
⬇️
</div>

<div class="card">
    <h3>④ Chat with Your Research Paper</h3>
    <p>💬 Ask intelligent questions and receive context-aware answers from the paper.</p>
</div>

<div style="text-align:center;font-size:30px;padding:8px;">
⬇️
</div>

<div class="card">
    <h3>⑤ Compare Prompt Engineering</h3>
    <p>🧠 Compare Basic and Advanced prompts to see how prompt design improves AI responses.</p>
</div>
""", unsafe_allow_html=True)

    st.success("""
🚀 **Ready to explore your research paper?**

Upload a PDF from the **Upload Paper** page and let **ResearchGPT** summarize, analyze, answer questions, and compare prompt engineering strategies in seconds.
""")
# ==========================================================
# UPLOAD PAGE
# ==========================================================

elif page == "Upload Paper":

    st.title("📄 Upload Research Paper")
    st.write(
        "Upload a research paper and let AI analyze it using NLP and Large Language Models."
    )

    uploaded_file = st.file_uploader(
        "Choose a PDF Research Paper",
        type=["pdf"]
    )

    if uploaded_file:

        with st.spinner("📖 Extracting text from research paper..."):

            # Extract PDF text
            paper = extract_text_from_pdf(uploaded_file)

            # NLP Preprocessing
            cleaned_text = preprocess_text(paper["text"])

            # Store for other pages
            st.session_state["paper_text"] = paper["text"]
            st.session_state["clean_text"] = cleaned_text
            st.session_state["paper_data"] = paper

        st.success("✅ Research Paper Uploaded Successfully!")

        # -------------------------
        # Document Statistics
        # -------------------------
        col1, col2, col3, col4 = st.columns(4)

        col1.metric("📄 Pages", paper["pages"])
        col2.metric("📝 Words", paper["words"])
        col3.metric("🔤 Characters", paper["characters"])
        col4.metric("⏱ Reading Time", f"{paper['reading_time']} min")

        st.divider()

        # -------------------------
        # Paper Preview
        # -------------------------
        st.subheader("📖 Extracted Text Preview")

        st.text_area(
            label="",
            value=paper["text"][:3000],
            height=350,
            disabled=True
        )

        if len(paper["text"]) > 3000:
            st.info("Only the first 3000 characters are shown here.")

        st.divider()

        # -------------------------
        # Next Step
        # -------------------------
        if st.button(
            "🚀 Generate AI Summary",
            use_container_width=True
        ):
            st.success("Paper processed successfully! Navigate to the Summary page from the sidebar.")
# ==========================================================
# SUMMARY
# ==========================================================

elif page == "Summary":

    st.title("📝 AI Research Paper Summary")

    if "paper_text" not in st.session_state:
        st.warning("Please upload a research paper first.")
    else:

        if st.button("✨ Generate Summary", use_container_width=True):

            with st.spinner("Generating AI Summary..."):

                summary = generate_summary(
                    st.session_state["paper_text"]
                )

                st.session_state["summary"] = summary

        if "summary" in st.session_state:

            st.success("Summary Generated Successfully!")

            st.markdown(st.session_state["summary"])

            st.download_button(
                "⬇ Download Summary",
                data=st.session_state["summary"],
                file_name="research_summary.txt",
                mime="text/plain",
            )

# ==========================================================
# KEY CONTRIBUTIONS
# ==========================================================

elif page == "Key Contributions":

    st.title("⭐ AI Key Contributions")

    if "paper_text" not in st.session_state:
        st.warning("⚠️ Please upload a research paper first.")

    else:

        st.write(
            "Extract the most important contributions from the uploaded research paper using AI."
        )

        if st.button("🚀 Generate Key Contributions", use_container_width=True):

            with st.spinner("Analyzing research paper..."):

                contributions = extract_key_contributions(
                    st.session_state["paper_text"]
                )

            st.success("✅ Key Contributions Generated Successfully!")

            # Convert AI response into clean bullet cards
            points = [
                p.strip("-•1234567890. ").strip()
                for p in contributions.split("\n")
                if p.strip()
            ]

            st.markdown("### ⭐ Top Research Contributions")

            for point in points:

                # Remove markdown symbols if Gemini returns them
                point = point.replace("**", "").replace("*", "")

                st.markdown(
                    f"""
<div style="
padding:18px;
margin-bottom:15px;
border-radius:12px;
background-color:#262730;
border-left:6px solid #00C853;
color:white;
font-size:17px;
line-height:1.7;
box-shadow:0 3px 10px rgba(0,0,0,0.25);
">
✅ {point}
</div>
""",
                    unsafe_allow_html=True,
                )
# ==========================================================
# ASK QUESTIONS
# ==========================================================

elif page == "Ask Questions":

    st.title("💬 Chat with your Research Paper")

    if "paper_text" not in st.session_state:
        st.warning("⚠️ Please upload a research paper first.")

    else:

        # Initialize chat history
        if "messages" not in st.session_state:
            st.session_state.messages = []

        # Clear Chat button
        col1, col2 = st.columns([5, 1])

        with col2:
            if st.button("🗑 Clear Chat"):
                st.session_state.messages = []
                st.rerun()

        st.caption("💡 Ask questions based only on the uploaded research paper.")

        # Display previous messages
        for message in st.session_state.messages:
            with st.chat_message(message["role"]):
                st.markdown(message["content"])

        # Chat input
        question = st.chat_input(
            "💬 Ask anything about your research paper..."
        )

        if question and question.strip():

            # Save user message
            st.session_state.messages.append(
                {
                    "role": "user",
                    "content": question
                }
            )

            with st.chat_message("user"):
                st.markdown(question)

            with st.spinner("🤖 Gemini is analyzing your paper..."):

                answer = answer_question(
                    st.session_state["paper_text"],
                    question,
                    st.session_state.messages
                )

            # Save assistant message
            st.session_state.messages.append(
                {
                    "role": "assistant",
                    "content": answer
                }
            )

            with st.chat_message("assistant"):
                st.markdown(answer)
# ==========================================================
# PROMPT COMPARISON
# ==========================================================

elif page == "Prompt Comparison":

    st.title("🧠 Prompt Engineering Comparison")

    if "paper_text" not in st.session_state:
        st.warning("⚠️ Please upload a research paper first.")

    else:

        st.write(
            "Compare how prompt engineering changes the quality of AI-generated summaries."
        )

        if st.button(
            "🚀 Generate Prompt Comparison",
            use_container_width=True
        ):

            col1, col2 = st.columns(2)

            with st.spinner("Generating summaries..."):

                basic = basic_summary(
                    st.session_state["paper_text"]
                )

                advanced = advanced_summary(
                    st.session_state["paper_text"]
                )

            with col1:

                st.subheader("🟠 Basic Prompt Output")

                st.code(
                    "Summarize this research paper."
                )

                st.markdown(basic)

            with col2:

                st.subheader("🟢 Advanced Prompt Output")

                st.code(
"""
You are an expert AI Research Assistant.

Summarize the paper.

Include:
• Overview
• Methodology
• Results
• Contributions
• Future Scope
"""
                )

                st.markdown(advanced)

                st.divider()

        st.subheader("📊 Prompt Comparison")

        comparison_data = {
            "Feature": [
                "Structure",
                "Methodology",
                "Results",
                "Future Scope",
                "Readability",
                "Level of Detail",
            ],
            "Basic Prompt": [
                "❌ Unstructured",
                "⚠️ Brief",
                "⚠️ Mixed",
                "❌ Missing",
                "⭐⭐⭐",
                "Medium",
            ],
            "Advanced Prompt": [
                "✅ Well Structured",
                "✅ Detailed",
                "✅ Clearly Separated",
                "✅ Included",
                "⭐⭐⭐⭐⭐",
                "High",
            ],
        }

        st.table(comparison_data)

        st.info("""
### 💡 Why Prompt Engineering Matters

A well-designed prompt helps the AI generate:

- ✅ Better structured responses
- ✅ More accurate information
- ✅ Clear separation of methodology and results
- ✅ Better reasoning
- ✅ Improved readability

This demonstrates how prompt engineering can significantly improve the quality of Large Language Model (LLM) outputs.
""")
# ==========================================================
# ABOUT
# ==========================================================

elif page == "About":

    st.title("ℹ About ResearchGPT")

    st.markdown("""
# 📚 ResearchGPT – AI Research Assistant

ResearchGPT is an AI-powered platform that helps researchers
understand research papers quickly using Natural Language Processing
and Large Language Models.

---

## 🚀 Features

- 📄 PDF Upload

- 📝 AI Summary

- ⭐ Key Contributions

- 🔑 Keyword Extraction

- 💬 Question Answering

- 🧠 Prompt Engineering Comparison

---

## 🛠 Technology Stack

- Python

- Streamlit

- Google Gemini

- PyMuPDF

- NLTK

- spaCy

---

## 👩‍💻 Developed By

Shruti Singh

B.Tech CSE (AI & ML)

""")

# ==========================================================
# FOOTER
# ==========================================================

st.markdown("---")

st.markdown(
    """
<div style="text-align:center;color:gray;padding:15px;">

Built with ❤️ using
<b>Python</b> •
<b>Streamlit</b> •
<b>Google Gemini</b> •
<b>NLP</b>

<br><br>

© 2026 ResearchGPT | Developed by Shruti Singh

</div>
""",
unsafe_allow_html=True
)