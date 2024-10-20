import notebook

from datetime import datetime

print("------------------------------Fatura do cartão de crédito---------------------------")
valor_fatura = 0.0

while True:
    valor = float(input("Digite o valor de uma compra (caso seja a última, digite 0): "))
    if valor == 0:
        break
    valor_fatura += valor


data_pagamento = input("Insira a data de pagamento (DD-MM-AAAA): ")
data_pagamento = datetime.strptime(data_pagamento, "%d-%m-%Y")

# Data limite para pagamento sem juros
data_limite = datetime(data_pagamento.year, data_pagamento.month, 25)

# Cálculo dos juros
if data_pagamento <= data_limite:
    juros = 0
else:
    dias_atraso = (data_pagamento - data_limite).days
    juros = (0.03 * valor_fatura) + (0.01 * valor_fatura * dias_atraso)

# Valor total com juros
valor_total = valor_fatura + juros

# formas de pagamento
meio_pagamento = input("Escolha o meio de pagamento (pix, codigo de barras, debito em conta): ").lower()

# Definir prazos de restabelecimento de limite
if meio_pagamento == "pix":
    prazo_restabelecimento = 1  # 1 dia útil
elif meio_pagamento == "codigo de barras":
    prazo_restabelecimento = 5  # 5 dias úteis
elif meio_pagamento == "debito em conta":
    prazo_restabelecimento = 2  # 2 dias úteis
else:
    prazo_restabelecimento = 0
    print("forma de pagamento inexistente!")

print(f"Valor total a pagar: R${valor_total:.2f}")
print(f"Prazo de restabelecimento de limite: até {prazo_restabelecimento} dias úteis")
print("--------------------------------------------------------------------------")
print(" Em caso de duvidas entre em contato com a nossa central de atendimento")
print("Numero de telefone: 8008-0002, 24H por dia ")



