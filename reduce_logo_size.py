import os

# Target directory
target_dir = r"c:\Users\anmol\Downloads\stitch_sunergy_website_replica (1)\stitch_sunergy_website_replica"

count = 0
for root, dirs, files in os.walk(target_dir):
    for file in files:
        if file.endswith('.html'):
            filepath = os.path.join(root, file)
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
            
            modified = False
            
            # Replace Kingsol Logo (Home page footer logo)
            if 'alt="Kingsol Logo" class="h-16 w-auto"' in content:
                content = content.replace('alt="Kingsol Logo" class="h-16 w-auto"', 'alt="Kingsol Logo" class="h-20 w-auto"')
                modified = True
                
            # Replace Sunergy Logo (Other pages footer logo)
            if 'alt="Sunergy Logo" class="h-16 w-auto"' in content:
                content = content.replace('alt="Sunergy Logo" class="h-16 w-auto"', 'alt="Sunergy Logo" class="h-20 w-auto"')
                modified = True
                
            if modified:
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(content)
                print(f"Reduced logo size in: {file}")
                count += 1

print(f"Total HTML files updated: {count}")
