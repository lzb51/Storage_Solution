from py3dbp import Packer, Bin, Item

def bin_packing(bin,caixas):
    packer = Packer()
    packer.add_bin(Bin('large-box', bin["altura"], bin["largura"], bin["profundidade"], 1000))

    for i, caixa in enumerate(caixas):
       packer.add_item(Item(f'caixa {i}', caixa["altura"], caixa["largura"], caixa["profundidade"], 1)) 

    packer.pack()

    responses = []
    for b in packer.bins:
        for item in b.items:
            responses.append(item.string())

    #TO-Do usar o caht chagpt para extrair os valores de x y e z para cada caixa do sexmeplo a segui ['caixa 0(1.000x1.000x1.000, weight: 1.000) pos([0, 0, 0]) rt(0) vol(1.000)']
    

    return responses
