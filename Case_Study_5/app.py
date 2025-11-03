import streamlit as st
import google.generativeai as genai
from dotenv import load_dotenv
import os

# ------------------------
# 1️⃣ Setup
# ------------------------
st.title("Summarizer Tool (Gemini 2.5)")
st.write("This app uses Gemini 2.5 to summarize famous research papers in different styles.")

# Load environment variables
load_dotenv()

# Configure Gemini API Key
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# ------------------------
# 2️⃣ User Inputs
# ------------------------
paper_input = st.selectbox(
    "Select Research Paper Name",
    [
        "Attention Is All You Need",
        "BERT: Pre-training of Deep Bidirectional Transformers",
        "GPT-3: Language Models are Few-Shot Learners",
        "Diffusion Models Beat GANs on Image Synthesis"
    ]
)

style_input = st.selectbox(
    "Select Explanation Style",
    ["Beginner-Friendly", "Technical", "Code-Oriented", "Mathematical"]
)

length_input = st.selectbox(
    "Select Explanation Length",
    ["Short (1-2 paragraphs)", "Medium (3-5 paragraphs)", "Long (detailed explanation)"]
)

# ------------------------
# 3️⃣ Create Prompt
# ------------------------
prompt = f"""
Please summarize the research paper titled "{paper_input}" with the following specifications:
- Explanation Style: {style_input}
- Explanation Length: {length_input}

Include the following elements:
1. **Mathematical Formulations**:  
   - Include relevant equations or mathematical ideas used in the paper.  
   - Explain their role in the paper’s findings.  

2. **Analogies**:  
   - Use analogies to simplify complex ideas.  
   - Relate these to everyday experiences for better understanding.  

If certain information is not available in the paper, respond with: "Information not available in the paper."

Ensure the summary is clear, accurate, and matches the requested style and length.
"""

# ------------------------
# 4️⃣ Generate Summary using Gemini
# ------------------------
if st.button("Generate Summary"):
    try:
        model = genai.GenerativeModel("gemini-2.5-flash")  # or "gemini-2.5-pro" for higher quality
        response = model.generate_content(prompt)
        st.subheader("🧾 Generated Summary:")
        st.write(response.text)
    except Exception as e:
        st.error(f"Error: {e}")
