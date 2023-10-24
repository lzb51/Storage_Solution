def combinar_coordenadas(solutions, caixas):
  data_list = []
  for solution, caixa in zip(solutions,caixas):
    X = solution[0] 
    Y = solution[1]
    Z = solution[2]
    L = caixa["largura"]
    P = caixa["profundidade"]
    A = caixa["altura"]
    data_list.append(([Y, Y + L, Y + L, Y, Y, Y + L, Y + L, Y, Y, Y, Y + L, Y + L, Y + L, Y + L, Y, Y],
     [X, X, X + P, X + P, X, X, X + P, X + P, X, X, X, X, X + P, X + P, X + P, X + P],
     [Z, Z, Z, Z, Z + A, Z + A, Z + A, Z + A, Z, Z + A, Z, Z + A, Z, Z + A, Z, Z + A],
     [(0, 1), (1, 2), (2, 3), (3, 0), (4, 5), (5, 6), (6, 7), (7, 4), (8, 9), (10, 11), (12, 13), (14, 15)]))
  return(data_list)









