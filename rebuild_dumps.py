import os
import ast

def retrieve_dumps(dir):
  data = []
  dump_files = [f for f in os.listdir(dir) 
         if os.path.isfile(os.path.join(dir, f)) and f.startswith('Dump')]
  for file in dump_files:
    file_path = os.path.join(dir, file)
    with open(file_path, 'r') as f:
        file_content = f.read().strip()
        try:
            data.extend(ast.literal_eval(file_content))
        except (ValueError, SyntaxError):
            print(f"Error reading {file}: Invalid format")

  return data
