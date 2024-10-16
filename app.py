import streamlit as st
from rag_pipeline import answer_question

st.title("Advanced RAG System with LangChain and Apache Solr")

question = st.text_input("Enter your question:")

if st.button("Get Answer"):
    if question.strip() == "":
        st.warning("Please enter a question.")
    else:
        with st.spinner("Generating answer..."):
            answer = answer_question(question)
        st.success("Answer:")
        st.write(answer)
