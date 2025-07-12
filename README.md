# 📄 Resume Classifier (NLP ATS Filter)

**Goal:** NLP tool to automatically rank resumes based on how well they match a given job description (JD). Built with Streamlit + Scikit-learn + spaCy.

## 🧠 Key Features
- Upload a Job Description and multiple resumes (text or PDF)
- Preprocess text using TF-IDF and NER (spaCy)
- Score and rank resumes based on relevance to the JD

## 📁 Folder Structure
```
resume-classifier/
├── data/
│   └── sample_resumes/
├── notebooks/
│   └── text_cleaning.ipynb
├── src/
│   └── app.py
├── requirements.txt
├── LICENSE
├── README.md
```

## 🚀 Run the App
```bash
streamlit run src/app.py
```

## 🔧 Tech Stack
- Python, Streamlit
- Scikit-learn, spaCy, PyPDF2
- TF-IDF, Cosine Similarity

## 🏗️ To-do
- Add PDF parsing support
- Integrate with real ATS
