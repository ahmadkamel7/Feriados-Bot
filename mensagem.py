import datetime

def bot_message():

    #lista com o texto relacionado a cada feriado (seguindo a ordem do calendário)
    feriados_texto = [
        'Ano Novo',
        'Carnaval',
        'Carnaval',
        'Quarta-Feira de Cinzas',
        'Sexta-Feira Santa',
        'feriado de Tiradentes',
        'Dia do Trabalho',
        'feriado de Corpus Christi',
        'dia da Independência do Brasil',
        'dia de Nossa Sra. Aparecida',
        'dia de Finados',
        'dia da Proclamação da República',
        'Natal',
        'Ano Novo'
    ]

    #lista com a data de cada feriado (seguindo a ordem do calendário)
    #datetime.date.today().year -> extrai o ano atual dinamicamente
    feriados_datas = [
        datetime.date(datetime.date.today().year,1,1  ), #ano novo
        datetime.date(datetime.date.today().year,2,20 ), #carnaval (muda todo ano - atualizar)
        datetime.date(datetime.date.today().year,2,21 ), #carnaval (muda todo ano - atualizar)
        datetime.date(datetime.date.today().year,2,22 ), #quarta de cinzas (muda todo ano - atualizar)
        datetime.date(datetime.date.today().year,4,7  ), #sexta santa (muda todo ano - atualizar)
        datetime.date(datetime.date.today().year,4,21 ), #tiradentes
        datetime.date(datetime.date.today().year,5,1  ), #dia do trabalho
        datetime.date(datetime.date.today().year,6,8  ), #corpus christi (muda todo ano - atualizar)
        datetime.date(datetime.date.today().year,9,7  ), #independencia 
        datetime.date(datetime.date.today().year,10,12), #nossa sra.
        datetime.date(datetime.date.today().year,11,2 ), #finados
        datetime.date(datetime.date.today().year,11,15), #proclamação da rep.
        datetime.date(datetime.date.today().year,12,25), #natal
        datetime.date(datetime.date.today().year+1,1,1)  #ano novo
    ]

    #lista com a data de todas as potenciais emendas de feriado (atualizar todo ano)
    emendas_datas = [
        datetime.date(datetime.date.today().year,6,9  ), #christi + 1 (feriado quinta, emenda sexta)
        datetime.date(datetime.date.today().year,9,8  ), #independencia + 1 (feriado quinta, emenda sexta)
        datetime.date(datetime.date.today().year,10,13), #nossa sra. + 1 (feriado quinta, emenda sexta)
        datetime.date(datetime.date.today().year,11,3 ), #finados + 1 (feriado quinta, emenda sexta)
    ]


    message = '' #inicialização da variável que conterá o texto que será exibido no tweet

    for num in range(14): # de 0 a 13, contando de 1 em 1 

        #número de dias entre hoje e o potencial próximo feriado
        num_dias = (feriados_datas[num] - datetime.date.today()).days

        feriado_atual = feriados_texto[num] #texto relativo ao potencial próximo feriado

        if num_dias >= 0: #se o dia atual vem antes desse feriado em análise (se n vem, volta pro laço)
            
            #se o dia de hoje é uma "emenda"...
            if datetime.date.today() in emendas_datas: 
                message='Boa emenda de feriado pra quem tá tendo! 😄'
                break # sai do laço, uma vez que a mensagem de interesse já foi encontrada

            #se não falta dias pro feriado...
            elif num_dias == 0:
                if num==10:
                    message = 'Hoje é '+feriado_atual+'!' #se for finados, tira o emoji em respeito...
                    break # sai do laço, uma vez que a mensagem de interesse já foi encontrada
                else:
                    message = 'Hoje é '+feriado_atual+'!\n\nAproveitem 😉'
                    break # sai do laço, uma vez que a mensagem de interesse já foi encontrada

            #se falta exatamente um dia pro feriado...
            elif num_dias == 1:
                if num==4: #se for sexta-feira santa, muda a frase pro feminino
                    message = 'Falta 1 dia para a '+feriado_atual+'!'
                    break # sai do laço, uma vez que a mensagem de interesse já foi encontrada
                else:
                    message = 'Falta 1 dia para o '+feriado_atual+'!'
                    break # sai do laço, uma vez que a mensagem de interesse já foi encontrada

            #se falta mais de um dia pro feriado...
            elif num_dias > 1:
                if num==4: #se for sexta-feira santa, muda a frase pro feminino
                    message = 'Faltam '+str(num_dias)+' dias para a '+feriado_atual+'!'
                    break # sai do laço, uma vez que a mensagem de interesse já foi encontrada
                else:
                    message = 'Faltam '+str(num_dias)+' dias para o '+feriado_atual+'!'
                    break # sai do laço, uma vez que a mensagem de interesse já foi encontrada

    return message #retorna a mensagem a ser exibida no tweet