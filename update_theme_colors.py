import os
import glob

def update_colors():
    html_files = glob.glob("d:/Projects/kingsol_final-main/kingsol_final-main/*.html") + glob.glob("d:/Projects/kingsol_final-main/kingsol_final-main/**/*.html")
    
    replacements = [
        ('"slate-dark": "#2B3152"', '"slate-dark": "#0F172A"'),
        ('"slate-dark": "#2b3152"', '"slate-dark": "#0F172A"'),
        ('"on-surface-variant": "#777B93"', '"on-surface-variant": "#334155"'),
        ('"on-surface-variant": "#777b93"', '"on-surface-variant": "#334155"'),
        ('"on-surface": "#2B3152"', '"on-surface": "#0F172A"'),
        ('"on-background": "#2B3152"', '"on-background": "#0F172A"'),
    ]

    count = 0
    for file_path in html_files:
        if not os.path.isfile(file_path):
            continue
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            new_content = content
            for old_str, new_str in replacements:
                new_content = new_content.replace(old_str, new_str)
                
            if new_content != content:
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                print(f"Updated: {file_path}")
                count += 1
        except Exception as e:
            print(f"Error processing {file_path}: {e}")
            
    print(f"Done! Updated {count} HTML files.")

if __name__ == "__main__":
    update_colors()
