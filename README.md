# Study-Assistant
Artificial Intelligence powered education tool to assist student in most of their studies to catch up or be ahead in terms of their educational goals. The tool will generates quizzes from a typed topics, and also clarifies most cases which seem not to flow to the Student. The study tool will only read designed to support students with a fast and personalized learning.

## Features
* Topic based quiz generation (Classic and Artificial Intelligency Powered)
* Feedback engine for selected answers
* Artificial Intelligency Powered summary generator
* CLI and web interface (HTML/CSS/PHP)
* Modular backend for future Machine Learning Integration

## Technologies
| Layer | Stack |
|----------|----------|
| Frontend    | HTML, CSS, PHP (Optional JS)     |
| Backend   | Python (Flask or FastAPI)     |
| AI Engine  | OpenAI API / Transformers NLP    |
| PDF Export  | ReportLab / WeasyPrint   |
| CLI Tool  | Python (modular architecture)  |

## Folder Structure
**Study_Assistant**

cli/     **Command line interface**
* _init_.py
* main.py

core/    **AI and quiz logic**
* _init_.py
* quiz_engine.py
* quiz_ai.py
* summary_ai.py
* pdf_export.py

web/    **Frontend (HTML/CSS/PHP)**
* index.html
* style.css
* submit.php

.env   **API keys and secrets**

requirements.txt  **Python dependencies**

README.md

### Project Milestone
[Setup](https://github.com/Mr-Kheswa/Study-Assistant/issues/1)
