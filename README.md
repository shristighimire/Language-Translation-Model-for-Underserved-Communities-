L# Language Translation Model for Underserved Communities

## Overview
The **Language Translation Model for Underserved Communities** project aims to bridge communication gaps in underserved communities by developing an accurate translation system for **Nepali**, **Mongolian**, and **Tigrinya**. By fine-tuning **GPT-3**, this model enhances translation capabilities and makes it easier for individuals in these communities to access critical information in their native languages.

The project leverages **Retrieval-Augmented Generation (RAG)**, where relevant translation prompts from these languages are used to improve the model's performance. The fine-tuned model was deployed on **AWS SageMaker** to improve scalability, reduce latency, and support high request volumes, ensuring that the system can handle **1,000 requests per minute**.

## Key Achievements
- **Fine-tuned GPT-3**: Improved translation accuracy by **63%** for Nepali, Mongolian, and Tigrinya languages by leveraging custom datasets and RAG-based prompts.
- **AWS SageMaker Deployment**: The model was successfully deployed on **AWS SageMaker**, which resulted in a **40% reduction in processing time** and ensured the system could handle up to **1,000 requests per minute** during trials.
- **Translation Efficiency**: The fine-tuned model provides faster, more accurate translations that can be used by underserved communities to overcome language barriers.

## Features
- **Fine-Tuning with Custom Data**: The model is fine-tuned using data from Nepali, Mongolian, and Tigrinya language pairs to improve translation accuracy.
- **RAG Implementation**: The project uses **RAG files** to augment the translation process, making it contextually aware and more effective in translating less-common language pairs.
- **AWS SageMaker Deployment**: Scalable deployment ensures quick processing of high-volume translation requests, reducing latency and improving user experience.
- **High Throughput**: Designed to handle **1,000 requests per minute** during real-world trials.

## Project Team
- **Shristi Ghimire**: Project Lead, AI
- **Tergel Khoroldavaa**: AI Developer
- **Sidon Woldeabzghi**: Python Developer, AWS
- **Angeline Blandine Ngando**: AWS Developer, AI
- **Meshari Almousa**: Database Manager

## Technologies Used
- **GPT-3**: Used for natural language processing and translation tasks.
- **RAG (Retrieval-Augmented Generation)**: Implemented to enhance the translation model's context awareness and accuracy.
- **AWS SageMaker**: Deployed the model on AWS SageMaker for scalable deployment and low-latency requests.
- **Python**: Used for model training, data preprocessing, and real-time inference.
- **PyTorch**: Framework used for training and deploying the model.

## Getting Started
To get started with the project, follow these steps:

### Clone the Repository:
```bash
git clone https://github.com/yourusername/Language-Translation-Model-for-Underserved-Communities.git

Technologies Used
GPT-3: Used for natural language processing and translation tasks.
RAG (Retrieval-Augmented Generation): Implemented to enhance the translation model's context awareness and accuracy.
AWS SageMaker: Deployed the model on AWS SageMaker for scalable deployment and low-latency requests.
Python: Used for model training, data preprocessing, and real-time inference.
PyTorch: Framework used for training and deploying the model.
Getting Started
To get started with the project, follow these steps:

Clone the Repository:

bash
Copy code
git clone https://github.com/yourusername/Language-Translation-Model-for-Underserved-Communities.git
Install Dependencies:

bash
Copy code
pip install -r requirements.txt
Prepare Datasets:

Download and place the Nepali, Mongolian, and Tigrinya datasets in the dataset/ folder.
Fine-tune GPT-3: Run the model training script to fine-tune GPT-3 with the provided datasets.

bash
Copy code
python src/model_training.py
Evaluate the Model: Test the performance of the fine-tuned model using the evaluation script.

bash
Copy code
python src/model_evaluation.py
Real-time Translation: Use the inference script to make real-time translations using the deployed model.

bash
Copy code
python src/inference.py
Deploy on AWS SageMaker: Deploy the fine-tuned model using AWS SageMaker for scalable real-time inference.

bash
Copy code
python src/sagemaker_deployment.py
License
This project is licensed under the MIT License - see the LICENSE file for details.

