import os
import pandas

# Function to read files from a directory
def read_files_from_directory(directory, file_extension=None):
    file_data = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file_extension and not file.endswith(file_extension):
                continue
            file_path = os.path.join(root, file)
            with open(file_path, 'r', encoding='utf-8') as f:
                file_content = f.read()
                # Include full file path in the dataset
                file_data.append({
                    "file_name": file,
                    "file_path": file_path,  # Add the full file path here
                    "content": file_content
                })
    return file_data

# Concatenate content from all README and Rust files
def prepare_dataset_from_repo(repo_path):
    data = []

    # Read README files from project1 to project8
    for i in range(1, 9):
        project_dir = os.path.join(repo_path, f"project{i}")
        readme_file = os.path.join(project_dir, "README.md")
        if os.path.exists(readme_file):
            with open(readme_file, 'r', encoding='utf-8') as f:
                readme_content = f.read()
                prompt = f"Project {i} README:\n"
                completion = f" {readme_content}"
                data.append({"prompt": prompt, "completion": completion})

    # Read all Rust files from 'src' folder and subdirectories
    src_dir = os.path.join(repo_path, "src")
    rust_files = read_files_from_directory(src_dir, file_extension=".rs")

    for rust_file in rust_files:
        prompt = f"Rust Code from {rust_file['file_path']}:\n"  # Include full path in the prompt
        completion = f" {rust_file['content']}"
        data.append({"prompt": prompt, "completion": completion})

    return data

# Convert the dataset into a JSONL format and save it
def save_dataset_as_jsonl(data, output_path="repo_finetune.jsonl"):
    df = pd.DataFrame(data)
    df.to_json(output_path, orient="records", lines=True)
    print(f"Dataset saved to {output_path}")

# Prepare the dataset from the repository
repo_path = 'COS-ECE470-fa2024'  # Path to your Git repo folder
dataset = prepare_dataset_from_repo(repo_path)

# Save the dataset in JSONL format for fine-tuning
save_dataset_as_jsonl(dataset, output_path="bitcoin_client_data.jsonl")
