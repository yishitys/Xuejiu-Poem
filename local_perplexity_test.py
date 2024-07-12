import torch
from transformers import AutoTokenizer, AutoModelForCausalLM
import json


def calculate_perplexity(model, tokenizer, text, device):
    inputs = tokenizer(text, return_tensors="pt").to(device)
    loss = model(input_ids=inputs["input_ids"], labels=inputs["input_ids"]).loss
    perplexity = torch.exp(loss)
    return perplexity.item()


def main():
    # Path to your local model directory (current directory in this case)
    model_path = "./Qwen14B"  # Current directory since your script is in the same directory
    tokenizer_path = "./Qwen14B"  # Current directory

    # Load the tokenizer and model from local files
    tokenizer = AutoTokenizer.from_pretrained(tokenizer_path)
    model = AutoModelForCausalLM.from_pretrained(model_path)

    # Check if GPU is available and move the model to GPU if possible
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    model.to(device)

    # Define file paths
    input_json_path = "predict_simplified_tester.json"
    output_json_path = "output.json"

    # Read the input JSON file
    with open(input_json_path, 'r', encoding='utf-8') as infile:
        data = json.load(infile)
    print("loaded data.")
    # Check if data is a list
    if isinstance(data, list):
        output_data = []
        for entry in data:
            if isinstance(entry, dict) and "text" in entry:
                text = entry["text"]
                perplexity = calculate_perplexity(model, tokenizer, text, device)
                print(f"Perplexity of text '{text}': {perplexity}")
                output_data.append({
                    "text": text,
                    "perplexity": str(perplexity)
                })
            else:
                print("Skipping an entry that is not a dictionary or does not contain 'text' key.")

        # Write the output JSON file
        with open(output_json_path, 'w', encoding='utf-8') as outfile:
            json.dump(output_data, outfile, ensure_ascii=False, indent=4)

        print(f"Output written to {output_json_path}")
    else:
        print("Input JSON is not a list.")


if __name__ == "__main__":
    main()