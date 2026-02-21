# Aula 14 – Documentação Técnica

## 🎯 Objetivos de Aprendizagem
- Entender por que documentar é essencial (e não perda de tempo).
- Conhecer os tipos de documentação (Técnica vs. Usuário).
- Aprender a escrever um bom README.
- Conhecer o poder do Markdown.

## 📚 Conteúdo

### 1. "O código se documenta sozinho"? (Spoiler: Não!)
Um código limpo ajuda muito, mas ele não explica o **PORQUÊ** das decisões, nem como instalar e rodar o projeto.

!!! info "Amor ao Próximo"
    Documentação é um ato de respeito com os outros desenvolvedores (e com o seu "eu" do futuro). Ninguém gosta de herdar um projeto sem manual.

---

### 2. Tipos de Documentação

#### A) Documentação de Usuário
Focada em quem vai usar o software.
-   **Guia de Início Rápido**: Como começar?
-   **FAQ**: Dúvidas comuns.

#### B) Documentação Técnica
Focada em quem vai manter o software.
-   **README**: O cartão de visitas do projeto.
-   **Documentação de API**: Como outros sistemas se conectam ao seu (ex: Swagger).
-   **Diagramas**: Arquitetura visual (Aula 05 e 06).

---

### 3. O Poder do Markdown
Markdown é uma linguagem simples de marcação que se tornou o padrão para documentar software.

!!! tip "Dica de Escrita"
    Use `#` para títulos, `**negrito**` para destaque e `` `código` `` para comandos. É leve e renderiza em qualquer lugar (GitHub, MkDocs, etc.).

---

### 4. Criando um README no Terminal (TermynalJS)

<div class="termy" markdown>
```bash
$ touch README.md
$ echo "# Nome do Meu Projeto" >> README.md
$ echo "## Como instalar" >> README.md
$ echo "npm install" >> README.md
$ cat README.md
$ # Resultado: Arquivo README criado com sucesso!
```
</div>

---

## 📝 Exercícios Progressivos

1.  **[Básico]** Qual a principal função de um arquivo README?
2.  **[Básico]** Cite um exemplo de documentação para usuário.
3.  **[Intermediário]** Por que comentar o código deve ser feito "com moderação"? (O que devemos comentar de verdade?).
4.  **[Intermediário]** O que significa "Autodocumentação" em código limpo?
5.  **[Desafio]** Você entrou em um projeto legado sem nenhuma documentação. Quais seriam os 3 primeiros passos que você daria para tentar entender o sistema?

---

## 🚀 Mini-Projeto 14: Documentando meu Trabalho
Crie um arquivo chamado `ABOUT_ME.md` usando sintaxe Markdown. Escreva uma breve biografia, liste 3 habilidades técnicas suas em uma lista e adicione uma frase em negrito sobre seu objetivo no curso.

---

## 📅 Atividades

- [ ] :material-presentation: **[Ver Slides da Aula](../slides/slide-14.html)**
- [ ] :material-school: **[Fazer Quiz](../quizzes/quiz-14.md)**
- [ ] :material-dumbbell: **[Praticar Exercícios](../exercicios/exercicio-14.md)**
- [ ] :material-rocket: **[Realizar Projeto](../projetos/projeto-14.md)**
