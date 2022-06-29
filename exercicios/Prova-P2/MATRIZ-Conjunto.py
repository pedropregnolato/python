'''Faça um programa que leia uma matriz e transforme numa lista mostrando apenas
uma vez todos os numeros presentes na matriz em ordem crescente'''

def combinar(input):  

    resultado = set(input[0])  

    for array in input[1:]:  
        resultado.update(array)  
    
    return list(resultado)  
    
if __name__ == "__main__":  
    input = [[1, 2, 10, 4, 3, 1], 
             [5, 6, 3, 4], 
             [9, 5, 7, 7], 
             [8, 5, 1, 3]]   
    print (combinar(input))