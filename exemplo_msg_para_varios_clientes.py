# Exemplo de emissao de mensagem para diversos cliente de uma lista
#

clientes = [ 'Mauricio',
             'Jose da Silva',
             'Antonio Santos',
             'Maria Alves']

desconto = '10'
valor_compra = 'R$ 100.00'
valor_frete_gratis = 'R$ 150.00'

mensagem = '''

Caro Sr. {}

Imformamos que rebemos mercadorias novas esta semana.

Tambem temos boas noticias para voce!

Um desconto de {}% na compra acima de {}!

E na compra acima de {} o frete é grátis!

'''
for nome in clientes:
    print(mensagem.format(nome, desconto, valor_compra, valor_frete_gratis))
    print('-'*80)
