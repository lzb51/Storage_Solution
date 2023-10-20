def combinar_coordenadas(solutions, caixas):
  data_list = []
  for solution, caixa in zip(solutions,caixas):
    X = solution[0] 
    Y = solution[1]
    Z = solution[2]
    L = caixa["largura"]
    P = caixa["profundidade"]
    A = caixa["altura"]
    data_list.append(([X, X + L, X + L, X, X, X + L, X + L, X, X, X, X + L, X + L, X + L, X + L, X, X],
     [Y, Y, Y + P, Y + P, Y, Y, Y + P, Y + P, Y, Y, Y, Y, Y + P, Y + P, Y + P, Y + P],
     [Z, Z, Z, Z, Z + A, Z + A, Z + A, Z + A, Z, Z + A, Z, Z + A, Z, Z + A, Z, Z + A],
     [(0, 1), (1, 2), (2, 3), (3, 0), (4, 5), (5, 6), (6, 7), (7, 4), (8, 9), (10, 11), (12, 13), (14, 15)]))
  return(data_list)