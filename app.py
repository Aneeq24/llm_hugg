import streamlit as st
from llm_utils import generate_study_plan, generate_answer, generate_diagram

def main():
    st.set_page_config(page_title="Personalized Learning Assistant", layout="wide")
    st.title("Personalized Learning Assistant")
    st.markdown("Enter your learning preferences and ask questions to get personalized study plans and answers!")

    # User inputs
    with st.form(key="learning_form"):
        subject = st.selectbox("Choose a subject", ["Mathematics", "Science", "History", "Literature"])
        level = st.selectbox("Choose your level", ["Beginner", "Intermediate", "Advanced"])
        user_question = st.text_area("Ask a question or request a diagram (e.g., 'Explain photosynthesis with a diagram')")
        submit_button = st.form_submit_button(label="Get Response")

    # Process inputs and display results
    if submit_button and user_question:
        with st.spinner("Generating response..."):
            # Generate study plan
            study_plan = generate_study_plan(subject, level)
            st.subheader("Your Personalized Study Plan")
            st.markdown(study_plan)

            # Generate answer
            answer = generate_answer(user_question)
            st.subheader("Answer to Your Question")
            st.markdown(answer)

            # Generate diagram if requested
            if "diagram" in user_question.lower():
                diagram_url = generate_diagram(user_question)
                if diagram_url:
                    st.subheader("Generated Diagram")
                    st.image(diagram_url, caption="Diagram generated for your query")

if __name__ == "__main__":
    main()