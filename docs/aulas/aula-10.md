# Aula 10 – Testes de Software

## 🎯 Objetivos de Aprendizagem
- Entender a importância dos testes automatizados.
- Conhecer a Pirâmide de Testes.
- Diferenciar Testes Unitários de Integração.
- Introduzir o conceito de TDD (Test Driven Development).

## 📚 Conteúdo

### 1. Por que testar automaticamente?
Testar manualmente (clicar no botão toda vez que muda o código) é:
- Lento.
- Chato.
- Propenso a erro humano.

Testes automatizados são robôs que verificam seu código em milissegundos.

### 2. A Pirâmide de Testes
Idealizada por Mike Cohn, sugere a quantidade de testes que devemos ter:
1.  **Base (Muitos)**: Testes Unitários. Rápidos e baratos.
2.  **Meio (Alguns)**: Testes de Integração.
3.  **Topo (Poucos)**: Testes de Interface (E2E). Lentos e caros.

### 3. Tipos de Teste
#### Teste Unitário
Testa a menor parte do código isoladamente (uma função, uma classe).
- *Ex*: A função `somar(2, 2)` retorna `4`?

#### Teste de Integração
Testa se duas ou mais partes funcionam juntas.
- *Ex*: A função `SalvarPedido` consegue gravar no `BancoDeDados`?

#### Teste End-to-End (E2E)
Testa o fluxo completo do usuário.
- *Ex*: Um robô abre o navegador, clica em comprar e verifica se apareceu "Sucesso".

### 4. TDD (Test Driven Development)
Uma técnica onde você escreve o teste ANTES do código.
- **Red**: Escreve o teste (ele falha, pois o código não existe).
- **Green**: Escreve o código mínimo para o teste passar.
- **Refactor**: Melhora o código garantindo que o teste continua passando.

---

---

## 📅 Atividades

- [ ] **[Ver Slides da Aula](../slides/slide-10.html)**
- [ ] **[Fazer Quiz](../quizzes/quiz-10.md)**
- [ ] **[Praticar Exercícios](../exercicios/exercicio-10.md)**
- [ ] **[Realizar Projeto](../projetos/projeto-10.md)**
