#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 11 19:09:43 2025

@author: sidi
"""

import pandas as pd

# ---- Load Data ----
df = pd.read_csv("findata.csv")


# Get the latest fiscal year for each company
latest_data = df.groupby("Company").apply(lambda x: x.sort_values("Fiscal Year").iloc[-1])

# ---- Chatbot Function ----
def simple_chatbot():
    print("👋 Welcome to GFC's Financial Insight Chatbot Prototype!")
    print("Ask a question like:\n"
          " - What is the total revenue of Apple?\n"
          " - What is the net income of Tesla?\n"
          " - How has Microsoft's net income changed over the last year?\n"
          "Type 'exit' to end.\n")

    while True:
        user_query = input("You: ").strip().lower()
        if user_query == "exit":
            print("Chatbot: Goodbye! 👋")
            break

        response = get_response(user_query)
        print("Chatbot:", response)
        print()

# ---- Rule-Based Responses ----
def get_response(query):
    #
    if "total revenue" in query:
        for company in df['Company'].unique():
            if company.lower() in query:
                revenue = latest_data.loc[company, "Total Revenue (Million $)"]
                return f"{company}'s total revenue for {int(latest_data.loc[company, 'Fiscal Year'])} was ${revenue:,} million."
        return "Please specify which company you'd like revenue information for (Apple, Microsoft, or Tesla)."

 
    elif "net income" in query and "change" not in query:
        for company in df['Company'].unique():
            if company.lower() in query:
                income = latest_data.loc[company, "Net Income (Million $)"]
                return f"{company}'s net income for {int(latest_data.loc[company, 'Fiscal Year'])} was ${income:,} million."
        return "Please specify which company you'd like net income information for."

   
    elif "net income" in query and "change" in query:
        for company in df['Company'].unique():
            if company.lower() in query:
                subset = df[df['Company'] == company].sort_values("Fiscal Year")
                change = subset.iloc[-1]["Net Income (Million $)"] - subset.iloc[-2]["Net Income (Million $)"]
                direction = "increased" if change > 0 else "decreased"
                pct_change = (change / subset.iloc[-2]["Net Income (Million $)"]) * 100
                return f"{company}'s net income has {direction} by ${abs(change):,.0f} million ({pct_change:.2f}%) from {int(subset.iloc[-2]['Fiscal Year'])} to {int(subset.iloc[-1]['Fiscal Year'])}."
        return "Please specify which company you want to know the net income change for."

    
    elif "asset" in query:
        for company in df['Company'].unique():
            if company.lower() in query:
                assets = latest_data.loc[company, "Total Assets (Million $)"]
                return f"{company}'s total assets for {int(latest_data.loc[company, 'Fiscal Year'])} were ${assets:,} million."
        return "Please specify which company you'd like asset information for."

    elif "liabilit" in query:
        for company in df['Company'].unique():
            if company.lower() in query:
                liab = latest_data.loc[company, "Total Liabilities (Million $)"]
                return f"{company}'s total liabilities for {int(latest_data.loc[company, 'Fiscal Year'])} were ${liab:,} million."
        return "Please specify which company you'd like liability information for."

    
    elif "cash flow" in query:
        for company in df['Company'].unique():
            if company.lower() in query:
                cash = latest_data.loc[company, "Cash Flow from Operating Activities (Million $)"]
                return f"{company}'s cash flow from operating activities for {int(latest_data.loc[company, 'Fiscal Year'])} was ${cash:,} million."
        return "Please specify which company you'd like cash flow information for."

    # Default response
    else:
        return "Sorry, I can only answer predefined queries related to revenue, net income, assets, liabilities, or cash flow."

# ---- Run the Chatbot ----
if __name__ == "__main__":
    simple_chatbot()
