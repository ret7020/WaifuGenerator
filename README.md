# Waifu Generator
This is a simple bot to generate Waifu images from prompts in english language. You have to use machine with gpu(cuda)!

## Installation 
```
pip3 install -r requirements.txt
```
Create `config.py` file in root and write `API_TOKEN` inside it, like that:
```
API_TOKEN = "TOKEN"
```
Than you can run bot. First time, it will download weights for model, tokenizer and other. Be patient (about 5GB of data).
```
python3 main.py
```