import os
import json

def scan_tex_files(directory):
    # Dictionary to store tex file contents
    tex_files_content = {}

    # Walk through all the files in the directory
    for root, dirs, files in os.walk(directory):
        for file in files:
            # Check if the file has a .tex extension
            if file.endswith(".tex"):
                tex_file_path = os.path.join(root, file)
                
                # Read the content of the .tex file
                with open(tex_file_path, 'r', encoding='utf-8') as tex_file:
                    content = tex_file.read()
                
                # Add content to dictionary, using file name as the key
                tex_files_content[file] = content

    return tex_files_content

def write_to_json(tex_files_content, output_file):
    # Write the dictionary to a JSON file
    with open(output_file, 'w', encoding='utf-8') as json_file:
        json.dump(tex_files_content, json_file, ensure_ascii=False, indent=4)

if __name__ == "__main__":
    # Directory where your .tex files are located
    directory = "lecture_notes"

    # Output JSON file path
    output_file = "lecture_notes.json"

    # Scan through .tex files
    tex_files_content = scan_tex_files(directory)

    # Write to JSON file
    write_to_json(tex_files_content, output_file)

    print(f"Successfully converted .tex files to {output_file}")
