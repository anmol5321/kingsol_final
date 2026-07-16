import os
import re

# Target directory
target_dir = r"c:\Users\anmol\Downloads\stitch_sunergy_website_replica (1)\stitch_sunergy_website_replica"

# Regex pattern to match the white submit button with any spacing/newlines
pattern = re.compile(
    r'(\s*)<button\s+class="btn-transition bg-white text-primary border-2 border-white hover:bg-transparent hover:text-white font-bold font-label-caps text-label-caps py-5 px-14 flex items-center group shadow-lg"\s+type="submit">',
    re.IGNORECASE
)

def replacer(match):
    indent = match.group(1)
    # Find the spaces on the line containing the button tag
    if '\n' in indent:
        spaces = indent.split('\n')[-1]
    else:
        spaces = indent
        
    return (
        f"{indent}<button\n"
        f"{spaces}    class=\"btn-transition font-bold font-label-caps text-label-caps py-5 px-14 flex items-center group shadow-lg\"\n"
        f"{spaces}    style=\"background-color:#60B0E9; color:#ffffff; border: 2px solid #60B0E9; transition: background-color 0.3s ease, border-color 0.3s ease;\"\n"
        f"{spaces}    onmouseover=\"this.style.backgroundColor='#F97316'; this.style.borderColor='#F97316';\"\n"
        f"{spaces}    onmouseout=\"this.style.backgroundColor='#60B0E9'; this.style.borderColor='#60B0E9';\"\n"
        f"{spaces}    type=\"submit\">"
    )

count = 0
for root, dirs, files in os.walk(target_dir):
    for file in files:
        if file.endswith('.html'):
            filepath = os.path.join(root, file)
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
            
            if pattern.search(content):
                new_content = pattern.sub(replacer, content)
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                print(f"Updated submit button in: {file}")
                count += 1

print(f"Total files updated: {count}")
