import random
def rolar_dados(quantidade):
    return [random.randint(1, 6) for _ in range(quantidade)]
import random
def rolar_dados(quantidade):
    return [random.randint(1, 6) for _ in range(quantidade)]

def guardar_dado(dados_rolados,dados_no_estoque,dado_para_guardar):
    antes=[]
    dados_no_estoque.append(dados_rolados[dado_para_guardar])
    for i in range(len(dados_no_estoque)-1):
        if len(antes)<=len(dados_no_estoque)-1:
            antes.append(dados_no_estoque[i])
    retornar=[antes,dados_no_estoque]
    
    return retornar