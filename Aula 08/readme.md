## EXERCÍCIOS DO DIA 04/04/2024

### Exercício 1

- Leia a idade e altura;

````
se idade > 17:
    se altura > 160:
        bolsa = 1120
    senão:
        bolsa = 1410
senão:
    bolsa = 1439
````
<hr>

### Exercício 2

- Leia o saldo e dias;

````
se saldo < 0:
    se dias < 30:
        saldo = saldo * 1.04
    se dias > 30:
        saldo = saldo + (0.8)**dias
senão
    se dias < 30:
        saldo = saldo * 1.08
    se dias > 30:
        saldo = saldo + (0.7)**dias
````
<hr>

### Exercício 3

- Leia x1, x2, y1 e y2;
- Calcular Δ1 = (x2-x1)² e Δ2 = (y2-y1)²;

````
se Δ1 > Δ2:
    se x1 > x2:
        alfa = Δ1 * x1²
    senao:
        alfa = Δ1 * x2²
senão:
    alfa = (Δ2 - Δ1)²
````
<hr>

### Exercício 4

- Leia o total e a série da nota fiscal;

````
se serie == 'E1':
    se total > 180:
        imposto = total * 0.17
    senão
        imopsto = total * 0.14
senão:
    se total > 199:
        imposto = total * 0.18
    senão
        imposto = total * 0.16
````
<hr>

### Exercício 5

- Leia os valores do aluguel, a área e o total;

````
se area > 50:
    se total > 350000:
        se alguel > 1800:
            preço = aluguel * 12 + total
        senão:
            preço = aluguel * 6 + total
    senão
        preço = aluguel + total
senão
    preço = total * 1.12
````
<hr>

### Exercício 6

- Leia a idade, renda e a experiência;

````
se idade < 18:
    se experiencia < 6:
        se renda <= 1200:
            imposto = 0
        senão:
            imposto = renda * 0.04
    senão:
        se experiencia > 18:
            imposto = renda * 0.16
        senão:
            imposto = renda * 0.14
senão
    imposto = renda * 0.22
````
<hr>

### Exercício 7

- Leia cargo, nível de acesso e segurança;

````
se cargo == "CEO":
    se nivel == 1:
        se seguranca == 0:
            tempo = 166
        senão:
            tempo = 150
    senão:
        se seguranca > 0:
            tempo = 120
        senão:
            tempo = 115
senão
    se nivel > 1:
        tempo = 110
    senão:
        tempo = 106
````
<hr>

### Exercício 8

- Leia total e itens;

````
if itens > 10 and total > 100:
    desconto = total * 0.15
else:
    desconto = total * 0.06
````
<hr>

### Exercício 9

- Leia tempo e idade;

````
if idade > 65 or tempo > 35:
    aposentadoria = "100%"
else:
    aposentadoria = "75%"
````
