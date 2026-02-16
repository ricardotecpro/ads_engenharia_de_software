
import pathlib
import re

def fix_slide_content(md_path: pathlib.Path):
    content = md_path.read_text(encoding='utf-8')
    
    # Check if it's already in the correct format (contains "---")
    if '\n---\n' in content:
        print(f"Skipping {md_path.name} (already formatted)")
        return

    print(f"Fixing {md_path.name}...")
    
    new_lines = []
    
    # Add title slide if not present in the content (based on filename)
    # But usually the first item is the title slide.
    
    lines = content.split('\n')
    current_slide = []
    
    for line in lines:
        line = line.strip()
        if not line:
            continue
            
        # Match "- **Slide X: Title**"
        match = re.match(r'-\s*\*\*(Slide \d+: .+?)\*\*', line)
        if match:
            # If we have a previous slide, add it to new_lines with separator
            if current_slide:
                new_lines.extend(current_slide)
                new_lines.append('\n---\n') # Separator
                current_slide = []
            
            # Start new slide with the title as H2
            title = match.group(1).split(':', 1)[1].strip()
            current_slide.append(f"## {title}\n")
        
        # Match bullet points "- Content"
        elif line.startswith('- '):
            content_line = line[2:].strip()
            current_slide.append(f"- {content_line}")
        
        # Keep other lines (like top header) if they don't look like the summary list
        elif line.startswith('# '):
            # It's the main file header, maybe keep it as the first slide title
            # But the first slide usually covers it.
            # Let's add it as a standalone title slide if we want, or just ignore if it's "Slide XX"
            pass
            
    # Add the last slide
    if current_slide:
        new_lines.extend(current_slide)
    
    # Write back
    new_content = '\n'.join(new_lines)
    md_path.write_text(new_content, encoding='utf-8')

def main():
    src_dir = pathlib.Path('docs/slides/.src')
    if not src_dir.exists():
        print(f"Directory {src_dir} not found!")
        return

    for md_file in src_dir.glob('slide-*.md'):
        fix_slide_content(md_file)

if __name__ == '__main__':
    main()
