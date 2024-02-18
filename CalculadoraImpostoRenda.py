"""
Em um país imaginário denominado banania, todos os habitantes ficam felizes em
pagar seus impostos (haja muita imaginação), pois sabem
que nele não existem políticos corruptos e os recursos arrecadados são
utilizados em benefício da população, sem
qualquer desvio. A moeda deste país é o Rombus, cujo símbolo é o R$.
Leia um valor com duas casas decimais, equivalente ao salário de uma pessoa
de Lisarb. Em seguida, calcule e
mostre o valor que esta pessoa deve pagar de Imposto de Renda, segundo a
tabela abaixo.
Imposto de Renda:
de 0.00 a R$ 2000.00 -------------- Isento
de R$ 2000.01 até R$ 3000.00 ------ 8 %
de R$ 3000.01 até R$ 4500.00 ------ 18 %
acima de R$ 4500.00 --------------- 28 %
Lembre-se que o valor deve ser impresso com duas casas decimais.
"""
imposto = 0
salario = int(input("Salário do usuário: "))
if(salario >= 0 and salario <= 2000): {
    print("Usuário está isento de imposto de renda")
} 
elif (salario > 2000 and salario <=3000):
    imposto = salario * 0.08
    print("Usuário terá que pagar 8% de imposto de renda, totalizando {:.2f}.".format(imposto))
elif (salario > 3000 and salario <= 4500):
    imposto = salario * 0.18
    print("Usuário terá que pagar 18% de imposto de renda, totalizando {:.2f}.".format(imposto))
elif (salario > 4500):
    imposto = salario * 0.28
    print("Usuário terá que pagar 28% de imposto de renda, totalizando {:.2f}.".format(imposto))
else:
    print("Valor inválido")