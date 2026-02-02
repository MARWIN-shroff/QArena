import streamlit as st

st.set_page_config(page_title="QArena", layout="centered")

st.title("🧪 QArena")
st.subheader("AI-Powered End-to-End Unit Testing Agent")

st.markdown("""
QArena automates test generation, execution, and result analysis
using intelligent testing agents.
""")

st.divider()

project_path = st.text_input(
    "📂 Project Path",
    placeholder="/path/to/your/project"
)

test_type = st.selectbox(
    "🧠 Select Testing Mode",
    ["Unit Testing", "Integration Testing", "End-to-End Testing"]
)

col1, col2, col3 = st.columns(3)

with col1:
    if st.button("Generate Tests"):
        st.success("Test generation started 🚀")
        st.info("Analyzing project structure...")

with col2:
    if st.button("Run Tests"):
        st.success("Executing tests 🧪")
        st.info("Running test suite...")

with col3:
    if st.button("Analyze Results"):
        st.success("Analyzing results 🤖")
        st.write("No critical failures detected ✅")
