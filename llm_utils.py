
import requests
import os
from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

MODEL_NAME = "mistralai/Mistral-7B-Instruct-v0.2"
model = None
tokenizer = None

def load_model():
    global model, tokenizer
    if model is None or tokenizer is None:
        token = os.getenv("HUGGINGFACE_TOKEN")
        model = AutoModelForCausalLM.from_pretrained(
            MODEL_NAME,
            torch_dtype=torch.float16,
            device_map="auto",
            token=token
        )
        tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME, token=token)
    return model, tokenizer

def generate_study_plan(subject, level):
    model, tokenizer = load_model()
    prompt = f"Create a detailed study plan for {subject} at {level} level. Include 5 steps with clear descriptions."
    inputs = tokenizer(prompt, return_tensors="pt").to(model.device)
    outputs = model.generate(
        **inputs,
        max_length=300,
        num_return_sequences=1,
        temperature=0.7,
        top_p=0.9
    )
    return tokenizer.decode(outputs[0], skip_special_tokens=True)

def generate_answer(question):
    model, tokenizer = load_model()
    prompt = f"Provide a clear and concise answer to the following question: {question}"
    inputs = tokenizer(prompt, return_tensors="pt").to(model.device)
    outputs = model.generate(
        **inputs,
        max_length=200,
        num_return_sequences=1,
        temperature=0.7,
        top_p=0.9
    )
    return tokenizer.decode(outputs[0], skip_special_tokens=True)

def generate_diagram(prompt):
    # Placeholder for Stable Diffusion API (replace with your API key and endpoint)
    api_key = os.getenv("STABLE_DIFFUSION_API_KEY", "api")
    api_url = "https://api.stability.ai/v1/generation/stable-diffusion-xl"
    headers = {"Authorization": f"Bearer {api_key}"}
    payload = {
        "text_prompts": [{"text": f"A clear educational diagram for: {prompt}"}],
        "height": 512,
        "width": 512,
        "steps": 50
    }
    try:
        response = requests.post(api_url, json=payload, headers=headers)
        if response.status_code == 200:
            return response.json()["artifacts"][0]["url"]
        else:
            return None
    except Exception as e:
        print(f"Error generating diagram: {e}")
        return None