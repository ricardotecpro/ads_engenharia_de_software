# Exercício 08 - Design de Software

## 🛠 Questões Práticas

**1. Refatorando**
Analise o código abaixo (JavaScript simples) e diga qual princípio ele viola (DRY ou KISS):
```javascript
function calcularAreaQuadrado() { return 5 * 5; }
function calcularAreaSala() { return 5 * 5; }
function calcularAreaTapete() { return 5 * 5; }
```
Como você corrigiria?

**2. Responsabilidade Única**
Você tem uma classe `Usuario`. Ela deveria ter um método `enviarEmailPromocional()`? Por que? (Pensa na coesão).

**3. Acoplamento**
Imagine que a classe `Carro` chama diretamente a classe `PneuMichelin`. Se quisermos trocar o pneu para `Pirelli`, teremos que mudar a classe `Carro`. Isso é alto acoplamento. Como resolver? (Dica: criar uma interface genérica `Pneu`).
