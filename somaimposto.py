def somaimposto(taxaImposto, Custo):
    return (1 + taxaImposto/100)*Custo
t = float(input('Digite a taxa de imposto que sera cobrada: '))
c = float(input('Digite o custo do produto/serviço: '))
print('Valor com imposto:', somaimposto(t,c))