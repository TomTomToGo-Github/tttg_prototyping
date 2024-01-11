from gpt4all import GPT4All
from pathlib import Path
model_name = "orca-2-7b.Q4_0.gguf"
# model_path = Path(r"C:/Users/thoma/Desktop/Tommy/Programmieren/gpt4all/models")
# llm_model = GPT4All(model_name, model_path=model_path) # device='amd', device='intel'
llm_model = GPT4All(model_name) # device='amd', device='intel'
llm_model.generate("Today I am feeling", max_tokens=100)
