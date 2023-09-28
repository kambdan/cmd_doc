import re
import argparse

COMMENTS_STYLES = {
    '.js': r'(?://[/]?)([^\n]*)',
    '.cpp': r'(?://[/]?)([^\n]*)',
    '.py': r'(?://|#)([^\n]*)',
    '.sql': r'(?://|--)([^\n]*)',
    '.dart': r'(?://[/]?)([^\n]*)'
}

def extract_comments(filename, comment_style):
    comments_list = []
    with open(filename, 'r') as file:
        content = file.read()
        pattern = re.compile(comment_style)
        comments = pattern.findall(content)
        
        for comment in comments:
            stripped_comment = comment.strip()
            if stripped_comment:
                comments_list.append(stripped_comment)
    return comments_list

def to_markdown(comments, output_filename):
    with open(output_filename, 'w') as md_file:
        for comment in comments:
            if comment.startswith("///"):
                md_file.write(f"## {comment[3:].strip()}\n")
            else:
                md_file.write(f"* {comment[2:].strip()}\n")

def main():
    parser = argparse.ArgumentParser(description="Extrae comentarios de un archivo y genera un Markdown.")
    parser.add_argument("filename", help="Nombre del archivo de código a analizar.")
    args = parser.parse_args()

    output_filename = 'documentation.md'

    extension = "." + args.filename.split('.')[-1]
    comment_style = COMMENTS_STYLES.get(extension)

    if not comment_style:
        print(f"Error: No se reconoce la extensión {extension}.")
        return

    comments = extract_comments(args.filename, comment_style)
    to_markdown(comments, output_filename)

    print(f"Documentación generada en {output_filename}")

if __name__ == "__main__":
    main()
