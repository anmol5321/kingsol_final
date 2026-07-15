
import os
import re

# Define the replacement mappings
# For solar panel cards: use photo-1509391366360-2e959784a276
# For inverter cards: use photo-1620027136027-e3f322c2a5bf
# For hero backgrounds: use either solar farm or rooftop solar
# For other context-specific images, use appropriate ones

def replace_images_in_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # First, handle product cards
    # Solar panel cards (look for "Solar Module" in nearby text or alt text)
    # Let's first find all img tags and check their context
    # Let's start by replacing all product card images
    # Solar panels first:
    solar_panel_url = "https://images.unsplash.com/photo-1509391366360-2e959784a276?auto=format&fit=crop&w=800&q=80"
    inverter_url = "https://images.unsplash.com/photo-1620027136027-e3f322c2a5bf?auto=format&fit=crop&w=800&q=80"
    solar_rooftop_url = "https://images.unsplash.com/photo-1516259762381-22954d7d3ad2?auto=format&fit=crop&w=1920&q=80"
    solar_farm_url = "https://images.unsplash.com/photo-1509391366360-2e959784a276?auto=format&fit=crop&w=1920&q=80"
    engineers_url = "https://images.unsplash.com/photo-1508514177221-188b1cf16e9d?auto=format&fit=crop&w=800&q=80"
    wind_turbines_url = "https://images.unsplash.com/photo-1466611653911-95081537e5b7?auto=format&fit=crop&w=800&q=80"

    # Now, let's process the content
    original_content = content

    # First, handle solar panel product cards (look for "Solar Module" in the vicinity)
    # Let's create a regex that captures img tags with picsum, and check the surrounding text for "Solar Module"
    # Let's split the content into sections and process product cards
    # Alternatively, let's replace all picsum images based on context
    # Let's start by replacing images in product cards
    # Let's look for product card patterns
    # Let's use a regex to find all <img> tags with picsum
    img_pattern = re.compile(r'<img[^>]*src="https://picsum\.photos/[^"]*"[^>]*>', re.IGNORECASE)

    # We need to process each match and decide what to replace it with
    # Let's get all matches
    matches = list(img_pattern.finditer(content))
    # We need to process in reverse order so that earlier replacements don't affect later indices
    for match in reversed(matches):
        # Get the surrounding context
        start_idx = max(0, match.start() - 200)
        end_idx = min(len(content), match.end() + 200)
        context = content[start_idx:end_idx]

        # Decide what to replace with
        replacement = solar_panel_url  # Default
        if "Solar Module" in context or "solar panel" in context.lower() or "solar panels" in context.lower():
            replacement = solar_panel_url
        elif "Inverter" in context:
            replacement = inverter_url
        elif "hero" in content[max(0, match.start() - 500):match.start()].lower() or "breadcrumb" in content[max(0, match.start() - 500):match.start()].lower():
            # Hero background
            # Check if it's a parallax img or div background
            if "parallax-img" in match.group(0):
                replacement = solar_farm_url
        # For other images, let's use appropriate ones based on alt text
        elif "engineer" in context.lower() or "installation" in context.lower():
            replacement = engineers_url
        elif "wind" in context.lower():
            replacement = wind_turbines_url
        elif "rooftop" in context.lower():
            replacement = solar_rooftop_url

        # Now, replace the src in the img tag
        img_tag = match.group(0)
        # Find the src attribute
        src_match = re.search(r'src="([^"]*)"', img_tag)
        if src_match:
            new_src = replacement
            new_img_tag = img_tag[:src_match.start(1)] + new_src + img_tag[src_match.end(1):]
            content = content[:match.start()] + new_img_tag + content[match.end():]

    # Write back the modified content
    if content != original_content:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Modified: {file_path}")
    else:
        print(f"No changes: {file_path}")

def main():
    html_dir = r"c:\Users\anmol\Downloads\stitch_sunergy_website_replica (1)\stitch_sunergy_website_replica"
    for filename in os.listdir(html_dir):
        if filename.endswith(".html") and filename != "index.html":
            file_path = os.path.join(html_dir, filename)
            replace_images_in_file(file_path)

if __name__ == "__main__":
    main()
