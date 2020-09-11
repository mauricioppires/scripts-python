import os

def resultado_valor( nome, valor ):
    print('-'*80)
    print('{: ^80s}'.format(nome))
    if valor == 1:
        texto = ['Número 1\n',
                 'Este número simboliza o início de tudo, a totalidade! É representação de ',
                 'iniciativa, liderança, poder e o autoconhecimento da sua essência e conexão ',
                 'com o "eu" mais profundo.\n',
                 'Ele atribui coragem, harmonia, confiança, independência e realizações. O ',
                 'número 1 significa a originalidade e objetividade completa!' ]
    elif valor == 2:
        texto = [ 'Número 2\n',
                  'Representa o total equilíbrio, prosperidade e harmonização. O número dois já ',
                  'é a dualidade e o complemento do 1. Possui então uma natureza de muita ',
                  'intuição, sensibilidade, poder, adaptabilidade, pacificidade e é acima de ',
                  'tudo o espiritual livre.' ]
    elif valor == 3:
        texto = [ 'Número 3\n',
                  'Comunicação, evolução, interatividade, sinceridade e expressão é a chave do ', 
                  'contexto que este número carrega. Ele representa o mundo de maneira clara e ', 
                  'igualitária, onde todos que compõe possuem força, criatividade e transformação.' ]
    elif valor == 4:
        texto = [ 'Número 4\n',
                  'O número 4 é mais sério e guardado, representa estabilidade, força, segurança ',
                  'e proteção. É um símbolo muito conservador e por isso possui muita ordem e ', 
                  'organização. Portanto ele tende sempre para a racionalidade, e simboliza as ', 
                  'quatro estações do ano ou os quatros elementos.' ]
    elif valor == 5:
        texto = [ 'Número 5\n',
                  'O número do pentagrama, aquele que conecta o homem aos céus e à sua essência, ', 
                  'por isso simboliza a liberdade, transformação, evolução, crescimento e ', 
                  'aventura. É o símbolo de mudanças, de movimentação e versatilidade.' ]
    elif valor == 6:
        texto = [ 'Número 6\n',
                  'Podemos enxergar este número como harmonioso e calmo. Aquele que é justo, ', 
                  'conciliador, responsável e presa sempre por amor, equilíbrio, fidelidade e ', 
                  'honestidade.' ]
    elif valor == 7:
        texto = [ 'Número 7\n',
                  'Grande espiritualidade, ele representa os 7 dias da semana ou 7 cores do ', 
                  'arco-íris. De todos é o que mais vibra a perfeição. É aquele que se envolve ', 
                  'com a curiosidade, com o encontro da paz, autoconhecimento, sabedoria e ', 
                  'misticismo.' ]
    elif valor == 8:
        texto = [ 'Número 8\n',
                  'Vitória, poder, força, prosperidade, evolução, superação e facilidade com ', 
                  'administração de dinheiro.\n',
                  'Por isso a pessoa que está sob energia desse numeral, saberá dominar a riqueza ', 
                  'material com responsabilidade, garra e perseverança.' ]
    elif valor == 9:
        texto = [ 'Número 9\n',
                  'Compaixão, empatia e fraternidade pura! Ele simboliza a compreensão, ', 
                  'realização e amor incondicional. É a elevada espiritualidade e a experiência ', 
                  'de todos os números anteriores.' ]
    elif valor == 11:
        texto = [ 'Número 11\n',
                  'A maior força deste número é a intuição e sensibilidade extrema. Ele se volta ', 
                  'para invenções sempre buscando o bem da humanidade que elevam o coração e o ', 
                  'espírito do homem.\n',
                  'Simboliza a clarividência e a colaboração com todos.' ]
    elif valor == 12:
        texto = [ 'Número 12\n',
                  'É o encontro com uma Energia Maior, com a fé aprofundada em nosso espírito. ', 
                  'E o que há de mais sagrado em nossos corações. Ele não é um união qualquer, ', 
                  'mas representa diversas coisas: 12 meses do ano, 12 signos, 12 apóstolos de ', 
                  'Jesus, Israel era composta por 12 tribos.' ]
    elif valor == 18:
        texto = [ 'Número 18\n',
                  'Para os cabalistas esse magnífico número é o poder e a vontade da alma. Quer ', 
                  'dizer vida longa com bons sentimentos e momentos. E por isso a vida é como um ', 
                  'mérito simbolizado pelo número 18.' ]
    elif valor == 22:
        texto = [ 'Número 22\n',
                  'Trabalho e construção, está envolvido e relacionado a tudo que é material e ', 
                  'concreto. Por isso também é o número do poder, otimismo, eficiência, lealdade ', 
                  'e raciocínio lógico. Simboliza a agilidade e que sempre traz vibrações de ', 
                  'rapidez.' ]
    elif valor == 33:
        texto = [ 'Número 33\n',
                  'Sagrado, poderoso que transforma e renova o interior. Muito conhecido como a ', 
                  'idade de Jesus Cristo quando foi crucificado. É um número mestre e que reserva ', 
                  'alta consciência universal e espiritual, além do desenvolvimento pessoal.' ]
    elif valor == 44:
        texto = [ 'Número 44\n',
                  'É o número da sabedoria e da fácil mudança a partir da descoberta de um erro. ', 
                  'Representa a facilidade de expressão, poder, controle, agilidade e inteligência.\n',
                  'Os altos cargos geralmente são representados por este número.' ]
    elif valor == 55:
        texto = [ 'Número 55\n',
                  'Energia pura e vital, que renasce e se fortalece. Expressa a abertura total ', 
                  'para o mundo espiritual junto a força, iluminação e dons a serem desenvolvidos!' ]
    elif valor == 66:
        texto = [ 'Número 66\n',
                  'Autorrealização humana, desejos, cumprimento do krma, luta, capacidade de amar ', 
                  'incondicionalmente. Desta forma representa também a liberdade e a paz divina.' ]
    elif valor == 77:
        texto = [ 'Número 77\n',
                  'Representa a libertação da alma, capacidade de aceitar muitas mudanças e ', 
                  'aproveitar delas para transformar o interior, por isso também simboliza o ', 
                  'sucesso, compreensão e crescimento.' ]
    elif valor == 108:
        texto = [ 'Número 108\n',
                  'Este número é a conclusão bem sucedida de um ciclo. Em muitas culturas é ', 
                  'considerado um número sagrado que promove toda limpeza da alma e dos resquícios ',
                  'de impurezas que acumulamos em energia durante nossos dias.\n',
                  'Muitas vezes pensamos: “quais seriam meus números da sorte? “Mas na verdade o ', 
                  'que é importante compreendermos são as vibrações que estes valores podem ', 
                  'influenciar em nossas vidas, e desta forma você descobrirá que qualquer um pode ', 
                  'representar sorte, desde que você alcance o autoconhecimento necessário para ', 
                  'desenvolver o que há de mais especial em você.' ]
    else:
        texto = [ '*',
                  '{}'.format(valor) ]

    for t in texto:
        print( t )

    print('-'*80)

def nome_valor( nome ):
    tabela = {'A': 1,
              'B': 2,
              'C': 3,
              'D': 4,
              'E': 5,
              'F': 6,
              'G': 7,
              'H': 8,
              'I': 9,
              'J': 9,
              'K': 10,
              'L': 20,
              'M': 30,
              'N': 40,
              'O': 50,
              'P': 60,
              'Q': 70,
              'R': 80,
              'S': 90,
              'T': 100,
              'U': 200,
              'V': 200,
              'W': 200,
              'X': 300,
              'Y': 9,
              'Z': 400 }
    nome = nome.upper()
    preserva_nome = nome
    nm2 = ''
    for nm in nome.split():
        nm2 += nm
    nome = nm2
    valor = 0

    for n in nome:
        valor += tabela[n]

    while True:
        if valor == 1 or valor == 2 or valor == 3 or valor == 4 or valor == 5 or \
           valor == 6 or valor == 7 or valor == 8 or valor == 9 or \
           valor == 11 or valor == 12 or valor == 18 or \
           valor == 22 or valor == 33 or valor == 44 or \
           valor == 55 or valor == 66 or valor == 77 or \
           valor == 108:

            resultado_valor( preserva_nome, valor )
            return ''

        else:
            tmp_valor = valor
            valor = 0
            for w in str(tmp_valor):
                valor += int(w)


if __name__ == '__main__':
    # os.system('cls')
    print(" Numerologia Cabalística ".center(80, "-"))
    pnome = input('Digite seu nome: ')
    print(nome_valor(pnome))
    print('-'*80)
