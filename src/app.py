import streamlit as st
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import os

st.title("📄 Resume Classifier (NLP ATS Filter)")

jd_text = st.text_area("Paste Job Description (JD)", height=200)

resume_files = st.file_uploader("Upload Resumes (Text files)", accept_multiple_files=True, type=["txt"])

if jd_text and resume_files:
    resumes = []
    resume_names = []

    for uploaded_file in resume_files:
        content = uploaded_file.read().decode("utf-8")
        resumes.append(content)
        resume_names.append(uploaded_file.name)

    vectorizer = TfidfVectorizer()
    all_docs = [jd_text] + resumes
    tfidf_matrix = vectorizer.fit_transform(all_docs)

    jd_vec = tfidf_matrix[0]
    resume_vecs = tfidf_matrix[1:]

    scores = cosine_similarity(jd_vec, resume_vecs)[0]
    ranked = sorted(zip(resume_names, scores), key=lambda x: x[1], reverse=True)

    st.subheader("📊 Resume Relevance Ranking:")
    for name, score in ranked:
        st.write(f"✅ **{name}** — Relevance Score: `{score:.2f}`")
