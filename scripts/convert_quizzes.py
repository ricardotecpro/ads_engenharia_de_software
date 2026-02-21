"""
Script para converter automaticamente todos os quizzes de markdown para HTML interativo
"""
import pathlib
import re
from rich import print
from rich.progress import track


def parse_quiz_markdown(content: str) -> list:
    """
    Parse quiz markdown format e extrai perguntas no formato texto
    
    Formato esperado:
    **1. Pergunta?**
    A) Opção A
    B) Opção B
    ...
    **Gabarito:**
    1-A, 2-B
    """
    questions = []
    
    # 1. Extrair Gabarito primeiro para saber as respostas
    gabarito_match = re.search(r'Gabarito:\*?\*?\s*\n?(.+)', content, re.IGNORECASE | re.DOTALL)
    answers_map = {}
    if gabarito_match:
        gabarito_text = gabarito_match.group(1).strip()
        # Parse "1-A, 2-B" or "1-A 2-B"
        # Regex finds pairs of Number + Buffer + Letter
        pairs = re.findall(r'(\d+)\s*[-:]\s*([A-D])', gabarito_text, re.IGNORECASE)
        for num, letter in pairs:
            answers_map[int(num)] = letter.upper()

    # 2. Extrair Perguntas
    # Regex flexível para "**1. Pergunta**" ou "1. Pergunta"
    question_pattern = r'(?:\*\*)?(\d+)\.\s+(.+?)(?:\*\*)?\n'
    
    current_pos = 0
    while True:
        match = re.search(question_pattern, content[current_pos:])
        if not match:
            break
            
        q_num = int(match.group(1))
        q_text = match.group(2).strip()
        start = current_pos + match.end()
        
        # Encontrar onde termina esta pergunta (começo da próxima ou Gabarito ou fim)
        next_match = re.search(question_pattern, content[start:])
        gabarito_start = re.search(r'Gabarito:', content[start:], re.IGNORECASE)
        
        end = len(content)
        if next_match:
            end = start + next_match.start()
        if gabarito_start and (start + gabarito_start.start() < end):
            end = start + gabarito_start.start()
            
        options_block = content[start:end]
        
        # Parse Opções A) B) C) D)
        options = []
        # Regex finds "A) Text"
        opt_matches = re.findall(r'([A-D])\)\s+(.+?)(?=\n[A-D]\)|\n\n|\Z)', options_block, re.DOTALL)
        
        correct_letter = answers_map.get(q_num, 'A') # Default to A if not found (avoid crash)
        
        for letter, text in opt_matches:
            is_correct = (letter.upper() == correct_letter)
            options.append({
                'text': text.strip(),
                'correct': is_correct,
                'letter': letter
            })
            
        if options:
            questions.append({
                'number': str(q_num),
                'text': q_text,
                'options': options
            })
            
        current_pos = end
        # Break if we reached gabarito or end
        if gabarito_start and (current_pos >= start + gabarito_start.start()):
            break

    return questions


def generate_quiz_html(quiz_number: int, questions: list) -> str:
    """Gera HTML completo do quiz"""
    
    # Cabeçalho
    html_parts = [
        f"# Quiz {quiz_number:02d} - Introdução\n",
        '\n--8<-- "assets/quiz.html"\n\n'
    ]
    
    # Gerar cada pergunta
    for q in questions:
        html_parts.append('<div class="quiz-container">\n')
        html_parts.append(f'  <div class="quiz-question">{q["number"]}. {q["text"]}</div>\n')
        
        for opt in q['options']:
            correct_attr = 'true' if opt['correct'] else 'false'
            feedback = f"✅ Correto! {opt['text']}" if opt['correct'] else f"Incorreto. Tente novamente."
            
            html_parts.append(
                f'  <div class="quiz-option" data-correct="{correct_attr}" '
                f'data-feedback="{feedback}">{opt["text"]}</div>\n'
            )
        
        html_parts.append('  <div class="quiz-feedback"></div>\n')
        html_parts.append('</div>\n\n')
    
    # Adicionar Gabarito
    html_parts.append('<hr>\n<details>\n<summary><strong>Gabarito:</strong></summary>\n<ul>\n')
    for q in questions:
        correct_opt = next((opt['text'] for opt in q['options'] if opt['correct']), "Nenhuma")
        html_parts.append(f'  <li>{q["number"]}- {correct_opt}</li>\n')
    html_parts.append('</ul>\n</details>\n')

    return ''.join(html_parts)


def convert_quiz(quiz_path: pathlib.Path) -> bool:
    """Converte um arquivo de quiz"""
    try:
        content = quiz_path.read_text(encoding='utf-8')
        
        # Parse perguntas
        questions = parse_quiz_markdown(content)
        
        if not questions:
            print(f"  [yellow]⚠[/yellow] Nenhuma pergunta encontrada em {quiz_path.name}")
            return False
        
        # Extrair número do quiz
        quiz_num = int(re.search(r'quiz-(\d+)', quiz_path.name).group(1))
        
        # Gerar HTML
        html_content = generate_quiz_html(quiz_num, questions)
        
        # Salvar em docs/quizzes (um nível acima de src)
        output_path = quiz_path.parent.parent / quiz_path.name
        output_path.write_text(html_content, encoding='utf-8')
        
        print(f"  [green]✓[/green] Converteu {quiz_path.name} -> {output_path} ({len(questions)} perguntas)")
        return True
        
    except Exception as e:
        print(f"  [red]✗[/red] Erro em {quiz_path.name}: {e}")
        return False


def convert_all_quizzes():
    """Converte todos os quizzes"""
    # Usar pasta .src como fonte
    quizzes_src_dir = pathlib.Path('docs/quizzes/src')
    
    if not quizzes_src_dir.exists():
        print("[yellow]⚠ Pasta docs/quizzes/src/ não encontrada. Criando...[/yellow]")
        quizzes_src_dir.mkdir(parents=True, exist_ok=True)
        print("[yellow]⚠ Por favor, coloque os arquivos markdown originais em docs/quizzes/src/[/yellow]")
        return
    
    print("\n[bold cyan]🧠 Convertendo Quizzes para HTML...[/bold cyan]")
    print(f"Fonte: {quizzes_src_dir}")
    
    quiz_files = sorted(quizzes_src_dir.glob('quiz-*.md'))
    
    if not quiz_files:
        print("[yellow]⚠ Nenhum arquivo de quiz encontrado em docs/quizzes/src/[/yellow]")
        return
    
    converted = 0
    for quiz_path in track(quiz_files, description="Processando quizzes..."):
        if convert_quiz(quiz_path):
            converted += 1
    
    print(f"\n[green]✓ {converted}/{len(quiz_files)} quizzes convertidos com sucesso![/green]")


def main():
    """Função principal"""
    print("[bold]🚀 Conversão Automática de Quizzes[/bold]")
    print("=" * 50)
    
    convert_all_quizzes()
    
    print("\n[green]✅ Conversão concluída![/green]")
    print("\n[cyan]💡 Dica:[/cyan] Teste os quizzes em http://localhost:8000/quizzes/")


if __name__ == '__main__':
    main()
