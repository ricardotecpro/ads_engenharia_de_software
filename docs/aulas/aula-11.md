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

---

## 📅 Atividades

- [ ] **[Ver Slides da Aula](../slides/slide-11.html)**
- [ ] **[Fazer Quiz](../quizzes/quiz-11.md)**
- [ ] **[Praticar Exercícios](../exercicios/exercicio-11.md)**
- [ ] **[Realizar Projeto](../projetos/projeto-11.md)**
