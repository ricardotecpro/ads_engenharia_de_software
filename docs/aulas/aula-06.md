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

## 📽 Roteiro de Slides
- **Slide 1**: Arquitetura de Software
- **Slide 2**: O conceito (Estrutura fundamental).
- **Slide 3**: Monólito (Blocão único).
- **Slide 4**: Microserviços (Muitas partes pequenas).
- **Slide 5**: Cliente-Servidor (A base da Web).
- **Slide 6**: Camadas (UI, Lógica, Dados).

---

## 📝 Quiz

**1. Qual a principal característica de uma arquitetura Monolítica?**
A) O sistema é composto por milhares de pequenos serviços.
B) O sistema é um único bloco de código onde tudo está junto.
C) O sistema não usa banco de dados.
D) O sistema só roda em celulares.

**2. Na arquitetura Cliente-Servidor, o que o "Cliente" geralmente faz?**
A) Armazena todos os dados do mundo.
B) Processa pagamentos bancários sozinho.
C) Envia requisições e exibe a interface para o usuário.
D) Gera energia para o servidor.

**3. Qual a vantagem dos Microserviços?**
A) São extremamente simples de configurar.
B) Se um serviço falhar, o resto do sistema pode continuar funcionando.
C) Não precisam de internet.
D) Usam menos memória sempre.

**4. O que é a camada de "Lógica de Negócio"?**
A) A parte visual (cores e botões).
B) Onde ficam as regras do sistema (ex: cálculos, validações).
C) O cabo de rede.
D) A marca do computador.

**5. Arquitetura de Software é fácil de mudar depois que o projeto está pronto?**
A) Sim, muda-se em 5 minutos.
B) Não, geralmente é caro e difícil (como mudar a fundação de um prédio).
C) Depende da cor do software.
D) Arquitetura não existe.

**Gabarito:**
1-B, 2-C, 3-B, 4-B, 5-B

---

## 🛠 Exercícios
1.  **Análise de App**: Pense no Uber. O App no seu celular é o **Cliente** ou o **Servidor**? Onde ficam guardados os dados dos motoristas?
2.  **Desenho**: Desenhe três caixas empilhadas representando as camadas: Apresentação (Topo), Lógica (Meio) e Dados (Base). Onde você colocaria o código que verifica se a senha do usuário tem 8 dígitos?
3.  **Reflexão**: Por que a Netflix usa Microserviços? (Dica: Imagine milhões de pessoas assistindo coisas diferentes ao mesmo tempo. Se o módulo de "Legendas" falhar, o filme deve parar?).

---

## 🚀 Projeto da Aula: Definindo a Arquitetura
**Atividade da Aula:**
Vamos definir a arquitetura do To-Do App.

1.  **Tipo**: Vamos usar uma arquitetura **Web Simples (SPA - Single Page Application)**.
    - **Frontend**: HTML/JS (simulado no navegador).
    - **Backend**: Simulado (Local Storage do navegador).
2.  **Desenho da Arquitetura**:
    - Desenhe um quadrado "Navegador" contendo "HTML" e "JavaScript".
    - Desenhe um "Banco de Dados Local" dentro do navegador.
    - Isso mostra que, no nosso MVP, não teremos servidor externo (Serverless/Local).
3.  **Decisão**: Escreva no seu documento de projeto: "Arquitetura escolhida: Local/Client-side apenas". Justificativa: "Simplicidade para aprender e custo zero".
