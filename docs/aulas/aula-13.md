# Aula 13 – Gerenciamento de Projetos e Estimativas

## 🎯 Objetivos de Aprendizagem
- Entender o Triângulo de Ferro (Escopo, Tempo, Custo).
- Aprender o conceito de MVP (Minimum Viable Product).
- Conhecer técnicas de estimativa Ágil.
- Saber priorizar tarefas usando o método MoSCoW.

## 📚 Conteúdo

### 1. O Triângulo de Ferro
Em qualquer projeto de engenharia, você lida com três restrições interligadas. Se você mexer em uma, as outras serão afetadas.

1.  **Escopo**: O que será feito.
2.  **Tempo**: Qual o prazo.
3.  **Custo**: Quanto dinheiro e recursos temos.

!!! info "Equilíbrio Delicado"
    Se você quer aumentar o Escopo (fazer mais coisas) sem aumentar o Tempo (prazo), o Custo (esforço/equipe) obrigatoriamente terá que subir.

---

### 2. MVP (Mínimo Produto Viável)
O MVP não é um produto mal acabado, mas sim a versão mais simples que resolve o problema central do usuário.

!!! tip "Ideia Chave"
    Se você quer construir um carro, não comece fabricando uma roda. Comece com um skate (MVP), depois um patinete, até chegar ao carro. Assim você entrega valor desde o dia 1.

---

### 3. Priorização com MoSCoW
Como decidir o que entra no MVP?

-   **M**ust Have: Obrigatório (O sistema não funciona sem isso).
-   **S**hould Have: Importante (Mas o sistema sobrevive sem).
-   **C**ould Have: Desejável (Um "luxo" se sobrar tempo).
-   **W**on't Have: Não terá agora (Fica para a versão 2.0).

---

### 4. Estimativas no Terminal (TermynalJS)

<div class="termy" markdown>
```bash
$ # Rodando sessão de Planning Poker
$ planning-poker start --task "Criar Login"
$ # Dev 1: 3 pontos
$ # Dev 2: 5 pontos
$ # Dev 3: 13 pontos (Divergel!)
$ # Alinhamento: "Ah, esqueci da validação de 2 etapas!" -> Média: 8 pontos.
```
</div>

---

## 📝 Exercícios Progressivos

1.  **[Básico]** Quais são as 3 pontas do Triângulo de Ferro?
2.  **[Básico]** O que significa a sigla MVP?
3.  **[Intermediário]** Explique a diferença entre uma tarefa "Must Have" e uma "Should Have".
4.  **[Intermediário]** Por que usamos pontos (Story Points) em vez de horas para estimar tarefas no Ágil?
5.  **[Desafio]** Um cliente pede para adicionar uma funcionalidade complexa (Escopo) sem mudar a data de entrega (Tempo). Usando o Triângulo de Ferro, quais são suas opções como engenheiro?

---

## 🚀 Mini-Projeto 13: Meu Planejamento MoSCoW
Imagine que você vai criar um app de "Lista de Compras". Liste 2 itens para cada categoria do MoSCoW. O que é "Must Have" para o app ser útil?

---

## 📅 Atividades

- [ ] :material-presentation: **[Ver Slides da Aula](../slides/slide-13.html)**
- [ ] :material-school: **[Fazer Quiz](../quizzes/quiz-13.md)**
- [ ] :material-dumbbell: **[Praticar Exercícios](../exercicios/exercicio-13.md)**
- [ ] :material-rocket: **[Realizar Projeto](../projetos/projeto-13.md)**
