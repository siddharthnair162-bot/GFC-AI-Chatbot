

**GFC AI Chatbot Prototype — Rule-Based Financial Assistant**

**Developer:** Siddharth D. Nair
**Role:** Junior Data Scientist — BCG GenAI Consulting Team
**Client:** Global Finance Corporation (GFC)
**Project Duration:** Phase 2 — Financial Data AI Integration



PROJECT OVERVIEW

This project is part of BCG’s AI-powered financial analysis initiative for Global Finance Corporation (GFC).
The goal is to create a rule-based AI chatbot that interprets 10-K financial data from Apple, Microsoft, and Tesla and provides instant, reliable financial insights.

The chatbot prototype demonstrates how AI can simplify access to key performance indicators and support decision-making for GFC.

 CORE FEATURES

Rule-Based Query Handling**: Responds to 5 predefined financial query types (Revenue, Net Income, Assets, Liabilities, Cash Flow).
Data-Driven Responses**: Uses real 10-K data (2022–2025) from SEC EDGAR filings.
Interactive CLI Chatbot**: Accepts natural language-style queries.
Year-over-Year Analysis**: Computes net income changes across fiscal years.
Extendable Logic**: Future-ready for NLP and ML-based enhancements.



HOW IT WORKS

1. Loads company financial data from `financial_data.csv`.
2. Accepts predefined financial queries (via CLI).
3. Uses conditional logic to map questions to corresponding data.
4. Displays formatted financial insights.
5. Type `exit` to end the chat.



SUPPORTED QUERIES

Examples:

* “What is the total revenue of Apple?”
* “What is the net income of Tesla?”
* “How has Microsoft’s net income changed over the last year?”
* “What are Apple’s total assets?”
* “What are Tesla’s total liabilities?”
* “What is Microsoft’s cash flow?”




 🧱 SETUP INSTRUCTIONS

1. Install dependencies
pip install pandas

2. Run the chatbot**
python ai_chatbot.py


Example startup message:


👋 Welcome to GFC's Financial Insight Chatbot Prototype!
Ask questions like:
 - What is the total revenue of Apple?
 - How has Microsoft’s net income changed over the last year?
Type 'exit' to end.




FUTURE ENHANCEMENTS

Add NLP integration with spaCy or Hugging Face.
Implement real-time financial API data updates.
Build web interface using Flask or Django.
Introduce speech-based query interaction.


LIMITATIONS

* Handles only predefined queries.
* Static dataset (no live updates).
* Limited company scope (Apple, Microsoft, Tesla).
