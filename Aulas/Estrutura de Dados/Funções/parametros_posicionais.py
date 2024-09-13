def jogo(nome, lancamento, genero, /, vendas):
    print(nome, lancamento, genero, vendas);

jogo("Call of Duty", 2019, "tiro", vendas=1232392);

def pessoa(*, nome, idade, genero, aniversario):
    print("\nNome:",nome,"\nIdade:",idade, "\nGênero:",genero, "\nAniversário:",aniversario);
    
pessoa(nome = "Paulo", idade=20, genero="masculino", aniversario="04/12");