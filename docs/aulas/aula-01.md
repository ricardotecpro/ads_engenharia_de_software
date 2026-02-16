# Aula 01 – Fundamentos da Engenharia de Software

## 🎯 Objetivos de Aprendizagem
- Compreender o que é Engenharia de Software e sua importância.
- Diferenciar "programação" (coding) de "engenharia de software".
- Conhecer o Ciclo de Vida de Desenvolvimento de Software (SDLC).
- Entender as fases fundamentais da construção de um software.

## 📚 Conteúdo

### 1. O que é Engenharia de Software?
Engenharia de Software é a aplicação de uma abordagem sistemática, disciplinada e quantificável para o desenvolvimento, operação e manutenção de software. Diferente de apenas escrever código, ela se preocupa com:
- **Qualidade**: O software funciona como esperado? É seguro?
- **Prazo e Custo**: O projeto será entregue no tempo e orçamento previstos?
- **Manutenibilidade**: O código pode ser entendido e alterado por outras pessoas no futuro?

> "Software Engineering is programming integrated over time." — Titus Winters (Google)

### 2. A Crise do Software e a Necessidade de Processos
Historicamente, muitos projetos de software falhavam (estouravam prazos, orçamentos ou não funcionavam). Isso levou à **Crise do Software**, que impulsionou a criação de métodos para organizar o trabalho.

### 3. O Ciclo de Vida de Desenvolvimento de Software (SDLC)
O SDLC (Software Development Life Cycle) é a estrutura que define as etapas envolvidas na criação de um software. As fases clássicas são:

1.  **Levantamento de Requisitos**: Entender O QUE deve ser construído (ex: "O usuário precisa fazer login").
2.  **Análise e Design**: Planejar COMO será construído (ex: "Usaremos um banco de dados SQL e uma interface web").
3.  **Implementação (Codificação)**: Escrever o código de fato.
4.  **Testes (Verificação)**: Garantir que não há erros (bugs).
5.  **Implantação (Deploy)**: Colocar o software no ar para o usuário.
6.  **Manutenção**: Corrigir problemas e adicionar novas funcionalidades após o lançamento.

### 4. Analogia: Construindo uma Casa
- **Requisitos**: Conversar com o arquiteto sobre quantos quartos a casa terá.
- **Design**: Desenhar a planta baixa e escolher os materiais.
- **Implementação**: Pedreiros levantando paredes e instalando encanamento.
- **Testes**: Verificar se as luzes acendem e se não há vazamentos.
- **Implantação**: Entregar as chaves ao dono.
- **Manutenção**: Pintar paredes descascadas ou consertar uma telha quebrada anos depois.

---

## 📽 Roteiro de Slides
- **Slide 1: Capa**
    - Título: Fundamentos da Engenharia de Software
    - Subtítulo: Aula 01
- **Slide 2: Definição**
    - Engenharia de Software vs. Programação Simples
    - Foco em qualidade, prazo e manutenção.
- **Slide 3: O Ciclo de Vida (SDLC)**
    - Diagrama circular com as 6 fases.
    - Requisitos -> Design -> Código -> Teste -> Deploy -> Manutenção.
- **Slide 4: Analogia da Casa**
    - Comparação visual entre construir software e construir uma casa.
- **Slide 5: Conclusão**
    - Software é mais do que código; é processo e disciplina.

---

## 📝 Quiz

**1. Qual é o principal objetivo da Engenharia de Software?**
A) Escrever código o mais rápido possível, sem se preocupar com erros.
B) Aplicar uma abordagem sistemática e disciplinada para o desenvolvimento de software.
C) Criar apenas jogos de computador.
D) Consertar computadores quebrados (hardware).

**2. O que significa a sigla SDLC?**
A) Software Design Leveled Code
B) System Development Linear Code
C) Software Development Life Cycle (Ciclo de Vida de Desenvolvimento de Software)
D) Super Dynamic Life Cycle

**3. Em qual fase do SDLC definimos "O QUE" será construído?**
A) Testes
B) Implementação
C) Levantamento de Requisitos
D) Manutenção

**4. O que ocorre na fase de "Manutenção"?**
A) O software é deletado.
B) O software é planejado do zero.
C) Correções e melhorias são feitas após o software estar em uso.
D) Os desenvolvedores tiram férias.

**5. Qual a diferença principal entre Programação e Engenharia de Software?**
A) Programação é apenas escrever código; Engenharia envolve todo o ciclo de vida e gestão.
B) Não há diferença, são sinônimos.
C) Engenharia de Software é apenas para hardware.
D) Programação é mais difícil que Engenharia.

**Gabarito:**
1-B, 2-C, 3-C, 4-C, 5-A

---

## 🛠 Exercícios
1.  **Identificação de Fases**: Pense em um aplicativo que você usa (ex: Instagram). Liste uma atividade que provavelmente ocorreu na fase de *Design* e uma na fase de *Testes* desse app.
2.  **Cenário de Erro**: Se um erro grave é descoberto apenas na fase de *Implantação*, qual fase anterior provavelmente falhou em detectá-lo? Por que corrigir agora é mais caro?
3.  **Debate**: Por que não devemos pular direto para a fase de *Codificação* sem fazer *Requisitos* ou *Design*?

---

## 🚀 Projeto da Aula: To-Do App (Início)
Neste curso, vamos simular o desenvolvimento de um **Sistema de Gerenciamento de Tarefas (To-Do App)** completo.

**Atividade da Aula:**
- **Papel**: Você é o Engenheiro de Software responsável.
- **Tarefa**: Definir o escopo inicial (Requisitos de Alto Nível).
- **Ação**: Crie um documento de texto simples listando 3 funcionalidades essenciais que um App de Tarefas DEVE ter para ser útil (ex: "Adicionar tarefa"). Isso será a base para as próximas aulas.
