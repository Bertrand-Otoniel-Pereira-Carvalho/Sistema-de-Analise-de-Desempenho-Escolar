def tentar_converter_para_int(valor,nome_entrada):
    try:
        return int(valor)
    except (ValueError,TypeError):
        return tentar_valor_ate_conseguir(tentar_converter_para_int,nome_entrada)

def tentar_valor_ate_conseguir(funcao,nome_entrada_invalida):
    novo_valor = 0
    print(f"{nome_entrada_invalida} inválida. Tente novamente:")
    novo_valor = input("Digite um novo valor:\n")
    return funcao(novo_valor,nome_entrada_invalida)

