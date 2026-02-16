
from pathlib import Path
import os

def check_slide_content():
    cwd = os.getcwd()
    print(f"Current Working Directory: {cwd}")
    
    slides_dir = Path("docs/slides")
    slide_path = slides_dir / "slide-04.md"
    
    print(f"Checking file: {slide_path.absolute()}")
    
    if not slide_path.exists():
        print("File does not exist!")
        return
        
    content = slide_path.read_text(encoding='utf-8')
    print("-" * 20)
    print(f"Content length: {len(content)}")
    print("First 100 characters:")
    print(content[:100])
    print("-" * 20)
    
    if '---' in content or '#' in content:
        print("VALID: Contains '---' or '#'")
    else:
        print("INVALID: Missing markdown markers")

if __name__ == "__main__":
    check_slide_content()
