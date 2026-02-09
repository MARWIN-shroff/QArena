import streamlit as st
import sys
from pathlib import Path

# Add the parent directory to Python path
parent_dir = Path(__file__).parent.parent
sys.path.insert(0, str(parent_dir))

# Now you can import from agent
from agent.test_generator import generate_tests
from agent.test_executor import execute_tests
from agent.result_analyzer import analyze_results


# -------------------- Page Config --------------------
st.set_page_config(
    page_title="QArena",
    layout="centered"
)

# -------------------- Header --------------------
st.title("🧪 QArena")
st.subheader("AI-Powered End-to-End Unit Testing Agent")

st.markdown("""
QArena orchestrates intelligent testing agents to **generate tests,
execute them automatically, and analyze outcomes** — all in one flow.
""")

st.divider()

# -------------------- User Input --------------------
project_path = st.text_input(
    "📂 Project Path",
    placeholder="/path/to/your/project"
)

testing_mode = st.selectbox(
    "🧠 Testing Mode",
    ["Unit Testing", "Integration Testing", "End-to-End Testing"]
)

st.divider()

# -------------------- Action Button --------------------
if st.button("🚀 Run QArena"):
    if not project_path:
        st.error("Please provide a valid project path.")
    else:
        with st.spinner("QArena agents are working..."):

            # -------- Step 1: Test Generation --------
            st.markdown("### 🧠 Test Generator Agent")
            try:
                generated_tests = generate_tests(project_path)
                st.success("Test generation completed.")
                st.code("\n\n".join(generated_tests), language="python")
            except Exception as e:
                st.error(f"Test generation failed: {e}")
                st.stop()

            # -------- Step 2: Test Execution --------
            st.markdown("### 🧪 Test Executor Agent")
            try:
                output, error = execute_tests(project_path)
                st.success("Test execution completed.")
                st.text_area("PyTest Output", output, height=200)
                if error:
                    st.text_area("PyTest Errors", error, height=150)
            except Exception as e:
                st.error(f"Test execution failed: {e}")
                st.stop()

            # -------- Step 3: Result Analysis --------
            st.markdown("### 📊 Result Analyzer Agent")
            try:
                analysis = analyze_results(output, error)
                st.success("Result analysis completed.")
                st.markdown(f"""
                **Status:** {analysis['status']}  
                **Failure Type:** {analysis['classification']}  

                **Root Cause:**  
                {analysis['root_cause']}  

                **Suggested Action:**  
                {analysis['suggestion']}
                """)

            except Exception as e:
                st.error(f"Result analysis failed: {e}")
                st.stop()
            


st.divider()
# -------------------- Footer --------------------
st.caption("QArena • Autonomous Testing Agents • Zero-Cost AI Infrastructure")

