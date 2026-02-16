# Aula 07 – Versionamento de Código (Git & GitHub)

## 🎯 Objetivos de Aprendizagem
- Entender para que serve o Versionamento de Código.
- Conhecer o Git (ferramenta) e o GitHub (plataforma).
- Aprender os comandos básicos: `init`, `add`, `commit`, `push`.
- Entender o conceito de Branches (Ramos).

## 📚 Conteúdo

### 1. O Problema das Versões
Sem versionamento, os arquivos ficam assim:
- `trabalho_final.doc`
- `trabalho_final_agora_vai.doc`
- `trabalho_final_V2_corrigido.doc`

No desenvolvimento de software, isso é o caos. Precisamos de uma máquina do tempo.

### 2. O que é Git?
O Git é um sistema de controle de versão distribuído. Ele registra **quem** mudou **o que** e **quando**.
- **Máquina do Tempo**: Você pode voltar o código para como ele estava ontem.
- **Trabalho em Equipe**: Permite que várias pessoas mexam no mesmo projeto sem apagar o trabalho uma da outra.

### 3. O que é GitHub?
O GitHub é uma rede social para códigos. É um servidor na nuvem onde você guarda seus repositórios Git.
- **Git** = Ferramenta instalada no seu PC.
- **GitHub** = Site onde o código fica hospedado.

### 4. Ciclo Básico
1.  **Working Directory**: Onde você edita os arquivos.
2.  **Staging Area (`git add`)**: Escolhe os arquivos que vão ser salvos.
3.  **Repository (`git commit`)**: Tira uma "foto" definitiva (Save Point).
4.  **Remote (`git push`)**: Envia para o GitHub.

### 5. Branches (Ramos)
Imagine uma linha do tempo principal (`main`). Para criar uma nova funcionalidade sem quebrar o que já funciona, criamos uma linha paralela (`feature`). Se der certo, juntamos tudo (`merge`).

---

## 📽 Roteiro de Slides
- **Slide 1**: Git e GitHub
- **Slide 2**: O problema "trabalho_final_v2" (Caos de versões).
- **Slide 3**: Git (Ferramenta local) vs. GitHub (Nuvem).
- **Slide 4**: Comandos Essenciais (add, commit, push, pull).
- **Slide 5**: A metáfora da "Foto" (Snapshot).
- **Slide 6**: Branches (Trabalho paralelo).

---

## 📝 Quiz

**1. Qual a diferença entre Git e GitHub?**
A) Git é pago, GitHub é grátis.
B) Git é a ferramenta de versionamento; GitHub é a plataforma de hospedagem.
C) São a mesma coisa.
D) GitHub é para jogos.

**2. Qual comando "tira a foto" (salva a versão) no histórico local?**
A) `git add`
B) `git upload`
C) `git commit`
D) `git save`

**3. O que é um "Branch"?**
A) Um erro no código.
B) Uma ramificação paralela para desenvolver sem afetar o código principal.
C) A marca do computador.
D) Um tipo de vírus.

**4. Para que serve o `git push`?**
A) Para empurrar o computador.
B) Para enviar as alterações locais para o repositório remoto (GitHub).
C) Para baixar atualizações.
D) Para apagar tudo.

**5. Por que usamos controle de versão?**
A) Para gastar mais espaço em disco.
B) Para ter histórico, backup e facilitar o trabalho em equipe.
C) Porque é difícil.
D) Para nada.

**Gabarito:**
1-B, 2-C, 3-B, 4-B, 5-B

---

## 🛠 Exercícios
1.  **Analogia**: Explique para uma criança o que é `git commit` usando a metáfora de um videogame (Save Point).
2.  **Cenário**: Você apagou sem querer uma parte importante do código hoje de manhã. Se você estiver usando Git, como ele pode te salvar?
3.  **Fluxo**: Desenhe setas conectando:
    - `Meu PC` -> `Área de Preparação` -> `Histórico Local` -> `GitHub`
    - (Associe aos comandos: `add`, `commit`, `push`).

---

## 🚀 Projeto da Aula: Versionando o Projeto
**Atividade da Aula:**
Vamos simular o versionamento do nosso To-Do App.

1.  **Inicializar**: Imagine que você rodou `git init` na pasta do projeto.
2.  **Primeiro Commit**:
    - Você criou os arquivos iniciais (`index.html`, `style.css`).
    - Rodou `git add .`
    - Rodou `git commit -m "Estrutura inicial do projeto"`.
3.  **Simulação de Branch**:
    - Você quer tentar mudar a cor de fundo para rosa, mas não tem certeza se vai gostar.
    - O que você faz? Tenta direto na `main` ou cria uma `branch experimentacao-cor`?
4.  **No Documento**: Escreva o nome de 3 commits que você faria ao longo do projeto (ex: "Adicionar funcionalidade de login").
