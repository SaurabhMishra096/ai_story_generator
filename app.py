import streamlit as st
from story_generator_hf import generate_story

st.set_page_config(page_title="AI Story Generator", layout="centered")

st.markdown("""
    <div style="text-align: center;">
        <h1 style="color: #6C63FF;">🧠 AI Story Generator</h1>
        <p>Enter a story prompt and let AI turn your imagination into words!</p>
    </div>
    <hr style="border:1px solid #eee;">
""", unsafe_allow_html=True)

# Story input
prompt = st.text_input("✍️ Enter your story prompt", placeholder="e.g., A girl got lost in the forest...")

# Desired word count slider
word_count = st.slider("📖 Desired Story Length (in words)", min_value=50, max_value=500, value=250, step=50)
temperature = st.slider("🔥 Creativity Level", min_value=0.1, max_value=1.5, value=0.9, step=0.1)

if st.button("🚀 Generate Story"):
    if prompt.strip():
        with st.spinner("Generating your story... please wait ✨"):
            try:
                # Convert word count to tokens (approx. 1.3 tokens per word)
                token_count = int(word_count * 1.3)
                story = generate_story(prompt, max_new_tokens=token_count, temperature=temperature)
                st.success("✅ Story Generated Successfully!")
                st.markdown("### 📘 Generated Story")
                st.text_area(" ", value=story, height=350, max_chars=None, key="story_output")
            except Exception as e:
                st.error(f"⚠️ Error generating story: {e}")
    else:
        st.warning("⚠️ Please enter a prompt to generate a story.")
