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

Exemplo de fluxo no terminal:
```bash
$ git init
$ git add .
$ git commit -m "Meu primeiro commit"
$ git push origin main
```

### 5. Branches (Ramos)
Imagine uma linha do tempo principal (`main`). Para criar uma nova funcionalidade sem quebrar o que já funciona, criamos uma linha paralela (`feature`). Se der certo, juntamos tudo (`merge`).

---

---

## 📅 Atividades

- [ ] **[Ver Slides da Aula](../slides/slide-07.html)**
- [ ] **[Fazer Quiz](../quizzes/quiz-07.md)**
- [ ] **[Praticar Exercícios](../exercicios/exercicio-07.md)**
- [ ] **[Realizar Projeto](../projetos/projeto-07.md)**
