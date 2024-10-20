from datetime import datetime

# Inicializar o valor total da fatura
valor_fatura = 0.0

# Estrutura de repetição para múltiplos valores de compras
while True:
    valor = float(input("Digite o valor de uma compra (caso seja a última, digite 0): "))
    if valor == 0:
        break
    valor_fatura += valor

# Solicitar entrada do usuário para data de pagamento
data_pagamento = input("Insira a data de pagamento (AAAA-MM-DD): ")
data_pagamento = datetime.strptime(data_pagamento, "%Y-%m-%d")

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

print(f"Valor total a pagar: R${valor_total:.2f}")


