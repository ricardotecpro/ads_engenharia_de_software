# Aula 06 – Arquitetura de Software

## 🎯 Objetivos de Aprendizagem
- Entender o conceito de Arquitetura de Software.
- Conhecer padrões arquiteturais comuns (Monólito, Microserviços).
- Entender a separação Frontend vs. Backend.
- Compreender MVC e Padrões de Camadas.

## 📚 Conteúdo

### 1. O que é Arquitetura?
Se a modelagem (Aula 05) é a planta baixa da casa, a Arquitetura é a estrutura e engenharia por trás. Define se será um prédio de aço, uma casa de madeira ou uma cabana.
- Define a organização fundamental do sistema.
- Difícil de mudar depois de pronto.

### 2. Monólito vs. Microserviços
#### Monólito (Tudo junto)
O sistema inteiro é um único bloco de código.
- **Vantagens**: Simples de desenvolver e implantar no início.
- **Desvantagens**: Se uma parte cai, tudo cai. Difícil de escalar.

#### Microserviços (Peças separadas)
O sistema é dividido em pequenos serviços independentes que conversam entre si (via API).
- **Vantagens**: Se o serviço de "Pagamento" cair, o "Catálogo" continua funcionando. Cada time cuida de um pedaço.
- **Desvantagens**: Muito mais complexo de gerenciar.

### 3. Client-Server (Cliente-Servidor)
A arquitetura mais comum na Web.
- **Client (Frontend)**: O que o usuário vê (Navegador, App Mobile).
- **Server (Backend)**: Onde os dados e a lógica vivem.
- Eles conversam via **HTTP** (Internet).

### 4. Padrões de Camadas (Layered)
Organizar o código em "fatias" para não virar uma bagunça.
- **Apresentação (UI)**: Botões, telas.
- **Lógica de Negócio**: Regras (ex: "Não pode sacar mais que o saldo").
- **Dados (Persistência)**: Salvar no Banco de Dados.

---

---

## 📅 Atividades

- [ ] **[Ver Slides da Aula](../slides/slide-06.html)**
- [ ] **[Fazer Quiz](../quizzes/quiz-06.md)**
- [ ] **[Praticar Exercícios](../exercicios/exercicio-06.md)**
- [ ] **[Realizar Projeto](../projetos/projeto-06.md)**
