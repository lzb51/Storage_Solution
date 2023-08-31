def coletar_informacoes_caixa(numero_caixas):
    informacoes_caixas = []

    for i in range(numero_caixas):
        print(f"\nCaixa {i+1}:")
        altura = float(input("Qual é a altura da caixa em centímetros? "))
        largura = float(input("Qual é a largura da caixa em centímetros? "))
        profundidade = float(input("Qual é a profundidade da caixa em centímetros? "))
        peso = float(input("Qual é o peso da caixa em quilogramas? "))

        print("\nEm uma escala de 1 a 5, o quão frágil é a caixa?")
        while True:
            fragilidade = int(input("Digite um número de 1 a 5 (sendo 1 menos frágil e 5 mais frágil): "))
            if 1 <= fragilidade <= 5:
                break
            else:
                print("Valor inválido! Digite um número entre 1 e 5.")

        informacoes_caixa = {
            "altura": altura,
            "largura": largura,
            "profundidade": profundidade,
            "peso": peso,
            "fragilidade": fragilidade
        }

        informacoes_caixas.append(informacoes_caixa)

    return informacoes_caixas

def coletar_informacoes_bin():
    bin = {}
    altura = float(input("Qual é a altura do bin em centímetros? "))
    largura = float(input("Qual é a largura do bin em centímetros? "))
    profundidade = float(input("Qual é a profundidade do bin em centímetros? ")) 
    bin["altura"] = altura
    bin["largura"] = largura
    bin["profundidade"] = profundidade
    return bin
        



