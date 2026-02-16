"""
Testes automatizados para verificar interatividade de quizzes
"""
import pytest
import re
from playwright.sync_api import Page, expect


class TestQuizzes:
    """Testes para quizzes interativos"""

    def test_quiz_index_loads(self, page_with_base_url: Page, base_url: str):
        """Verifica se a página de índice de quizzes carrega"""
        page = page_with_base_url
        page.goto(f"{base_url}/quizzes/")
        
        # Verifica se não é 404
        expect(page).not_to_have_title("404")
        expect(page.locator("h1")).to_contain_text("Quiz")

    @pytest.mark.parametrize("quiz_number", range(1, 17))
    def test_quiz_page_loads(self, page_with_base_url: Page, base_url: str, quiz_number: int):
        """Verifica se cada página de quiz carrega sem erro 404"""
        page = page_with_base_url
        quiz_url = f"{base_url}/quizzes/quiz-{quiz_number:02d}/"
        
        page.goto(quiz_url)
        
        # Verifica se não é 404
        expect(page).not_to_have_title("404")

    def test_quiz_has_text_content(self, page_with_base_url: Page, base_url: str):
        """Verifica se o quiz 01 tem conteúdo de texto (perguntas e gabarito)"""
        page = page_with_base_url
        page.goto(f"{base_url}/quizzes/quiz-01/")
        
        # Verifica cabeçalho Quiz
        expect(page.locator("h1")).to_contain_text("Quiz")
        
        # Verifica se há perguntas (pelo menos a string "1.")
        # Como é markdown, deve estar em <p><strong>1. ...
        body_text = page.locator("body")
        expect(body_text).to_contain_text("1.")
        expect(body_text).to_contain_text("Gabarito:")
        expect(body_text).to_contain_text("1-")
