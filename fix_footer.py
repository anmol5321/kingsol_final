import os

# Target directory
target_dir = r"c:\Users\anmol\Downloads\stitch_sunergy_website_replica (1)\stitch_sunergy_website_replica"

old_grid_class = 'class="max-w-7xl mx-auto px-grid-gutter grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-16 mb-20"'
new_grid_class = 'class="max-w-7xl mx-auto px-grid-gutter grid grid-cols-1 md:grid-cols-2 lg:grid-cols-5 gap-10 mb-20"'

new_footer_columns = """<!-- Quick Links -->
            <div class="">
                <h4
                    class="font-label-caps text-label-caps text-white mb-10 border-b border-primary/40 pb-4 inline-block uppercase tracking-widest font-bold">
                    Quick Links</h4>
                <ul class="space-y-4 text-sm font-medium">
                    <li class=""><a class="hover:text-primary transition-colors duration-400" href="index.html">Home</a></li>
                    <li class=""><a class="hover:text-primary transition-colors duration-400" href="about.html">About Us</a></li>
                    <li class=""><a class="hover:text-primary transition-colors duration-400" href="products.html">Products</a></li>
                    <li class=""><a class="hover:text-primary transition-colors duration-400" href="company.html">Company</a></li>
                    <li class=""><a class="hover:text-primary transition-colors duration-400" href="projects.html">Projects</a></li>
                </ul>
            </div>
            <!-- Resources -->
            <div class="">
                <h4
                    class="font-label-caps text-label-caps text-white mb-10 border-b border-primary/40 pb-4 inline-block uppercase tracking-widest font-bold">
                    Resources</h4>
                <ul class="space-y-4 text-sm font-medium">
                    <li class=""><a class="hover:text-primary transition-colors duration-400" href="media.html">Media</a></li>
                    <li class=""><a class="hover:text-primary transition-colors duration-400" href="blog.html">Blog</a></li>
                    <li class=""><a class="hover:text-primary transition-colors duration-400" href="careers.html">Careers</a></li>
                    <li class=""><a class="hover:text-primary transition-colors duration-400" href="contacts.html">Contacts</a></li>
                </ul>
            </div>
            """

logo_targets = [
    'alt="Sunergy Logo" class="h-16 w-auto"',
    'alt="Sunergy Logo" class="h-8 w-auto"',
    'alt="Kingsol Logo" class="h-16 w-auto"',
    'alt="Kingsol Logo" class="h-8 w-auto"'
]

logo_replacement = 'alt="Sunergy Logo" class="h-24 w-auto"'

count = 0
for root, dirs, files in os.walk(target_dir):
    for file in files:
        if file.endswith('.html'):
            # Skip code.html files in refinement folders if we want, but let's process all
            filepath = os.path.join(root, file)
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
            
            modified = False
            
            # Find boundaries for Quick Links split
            start_comment = "<!-- Quick Links -->"
            end_comment = "<!-- Services-->"
            
            if start_comment in content and end_comment in content:
                start_idx = content.find(start_comment)
                end_idx = content.find(end_comment)
                
                # Replace the section in between
                before_section = content[:start_idx]
                after_section = content[end_idx:]
                
                # Replace the grid class too
                if old_grid_class in before_section:
                    before_section = before_section.replace(old_grid_class, new_grid_class)
                
                # Replace the footer logo size (only in the before section or after the footer tag)
                # To be precise, we replace it inside the footer block
                for target in logo_targets:
                    if target in before_section:
                        # For index.html, we might want to preserve "Kingsol Logo" name
                        current_replacement = logo_replacement
                        if 'Kingsol' in target:
                            current_replacement = 'alt="Kingsol Logo" class="h-24 w-auto"'
                        before_section = before_section.replace(target, current_replacement)
                        modified = True
                    if target in after_section:
                        current_replacement = logo_replacement
                        if 'Kingsol' in target:
                            current_replacement = 'alt="Kingsol Logo" class="h-24 w-auto"'
                        after_section = after_section.replace(target, current_replacement)
                        modified = True
                
                new_content = before_section + new_footer_columns + after_section
                
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                print(f"Updated footer & logo in: {file}")
                count += 1

print(f"Total files updated: {count}")
