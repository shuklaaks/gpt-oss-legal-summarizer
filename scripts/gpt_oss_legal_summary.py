"""
GPT-OSS Legal Contract Summarizer
Author: [Your Name]
"""

from transformers import AutoTokenizer, AutoModelForCausalLM
import torch
import pandas as pd
from pypdf import PdfReader

# Load contract text (replace with your source)
contract_text = open("data/sample_contract.txt", "r").read()

# Alternative loading methods
# with open("path/to/your_file.txt", "r") as f:
#     contract_text = f.read()
# df = pd.read_csv("path/to/your_file.csv")
# contract_text = " ".join(df['contract'].astype(str).tolist())
# reader = PdfReader("path/to/your_file.pdf")
# contract_text = " ".join([page.extract_text() for page in reader.pages])

# Model selection
model_name = "openai/gpt-oss-20b"  # Change to gpt-oss-120b for higher capacity

print(f"Loading model: {model_name} ... This may take a few minutes.")

# Load model
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(
    model_name,
    device_map="auto",
    torch_dtype=torch.float16,
    load_in_8bit=False
)

# Prompt
prompt = f"""
You are a legal compliance assistant.
Summarize the key obligations and termination rights from the following contract.
Also list any potential compliance risks.

Contract:
{contract_text}
"""

# Inference
inputs = tokenizer(prompt, return_tensors="pt").to(model.device)
outputs = model.generate(
    **inputs,
    max_new_tokens=400,
    temperature=0.2,
    do_sample=False
)

# Output
print("\n" + "="*30 + " MODEL OUTPUT " + "="*30)
print(tokenizer.decode(outputs[0], skip_special_tokens=True))
