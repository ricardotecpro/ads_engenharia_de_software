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

## 📽 Roteiro de Slides
- **Slide 1**: Design de Software
- **Slide 2**: O objetivo (Código limpo e sustentável).
- **Slide 3**: Coesão vs. Acoplamento (A regra de ouro).
- **Slide 4**: Princípios KISS e DRY.
- **Slide 5**: Introdução ao SOLID (Só os nomes).
- **Slide 6**: Exemplo Visual (Espaguete vs. Modular).

---

## 📝 Quiz

**1. O que é "Coesão" no design de software?**
A) Quando o código está todo junto num arquivo só.
B) Quando um módulo/classe foca em uma única responsabilidade bem definida.
C) Quando usamos cola para unir as páginas.
D) Quando o software não funciona.

**2. O que queremos em um bom sistema?**
A) Baixo Acoplamento e Alta Coesão.
B) Alto Acoplamento e Baixa Coesão.
C) Código Espaguete.
D) Bugs complexos.

**3. O que significa a sigla DRY?**
A) Do Repeat Yourself (Repita-se).
B) Don't Repeat Yourself (Não se repita - Evite duplicação).
C) Data Run Yard.
D) Dry Code (Código Seco).

**4. O princípio KISS sugere que:**
A) Devemos beijar o computador.
B) Devemos criar as soluções mais complexas possíveis.
C) Devemos manter as coisas simples (Keep It Simple).
D) Code is Stupid Simple.

**5. Qual a letra "S" do SOLID?**
A) Simple Code Principle.
B) Single Responsibility Principle (Princípio da Responsabilidade Única).
C) Super Class Principle.
D) Silicon Valley.

**Gabarito:**
1-B, 2-A, 3-B, 4-C, 5-B

---

## 🛠 Exercícios
1.  **Refatoração (Teórica)**: Você encontrou uma função de 500 linhas chamada `GerenciarUsuario` que cadastra, envia e-mail de boas-vindas, valida CPF e gera relatório. Usando o princípio da **Coesão**, como você dividiria essa função?
2.  **Identificando DRY**: Se você escreveu a lógica de calcular desconto de 10% em 5 lugares diferentes do código, o que acontece se o desconto mudar para 15%? Como o princípio DRY resolveria isso?
3.  **Monstro de Espaguete**: Pesquise o termo "Spaghetti Code" e escreva uma frase sobre como evitá-lo.

---

## 🚀 Projeto da Aula: Refatorando o Design
**Atividade da Aula:**
Vamos aplicar o DRY no nosso projeto teórico.

1.  **Cenário**: No nosso To-Do App, toda vez que uma tarefa é concluída, precisamos atualizar o contador de "Tarefas Pendentes" na tela. Isso acontece quando criamos, excluímos ou completamos uma tarefa.
2.  **Problema**: Se escrevermos o código de contar e atualizar a tela em todos esses lugares, ferimos o DRY.
3.  **Solução**: Crie uma função chamada `atualizarContador()`.
4.  **No Documento**: Escreva em pseudocódigo:
    ```
    função atualizarContador() {
       pendentes = contarTarefasNaoFeitas()
       tela.exibir(pendentes)
    }
    
    // Agora só chamamos a função:
    aoCriarTarefa -> atualizarContador()
    aoExcluirTarefa -> atualizarContador()
    ```
