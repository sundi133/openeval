# Question-Answer Generator

This project is a tool for generating question-answer pairs based on provided data. It allows you to generate questions related to product information by specifying various parameters such as the data file path, the number of questions to generate, and more.


| Trying to evaluate an LLM on massive documents without automated eval dataset. | Realizing the importance of eval dataset generation for accurate llm app evaluations. |
| ----------------------------------------------------------------------- | ------------------------------------------------------------------ |
| ![Confused Person](data/images/confused_person.png)                    | ![Confident Person](data/images/confident_person.png)             |

## Why Dataset Generation Matters

Evaluating LLM applications on massive documents can be a daunting task, especially when you don't have the right evaluation dataset. The quality and relevance of your dataset can significantly impact the accuracy of your LLM app evaluations. Manual dataset creation can be time-consuming and error-prone, leading to inaccurate results.

### Prerequisites

- Python (>=3.9)
- Poetry (for dependency management)
 
## Installation

1. Clone this repository to your local machine:

   ```bash
   git clone https://github.com/yourusername/question-answer-generator.git
   cd question-answer-generator
   ```

2. Install the required dependencies using Poetry:

   ```bash
   poetry install
   ```

## Usage

To generate question-answer pairs for a csv, use the following command:

```bash
poetry run python src/main.py \ 
--data_path ./data/fixtures/amazon_uk_shoes_cleaned.csv \
--number_of_questions 2 \
--sample_size 3 \
--products_group_size 3 \
--group_columns "brand,sub_category,category,gender" \
--output_file ./output/qa_sample.json
```

To generate training dataset for NER model training:
``` bash 
poetry run python src/main.py \
--data_path ./data/fixtures/ner/train_ad_ids.ner \
--number_of_questions 1 \
--sample_size 20 \
--products_group_size 3 \
--group_columns "brand,sub_category,category,gender" \
--output_file ./output/ner_ad_ids.json \
--prompt_key prompt_key_ner \
--llm_type ner \
--metadata_path ./data/fixtures/ner/entities_ad_ids.json
```

To generate training dataset for readme documents:
``` bash
poetry run python src/main.py \
--data_path https://docs.getjavelin.io/ \
--number_of_questions 4 \
--sample_size 50 \
--llm_type ".html" \
--generator_type text \
--prompt_key prompt_key_readme \
--output_file ./output/qa_readme.json
```

### Command Options

- `--data_path`: The path to the input data file (e.g., CSV, TXT, PDF).
- `--number_of_questions`: The number of questions to generate.
- `--sample_size`: The sample size for selecting groups.
- `--products_group_size`: The minimum number of products per group.
- `--group_columns`: Columns to group by (e.g., "brand,sub_category,category,gender").
- `--output_file`: The path to the output JSON file where question-answer pairs will be saved.
- `--prompt_key`: The prompt key to be used 
- `--llm_type`: The class to use from llmchain extension 
- `--metadata_path`: The path to any metadata file

### Example

In the provided command, we are generating 2 questions based on the `amazon_uk_shoes_cleaned.csv` data file. We are using a sample size of 3 and require a minimum of 3 products per group to generate questions. The questions will be grouped by the columns "brand," "sub_category," "category," and "gender," and the results will be saved to `qa_sample.json` in the `output` directory.

##### Example pair of QA dataset generated from the input file of type csv with a sample product catalog

```
{
"question": "What are the different categories of men's shoes available?", 
"answer": "The available categories of men's shoes are loafers & moccasins."
}

{
"question": "Are there any promotions available for the men's shoes?", 
"answer": "Yes, there is a promotion of up to 35% off on selected men's shoes."
}

{
"question": "What is the price range for Laredo Men's Lawton Western Boot?", 
"answer": - "The price range for Laredo Men's Lawton Western Boot is \u00a3117.19 - \u00a3143.41."
}

{
"question": "What is the material used for the outer sole of Laredo Men's Wanderer Boot?",
"answer": "The outer sole of Laredo Men's Wanderer Boot is made of manmade material."
}

{
"question": "What promotions are currently available for the Saucony Women Sports Shoes Jazz Original Vintage Blue?",
"answer": "The Saucony Women Sports Shoes Jazz Original Vintage Blue is currently on sale with a 25% discount."
}

{
"question": "What are the features of the Saucony Women's Jazz Original Trainers?",
"answer": "The Saucony Women's Jazz Original Trainers have a leather outer material, rubber sole, lace-up closure, and a flat heel type."
}
```

##### Example pair of QA dataset generated from the input of type readme online docs

```
{
"question":"What are some examples of exceptions thrown by Javelin Python SDK?",
"answer":"Javelin Python SDK throws various exceptions for different error scenarios. For example, you can catch specific exceptions to handle errors related to authentication, network connectivity, or data validation.",
"url":"https://docs.getjavelin.io/docs/javelin-python/quickstart"
}

{
"question":"How can I access the data model in Javelin?",
"answer":"To access the data model in Javelin, you can refer to the documentation provided at the given URL.",
"url":"https://docs.getjavelin.io/docs/javelin-python/models#routes"
}

{
"question":"What are the fields available in the Javelin data model?",
"answer":"The Javelin data model includes various fields that can be used to store and manipulate data.",
"url":"https://docs.getjavelin.io/docs/javelin-python/models#model"
}

{
"question":"How does Javelin handle load balancing?",
"answer":"The documentation does not provide specific information on how Javelin handles load balancing.",
"url":"https://docs.getjavelin.io/docs/javelin-core/loadbalancing#__docusaurus_skipToContent_fallback"
}

{
"question":"What can Javelin do?",
"answer":"Javelin can send requests to models and retrieve responses based on the configured policies and route configurations.",
"url":"https://docs.getjavelin.io/docs/javelin-core/integration#llm-response"
}


```

## Linter
```bash
   poetry run flake8 src
   poetry run black src
```

## License

This project is licensed under the Apache 2.0 License - see the [LICENSE](LICENSE) file for details.

---
