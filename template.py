import os

# Define the directory structure
project_structure = {
    "homophonic_cipher_breaker": [
        "app/__init__.py",
        "app/cipher_breaker.py",
        "app/routes.py",
        "app/static/css/style.css",
        "app/static/js/script.js",
        "templates/index.html",
        "datasets/dataset1.txt",
        "datasets/dataset2.txt",
        "datasets/dataset3.txt",
        "main.py",
        "requirements.txt",
        "README.md"
    ]
}

# Function to create directory structure
def create_project_structure(structure):
    for root, files in structure.items():
        # Create the main project directory
        os.makedirs(root, exist_ok=True)
        
        # Create each file and its parent directories
        for file_path in files:
            full_path = os.path.join(root, file_path)
            os.makedirs(os.path.dirname(full_path), exist_ok=True)
            
            # Create an empty file
            with open(full_path, 'w') as f:
                pass

# Run the function to create the structure
create_project_structure(project_structure)

print("Project structure created successfully.")
