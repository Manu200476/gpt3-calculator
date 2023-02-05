from transformers import GPT2TokenizerFast
import streamlit as st
from utils import *

st.set_page_config(
    page_title="GPT-3 Calculator",
)

st.title("GPT-3 Calculator")
st.subheader(
    "A simple calculator to ESTIMATE the cost of your GPT-3 project in dollars.")

with st.form(key="url_form"):
    response_length = st.number_input("Response Length", min_value=1)
    text = st.text_area("Prompt Text")
    submit_button = st.form_submit_button(label="Calculate")

if submit_button:
    costs = get_cost(normal_costs, response_length, text)

    show_results(costs)

    import streamlit as st
