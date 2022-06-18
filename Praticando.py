pergunta = (input('Você gostaria de assistir os mercenários?'))
if (pergunta == 'não'):
    print('Ok então')
elif (pergunta == 'sim'):
    idade = int(input('Qual sua idade?'))
    if idade <= 15:
        print('Desculpe, mas você não tem idade suficiente para assistir ao filme!!')
    if idade >= 16:
        ingresso = str(input('Esta com o ingresso ai?'))
        if (ingresso == 'sim'):
            print('Pode entrar e bom filme!!')
        else:
                print('Desculpe, mas você esta sem o ingresso, compre-o na bilheteria e volte aqui!!')
