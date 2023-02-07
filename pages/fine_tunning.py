st.set_page_config(
    page_title="Fine Tunning",
)

tab1, tab2 = st.tabs(["Fine Tunning Training", "Fine Tunning Generation"])

with tab1:
    st.title("Fine Tunning Training Price Calculator")

    with st.form(key="fine_tunning_training_form"):
        n_texts = st.number_input("Number of texts to train", min_value=1)
        text = st.text_area("Example of training text")
        submit_button = st.form_submit_button(label="Calculate")

    if submit_button:
        costs = get_costs_fine_tunning(text, n_texts)

        show_results(costs)

with tab2:
    st.title("Fine Tunning Generation Price Calculator")

    with st.form(key="fine_tunning_generation_form"):
        response_length = st.number_input("Response Length", min_value=1)
        text = st.text_area("Prompt Text")
        submit_button = st.form_submit_button(label="Calculate")

    if submit_button:
        costs = get_cost(fine_tunning_generation, response_length, text)

        show_results(costs)
