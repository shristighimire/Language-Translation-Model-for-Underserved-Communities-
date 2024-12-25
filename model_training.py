from transformers import GPT2LMHeadModel, Trainer, TrainingArguments
from data_preprocessing import load_data, tokenize_data
import torch

def fine_tune_model(data, tokenizer):
    model = GPT2LMHeadModel.from_pretrained("gpt-3")

    inputs = tokenize_data(data, tokenizer)

    training_args = TrainingArguments(
        output_dir="./results",
        num_train_epochs=3,
        per_device_train_batch_size=8,
        save_steps=10_000,
        save_total_limit=2,
    )

    trainer = Trainer(
        model=model,
        args=training_args,
        train_dataset=inputs,
    )
    
    trainer.train()

if __name__ == "__main__":
    nepali_data = load_data("dataset/nepali_data.csv")
    mongolian_data = load_data("dataset/mongolian_data.csv")
    tigrinya_data = load_data("dataset/tigrinya_data.csv")

    tokenizer = GPT2Tokenizer.from_pretrained("gpt-3")

    fine_tune_model(nepali_data, tokenizer)
    fine_tune_model(mongolian_data, tokenizer)
    fine_tune_model(tigrinya_data, tokenizer)
