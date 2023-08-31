from imput import coletar_informacoes_caixa, coletar_informacoes_bin
from binpack import bin_packing
quantidade_caixas = int(input("Quantas caixas você gostaria de inserir? "))
bin = coletar_informacoes_bin()
caixas = coletar_informacoes_caixa(quantidade_caixas)
solution = bin_packing(bin,caixas)

