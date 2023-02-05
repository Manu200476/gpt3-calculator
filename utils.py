fine_tunning_costs = {
    "ADA": 0.0004,
    "BABBAGE": 0.0006,
    "CURIE": 0.0030,
    "DAVINCI": 0.0300,
}

fine_tunning_generation = {
    "ADA": 0.0016,
    "BABBAGE": 0.0024,
    "CURIE": 0.0120,
    "DAVINCI": 0.1200,
}

normal_costs = {
    "ADA": 0.0004,
    "BABBAGE": 0.0005,
    "CURIE": 0.0020,
    "DAVINCI": 0.0200,
}


def get_cost(models, response_length, text):
    total_costs = {}
    tokenizer = GPT2TokenizerFast.from_pretrained("gpt2")
    tokens = tokenizer(text)["input_ids"]

    print(len(tokens))

    for model in models:
        cost = ((response_length + len(tokens)) / 1000) * models[model]
        total_costs[model] = cost

    return total_costs


def get_costs_fine_tunning(text, n_texts):
    total_costs = {}
    tokenizer = GPT2TokenizerFast.from_pretrained("gpt2")
    tokens = tokenizer(text)["input_ids"]

    for model in fine_tunning_costs:
        cost = ((len(tokens) * n_texts) / 1000) * fine_tunning_costs[model]
        total_costs[model] = cost

    return total_costs


def show_results(costs):
    for index, col in enumerate(st.columns(len(costs))):
        model = list(costs.keys())[index]

        col.metric(label=f"{model}", value=f"{round(costs[model], 5)}$")
