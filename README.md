# Language Translation Model for Underresourced Languages

## Overview

This project focuses on improving translation accuracy for underserved communities, specifically translating between Nepali, Mongolian, Tigrinya, and English. The system uses **GPT-3** fine-tuned with custom datasets from these languages and **RAG (Retrieval-Augmented Generation)** files to enhance contextual understanding, achieving a 63% improvement in translation accuracy. The project also deploys the model on **AWS SageMaker**, reducing processing time by 40% and enabling the system to handle 1,000 requests per minute.

## Key Features

- **Fine-tuned GPT-3** model for Nepali, Mongolian, and Tigrinya translations.
- **RAG (Retrieval-Augmented Generation)** files for improved translation accuracy.
- Deployment on **AWS SageMaker** for scalable, low-latency translation.
- 63% improvement in translation accuracy and 40% reduction in processing time.

## Team Members

- **Shristi Ghimire** - Project Lead, AI
- **Tergel Khoroldavaa** - AI Developer
- **Sidon Woldeabzghi** - Python Developer, AWS
- **Angeline Blandine Ngando** - AWS Developer, AI
- **Meshari Almousa** - Database Manager

## Getting Started

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/yourusername/Language-Translation-Model-for-Underserved-Communities.git

Install Dependencies:

bash
Copy code
pip install -r requirements.txt
Prepare Datasets:

Ensure that the dataset files (nepali_data.csv, mongolian_data.csv, tigrinya_data.csv) are in the dataset/ folder.
Fine-tune GPT-3:

bash
Copy code
python src/model_training.py
Evaluate the Model:

bash
Copy code
python src/model_evaluation.py
Real-time Translation:

bash
Copy code
python src/inference.py
Deploy on AWS SageMaker:

bash
Copy code
python src/sagemaker_deployment.py
License
This project is licensed under the MIT License - see the LICENSE file for details.
