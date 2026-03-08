import numpy as np
"""lista = [1,2,3,4,5,6,7,8,9]
matriz = np.array(lista).reshape(3,3)
print(matriz)"""
def calculate(numbers):
    matrix = np.array(numbers).reshape(3,3)

    #calcular media
    mean_row = np.mean(matrix, axis=1)
    mean_col = np.mean(matrix, axis=0)
    mean_total = np.mean(matrix)

    #calculo de la varianza
    var_row = np.var(matrix, axis=1)
    var_col = np.var(matrix, axis=0)
    var_total = np.var(matrix)

    #calcular desvación estandar
    std_row = np.std(matrix,axis=1)
    std_col = np.std(matrix, axis=0)
    std_total = np.std(matrix)

    #calcular máximo
    max_row = np.max(matrix, axis=1)
    max_col = np.max(matrix, axis=0)
    max_total = np.max(matrix)

    #clacular mínimo
    min_row = np.min(matrix, axis=1)
    min_col = np.min(matrix, axis=0)
    min_total = np.min(matrix)

    #calcular suma
    sum_row = np.sum(matrix, axis=1)
    sum_col = np.sum(matrix, axis=0)
    sum_total = np.sum(matrix)

    #agregar diccionario
    result = { 
        "mean": [mean_row.tolist(), mean_col.tolist(), mean_total],        
        "variance": [var_row.tolist(), var_col.tolist(), var_total],
        "standard deviation": [std_row.tolist(), std_col.tolist(), std_total],
        "max": [max_row.tolist(), max_col.tolist(), max_total],
        "min": [min_row.tolist(), min_col.tolist(), min_total],
        "sum": [sum_row.tolist(), sum_col.tolist(), sum_total]
    }
    return result

if __name__ == "__main__":
    prueba = [0,1,2,3,4,5,6,7,8,]
    print(calculate(prueba))




