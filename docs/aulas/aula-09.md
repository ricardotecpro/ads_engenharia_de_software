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

## 📽 Roteiro de Slides
- **Slide 1**: Qualidade de Software
- **Slide 2**: O que é Qualidade? (Requisitos + Expectativas).
- **Slide 3**: A trilogia do erro: Erro -> Defeito -> Falha.
- **Slide 4**: O papel do QA (Prevenção > Correção).
- **Slide 5**: Regra 1-10-100 (Custo da correção).
- **Slide 6**: Exemplos de falhas famosas de software.

---

## 📝 Quiz

**1. Um desenvolvedor estava cansado e digitou a fórmula de juros errada. Isso é um:**
A) Defeito.
B) Erro (Ação Humana).
C) Falha.
D) Acerto.

**2. O sistema calculou o valor errado para o cliente na tela. Isso é uma:**
A) Erro.
B) Defeito.
C) Falha (Comportamento observável).
D) Feature.

**3. Qual a diferença entre QA e Teste?**
A) QA foca em prevenir defeitos (processo); Teste foca em achar defeitos (produto).
B) QA é para hardware.
C) Teste é feito pelo cliente.
D) São sinônimos.

**4. Segundo a regra 1-10-100, quando é mais barato corrigir um problema?**
A) Na produção (quando o cliente usa).
B) Nos testes.
C) No início (Requisitos/Design).
D) Nunca.

**5. Um software perfeito é:**
A) Aquele sem nenhum bug (impossível na prática, mas almejado).
B) Aquele que atende aos requisitos e satisfaz o usuário.
C) Aquele feito em Python.
D) Aquele que nunca foi lançado.

**Gabarito:**
1-B, 2-C, 3-A, 4-C, 5-B

---

## 🛠 Exercícios
1.  **Classificação**: O programador esqueceu de converter uma data (`Erro`). O código ficou salvando o ano como 1900 (`Defeito`). O cliente viu sua idade como 123 anos (`Falha`). Identifique cada um no seu próprio exemplo.
2.  **Debate**: Por que corrigir um bug em produção custa 100x mais? (Pense em: parar o time, fazer patch, reputação da marca, dados corrompidos).
3.  **QA vs Teste**: Se você revisa o documento de requisitos para ver se falta algo, você está fazendo QA ou Teste de Código?

---

## 🚀 Projeto da Aula: Planejando a Qualidade
**Atividade da Aula:**
Como vamos garantir a qualidade do To-Do App?

1.  **Critérios de Aceite**: Revise os critérios que você criou na Aula 04. Eles são a base do teste.
2.  **Checklist de QA Manual**: Crie uma lista de checagem para ser feita ANTES de dizer que uma tarefa está pronta.
    - *Ex*:
        - [ ] Funciona no Chrome?
        - [ ] Funciona no Celular?
        - [ ] O que acontece se eu tentar criar uma tarefa sem título? (Teste Negativo)
3.  **Ação**: Adicione esse "Checklist de Qualidade" ao seu documento de projeto.
