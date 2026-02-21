# Aula 12 – Segurança de Software

## 🎯 Objetivos de Aprendizagem
- Entender o conceito de Security by Design.
- Conhecer a Tríade CIA (Confidencialidade, Integridade e Disponibilidade).
- Diferenciar Autenticação de Autorização.
- Conhecer os principais riscos da OWASP (Injeção).

## 📚 Conteúdo

### 1. Security by Design
Muitos sistemas falham porque a segurança é pensada apenas no final. A engenharia moderna exige que a segurança faça parte do design inicial.

!!! info "Mentalidade de Segurança"
    Segurança não é um produto que você compra, é um processo que você constrói desde a primeira linha de código.

---

### 2. A Tríade CIA (Confidencialidade, Integridade e Disponibilidade)
Os 3 pilares fundamentais da segurança da informação:

1.  **Confidencialidade**: Garante que o dado só seja visto por quem tem permissão.
2.  **Integridade**: Garante que a informação não seja alterada indevidamente.
3.  **Disponibilidade**: Garante que o sistema esteja acessível quando o usuário precisar.

!!! tip "Dica Didática"
    **C** (Segredo) :material-arrow-right: **I** (Verdade) :material-arrow-right: **A** (Acesso).

---

### 3. Autenticação vs. Autorização
Termos que parecem iguais, mas têm papéis diferentes:

-   **Autenticação**: "Quem é você?" (Login, Senha, Biometria).
-   **Autorização**: "O que você pode fazer?" (O usuário pode ler, mas só o admin pode apagar).

---

### 4. Simulação de Segurança (TermynalJS)

<div class="termy" markdown>
```bash
$ # Rodando Scanner de Vulnerabilidades
$ security-audit ./projeto
$ # [ALERT] Vulnerabilidade encontrada no campo de Busca!
$ # Risco: SQL Injection (Injeção de Código)
$ # Sugestão: Use consultas parametrizadas.
```
</div>

---

## 📝 Exercícios Progressivos

1.  **[Básico]** O que significa a sigla CIA em segurança?
2.  **[Básico]** Qual a diferença entre Autenticação e Autorização?
3.  **[Intermediário]** Explique o conceito de "Security by Design".
4.  **[Intermediário]** O que é um ataque de Injeção (SQL Injection)?
5.  **[Desafio]** Imagine que um site de notícias sofreu um ataque e todas as notícias foram apagadas. Qual pilar da tríade CIA foi mais afetado? Justifique.

---

## 🚀 Mini-Projeto 12: O Checkup de Segurança
Escolha um aplicativo bancário ou de e-commerce que você usa. Liste quais métodos de Autenticação (ex: senha, biometria, Token) ele utiliza para garantir a Confidencialidade dos seus dados.

---

## 📅 Atividades

- [ ] :material-presentation: **[Ver Slides da Aula](../slides/slide-12.html)**
- [ ] :material-school: **[Fazer Quiz](../quizzes/quiz-12.md)**
- [ ] :material-dumbbell: **[Praticar Exercícios](../exercicios/exercicio-12.md)**
- [ ] :material-rocket: **[Realizar Projeto](../projetos/projeto-12.md)**
