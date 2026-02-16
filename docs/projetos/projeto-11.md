# Projeto 11 - Política de Automação (CI Simplificado)

## 🎯 Objetivo
Estabelecer uma regra de "Integração Contínua Manual" para garantir a estabilidade.

## 📝 Descrição
Mesmo sem robôs, podemos ter a disciplina do CI. A regra é: **Código quebrado não entra no repositório**.

## 🚀 O Pipeline Manual

Defina os passos que **obrigatoriamente** devem ser seguidos antes de cada commit.

1.  **Build (Verificação de Sintaxe)**:
    - O código não tem erros de digitação óbvios?
    - O console do navegador (F12) mostra erros vermelhos?
2.  **Test (Verificação Funcional)**:
    - Execute os testes manuais definidos na Aula 10.
    - A nova funcionalidade quebrou algo antigo? (Teste de Regressão Rápido).
3.  **Commit (Integração)**:
    - Se tudo passou, aí sim: `git add` e `git commit`.

## 📤 Entrega
Adicione o texto acima (personalizado) ao seu documento, sob o título "Política de Qualidade e Integração".
