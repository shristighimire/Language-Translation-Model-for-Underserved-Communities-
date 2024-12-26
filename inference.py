import torch
from transformers import GPT2LMHeadModel, GPT2Tokenizer

def translate_sentence(sentence):
    model = GPT2LMHeadModel.from_pretrained("./results")
    tokenizer = GPT2Tokenizer.from_pretrained("gpt-3")

    inputs = tokenizer(sentence, return_tensors="pt")
    translated = model.generate(inputs['input_ids'])
    translated_text = tokenizer.decode(translated[0], skip_special_tokens=True)
    
    return translated_text

if __name__ == "__main__":
    sentence = "तपाईंलाई कस्तो छ?"
    translation = translate_sentence(sentence)
    print(f"Original: {sentence}")
    print(f"Translation: {translation}")
