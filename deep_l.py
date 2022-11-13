from transformers import pipeline
question = input("escribe el texto que quieres que rellene: ")
size = int(input("maximo de palabras:"))
sequences = int(input("numero de frases"))
generator = pipeline('text-generation', model = 'DeepESP/gpt2-spanish')
generator(question, max_length = size, num_return_sequences = sequences)
