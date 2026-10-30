
import streamlit as st
import re

st.set_page_config(
    page_title="AI Complexity Predictor",
    page_icon="🧠"
)

st.title("AI-Based Complexity Prediction Tool")

st.write("Enter your Python code to predict its time complexity.")

code = st.text_area(
    "Enter your code here:",
    height=220
)

def predict_complexity(code):

    # Check nested loops
    if re.search(r'for.*:', code) and re.search(r'for.*:', code[code.find('\n')+1:]):
        return "O(n²)", "Quadratic Time"

    # Check single loop
    elif re.search(r'\b(for|while)\b', code):
        return "O(n)", "Linear Time"

    # Check sorting
    elif "sort(" in code or "sorted(" in code:
        return "O(n log n)", "Linearithmic Time"

    else:
        return "O(1)", "Constant Time"


if st.button("Predict Complexity"):

    if code.strip():

        result, explanation = predict_complexity(code)

        st.subheader("Prediction Result")
        st.success("Time Complexity: " + result)
        st.write("Category: " + explanation)

    else:
        st.warning("Please enter some code!")
