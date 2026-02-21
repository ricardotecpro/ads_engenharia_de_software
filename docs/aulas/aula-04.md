# Aula 04 – Requisitos de Software

## 🎯 Objetivos de Aprendizagem
- Entender o que são Requisitos de Software.
- Diferenciar Requisitos Funcionais de Não-Funcionais.
- Aprender a escrever Histórias de Usuário (User Stories).
- Compreender a importância do documento de requisitos.

## 📚 Conteúdo

### 1. O que são Requisitos?
Requisitos são as necessidades e condições que o software deve atender. É a tradução do que o cliente "quer" para o que o time "vai construir".

!!! info "Fator de Sucesso"
    Ter requisitos claros e validados é o passo mais importante para evitar o desperdício de tempo e dinheiro no desenvolvimento.

---

### 2. Tipos de Requisitos

#### A) Requisitos Funcionais (RF)
Descrevem o que o sistema **FAZ**. São as funcionalidades que o usuário vê e usa.

!!! tip "Exemplos de RF"
    - "O sistema deve enviar um e-mail de confirmação após o cadastro."
    - "O sistema deve permitir a exclusão de itens do carrinho."

#### B) Requisitos Não-Funcionais (RNF)
Descrevem **COMO** o sistema deve se comportar. São restrições técnicas e de qualidade.

!!! warning "Exemplos de RNF"
    - **Performance**: "O login deve ser processado em menos de 1 segundo."
    - **Segurança**: "Todas as senhas devem ser salvas com hash SHA-256."
    - **Disponibilidade**: "O sistema deve estar online 99.9% do tempo."

---

### 3. User Stories (Histórias de Usuário)
No desenvolvimento ágil, simplificamos os requisitos usando o formato:

> **Como um** `<tipo de usuário>`, **eu quero** `<ação>`, **para que** `<benefício>`.

<div class="termy" markdown>
```text
$ # Exemplo de User Story
$ # Como um: Estudante
$ # Eu quero: Marcar aulas como concluídas
$ # Para que: Eu possa acompanhar meu progresso no curso
```
</div>

---

## 📝 Exercícios Progressivos

1.  **[Básico]** Qual a principal diferença entre um RF e um RNF?
2.  **[Básico]** Escreva uma User Story para a funcionalidade de "Resetar Senha" de um app.
3.  **[Intermediário]** Classifique os itens abaixo como RF ou RNF:
    - ( ) "O app deve abrir em menos de 3 segundos."
    - ( ) "O usuário deve poder filtrar produtos por preço."
4.  **[Intermediário]** O que são "Critérios de Aceite" em uma User Story?
5.  **[Desafio]** Imagine um sistema de votação online. Liste 2 Requisitos Não-Funcionais CRÍTICOS para esse sistema e justifique sua escolha.

---

## 🚀 Mini-Projeto 04: Levantamento Inicial
Escolha um aplicativo que você usa muito (ex: Instagram, WhatsApp). Liste 3 Requisitos Funcionais e 2 Não-Funcionais que você percebe nele. Tente escrever um desses RFs no formato de User Story.

---

## 📅 Atividades

- [ ] :material-presentation: **[Ver Slides da Aula](../slides/slide-04.html)**
- [ ] :material-school: **[Fazer Quiz](../quizzes/quiz-04.md)**
- [ ] :material-dumbbell: **[Praticar Exercícios](../exercicios/exercicio-04.md)**
- [ ] :material-rocket: **[Realizar Projeto](../projetos/projeto-04.md)**
