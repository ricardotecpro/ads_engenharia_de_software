# Aula 15 – Manutenção e Evolução

## 🎯 Objetivos de Aprendizagem
- Entender que o software nunca está "pronto".
- Conhecer a diferença entre Manutenção Corretiva, Preventiva e Evolutiva.
- Entender o conceito de Refatoração.
- Analisar o conceito de Dívida Técnica (Technical Debt).

## 📚 Conteúdo

### 1. O Software Morre?
Diferente de uma ponte (que degrada sozinha com a chuva), o software só "estragar" se o ambiente mudar ou se tentarmos mudá-lo.
- **Lei de Lehman**: Um software que é usado precisa evoluir, senão torna-se obsoleto.

### 2. Tipos de Manutenção
- **Corretiva**: Consertar bugs (o "band-aid").
- **Adaptativa**: Mudar para usar novo SO ou Banco de Dados (ex: migrar para Windows 11).
- **Perfeccionista (Evolutiva)**: Adicionar novas funcionalidades ou melhorar performance.
- **Preventiva (Refatoração)**: Melhorar a estrutura do código antes que quebre.

### 3. Refatoração (Refactoring)
É limpar a cozinha depois de cozinhar. Alterar a estrutura interna do código sem mudar seu comportamento externo.
- Objetivo: Tornar o código mais fácil de entender e modificar.
- Quando fazer? O tempo todo (regra do escoteiro: deixe o código mais limpo do que encontrou).

### 4. Dívida Técnica (Technical Debt)
Às vezes, fazemos o código "rápido e sujo" para entregar logo. Isso é um empréstimo.
- O "juro" é a dificuldade extra de trabalhar nesse código depois.
- Se não pagarmos a dívida (refatorando), o projeto pode falir (ficar impossível de manter).

---

## 📽 Roteiro de Slides
- **Slide 1**: Manutenção de Software
- **Slide 2**: A Lei da Evolução (O software nunca está pronto).
- **Slide 3**: Os tipos de Manutenção (Corretiva, Evolutiva, etc).
- **Slide 4**: O que é Refatoração? (Limpar a cozinha).
- **Slide 5**: Dívida Técnica (O cartão de crédito do código).
- **Slide 6**: O Custo de não manter (Entropia).

---

## 📝 Quiz

**1. O que é Refatoração?**
A) Mudar o software para ele fazer coisas novas.
B) Apagar todo o código e começar do zero.
C) Alterar a estrutura interna do código para melhorá-lo, sem mudar o comportamento externo.
D) Adicionar bugs.

**2. O que significa "Dívida Técnica"?**
A) Quanto dinheiro o projeto deve ao banco.
B) O custo futuro gerado por escolher uma solução rápida e fácil agora em vez de uma abordagem melhor.
C) O salário do programador.
D) O preço da licença do software.

**3. Manutenção Corretiva serve para:**
A) Adicionar novas telas.
B) Corrigir defeitos (bugs).
C) Melhorar a performance.
D) Adaptar ao novo Windows.

**4. Segundo a Regra do Escoteiro no código:**
A) Devemos acampar no escritório.
B) Devemos sempre deixar o código um pouco mais limpo do que encontramos.
C) Só devemos mexer no que está quebrado.
D) Devemos apagar comentários.

**5. Por que o software precisa evoluir?**
A) Porque o mundo, os negócios e as tecnologias mudam.
B) Porque programadores ficam entediados.
C) Para gastar dinheiro.
D) Não precisa, software dura para sempre igual.

**Gabarito:**
1-C, 2-B, 3-B, 4-B, 5-A

---

## 🛠 Exercícios
1.  **Metáfora**: Explique Dívida Técnica comparando com não lavar a louça do jantar por uma semana. O que acontece quando você precisa cozinhar de novo?
2.  **Identificando Oportunidade**: Você abre um código e vê a mesma função de 20 linhas copiada em 3 arquivos diferentes. Que tipo de manutenção você deve fazer? (Preventiva/Refatoração).
3.  **Decisão**: Seu chefe quer lançar o produto AMANHÃ, mas o código está feio. Você assume a dívida técnica? Se sim, o que você deve negociar para depois do lançamento?

---

## 🚀 Projeto da Aula: Refatorando (De novo)
**Atividade da Aula:**
Vamos "pagar" uma dívida técnica do nosso To-Do App.

1.  **Analise seu CSS/Design**: Você escreveu estilos direto no HTML (`style="..."`) ou criou classes confusas?
2.  **Ação**: Simplifique. Se tiver cores repetidas, crie variáveis CSS (`:root { --cor-principal: blue; }`).
3.  **Documente**: No seu projeto, crie uma seção "Histórico de Mudanças" e adicione: "Refatoração do CSS para usar variáveis. Motivo: Facilitar mudança de tema futuro."
