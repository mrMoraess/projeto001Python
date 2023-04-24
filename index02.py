# construir um algorítimo que receba um valor em reais da renda mensal de uma pessoa física 
# as contas de água, luz e alimentação e uma determinada porcentagem do dinheiro da pessoa
# que deve ser investido, essa porcentagem deve ser calculada sobre o que sobrar após consi-
# -derar as demais contas a serem pagas. O algorítimo deve receber esses dados do usuário 
# e retornar um relatório completo.

# o seguinte código, juntamente com as funções importados para dentro deste arquivo, atendem
# aos requisitos do algorítimo descrito acima, recebendo dados do usuário e retornando 
# um dicionário de dicionário que contém os dados de saída do sistema

from modules.calculate import checkValues, calculateFinances

income = input('Total recebido este mês: ')

checkValues(income)

energy = input('Total a ser pago de conta de luz: ')
water = input('Total a ser pago de conta de água: ')
food = input('Total a ser reservado para alimentação: ')
invest = input('Total a ser reservado para investimentos: ')

checkValues(energy, water, food, invest)

data_dict = {
    'renda': income,
    'energia': energy,
    'água': water,
    'alimentação': food,
    'investimentos': invest,
}

print(calculateFinances(data_dict))
