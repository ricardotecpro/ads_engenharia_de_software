# Projeto 08 - Design de Código (Modularização)

## 🎯 Objetivo
Aplicar conceitos de modularização e DRY para organizar a lógica do sistema.

## 📝 Descrição
Antes de escrever muito código, vamos planejar nossas funções principais para evitar repetição.

## 🚀 Passo a Passo

### 1. Identificando Responsabilidades
Olhe para as funcionalidades do app. Quais ações se repetem?
- *Salvar no LocalStorage*: Vamos precisar salvar ao criar, editar e excluir.
- *Renderizar a Lista*: Vamos precisar desenhar a lista na tela ao carregar e ao mudar algo.

### 2. Definindo Funções Reutilizáveis
Crie uma lista de funções "Utilitárias" que seu projeto terá:
1. `salvarDados()`: Pega a lista de tarefas e salva no navegador.
2. `carregarDados()`: Lê do navegador e devolve a lista.
3. `renderizarTela()`: Limpa a lista atual e desenha os itens novamente.

### 3. Exemplo de Fluxo Limpo
Ao adicionar uma tarefa, o fluxo seria:
1. Ler dados (`carregarDados()`)
2. Adicionar novo item na lista.
3. Salvar dados (`salvarDados()`)
4. Atualizar tela (`renderizarTela()`)

## 📤 Entrega
Adicione esse planejamento de funções ao seu documento de projeto. Mostra que você pensou na estrutura antes de sair digitando.
