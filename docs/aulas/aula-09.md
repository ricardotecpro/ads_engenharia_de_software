# Aula 09 – Qualidade de Software e QA

## 🎯 Objetivos de Aprendizagem
- Entender o conceito de Qualidade de Software.
- Diferenciar Error, Fault (Defeito) e Failure (Falha).
- Conhecer o papel de QA (Quality Assurance).
- Entender o custo de corrigir bugs tardiamente.

## 📚 Conteúdo

### 1. O que é Qualidade?
Um software tem qualidade quando ele **atende aos requisitos** (faz o que deve fazer) e **atende às expectativas** do usuário (é rápido, seguro e intuitivo).

!!! info "Foco no Valor"
    Não adianta ter um código tecnicamente perfeito se ele não resolve o problema do usuário ou se é impossível de usar.

---

### 2. A anatomia de um problema
Na engenharia, somos precisos com os termos para identificar a origem dos problemas:

1.  **Erro (Mistake)**: É o equívoco humano (ex: o dev esqueceu de validar um campo).
2.  **Defeito (Fault/Bug)**: É a "marquinha" deixada no código pelo erro.
3.  **Falha (Failure)**: É o comportamento visível (ex: o app fechou sozinho).

!!! tip "Causa e Efeito"
    **Humano erra** :material-arrow-right: **Código ganha um Defeito** :material-arrow-right: **Usuário percebe a Falha**.

---

### 3. A Regra 1-10-100
Quanto mais tarde você descobre um problema, mais caro ele custa.

-   **$1 na fase de Requisitos**: Basta apagar uma linha de texto.
-   **$10 na fase de Desenvolvimento**: Precisa reescrever código.
-   **$100 em Produção**: Custa reputação, suporte técnico e correções de emergência.

---

### 4. Simulação de Qualidade (TermynalJS)

<div class="termy" markdown>
```bash
$ # Rodando análise de bugs (Linting)
$ npm run lint
$ # Erro encontrado: Variável 'total' não definida. (Aula 09)
$ # Defeito corrigido. Qualidade aumentada em 5%!
$ # Rodando testes de regressão... Passou!
```
</div>

---

## 📝 Exercícios Progressivos

1.  **[Básico]** O que é Qualidade de Software para você?
2.  **[Básico]** Diferencie Erro de Falha.
3.  **[Intermediário]** Por que a fase de manutenção costuma ser a mais cara se não houver qualidade inicial?
4.  **[Intermediário]** Explique a regra 1-10-100 com suas próprias palavras.
5.  **[Desafio]** Você é o QA de um novo app de banco. Onde você focaria seus esforços para economizar mais dinheiro para a empresa? (Pense na regra 1-10-100).

---

## 🚀 Mini-Projeto 09: Plano de Prevenção
Imagine que você está criando um app de delivery. Liste 3 possíveis falhas que os usuários poderiam encontrar e sugira como evitá-las ainda na fase de design.

---

## 📅 Atividades

- [ ] :material-presentation: **[Ver Slides da Aula](../slides/slide-09.html)**
- [ ] :material-school: **[Fazer Quiz](../quizzes/quiz-09.md)**
- [ ] :material-dumbbell: **[Praticar Exercícios](../exercicios/exercicio-09.md)**
- [ ] :material-rocket: **[Realizar Projeto](../projetos/projeto-09.md)**
