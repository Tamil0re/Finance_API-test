"""Event 2 kit: fake accounts and transactions on screen.

Run it:  python -m streamlit run app.py
"""

import streamlit as st

import bank

TEAM_NAME = "Your team name"  # TEAM TODO: change this

st.set_page_config(page_title=TEAM_NAME, layout="wide")


@st.cache_data(ttl=600, show_spinner="Calling the bank...")
def load():
    return bank.load_bank()


accounts, tx, source = load()

st.title(TEAM_NAME)
st.caption(f"Data source: {source} · All data is fake")

st.subheader("Accounts")
st.dataframe(accounts, hide_index=True)

st.subheader("Transactions")
st.caption("Positive = money out, negative = money in")
st.dataframe(tx, hide_index=True)

# SILVER QUEST 1: spending by category. Delete the # on the next 2 lines.
# st.subheader("Spending by category")
# st.bar_chart(tx[tx["amount"] > 0].groupby("category")["amount"].sum())

# SILVER QUEST 2: spending per month. Delete the # on the next 3 lines.
# st.subheader("Spending per month")
# spent = tx[tx["amount"] > 0]
# st.bar_chart(spent.groupby(spent["date"].astype(str).str[:7])["amount"].sum())
