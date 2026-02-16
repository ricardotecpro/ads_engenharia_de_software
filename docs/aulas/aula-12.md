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

## 📽 Roteiro de Slides
- **Slide 1**: Segurança de Software
- **Slide 2**: CIA (Confidencialidade, Integridade, Disponibilidade).
- **Slide 3**: Autenticação (Quem?) vs. Autorização (O quê?).
- **Slide 4**: Security by Design (Segurança no projeto).
- **Slide 5**: OWASP Top 10 (Riscos comuns).
- **Slide 6**: SQL Injection (O perigo de confiar no usuário).

---

## 📝 Quiz

**1. Qual e a diferença entre Autenticação e Autorização?**
A) Autenticação confirma quem você é; Autorização define o que você pode fazer.
B) São a mesma coisa.
C) Autenticação é para sair do sistema.
D) Autorização é para entrar no sistema.

**2. O que significa a sigla CIA em segurança?**
A) Central Intelligence Agency.
B) Confidentiality, Integrity, Availability.
C) Code Is Awesome.
D) Computer Internet Access.

**3. O que é SQL Injection?**
A) Uma técnica para deixar o banco de dados mais rápido.
B) Um ataque onde código malicioso é inserido em campos de entrada para manipular o banco de dados.
C) Uma vacina para computadores.
D) Um tipo de monitor.

**4. Quando devemos começar a pensar na segurança do software?**
A) Depois que o software for hackeado.
B) Apenas na fase de testes.
C) Desde o início do projeto (Security by Design).
D) Nunca, segurança é problema do usuário.

**5. O que é a OWASP?**
A) Uma marca de antivírus.
B) Uma organização que documenta e compartilha conhecimentos sobre segurança de software.
C) Um governo.
D) Um tipo de senha.

**Gabarito:**
1-A, 2-B, 3-B, 4-C, 5-B

---

## 🛠 Exercícios
1.  **Cenário de Ataque**: Você criou um site onde o usuário digita o ID do pedido na URL (`site.com/pedido?id=10`) para ver os detalhes. O que acontece se o usuário mudar o 10 para 11? Se ele ver o pedido de outra pessoa, qual pilar da segurança foi quebrado? (Confidencialidade).
2.  **Engenharia Social**: Por que o "fator humano" é frequentemente o elo mais fraco da segurança? (Pesquise sobre Phishing).
3.  **Senha Fraca**: Por que sites obrigam você a usar letras maiúsculas, números e símbolos na senha? Isso ajuda contra qual tipo de ataque? (Força Bruta).

---

## 🚀 Projeto da Aula: Modelagem de Ameaças
**Atividade da Aula:**
Vamos pensar como um hacker para proteger nosso To-Do App.

1.  **Identifique Riscos**:
    - *Risco 1*: Alguém pode ver as tarefas de outra pessoa? (No nosso caso localstorage, só quem usa o PC vê. Mas e se fosse na web?).
    - *Risco 2*: Injeção de Script (XSS). Se eu criar uma tarefa com o título `<script>alert('oi')</script>`, o navegador vai executar esse código?
2.  **Mitigação (Proteção)**:
    - Para o Risco 2: Devemos "higienizar" (sanitize) tudo que o usuário digita antes de mostrar na tela. O texto deve ser tratado como texto, nunca como código executável.
3.  **Documentação**: Adicione uma seção "Segurança" no seu projeto listando: "Risco de XSS nos títulos das tarefas" e a solução "Sanitize inputs".
