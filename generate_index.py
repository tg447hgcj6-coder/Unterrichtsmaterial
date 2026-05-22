#!/usr/bin/env python3
"""
Script to generate an index.html that lists all HTML files in the repository.
"""

import os
import pathlib
from datetime import datetime

def get_html_files(root_dir="."):
    """
    Recursively find all HTML files in the repository,
    excluding files in .git and node_modules directories.
    """
    html_files = []
    
    for root, dirs, files in os.walk(root_dir):
        # Skip hidden directories and common exclusions
        dirs[:] = [d for d in dirs if not d.startswith('.') and d not in ['node_modules', '.git']]
        
        for file in sorted(files):
            if file.endswith('.html') and file != 'index.html':
                file_path = os.path.join(root, file)
                # Convert to relative path
                rel_path = os.path.relpath(file_path, root_dir)
                html_files.append(rel_path)
    
    return sorted(html_files)

def generate_index_html(html_files):
    """Generate an HTML index page listing all HTML files."""
    
    html_content = """<!DOCTYPE html>
<html lang="de">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Unterrichtsmaterial - Übersicht</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }
        
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            min-height: 100vh;
            padding: 40px 20px;
        }
        
        .container {
            max-width: 900px;
            margin: 0 auto;
        }
        
        header {
            text-align: center;
            color: white;
            margin-bottom: 50px;
        }
        
        h1 {
            font-size: 3em;
            margin-bottom: 10px;
            text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
        }
        
        .subtitle {
            font-size: 1.2em;
            opacity: 0.9;
        }
        
        .content {
            background: white;
            border-radius: 15px;
            padding: 40px;
            box-shadow: 0 10px 40px rgba(0,0,0,0.3);
        }
        
        .file-list {
            list-style: none;
        }
        
        .file-item {
            margin-bottom: 15px;
            border-left: 4px solid #667eea;
            padding-left: 20px;
            padding-top: 10px;
            padding-bottom: 10px;
            transition: transform 0.2s, box-shadow 0.2s;
        }
        
        .file-item:hover {
            transform: translateX(5px);
        }
        
        .file-item a {
            text-decoration: none;
            color: #333;
            font-size: 1.1em;
            font-weight: 500;
            transition: color 0.3s;
        }
        
        .file-item a:hover {
            color: #667eea;
        }
        
        .file-path {
            font-size: 0.85em;
            color: #666;
            margin-top: 5px;
        }
        
        .empty-message {
            text-align: center;
            color: #999;
            padding: 40px;
            font-size: 1.1em;
        }
        
        footer {
            text-align: center;
            color: white;
            margin-top: 30px;
            font-size: 0.9em;
            opacity: 0.8;
        }
        
        @media (max-width: 600px) {
            h1 {
                font-size: 2em;
            }
            
            .content {
                padding: 20px;
            }
            
            .file-item a {
                font-size: 1em;
            }
        }
    </style>
</head>
<body>
    <div class="container">
        <header>
            <h1>📚 Unterrichtsmaterial</h1>
            <p class="subtitle">Übersicht aller verfügbaren Materialien</p>
        </header>
        
        <div class="content">
"""
    
    if html_files:
        html_content += "            <ul class=\"file-list\">\n"
        for file_path in html_files:
            # Extract filename without extension
            file_name = pathlib.Path(file_path).stem
            # Format the display name (replace underscores and hyphens with spaces)
            display_name = file_name.replace('_', ' ').replace('-', ' ').title()
            
            html_content += f"""                <li class="file-item">
                    <a href="{file_path}">{display_name}</a>
                    <div class="file-path">{file_path}</div>
                </li>\n"""
        html_content += "            </ul>\n"
    else:
        html_content += '            <div class="empty-message">Keine HTML-Dateien gefunden.</div>\n'
    
    html_content += f"""        </div>
        
        <footer>
            <p>Zuletzt aktualisiert: {datetime.now().strftime('%d.%m.%Y %H:%M:%S')}</p>
        </footer>
    </div>
</body>
</html>
"""
    
    return html_content

def main():
    """Main function to generate the index."""
    print("Generiere Index...")
    
    # Get all HTML files
    html_files = get_html_files()
    
    # Generate the index HTML
    index_html = generate_index_html(html_files)
    
    # Write to index.html
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(index_html)
    
    print(f"✅ index.html erfolgreich erstellt!")
    print(f"📄 {len(html_files)} HTML-Dateien gefunden und aufgelistet.")

if __name__ == "__main__":
    main()
