# [@feriadosbot](https://twitter.com/feriadosbot)

🐍 Este é um projeto feito em Python 3.8 e desenvolvido para ser um bot para a rede social Twitter. O bot faz um tweet todos os dias dizendo quantos dias faltam para o próximo feriado nacional que cai em dia de semana. 🐍

Para realizar o projeto, foi necessário importar a biblioteca [tweepy](https://www.tweepy.org/) e utilizar as funções que estabelecem comunicação direta com a conta do bot no Twitter. Essa comunicação só é bem sucedida configurando adequadamente a conta do bot pelo [Twitter for Developers](https://developer.twitter.com/en). Além disso, para a parte lógica do bot, que calcula o número de dias restantes para o próximo feriado, foi-se utilizada a biblioteca [datetime](https://docs.python.org/3/library/datetime.html) junto de preceitos básicos de programação. 

Os feriados considerados pelo bot são:

* Ano Novo
* Carnaval
* Quarta-Feira de Cinzas
* Sexta-Feira Santa
* Tiradentes
* Dia do Trabalho
* Corpus Christi
* Independência do Brasil
* Dia de Nossa Sra. Aparecida
* Finados
* Proclamação da República
* Consciência Negra
* Natal

Dado que alguns feriados mudam sua data a cada ano, o bot será atualizado anualmente de forma manual para ajustar essas datas.

O perfil do Bot no Twitter é [@feriadosbot](https://twitter.com/feriadosbot) e seu código está hospedado na plataforma [pythonanywhere](https://www.pythonanywhere.com/). Nela, o código do bot é programado para rodar uma vez por dia às 11:00.

## Considerações

Este bot só foi capaz de ser construído através do auxílio [deste tutorial no YouTube](https://www.youtube.com/watch?v=2UBcRiddwAo&t=331s&ab_channel=Indently), que tornou muito mais esclarecedor a burocracia exigida pelo Twitter para ter um bot na plataforma funcionando efetivamente.

No final de 2023, a API do twitter passou por atualizações e, por conta disso, foi-se necessário adaptar o código. Essa tarefa foi concluída através [deste tutorial](https://www.youtube.com/watch?v=Vk9TY3qNdr8&t=1261s&ab_channel=Simplilearn).

Além do tutorial, o bot foi concluído com êxito graças ao desenvolvedor [Arthur](https://github.com/ArthurSMg), criador do [@SpFerias](https://twitter.com/SpFerias), grande inspiração deste projeto. Arthur ajudou com esclarecimentos sobre algumas questões de como funciona o Twitter e, principalmente, com a hospedagem do código. Obrigado, Arthur!
