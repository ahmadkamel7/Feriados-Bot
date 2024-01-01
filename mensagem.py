import datetime

def bot_message():

    feriados_texto = [
        'Ano Novo',
        'Carnaval',
        'Carnaval',
        'Quarta-Feira de Cinzas',
        'Sexta-Feira Santa',
        #'feriado de Tiradentes', [2024 - domingo]
        'Dia do Trabalho',
        'Feriado de Corpus Christi',
        #'dia da Independência do Brasil', [2024 - sábado]
        #'dia de Nossa Sra. Aparecida', [2024 - sábado]
        #'dia de Finados', [2024 - sábado]
        'Dia da Proclamação da República',
        'Dia da Consciência Negra',
        'Natal',
        'Ano Novo'
    ]

    feriados_datas = [
        datetime.date(datetime.date.today().year,1, 1  ), #ano novo
        datetime.date(datetime.date.today().year,2, 12 ), #carnaval (muda todo ano - atualizar)
        datetime.date(datetime.date.today().year,2, 13 ), #carnaval (muda todo ano - atualizar)
        datetime.date(datetime.date.today().year,2, 14 ), #cinzas (muda todo ano - atualizar)
        datetime.date(datetime.date.today().year,3, 29 ), #sexta santa (muda todo ano - atualizar)
        #datetime.date(datetime.date.today().year,4, 21), #tiradentes [2024 - domingo]
        datetime.date(datetime.date.today().year,5, 1  ), #dia do trabalho
        datetime.date(datetime.date.today().year,5, 30 ), #christi (muda todo ano - atualizar)
        #datetime.date(datetime.date.today().year,9, 7 ), #independencia [2024 - sábado]
        #datetime.date(datetime.date.today().year,10,12), #nossa sra. [2024 - sábado]
        #datetime.date(datetime.date.today().year,11, 2), #finados [2024 - sábado]
        datetime.date(datetime.date.today().year,11, 15), #proclamação da rep.
        datetime.date(datetime.date.today().year,11, 20), #consciência negra
        datetime.date(datetime.date.today().year,12, 25), #natal
        datetime.date(datetime.date.today().year+1,1, 1)  #ano novo
    ]

    #emendas de feriado (atualizar todo ano)
    emendas_datas = [
        datetime.date(datetime.date.today().year,5,31 ), #christi + 1 (feriado quinta, emenda sexta)
    ]


    message = '' 

    for num in range(11): # tamanho do feriados_texto

        num_dias = (feriados_datas[num] - datetime.date.today()).days

        feriado_atual = feriados_texto[num] 

        if num_dias >= 0: 
            
            #se o dia de hoje é uma "emenda"...
            if datetime.date.today() in emendas_datas: 
                message='Boa emenda de feriado pra quem tá tendo! 😄'
                break 

            #se não falta dias pro feriado...
            elif num_dias == 0:
                #if num==10: 
                    #message = 'Hoje é '+feriado_atual+'!' #se for finados, tira o emoji em respeito...
                    #break 
                #else:
                message = 'Hoje é '+feriado_atual+'!\n\nAproveitem 😉'
                break 

            #se falta exatamente um dia pro feriado...
            elif num_dias == 1:
                if num==4: #se for sexta-feira santa, muda a frase pro feminino
                    message = 'Falta 1 dia para a '+feriado_atual+'!'
                    break 
                else:
                    message = 'Falta 1 dia para o '+feriado_atual+'!'
                    break 

            #se falta mais de um dia pro feriado...
            elif num_dias > 1:
                if num==4: #se for sexta-feira santa, muda a frase pro feminino
                    message = 'Faltam '+str(num_dias)+' dias para a '+feriado_atual+'!'
                    break 
                else:
                    message = 'Faltam '+str(num_dias)+' dias para o '+feriado_atual+'!'
                    break 

    return message 