# 🚀 TalentRank-AI
### AI-Powered Candidate Ranking System

> **Build an AI system that ranks candidates the way a great recruiter would — not by matching keywords, but by actually understanding who fits the role.**

![Python](https://img.shields.io/badge/Python-3.11-blue?style=for-the-badge&logo=python)
![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-ML-orange?style=for-the-badge&logo=scikitlearn)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)
![Status](https://img.shields.io/badge/Project-Active-success?style=for-the-badge)

---

# 📌 Overview

TalentRank-AI is an intelligent recruitment system that helps recruiters identify the best candidates for a role using **semantic understanding** and **hybrid AI scoring** instead of simple keyword matching.

Unlike traditional Applicant Tracking Systems (ATS), TalentRank-AI evaluates:

- ✅ Skills
- ✅ Experience
- ✅ Career progression
- ✅ Industry relevance
- ✅ Behavioral signals
- ✅ Semantic similarity

The result is a recruiter-friendly ranked shortlist with explainable recommendations.

---

# 🎯 Problem Statement

Traditional ATS systems often reject strong candidates because they rely heavily on keyword matching.

Example:

Job Description

Python
SQL
Power BI

Candidate Resume

Python
SQL
Tableau

Although Tableau and Power BI are closely related BI tools, many ATS systems fail to recognize this relationship.

TalentRank-AI solves this problem using semantic understanding and intelligent ranking.

---

# ✨ Features

- 📄 Job Description Understanding
- 👤 Candidate Profile Analysis
- 🔍 Semantic Resume Matching
- 📊 Hybrid Scoring Engine
- 📈 Candidate Ranking
- 💡 Explainable AI Recommendations
- 📁 CSV Output Generation
- ⚡ Fast & Lightweight

---

# 🏗 System Architecture

```text
                Job Description
                       │
                       ▼
            Job Understanding Module
                       │
                       ▼
          Structured Job Requirements
                       │
──────────────────────────────────────────────
                       │
                       ▼
             Candidate Processing
                       │
                       ▼
          Structured Candidate Profiles
                       │
                       ▼
             Semantic Matching Engine
                       │
                       ▼
               Hybrid Scoring Engine
                       │
                       ▼
             Explanation Generator
                       │
                       ▼
             Ranked Candidate Output
```

---

# 🔄 Project Pipeline

```text
Read Job Description
        │
        ▼
Extract Skills & Requirements
        │
        ▼
Read Candidate Profiles
        │
        ▼
Generate Candidate Features
        │
        ▼
Semantic Similarity Matching
        │
        ▼
Hybrid Score Calculation
        │
        ▼
LLM / Rule-based Explanation
        │
        ▼
Final Ranked Candidates
```

---

# 📊 Hybrid Scoring Formula

| Component | Weight |
|------------|---------|
| Semantic Similarity | 40% |
| Skill Match | 25% |
| Experience | 15% |
| Industry Match | 10% |
| Behavioral Signals | 10% |

Final Score

```
Final Score =
0.40 × Semantic +
0.25 × Skills +
0.15 × Experience +
0.10 × Industry +
0.10 × Behavior
```

---

# 📂 Repository Structure

```
TalentRank-AI/

│

├── data/
│   ├── candidates.csv
│   └── jobs.csv
│
├── src/
│   ├── parser.py
│   ├── preprocess.py
│   ├── matcher.py
│   ├── scorer.py
│   ├── explain.py
│   └── utils.py
│
├── output/
│   └── ranked_candidates.csv
│
├── tests/
│
├── README.md
├── requirements.txt
├── main.py
└── app.py
```

---

# ⚙ Installation

Clone the repository

```bash
git clone https://github.com/yourusername/TalentRank-AI.git
```

Go to project directory

```bash
cd TalentRank-AI
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run

```bash
python main.py
```

---

# 📈 Workflow

```text
Job Description

↓

Parser

↓

Job Understanding

↓

Candidate Parsing

↓

Semantic Search

↓

Hybrid Scoring

↓

Ranking

↓

Explanation Generation

↓

CSV Output
```

---

# 📊 Example Output

| Rank | Candidate | Score |
|------|-----------|------:|
| 1 | Aman Sharma | 96.5 |
| 2 | Rohit Singh | 94.3 |
| 3 | Neha Verma | 91.8 |

---

# 💡 Example Recommendation

Candidate: Aman Sharma

✔ SQL

✔ Python

✔ Power BI

✔ Healthcare Industry

✔ 4 Years Experience

Reason

> Strong semantic similarity with job requirements. Meets all required technical skills and has relevant industry experience.

---

# 🚀 Future Improvements

- FAISS Vector Search
- Sentence Transformers
- LLM Re-ranking
- LinkedIn Integration
- Resume PDF Parsing
- Streamlit Dashboard
- Recruiter Feedback Loop
- Bias Detection
- Explainable AI Dashboard

---

# 🧪 Technologies Used

- Python
- Pandas
- NumPy
- Scikit-Learn
- Sentence Transformers
- FAISS
- Streamlit
- spaCy

---

# 📌 Why TalentRank-AI?

Traditional ATS

❌ Keyword Matching

❌ Poor Explainability

❌ Misses Strong Candidates

TalentRank-AI

✅ Semantic Understanding

✅ Explainable Ranking

✅ Recruiter-Friendly

✅ Intelligent Candidate Matching

---

# 📄 License

MIT License

---

# 👨‍💻 Author

**Harsh Pandey**

AI • Data Analytics • Machine Learning

---

⭐ If you found this project useful, consider giving it a star!
