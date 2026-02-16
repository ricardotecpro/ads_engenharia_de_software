# Projeto 12

**Atividade da Aula:**
Vamos pensar como um hacker para proteger nosso To-Do App.

1.  **Identifique Riscos**:
    - *Risco 1*: Alguém pode ver as tarefas de outra pessoa? (No nosso caso localstorage, só quem usa o PC vê. Mas e se fosse na web?).
    - *Risco 2*: Injeção de Script (XSS). Se eu criar uma tarefa com o título `<script>alert('oi')</script>`, o navegador vai executar esse código?
2.  **Mitigação (Proteção)**:
    - Para o Risco 2: Devemos "higienizar" (sanitize) tudo que o usuário digita antes de mostrar na tela. O texto deve ser tratado como texto, nunca como código executável.
3.  **Documentação**: Adicione uma seção "Segurança" no seu projeto listando: "Risco de XSS nos títulos das tarefas" e a solução "Sanitize inputs".