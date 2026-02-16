# Aula 11 – DevOps e CI/CD

## 🎯 Objetivos de Aprendizagem
- Entender o que é DevOps (Cultura).
- Compreender Integração Contínua (CI).
- Compreender Entrega Contínua (CD).
- Conhecer o conceito de Pipeline de Automação.

## 📚 Conteúdo

### 1. O Problema "Funciona na minha máquina"
Antigamente, Desenvolvedores (Dev) criavam o  software e jogavam por cima do muro para Operações (Ops) instalar.
- Resultado: Conflitos, demoras e culpa ("Foi culpa do servidor!", "Não, foi culpa do código!").

### 2. DevOps (Dev + Ops)
DevOps não é uma cargo, é uma cultura. É a união de pessoas, processos e ferramentas para entregar software com velocidade e qualidade.
- **Objetivo**: Diminuir o tempo entre "Tive uma ideia" e "O cliente está usando".

### 3. CI/CD: A Esteira de Automação
Imagine uma fábrica de carros robotizada. Isso é CI/CD.

#### CI (Continuous Integration)
- Todo código novo é integrado ao projeto principal frequentemente.
- Robôs rodam os testes automaticamente.
- Se quebrar algo, o time para e conserta na hora.

#### CD (Continuous Delivery/Deployment)
- Após passar no CI, o código é preparado automaticamente para ir para produção.
- **Delivery**: Botão "Deploy" manual mas automatizado por trás.
- **Deployment**: Vai direto para o ar sem intervenção humana.

### 4. O Pipeline
O caminho que o código percorre:
1.  Dev faz `git push`.
2.  **Build**: O robô compila o código.
3.  **Test**: O robô roda os testes unitários.
4.  **Deploy**: O robô atualiza o site.

Se qualquer passo falhar, o processo para (Stop the Line).

---

## 📽 Roteiro de Slides
- **Slide 1**: DevOps e CI/CD
- **Slide 2**: O Muro da Confusão (Dev vs Ops).
- **Slide 3**: Cultura DevOps (Colaboração e Automação).
- **Slide 4**: O que é CI (Integração Contínua - Testes).
- **Slide 5**: O que é CD (Entrega Contínua - Deploy).
- **Slide 6**: Exemplo visual de Pipeline (Build -> Test -> Deploy).

---

## 📝 Quiz

**1. O que significa DevOps?**
A) Desenvolvimento de Operações Secretas.
B) Development + Operations (União de Desenvolvimento e Operações).
C) Um novo sistema operacional.
D) Departamento de Vendas.

**2. Qual o principal objetivo do DevOps?**
A) Criar barreiras entre os times.
B) Entregar software com mais velocidade e qualidade através da colaboração e automação.
C) Eliminar todos os gerentes.
D) Usar computadores mais rápidos.

**3. O que acontece na etapa de "CI" (Integração Contínua)?**
A) O código é misturado e testado automaticamente com frequência.
B) O cliente testa o software.
C) O computador é reiniciado.
D) Nada.

**4. A frase "Funciona na minha máquina" é um sintoma de:**
A) Falta de um ambiente padronizado e automatizado (Problema que DevOps resolve).
B) Um computador muito bom.
C) Um programador excelente.
D) Sorte.

**5. O que é um Pipeline de CI/CD?**
A) Um cano de água.
B) Uma sequência de passos automatizados que o código percorre (Build, Test, Deploy).
C) Um jogo de encanador.
D) Uma ferramenta de chat.

**Gabarito:**
1-B, 2-B, 3-A, 4-A, 5-B

---

## 🛠 Exercícios
1.  **Desenho**: Desenhe uma esteira de fábrica. Em vez de montar carros, coloque as etapas de software: `Checkout (Baixar código)` -> `Testar` -> `Construir` -> `Publicar`.
2.  **Cenário**: Sem CI, João subiu um código que quebrou o sistema na sexta-feira e foi embora. Com CI, o que teria acontecido assim que ele desse `git push`?
3.  **Pesquisa**: O que são "GitHub Actions"? (Dica: É uma ferramenta de CI/CD gratuita).

---

## 🚀 Projeto da Aula: Simulando o CI
**Atividade da Aula:**
Não vamos configurar um servidor Jenkins/GitHub Actions real, mas vamos simular o processo.

1.  **Regra do Projeto**: A partir de agora, ninguém (você) pode considerar uma tarefa "Pronta" sem rodar os testes da Aula 10.
2.  **O Pipeline Manual**:
    - Toda vez que você terminar uma tarefa:
        1.  Salve o arquivo.
        2.  Abra o navegador.
        3.  Teste se funciona (Executar Testes Manuais).
        4.  Se passar -> Faça o Commit.
        5.  Se falhar -> Corrija e volte ao passo 1.
3.  **Documentação**: Escreva no seu projeto: "Política de CI: Commits apenas após testes passarem com sucesso".
