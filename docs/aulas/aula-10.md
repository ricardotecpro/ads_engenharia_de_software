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

## 📽 Roteiro de Slides
- **Slide 1**: Testes de Software
- **Slide 2**: Manual vs. Automatizado (Tartaruga vs. Foguete).
- **Slide 3**: Pirâmide de Testes (Unitário > Integração > E2E).
- **Slide 4**: Teste Unitário (A lupa no código).
- **Slide 5**: Teste de Integração (O quebra-cabeça).
- **Slide 6**: TDD (Red -> Green -> Refactor).

---

## 📝 Quiz

**1. Qual teste fica na base da Pirâmide de Testes (devemos ter em maior quantidade)?**
A) Teste Manual.
B) Teste End-to-End (E2E).
C) Teste Unitário.
D) Teste de Usabilidade.

**2. O que valida um Teste Unitário?**
A) O sistema inteiro.
B) A menor parte testável do código (ex: uma função).
C) A integração com o banco de dados.
D) A cor do botão.

**3. No TDD (Test Driven Development), qual a ordem correta?**
A) Código -> Teste -> Refatoração.
B) Teste -> Código -> Refatoração.
C) Refatoração -> Teste -> Código.
D) Teste -> Refatoração -> Código.

**4. Por que não devemos ter APENAS testes manuais?**
A) Porque são lentos, caros e propensos a falhas humanas.
B) Porque testadores manuais não existem.
C) Porque computadores não gostam de mãos.
D) Porque é muito rápido.

**5. O que significa o estado "Red" no TDD?**
A) O teste falhou (porque a funcionalidade ainda não existe).
B) O computador está superaquecendo.
C) O código está pronto e funcionando.
D) O teste deve ser apagado.

**Gabarito:**
1-C, 2-B, 3-B, 4-A, 5-A

---

## 🛠 Exercícios
1.  **Escrevendo Testes (Papel)**: Imagine uma função `ehMaiorDeIdade(idade)`. Escreva 3 casos de teste para ela.
    - Ex: Entrada 10 -> Esperado: Falso.
    - Ex: Entrada 18 -> Esperado: ???
    - Ex: Entrada 25 -> Esperado: ???
2.  **Classificação**: Um teste que verifica se, ao clicar no botão "Login", o usuário é redirecionado para a "Home", é Unitário ou E2E?
3.  **Reflexão TDD**: Por que escrever o teste antes ajuda a desenhar melhor o código? (Pense em como você é "obrigado" a pensar na entrada e saída da função).

---

## 🚀 Projeto da Aula: Criando Casos de Teste
**Atividade da Aula:**
Vamos planejar os testes para o nosso To-Do App.

1.  **Escolha uma funcionalidade**: Vamos usar "Adicionar Tarefa".
2.  **Crie Casos de Teste (Cenários)**:
    - *CT01*: Adicionar tarefa com título válido. (Resultado Esperado: Tarefa aparece na lista).
    - *CT02*: Tentar adicionar tarefa sem título. (Resultado Esperado: Erro/Alerta, tarefa NÃO aparece).
    - *CT03*: Adicionar tarefa com título muito longo (ex: 500 caracteres). (Resultado Esperado: Truncar ou erro?).
3.  **Ação**: Adicione uma tabela "Plano de Testes" ao seu documento de projeto com esses casos.
