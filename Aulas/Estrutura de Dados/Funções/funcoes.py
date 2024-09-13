'''Uma função(método) pode receber parâmetros que deverão ser adicionados na execução da função. Além disso,
    poderá ou não ter um retorno especificado'''

'''def mensagem_nome(nome):
    print(f"Olá {nome}")

mensagem_nome(nome = "Paulo") '''

'''def sucessor_ant(numero):
    sucessor = numero + 1;
    antecessor = numero - 1;
    return sucessor, antecessor;

print(sucessor_ant(15));'''

def multiplicacao(a,b):
    return a*b;

def soma(a,b):
    return a+b;

def subtracao(a,b):
    return a-b;

def divisao(a,b):
    return a/b;

def result(a, b, funcao):
    resultado = funcao(a,b);
    print(f"Resultado = {resultado}");

result(20,5, multiplicacao);

operacao = multiplicacao;

print(operacao(5,10));