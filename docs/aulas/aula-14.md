# Aula 14 – Documentação Técnica

## 🎯 Objetivos de Aprendizagem
- Entender por que documentar é essencial (e não perda de tempo).
- Conhecer os tipos de documentação (Técnica vs. Usuário).
- Aprender a escrever um bom README.
- Conhecer ferramentas como Markdown e Wikis.

## 📚 Conteúdo

### 1. "O código se documenta sozinho"? (Mentira!)
Um código limpo ajuda, mas ele não explica o **PORQUÊ** das decisões, nem como instalar o projeto.
- Documentação é amor ao seu "eu" do futuro e aos colegas.

### 2. Tipos de Documentação
#### Para Usuário Final
- Manuais, Tutoriais, FAQ.
- Linguagem simples, sem jargão técnico.

#### Para Desenvolvedores (Técnica)
- **README**: A capa do projeto. O que é? Como instala?
- **Wiki/Docs Internos**: Arquitetura, padrões, decisões.
- **API Docs**: Swagger/OpenAPI (como integrar).
- **Comentários no Código**: Usar com moderação (explicar o *porquê*, não o *o quê*).

### 3. O Poder do Markdown
Markdown (o formato `.md` que estamos usando agora) é o padrão da indústria. Simples, legível e converte para HTML.
- Títulos com `#`
- Listas com `-`
- Código com crases `` ` ``

### 4. Como escrever um bom README
Um README deve responder em 5 segundos:
1.  O que esse projeto faz?
2.  Como eu rodo ele na minha máquina?
3.  Quais tecnologias usa?

---

## 📽 Roteiro de Slides
- **Slide 1**: Documentação Técnica
- **Slide 2**: O mito do código autoexplicativo ("O código diz O QUE, a doc diz POR QUE").
- **Slide 3**: Tipos de Doc (Usuário vs. Dev).
- **Slide 4**: Markdown (Linguagem universal de doc).
- **Slide 5**: Anatomia de um README perfeito.
- **Slide 6**: Ferramentas (MkDocs, Notion, Confluence).

---

## 📝 Quiz

**1. Qual a melhor definição para a frase "O código se documenta sozinho"?**
A) Uma verdade absoluta, nunca precisamos escrever documentos.
B) Um mito perigoso. Código limpo ajuda, mas documentação de contexto é essencial.
C) O código fala com a gente usando IA.
D) Documentação é proibida no Ágil.

**2. O que deve conter um arquivo README.md?**
A) A história da vida do programador.
B) Receitas de bolo.
C) Resumo do projeto, como instalar e usar.
D) Versículos bíblicos.

**3. Para quem é voltada a Documentação de API?**
A) Para o cliente final (dona de casa).
B) Para outros desenvolvedores que vão integrar com seu sistema.
C) Para o gerente de vendas.
D) Para ninguém.

**4. O que é Markdown?**
A) Uma marca de roupa.
B) Uma linguagem de marcação leve usada para formatar textos (como este aqui).
C) Um código difícil de ler.
D) Um banco de dados.

**5. Qual a diferença entre documentação de Usuário e Técnica?**
A) De usuário é para quem usa o software; Técnica é para quem constrói/mantém.
B) Não há diferença.
C) Técnica deve ser escrita em latim.
D) De usuário deve ser escrita em código.

**Gabarito:**
1-B, 2-C, 3-B, 4-B, 5-A

---

## 🛠 Exercícios
1.  **Refatorando README**: Você encontrou um projeto no GitHub que tem um README escrito apenas: "Projeto TCC Final". Como você melhoraria isso? Escreva 3 tópicos que faltam.
2.  **Markdown na Veia**: Escreva seu nome em Negrito, Itálico e como Código usando a sintaxe Markdown.
3.  **Comentários**: O comentário abaixo é bom ou ruim? Por que?
    ```javascript
    // Incrementa i em 1
    i = i + 1;
    ```

---

## 🚀 Projeto da Aula: Criando o README
**Atividade da Aula:**
Chegou a hora de criar a "capa" do nosso To-Do App.

1.  Crie um arquivo `README.md` (simulado no seu documento de projeto).
2.  Escreva:
    - **Título**: To-Do App Super.
    - **Descrição**: Um gerenciador de tarefas simples e ágil.
    - **Tecnologias**: HTML, CSS, JS, LocalStorage.
    - **Como rodar**: "Abra o arquivo index.html no navegador".
    - **Autor**: Seu Nome.
3.  **Entrega**: Cole o conteúdo Markdown no seu documento oficial.
