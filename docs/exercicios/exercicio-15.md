# Exercício 15 - Manutenção

## 🛠 Questões Práticas

**1. O Chefe Apressado**
Seu chefe diz "Não temos tempo para refatorar, temos que entregar features novas!". Como você explicaria para ele, usando uma metáfora financeira (Dívida), que se não refatorar agora, o time vai ficar cada vez mais lento nas próximas entregas?

**2. Código Legado**
Você recebeu um código escrito há 10 anos, sem documentação e com nomes de variáveis como `x`, `y` e `temp`. Qual o primeiro passo para começar a dar manutenção nisso sem quebrar tudo? (Dica: Testes).

**3. Refatoração Visual**
Olhe este código:
```python
if (idade > 18 and dinheiro > 50 and temCarro == True and naoBebeu == True):
   podeDirigir = True
```
Como você refatoraria essa condição complexa para torná-la legível? (Talvez extrair para uma função `estaAptoParaDirigir()`?).
