# Projeto 12 - Segurança e Ameaças

## 🎯 Objetivo
Identificar vulnerabilidades potenciais no projeto (Threat Modeling).

## 📝 Descrição
Nenhum sistema é 100% seguro, mas devemos conhecer os riscos. Vamos analisar o To-Do App.

## 🚀 Análise de Riscos

### 1. Cross-Site Scripting (XSS)
- **Ameaça**: Um usuário malicioso pode tentar salvar uma tarefa com código JavaScript no título. Ex: `<script>roubarCookies()</script>`.
- **Consequência**: Quando a lista for carregada, o navegador pode executar esse script.
- **Solução**: Nunca confiar no input do usuário. Ao exibir o texto na tela, usar funções que convertem caracteres especiais (ex: `<` vira `&lt;`). `innerText` é mais seguro que `innerHTML`.

### 2. Privacidade Local
- **Ameaça**: Como usamos LocalStorage, qualquer pessoa que usar o mesmo computador/navegador pode ver as tarefas.
- **Solução**: Aviso ao usuário: "Não use em computadores públicos". (Para um sistema real, precisaríamos de Login no Backend).

## 📤 Entrega
Adicione esses dois pontos ao seu documento. Desenhe um "Alerta de Segurança" simbólico.
