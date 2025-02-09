import os 

input_dir = "/caminho/para/input_dir"
parent_dir = os.path.dirname(input_dir)  # Volta uma pasta
# ou
parent_dir = os.path.join(input_dir, "..")  # Volta uma pasta
