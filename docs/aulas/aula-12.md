# Aula 12 – Segurança de Software

## 🎯 Objetivos de Aprendizagem
- Entender que segurança deve ser pensada desde o início (Security by Design).
- Conhecer a OWASP e os principais riscos.
- Entender conceitos básicos: Autenticação vs. Autorização.
- Aprender sobre injeção de código (SQL Injection).

## 📚 Conteúdo

### 1. Inseguro por padrão?
Muitos softwares nascem inseguros porque os devs pensam apenas na funcionalidade ("Tem que funcionar") e esquecem da segurança ("Tem que proteger").
- **Security by Design**: Pensar em segurança na fase de Design, não só no final.

### 2. A Tríade CIA
Os 3 pilares da segurança da informação:
- **C**onfidencialidade: Só quem deve ver, vê. (Senha, criptografia).
- **I**ntegridade: O dado não foi alterado indevidamente. (Ninguém mudou o saldo do banco).
- **D**isponibilidade (Availability): O sistema está no ar quando preciso.

### 3. Autenticação vs. Autorização
- **Autenticação**: Quem é você? (Login/Senha, Biometria).
- **Autorização**: O que você pode fazer? (Admin pode apagar tudo, Usuário só vê seus dados).

### 4. OWASP Top 10
A OWASP (Open Web Application Security Project) lista as falhas mais comuns. A nº 1 clássica é a **Injection** (Injeção).
- *Exemplo*: Um hacker escreve um comando de banco de dados no campo de login e o sistema executa, revelando senhas.

---

---

## 📅 Atividades

- [ ] **[Ver Slides da Aula](../slides/slide-12.html)**
- [ ] **[Fazer Quiz](../quizzes/quiz-12.md)**
- [ ] **[Praticar Exercícios](../exercicios/exercicio-12.md)**
- [ ] **[Realizar Projeto](../projetos/projeto-12.md)**
