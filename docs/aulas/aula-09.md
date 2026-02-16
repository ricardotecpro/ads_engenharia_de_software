# Aula 09 – Qualidade de Software e QA

## 🎯 Objetivos de Aprendizagem
- Entender o conceito de Qualidade de Software.
- Diferenciar Error, Fault (Defeito) e Failure (Falha).
- Conhecer o papel de QA (Quality Assurance).
- Entender o custo de corrigir bugs tardiamente.

## 📚 Conteúdo

### 1. O que é Qualidade?
Um software tem qualidade quando ele **atende aos requisitos** (faz o que deve fazer) e **atende às expectativas** do usuário (não trava, é rápido, é seguro).
- Não adianta ter código lindo se o botão de comprar não funciona.

### 2. Conceitos de "Erro"
Na engenharia, somos precisos com os termos:
1.  **Erro (Mistake)**: Ação humana errada.
    - *Ex*: O programador esqueceu um ponto-e-vírgula.
2.  **Defeito (Fault/Bug)**: O resultado do erro no código.
    - *Ex*: O código tem um loop infinito.
3.  **Falha (Failure)**: O comportamento errado percebido pelo usuário.
    - *Ex*: O site travou quando cliquei em "Salvar".

`Pessoa erra -> Cria Defeito -> Causa Falha.`

### 3. Quality Assurance (QA)
Garantia de Qualidade não é só testar no final. É um conjunto de atividades para garantir que o processo de desenvolvimento gere produtos bons.
- **QA (Processo)**: Foco em prevenir defeitos.
- **Teste (Produto)**: Foco em encontrar defeitos.

### 4. A Regra 1-10-100
Quanto mais tarde você descobre um bug, mais caro ele é para corrigir.
- Descobrir na fase de **Requisitos**: Custa $1.
- Descobrir na fase de **Testes**: Custa $10.
- Descobrir na **Produção** (Cliente achou): Custa $100 (ou o fim da reputação da empresa).

---

---

## 📅 Atividades

- [ ] **[Ver Slides da Aula](../slides/slide-09.html)**
- [ ] **[Fazer Quiz](../quizzes/quiz-09.md)**
- [ ] **[Praticar Exercícios](../exercicios/exercicio-09.md)**
- [ ] **[Realizar Projeto](../projetos/projeto-09.md)**
