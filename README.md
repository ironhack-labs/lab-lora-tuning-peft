![logo_ironhack_blue 7](https://user-images.githubusercontent.com/23629340/40541063-a07a0a8a-601a-11e8-91b5-2f13e4e6b441.png)

# Lab | LoRA Tuning using PEFT

## Getting Started

Follow the instructions provided in the notebook.

Read the instructions for each cell and provide your answers. Make sure to test your answers in each cell and save. Jupyter Notebook should automatically save your work progress. But it's a good idea to periodically save your work manually just in case.

## Deliverables

- Downloaded notebook with your responses to each of the exercises.

## Submission

- Upon completion, add your deliverables to git. 
- Then commit git and push your branch to the remote.
- Make a pull request and paste the PR link in the submission field in the Student Portal.

<br>

**Good luck!**

# RoboReviews: AI-Powered Product Review Analysis

## Overview
RoboReviews is a Flask-based web application that demonstrates how businesses can analyse, cluster, and summarize customer feedback using cutting-edge AI techniques. The project processes Amazon product reviews to provide actionable insights through sentiment analysis, category clustering, and automated summarization.

## Features
- **Sentiment Classification**: Automated categorization of reviews (positive/negative/neutral)
- **Category Clustering**: Smart grouping of products into meta-categories
- **Review Summarization**: AI-generated summaries of product reviews


## Data Pipeline
1. **Data Acquisition**: Downloads Amazon review datasets using Hugging Face
2. **Data Preparation**: Cleans and structures data for analysis
3. **Sentiment Classification**: Categorizes reviews using DistilRoBERTa
4. **Clustering**: Groups products into meta-categories with HDBSCAN
5. **Summarization**: Generates product summaries using Mistral-7B

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd roboreviews
```
2. Create and activate conda environment:
```bash
# Create environment from yml file
conda env create -f environment.yml

# Activate the environment
conda activate amazon_reviews

# For future updates to the environment
conda env update -f environment.yml
```
3. Manual package installations:
```bash
# Required manual installations
pip uninstall -y numpy
pip install numpy==1.23.5 --no-deps --force-reinstall
pip install torch==2.5.1 --no-deps
pip install -U bitsandbytes --no-deps    

# Install Flask for web interface
conda install flask   
# OR
pip install flask     
```

## Running the Application

1. Run the data pipeline:
```bash
# Run the complete pipeline
python scripts/run_pipeline.py --task all 

# Or run individual components
python scripts/run_pipeline.py --task classifier
python scripts/run_pipeline.py --task clusterer
python scripts/run_pipeline.py --task summariser --hf_token YOUR_TOKEN
```

2. Start the web interface to view the blogpost:
```bash
# Start the Flask server
python app.py

# Open your browser and navigate to:
http://localhost:5000
```

## Project Structure

```
.
├── README.md
├── app.py
├── data
│   └── amazon_reviews_backup
│       ├── processed
│       │   └── sampled
│       └── raw
│           ├── Office_Products.parquet
│           ├── Patio_Lawn_and_Garden.parquet
│           ├── Pet_Supplies.parquet
│           ├── Software.parquet
│           ├── Sports_and_Outdoors.parquet
│           ├── Subscription_Boxes.parquet
│           ├── Tools_and_Home_Improvement.parquet
│           ├── Toys_and_Games.parquet
│           ├── Unknown.parquet
│           └── Video_Games.parquet
├── environment.yml
├── invalid_path
├── notebooks
│   ├── Clusterer.ipynb
│   ├── Summariser.ipynb
│   ├── classifier.ipynb
│   ├── data_preparation.ipynb
│   ├── downloads.ipynb
│   ├── training_examples
│   └── training_examples.py
├── requirements
│   ├── classifier.txt
│   ├── clusterer.txt
│   ├── download.txt
│   ├── prepare.txt
│   ├── summariser.txt
│   └── test.txt
├── scripts
│   ├── export_requirements.py
│   └── run_pipeline.py
├── setup.py
├── src
│   ├── amazon_reviews
│   │   ├── __init__.py
│   │   ├── classifier.py
│   │   ├── clusterer.py
│   │   ├── download.py
│   │   ├── prepare.py
│   │   ├── setup_env.py
│   │   └── summariser.py
│   └── amazon_reviews.egg-info
│       ├── PKG-INFO
│       ├── SOURCES.txt
│       ├── dependency_links.txt
│       ├── requires.txt
│       └── top_level.txt
├── static
│   └── images
│       ├── amazon_category_clusters.png
│       ├── category_treemap.html
│       ├── cluster_comparison.png
│       ├── clustering_metrics.png
│       ├── confusion_matrix.png
│       ├── confusion_matrix_before.png
│       ├── probability_distribution.png
│       ├── realistic_robot_workspace.png
│       └── silhouette_analysis.png
└── tests
    ├── __init__.py
    ├── conftest.py
    ├── test_classifier.py
    ├── test_clusterer.py
    ├── test_data
    │   └── checkpoints
    │       ├── best_model.pt
    │       └── checkpoint.pt
    ├── test_download.py
    ├── test_evaluator.py
    ├── test_integration.py
    ├── test_prepare.py
    └── test_summariser.py
```
## Dataset

This project uses the [Amazon Reviews 2023 Dataset](https://amazon-reviews-2023.github.io/index.html) from the McAuley Lab, accessed through Hugging Face. The dataset provides:

- Product reviews with ratings, text, and metadata
- User interaction histories
- Product metadata including categories and descriptions

Example of loading the data:
```python
from datasets import load_dataset

# Suppress unnecessary HuggingFace warnings
import datasets
datasets.logging.set_verbosity_error()

# Load review data
dataset = load_dataset(
    "McAuley-Lab/Amazon-Reviews-2023", 
    "raw_review_All_Beauty", 
    trust_remote_code=True
)

# Example review structure:
{
    'rating': 5.0,
    'title': 'Such a lovely scent but not overpowering.',
    'text': "This spray is really nice...",
    'images': [],
    'asin': 'B00YQ6X8EO',
    'parent_asin': 'B00YQ6X8EO',
    'user_id': 'AGKHLEW2SOWHNMFQIJGBECAF7INQ',
    'timestamp': 1588687728923,
    'helpful_vote': 0,
    'verified_purchase': True
}
```

The dataset includes:
- Full review text and metadata
- Product information and categories
- User interaction histories

For more information, visit the [dataset documentation](https://amazon-reviews-2023.github.io/data_loading/huggingface.html).
