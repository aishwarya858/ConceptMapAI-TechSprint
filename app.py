import streamlit as st
import google.generativeai as genai

# 1. Setting up Gemini with the API Key
# Replace 'GEMINI_API_KEY' with the one from Google AI Studio
import streamlit as st
api_key = st.secrets["GEMINI_API_KEY"]
genai.configure(api_key=api_key)
model = genai.GenerativeModel('gemini-2.5-flash')

# 2. Design of the Website Interface
st.set_page_config(page_title="ConceptMap AI", page_icon="🎓")
st.title("🎓 ConceptMap AI")
st.subheader("Transforming notes into clarity")

# Text box for uploading the notes
user_input = st.text_area("Paste your Sahyadri lecture notes or textbook paragraphs here:", height=200)

# 3. The Logic
if st.button("Generate Study Map"):
    if user_input:
        with st.spinner("Analyzing your notes..."):
            # This is the 'Prompt' - it tells the AI exactly what to do
            prompt = f"""
            Act as an expert educator. Take the following text and return a structured summary. 
            List the 'Main Topic', then 5 'Sub-topics', and for each sub-topic, provide a 1-sentence explanation. 
            Format this as a clean bulleted list.
            Text: {user_input}
            """
            response = model.generate_content(prompt)
            
            # Display the result
            st.markdown("### 🗺️ Your Concept Breakdown")
            st.write(response.text)
    else:
        st.warning("Please paste some text first!")