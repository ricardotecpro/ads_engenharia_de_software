# Aula 08 – Design de Software e SOLID

## 🎯 Objetivos de Aprendizagem
- Entender os princípios de um bom design de software.
- Compreender os conceitos de Acoplamento e Coesão.
- Introduzir o princípio KISS (Keep It Simple, Stupid) e DRY (Don't Repeat Yourself).
- Conhecer os Princípios SOLID (visão geral).

## 📚 Conteúdo

### 1. Design de Software
Design não é (só) sobre cores. É sobre como organizar o código para que ele não se torne um "Monstro de Espaguete" impossível de dar manutenção.

### 2. Conceitos Chave
#### Coesão (Bom)
Uma peça de software (função, classe) deve fazer **uma única coisa** e fazê-la bem.
- *Exemplo Ruim*: Uma função `processarTudo()` que calcula imposto, salva no banco e envia e-mail.
- *Exemplo Bom*: 3 funções separadas: `calcularImposto()`, `salvarPedido()`, `enviarEmail()`.

#### Acoplamento (Ruim quando alto)
O quanto uma peça depende da outra. Se você muda A e precisa mudar B, C e D, o acoplamento está alto.
- Queremos **Baixo Acoplamento** e **Alta Coesão**.

### 3. Princípios Básicos
- **KISS (Keep It Simple, Stupid)**: A solução mais simples quase sempre é a melhor. Não complique.
- **DRY (Don't Repeat Yourself)**: Nunca copie e cole código. Se a lógica se repete, crie uma função.

### 4. SOLID (Visão Geral)
São 5 mandamentos da Orientação a Objetos:
- **S**RP (Single Responsibility): Uma classe deve ter um único motivo para mudar.
- **O**CP (Open/Closed): Aberto para extensão, fechado para modificação.
- **L**SP (Liskov): Filhos devem substituir pais sem quebrar nada.
- **I**SP (Interface Segregation): Interfaces específicas são melhores que uma geral.
- **D**IP (Dependency Inversion): Dependa de abstrações, não de implementações.

---

---

## 📅 Atividades

- [ ] **[Ver Slides da Aula](../slides/slide-08.html)**
- [ ] **[Fazer Quiz](../quizzes/quiz-08.md)**
- [ ] **[Praticar Exercícios](../exercicios/exercicio-08.md)**
- [ ] **[Realizar Projeto](../projetos/projeto-08.md)**
