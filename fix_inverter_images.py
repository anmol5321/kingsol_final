import os
import glob

working_inverter_img = "https://images.unsplash.com/photo-1548337138-e87d889cc369?auto=format&fit=crop&w=800&q=80"
broken_img_target = "photo-1620027136027-e3f322c2a5bf"

html_files = glob.glob("*.html")
updated_count = 0
replaced_occurrences = 0

for file_path in html_files:
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()
    
    if broken_img_target in content:
        # Find any full URL containing photo-1620027136027-e3f322c2a5bf
        # Usually: https://images.unsplash.com/photo-1620027136027-e3f322c2a5bf?auto=format&fit=crop&w=800&q=80
        # or w=1920
        lines = content.splitlines()
        new_lines = []
        file_replaced = 0
        for line in lines:
            if broken_img_target in line:
                # Replace the broken image URL with working inverter image URL
                # We handle both w=800, w=1920, etc.
                import re
                line_new = re.sub(
                    r'https://images\.unsplash\.com/photo-1620027136027-e3f322c2a5bf[^\s"\'<>]*',
                    working_inverter_img,
                    line
                )
                new_lines.append(line_new)
                file_replaced += 1
            else:
                new_lines.append(line)
        
        with open(file_path, "w", encoding="utf-8") as f:
            f.write("\n".join(new_lines))
        
        updated_count += 1
        replaced_occurrences += file_replaced
        print(f"Updated {file_path}: {file_replaced} occurrences replaced")

print(f"Done! Total files updated: {updated_count}, Total occurrences replaced: {replaced_occurrences}")
