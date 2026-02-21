# Aula 15 – Manutenção e Evolução

## 🎯 Objetivos de Aprendizagem
- Entender que o software nunca está "pronto".
- Conhecer a diferença entre Manutenção Corretiva, Preventiva e Evolutiva.
- Entender o conceito de Refatoração.
- Analisar o conceito de Dívida Técnica (Technical Debt).

## 📚 Conteúdo

### 1. O Software não é uma estátua
Diferente de um monumento de pedra, o software é vivo. Se o mundo ao redor muda (novos celulares, novas leis, novos navegadores), o software precisa mudar junto.

!!! info "Lei da Evolução (Lehman)"
    Um software que é usado em um ambiente real deve sofrer mudanças contínuas ou tornar-se progressivamente menos útil.

---

### 2. Tipos de Manutenção

-   **Corretiva**: Consertar erros/bugs (o famoso "apagar incêndio").
-   **Adaptativa**: Mudar o sistema para funcionar em um novo ambiente (ex: migrar para a nuvem).
-   **Evolutiva (Perfeccionista)**: Adicionar novas funcionalidades desejadas pelos usuários.
-   **Preventiva**: Melhorar o código para evitar que ele quebre no futuro.

---

### 3. Refatoração e Dívida Técnica
Refatorar é como limpar a cozinha enquanto você cozinha. Você não muda o sabor da comida (o comportamento), mas deixa o ambiente organizado (a estrutura).

!!! warning "Cuidado com a Dívida"
    Dívida Técnica ocorre quando escolhemos uma solução rápida em vez de uma solução correta. "Pagamos juros" cada vez que mexer nesse código fica mais difícil e lento.

---

### 4. Simulação de Refatoração (TermynalJS)

<div class="termy" markdown>
```bash
$ # Analisando complexidade do código
$ code-metrics ./src
$ # Resultado: Alerta de Complexidade Ciclomática Alta!
$ # Aplicando Refatoração: Extrair Método...
$ # Novo resultado: Código 40% mais legível. Dívida reduzida!
```
</div>

---

## 📝 Exercícios Progressivos

1.  **[Básico]** O que é manutenção Corretiva?
2.  **[Básico]** O que significa "Refatorar" um código?
3.  **[Intermediário]** Explique com uma metáfora o que é Dívida Técnica.
4.  **[Intermediário]** Qual a diferença entre manutenção Evolutiva e Preventiva?
5.  **[Desafio]** Qual o perigo de nunca refatorar um sistema que cresce constantemente?

---

## 🚀 Mini-Projeto 15: O Plano de Evolução
Escolha um aplicativo que você usa e que mudou recentemente (ex: Instagram, WhatsApp). Identifique uma mudança que foi **Corretiva** (bug que sumiu) e uma que foi **Evolutiva** (nova função).

---

## 📅 Atividades

- [ ] :material-presentation: **[Ver Slides da Aula](../slides/slide-15.html)**
- [ ] :material-school: **[Fazer Quiz](../quizzes/quiz-15.md)**
- [ ] :material-dumbbell: **[Praticar Exercícios](../exercicios/exercicio-15.md)**
- [ ] :material-rocket: **[Realizar Projeto](../projetos/projeto-15.md)**
