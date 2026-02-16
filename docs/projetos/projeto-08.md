# Projeto 08

**Atividade da Aula:**
Vamos aplicar o DRY no nosso projeto teórico.

1.  **Cenário**: No nosso To-Do App, toda vez que uma tarefa é concluída, precisamos atualizar o contador de "Tarefas Pendentes" na tela. Isso acontece quando criamos, excluímos ou completamos uma tarefa.
2.  **Problema**: Se escrevermos o código de contar e atualizar a tela em todos esses lugares, ferimos o DRY.
3.  **Solução**: Crie uma função chamada `atualizarContador()`.
4.  **No Documento**: Escreva em pseudocódigo:
    ```
    função atualizarContador() {
       pendentes = contarTarefasNaoFeitas()
       tela.exibir(pendentes)
    }
    
    // Agora só chamamos a função:
    aoCriarTarefa -> atualizarContador()
    aoExcluirTarefa -> atualizarContador()
    ```