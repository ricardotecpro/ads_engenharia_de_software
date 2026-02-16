# Aula 15 – Manutenção e Evolução

## 🎯 Objetivos de Aprendizagem
- Entender que o software nunca está "pronto".
- Conhecer a diferença entre Manutenção Corretiva, Preventiva e Evolutiva.
- Entender o conceito de Refatoração.
- Analisar o conceito de Dívida Técnica (Technical Debt).

## 📚 Conteúdo

### 1. O Software Morre?
Diferente de uma ponte (que degrada sozinha com a chuva), o software só "estragar" se o ambiente mudar ou se tentarmos mudá-lo.
- **Lei de Lehman**: Um software que é usado precisa evoluir, senão torna-se obsoleto.

### 2. Tipos de Manutenção
- **Corretiva**: Consertar bugs (o "band-aid").
- **Adaptativa**: Mudar para usar novo SO ou Banco de Dados (ex: migrar para Windows 11).
- **Perfeccionista (Evolutiva)**: Adicionar novas funcionalidades ou melhorar performance.
- **Preventiva (Refatoração)**: Melhorar a estrutura do código antes que quebre.

### 3. Refatoração (Refactoring)
É limpar a cozinha depois de cozinhar. Alterar a estrutura interna do código sem mudar seu comportamento externo.
- Objetivo: Tornar o código mais fácil de entender e modificar.
- Quando fazer? O tempo todo (regra do escoteiro: deixe o código mais limpo do que encontrou).

### 4. Dívida Técnica (Technical Debt)
Às vezes, fazemos o código "rápido e sujo" para entregar logo. Isso é um empréstimo.
- O "juro" é a dificuldade extra de trabalhar nesse código depois.
- Se não pagarmos a dívida (refatorando), o projeto pode falir (ficar impossível de manter).

---

---

## 📅 Atividades

- [ ] **[Ver Slides da Aula](../slides/slide-15.html)**
- [ ] **[Fazer Quiz](../quizzes/quiz-15.md)**
- [ ] **[Praticar Exercícios](../exercicios/exercicio-15.md)**
- [ ] **[Realizar Projeto](../projetos/projeto-15.md)**
