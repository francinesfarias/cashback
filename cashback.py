def calcular_cashback(valor_compra, desconto_percentual, is_vip):
    # 1. Aplicar desconto
    valor_final = valor_compra * (1 - desconto_percentual / 100)

    # 2. Cashback base (5%)
    cashback = valor_final * 0.05

    # 3. Bônus VIP (forma explícita)
    if is_vip:
        bonus = cashback * 0.10   # calcula 10% separado
        cashback = cashback + bonus  # soma depois

    # 4. Promoção (dobro se > 500)
    if valor_final > 500:
        cashback = cashback * 2

    return round(cashback, 2)