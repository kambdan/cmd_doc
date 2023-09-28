import re
import argparse
import os

PATTERN_DESCS_FUNC = r"(?:class\s+(\w+))?" + \
                     r"(?:/\*\s*\*([^*]*?)\*/)?" + \
                     r"(?:///\s*([^\n]+))??" + \
                     r"(?://\s([^\n]+)?)?" + \
                     r"((?:Future|void|String|int|double|bool|var|final)[\w\s\<\>\[\]]+\s*\([^)]*\)\s*async?)?"

def extract_comments_and_functions(filename):
    with open(filename, 'r') as file:
        content = file.read()
        matches = re.findall(PATTERN_DESCS_FUNC, content)
    return matches

def to_markdown(matches, output_filename):
    with open(output_filename, 'w') as md_file:
        for match in matches:
            class_name, general_desc, detail_desc, inout_desc, func = match
            
            if class_name:
                md_file.write(f"# class {class_name.strip()}\n\n")
            if general_desc:
                md_file.write(f"**{general_desc.strip()}**\n\n")
            if detail_desc:
                md_file.write(f"{detail_desc.strip()}\n\n")
            if inout_desc:
                md_file.write(f"{inout_desc.strip()}\n\n")
            if func.strip():
                md_file.write(f"```dart\n{func.strip()}\n```\n")
                md_file.write("---\n\n")

def main():
    parser = argparse.ArgumentParser(description="Extrae comentarios y funciones en Dart y genera un Markdown.")
    parser.add_argument("filename", help="Nombre del archivo Dart a analizar.")
    args = parser.parse_args()

    matches = extract_comments_and_functions(args.filename)
    
    # Cambio aquí: usa el nombre base del archivo y agrega la extensión .md
    base_name = os.path.splitext(args.filename)[0]
    output_filename = f"{base_name}.md"
    
    to_markdown(matches, output_filename)

    print(f"Documentación generada en {output_filename}.")
    print("Documentación generada exitosamente!")

if __name__ == "__main__":
    main()

if __name__ == "__main__":
    main()
