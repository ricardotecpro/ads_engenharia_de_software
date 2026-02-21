import re
import pathlib
from rich import print

def get_content_between(content: str, start_marker: str, end_markers: list) -> str:
    """Extract content between a start marker and any of the end markers."""
    start_index = content.find(start_marker)
    if start_index == -1:
        return ""
    
    # Find end of the line where marker was found to exclude the header itself
    line_end = content.find('\n', start_index)
    if line_end == -1:
        return ""
        
    content_start = line_end + 1
    
    # Find the earliest end marker
    end_index = len(content)
    for marker in end_markers:
        idx = content.find(marker, content_start)
        if idx != -1 and idx < end_index:
            end_index = idx
            
    return content[content_start:end_index].strip()

def refactor_lesson(lesson_path: pathlib.Path):
    """Refactor a single lesson file."""
    content = lesson_path.read_text(encoding='utf-8')
    lesson_num = re.search(r'aula-(\d+)', lesson_path.name).group(1)
    
    print(f"Processing Aula {lesson_num}...")

    # Define markers
    MARKER_SLIDES = "## 📽 Roteiro de Slides"
    MARKER_QUIZ = "## 📝 Quiz"
    MARKER_EXERCISES = "## 🛠 Exercícios"
    MARKER_PROJECT = "## 🚀 Projeto da Aula"
    
    # Markers that can end a section (including End of File)
    ALL_MARKERS = [MARKER_SLIDES, MARKER_QUIZ, MARKER_EXERCISES, MARKER_PROJECT, "---"]

    # Extract Sections
    slides_content = get_content_between(content, MARKER_SLIDES, ALL_MARKERS).strip()
    quiz_content = get_content_between(content, MARKER_QUIZ, ALL_MARKERS).strip()
    exercises_content = get_content_between(content, MARKER_EXERCISES, ALL_MARKERS).strip()
    project_content = get_content_between(content, MARKER_PROJECT, ALL_MARKERS).strip()

    # --- Write to Satellite Files ---

    # 1. Slides
    if slides_content:
        slide_path = pathlib.Path(f"docs/slides/src/slide-{lesson_num}.md")
        slide_path.parent.mkdir(parents=True, exist_ok=True)
        # Wrap content in a basic slide structure if it's just a list
        formatted_slides = f"# Slide {lesson_num}\n\n{slides_content}"
        slide_path.write_text(formatted_slides, encoding='utf-8')
        print(f"  -> Extracted Slides to {slide_path}")

    # 2. Quizzes
    if quiz_content:
        quiz_path = pathlib.Path(f"docs/quizzes/src/quiz-{lesson_num}.md")
        quiz_path.parent.mkdir(parents=True, exist_ok=True)
        formatted_quiz = f"# Quiz {lesson_num}\n\n{quiz_content}"
        quiz_path.write_text(formatted_quiz, encoding='utf-8')
        print(f"  -> Extracted Quiz to {quiz_path}")

    # 3. Exercises
    if exercises_content:
        # Note: Directory is docs/exercicios/ (plural, portuguese)
        ex_path = pathlib.Path(f"docs/exercicios/exercicio-{lesson_num}.md")
        ex_path.parent.mkdir(parents=True, exist_ok=True)
        formatted_ex = f"# Exercício {lesson_num}\n\n{exercises_content}"
        ex_path.write_text(formatted_ex, encoding='utf-8')
        print(f"  -> Extracted Exercises to {ex_path}")

    # 4. Projects
    if project_content:
        proj_path = pathlib.Path(f"docs/projetos/projeto-{lesson_num}.md")
        proj_path.parent.mkdir(parents=True, exist_ok=True)
        formatted_proj = f"# Projeto {lesson_num}\n\n{project_content}"
        proj_path.write_text(formatted_proj, encoding='utf-8')
        print(f"  -> Extracted Project to {proj_path}")

    # --- Update Main File ---
    # We want to keep headers up to the first extracted section.
    # Usually strict order: Obj -> Content -> Slides -> Quiz -> Ex -> Proj.
    # So we can just cut off at "## 📽 Roteiro de Slides" and append links.
    
    cutoff_index = content.find(MARKER_SLIDES)
    if cutoff_index != -1:
        new_content = content[:cutoff_index].strip()
        
        new_content += "\n\n---\n\n"
        new_content += f"## 📅 Atividades\n\n"
        
        # Add Links
        new_content += f"- [ ] **[Ver Slides da Aula](../slides/slide-{lesson_num}.html)**\n"
        new_content += f"- [ ] **[Fazer Quiz](../quizzes/quiz-{lesson_num}.md)**\n"
        new_content += f"- [ ] **[Praticar Exercícios](../exercicios/exercicio-{lesson_num}.md)**\n"
        new_content += f"- [ ] **[Realizar Projeto](../projetos/projeto-{lesson_num}.md)**\n"

        lesson_path.write_text(new_content, encoding='utf-8')
        print(f"  -> Updated {lesson_path}")
    else:
        print(f"  [yellow]Skipping {lesson_path.name} update (Slides marker not found)[/yellow]")


def main():
    print("[bold]Refactoring Content Separation[/bold]")
    aulas_dir = pathlib.Path("docs/aulas")
    for aula_file in sorted(aulas_dir.glob("aula-*.md")):
        refactor_lesson(aula_file)
    print("\n[green]Refactoring Complete![/green]")

if __name__ == "__main__":
    main()
