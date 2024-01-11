# pip install transformers==4.36 bitsandbytes==0.41.3 accelerate==0.25.0 scipy==1.11.4 sentencepiece==0.1.99 gradio==4.9.0
# pip install transformers bitsandbytes accelerate  scipy  sentencepiece  gradio optimum

# from torch import cuda
# cuda.is_available()
# cuda.device_count()

from torch import float16
from transformers import BitsAndBytesConfig, pipeline


# from transformers import AutoModelForCausalLM
# model_id = "mistralai/Mixtral-8x7B-Instruct-v0.1"
# model_id = "mistralai/Mistral-7B-Instruct-v0.2"
# model = AutoModelForCausalLM.from_pretrained(model_id, trust_remote_code=True)
# model.to_bettertransformer()  ## Not available for mistral: Faster CPU inference: https://huggingface.co/docs/transformers/perf_infer_cpu

model_id = "mistralai/Mistral-7B-Instruct-v0.2"
pipe = pipeline(
  "text-generation",
  model=model_id
)

messages = [{"role": "user", "content": "Explain what a Mixture of Experts is in less than 100 words."}]
prompt = pipe.tokenizer.apply_chat_template(messages, tokenize=False, add_generation_prompt=True)

outputs = pipe(prompt, max_new_tokens=256, do_sample=True, temperature=0.7, top_k=50, top_p=0.95)
print(outputs[0]["generated_text"])
# bnb_config = BitsAndBytesConfig(
#   load_in_4bit=True,
#   bnb_4bit_compute_dtype=float16,
#   device_map="auto"
# )
   
# pipe = pipeline(
#   "text-generation",
#   model=model_id,
#   model_kwargs={"torch_dtype": float16, "load_in_4bit": True, "quantization_config": bnb_config},
# )
