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
RoboReviews is a Flask-based web application that revolutionizes how businesses analyze, cluster, and summarize customer feedback using cutting-edge AI techniques. The project processes Amazon product reviews to provide actionable insights through sentiment analysis, category clustering, and automated summarization.

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

### Environment Setup

1. Clone the repository:


```git clone <repository-url> ```
``` cd roboreviews ```


2. Create and activate conda environment:

```bash```
Create environment from yml file
```conda env create -f environment.yml```
Activate the environment
```conda activate amazon_reviews```
For future updates to the environment
```conda env update -f environment.yml```

3. Required manual installations
```pip uninstall -y numpy```
```pip install numpy==1.23.5 --no-deps --force-reinstall```
```pip install torch==2.5.1 --no-deps```
```pip install -U bitsandbytes --no-deps```

### Running the Pipeline

Run the complete pipeline:


:
bash
Run just the classifier
python scripts/run_pipeline.py --task classifier
Run just the clusterer
python scripts/run_pipeline.py --task clusterer
Run the Summariser (requires Hugging Face token)
python scripts/run_pipeline.py --task summariser --hf_token YOUR_TOKEN

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
