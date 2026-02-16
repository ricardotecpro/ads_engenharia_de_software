# Projeto 07 - Controle de Versão

## 🎯 Objetivo
estabelecer uma estratégia de versionamento para o projeto.

## 📝 Descrição
Mesmo trabalhando sozinho, usar Git é essencial para criar o hábito de salvar "capítulos" do seu trabalho.

## 🚀 Passo a Passo

### 1. Mensagens de Commit
Boas mensagens explicam O QUE foi feito e POR QUE.
- **Ruim**: "alterações", "arrumei", "teste".
- **Bom**: "Adiciona botão de excluir tarefa", "Corrige erro de cálculo na soma".

### 2. Estratégia de Branches (Git Flow Simplificado)
Para nosso projeto, usaremos:
- `main`: Código que funciona (Produção).
- `develop` (opcional): Onde integramos as coisas.
- `feature/nome-da-tarefa`: Para cada item do Backlog.

**Exemplo**:
Vou criar o "Login".
1. Crio branch `feature/login`.
2. Faço o código.
3. Commit: "Implementa formulário de login".
4. Volto para `main` e "junto" (Merge) a `feature/login`.

## 📤 Entrega
Adicione ao seu documento:
1.  Um exemplo de mensagem de commit boa e uma ruim.
2.  O desenho de como seria visualmente sua árvore de commits (pode ser bolinhas ligadas por linhas).
