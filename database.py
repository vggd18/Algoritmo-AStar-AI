INF = 9999999
#distancia euclidiana entre os nos em questao
linha_vermelha = [10, 8, 2, 12]
linha_azul = [0, 1, 2, 3, 4, 5]
linha_amarela = [9, 1, 8, 7, 4, 6]
linha_verde = [11, 7, 3, 12, 13]

distdireta = [
    [0, 10, 24,8, 18.5, 36.4, 38.8, 35.8, 25.4, 17.6, 9.1, 16.7, 27.3, 27.7, 29.8], #E1
    [10, 0, 8.5, 14.8, 26.6, 29.1, 26.1, 17.3, 10, 3.5, 15.5, 20.9, 19.1, 21.8], #E2
    [18.5, 8.5, 0, 6.3, 18.2, 20.6, 17.6, 13.6, 9.4, 10.3, 19.5, 19.1, 12.1, 16.6], #E3
    [24.8, 14.8, 6.3, 0, 12, 14.4, 11.5, 12.4, 12.6, 16.7, 23.6, 18.6, 10.6, 15.4], #E4
    [36.4, 26.6, 18.2, 12, 0, 3, 2.4, 19.4, 23.3, 28.2, 34.2, 24.8, 14.5, 17.9], #E5
    [38.8, 29.1, 20.6, 14.4, 3, 0, 3.3, 22.3, 25.7, 30.3, 36.7, 27.6, 15.2, 18.2], #E6
    [35.8, 26.1, 17.6, 11.5, 2.4, 3.3, 0, 20, 23, 27.3, 34.2, 25.7, 12.4, 15.6], #E7
    [25.4, 17.3, 13.6, 12.4, 19.4, 22.3, 20, 0, 8.2, 20.3, 16.1, 6.4, 22.7, 27.6], #E8
    [17.6, 10, 9.4, 12.6, 23.3, 25.7, 23, 8.2, 0, 13.5, 11.2, 10.9, 21.2, 26.6], #E9
    [9.1, 3.5, 10.3, 16.7, 28.2, 30.3, 27.3, 20.3, 13.5, 0, 17.6, 24.2, 18.7, 21.2], #E10
    [16.7, 15.5, 19.5, 23.6, 34.2, 36.7, 34.2, 16.1, 11.2, 17.6, 0, 14.2, 31.5, 35.5], #E11
    [27.3, 20.9, 19.1, 18.6, 24.8, 27.6, 25.7, 6.4, 10.9, 24.2, 14.2, 0, 28.8, 33.6], #E12
    [27.6, 19.1, 12.1, 10.6, 14.5, 15.2, 12.4, 22.7, 21.2, 18.7, 31.5, 28.8, 0, 5.1], #E13
    [29.8, 21.8, 16.6, 15.4, 17.9, 18.2, 15.6, 27.6, 26.6, 21.2, 35.5, 33.6, 5.1, 0] #E14
]  
#distancia entre um no e outro a partir do mapa
distReal = [
    [0, 10, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF],#E1
    [10, 0, 8.5, INF, INF, INF, INF, INF, 10, 3.5, INF, INF, INF, INF],#E2
    [INF, 8.5, 0, 6.3, INF, INF, INF, INF, 9.4, INF, INF, INF, 18.7, INF],#E3
    [INF, INF, 6.3, 0, 13, INF, INF, 15.3, INF, INF, INF, INF, 12.8, INF],#E4
    [INF, INF, INF, 13, 0, 3, 2.4, 30, INF, INF, INF, INF, INF, INF],#E5
    [INF, INF, INF, INF, 3, 0, INF, INF, INF, INF, INF, INF, INF, INF],#E6
    [INF, INF, INF, INF, 2.5, INF, 0, INF, INF, INF, INF, INF, INF, INF],#E7
    [INF, INF, INF, 15.3, 30, INF, INF, 0, 9.6, INF, INF, 6.4, INF, INF],#E8
    [INF, 10, 9.4, INF, INF, INF, INF, 9.6, 0, INF, 12.2, INF, INF, INF],#E9
    [INF, 3.5, INF, INF, INF, INF, INF, INF, INF, 0, INF, INF, INF, INF],#E10
    [INF, INF, INF, INF, INF, INF, INF, INF, 12.2, INF, 0, INF, INF, INF],#E11
    [INF, INF, INF, INF, INF, INF, INF, 6.4, INF, INF, INF, 0, INF, INF],#E12
    [INF, INF, 18.7, 12.8, INF, INF, INF, INF, INF, INF, INF, INF, 0, 5.1],#E13
    [INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, 5.1, 0]#E14
]