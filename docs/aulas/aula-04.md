# Aula 04 – Requisitos de Software

## 🎯 Objetivos de Aprendizagem
- Entender o que são Requisitos de Software.
- Diferenciar Requisitos Funcionais de Não-Funcionais.
- Aprender a escrever Histórias de Usuário (User Stories).
- Compreender a importância do documento de requisitos.

## 📚 Conteúdo

### 1. O que são Requisitos?
Requisitos são as necessidades e condições que o software deve atender. É a tradução do que o cliente "quer" para o que o time "vai construir".
- **Sem requisitos claros** = Projeto fracassado (O famoso balanço na árvore).

### 2. Tipos de Requisitos
#### A) Requisitos Funcionais (RF)
Descrevem o que o sistema **FAZ**. São as funcionalidades perceptíveis pelo usuário.
- *Exemplo*: "O sistema deve permitir cadastrar um novo cliente."
- *Exemplo*: "O sistema deve calcular o total da compra."

#### B) Requisitos Não-Funcionais (RNF)
Descrevem **COMO** o sistema deve ser. São restrições e qualidades (performance, segurança, usabilidade).
- *Exemplo*: "O sistema deve carregar qualquer página em menos de 2 segundos." (Performance)
- *Exemplo*: "O sistema deve funcionar em celulares Android e iOS." (Portabilidade)
- *Exemplo*: "A senha deve ser criptografada." (Segurança)

### 3. User Stories (Histórias de Usuário)
No modelo Ágil, usamos User Stories para descrever requisitos de forma simples, focada no valor para o usuário.
**Modelo**:
`Como um <tipo de usuário>, eu quero <ação>, para que <benefício>.`

*Exemplo*:
"Como um **usuário do To-Do App**, eu quero **criar uma nova tarefa**, para que **eu não esqueça meus compromissos**."

### 4. Critérios de Aceite
Complementam a User Story definindo quando ela está "pronta".
*Ex para "Criar Tarefa"*:
- O campo de título é obrigatório.
- A data de vencimento é opcional.
- Ao salvar, deve aparecer na lista principal.

---

## 📽 Roteiro de Slides
- **Slide 1**: Requisitos de Software
- **Slide 2**: Funcionais vs. Não-Funcionais (O que faz vs. Como é).
- **Slide 3**: Exemplos de RF e RNF.
- **Slide 4**: User Stories (Como um... Quero... Para...).
- **Slide 5**: Critérios de Aceite (O "Done").
- **Slide 6**: A importância de requisitos claros (Evitar retrabalho).

---

## 📝 Quiz

**1. "O sistema deve enviar um e-mail de confirmação de cadastro". Isso é um:**
A) Requisito Não-Funcional.
B) Requisito Funcional.
C) Bug.
D) User Story.

**2. "O sistema deve suportar 1 milhão de usuários simultâneos". Isso é um:**
A) Requisito Não-Funcional (Performance).
B) Requisito Funcional.
C) Requisito de Design.
D) Exagero.

**3. Qual a estrutura correta de uma User Story?**
A) Quero <ação>, Como <usuário>, Para <benefício>.
B) Como <usuário>, Eu quero <ação>, Para que <benefício>.
C) O sistema deve <ação>.
D) O usuário precisa de <ação>.

**4. Para que servem os Critérios de Aceite?**
A) Para o cliente aceitar pagar mais.
B) Para definir as regras técnicas do banco de dados.
C) Para definir claramente quando uma história está concluída e correta.
D) Para nada.

**5. Qual o maior risco de requisitos mal definidos?**
A) O programador ficar entediado.
B) Construir o software errado, desperdiçando tempo e dinheiro.
C) O computador travar.
D) A Internet cair.

**Gabarito:**
1-B, 2-A, 3-B, 4-C, 5-B

---

## 🛠 Exercícios
1.  **Classificação**: Classifique os itens abaixo em RF (Funcional) ou RNF (Não-Funcional):
    - "O site deve ter fundo azul."
    - "O usuário pode recuperar sua senha via e-mail."
    - "O sistema deve rodar 24/7 sem cair."
    - "O sistema deve calcular juros compostos."
    
2.  **Escrita de User Story**: O To-Do App precisa de um "Modo Noturno". Escreva isso como uma User Story seguindo o modelo.

3.  **Critérios de Aceite**: Defina 3 critérios para a funcionalidade "Excluir Tarefa". (Ex: O sistema deve pedir confirmação? O que acontece com a tarefa depois de excluída?)

---

## 🚀 Projeto da Aula: Definindo Histórias
**Atividade da Aula:**
Vamos detalhar a **Sprint 1** (MVP) usando User Stories.

1.  Pegue os itens que você colocou na coluna "To Do" do seu quadro (Aula 03).
2.  Reescreva cada um deles no formato de User Story.
    - *Ex*: De "Login" para "Como um usuário cadastrado, quero fazer login, para acessar minhas tarefas privadas."
3.  Adicione pelo menos 2 Critérios de Aceite para cada história.
    - *Ex*: "Login com senha errada deve mostrar mensagem de erro."
4.  Identifique 1 Requisito Não-Funcional para seu app (ex: ele deve funcionar offline?).
