# -*- coding: utf-8 -*-
"""Aula_16_datatime

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1D4E62I0VzSDy57FlNL7eOBc0HjHEsFSa
"""

import datatime

data = datatime.now()

print(data)

hora neste momento e datas juntas.


método strftime -- método de formatação de data em string
Esse temo é formatado em string em Texto


from datetime import datetime

# date = datetime.now()
# print(date)



data =  datetime(2023,9,27)
h = data.strftime("%y, %B, %A")
print(h)



1. Importando o módulo datetime:
   Você pode começar importando o módulo `datetime`
da seguinte maneira:


   import datetime


2. Obtendo a data e hora atual:
   Para obter a data e hora atual, você pode usar a classe `datetime`:


   current_datetime = datetime.datetime.now()
   print(current_datetime)


3. Trabalhando com datas:
   Você pode criar objetos de data usando a classe `date`:


   date_obj = datetime.date(2023, 9, 27)
   print(date_obj)


4. Trabalhando com horários:
   Para criar objetos de horário, use a classe `time`:

   time_obj = datetime.time(14, 30, 0)
   # Hora:minuto:segundo
   print(time_obj)


5. Operações com datas e horários:
   Você pode realizar várias operações com
datas e horários, como adição, subtração e cálculos de
intervalo de tempo:


   from datetime import datetime, timedelta

   today = datetime.now()
   yesterday = today - timedelta(days=1)
   tomorrow = today + timedelta(days=1)

   time_difference = tomorrow - yesterday
   print(time_difference)


6. Formatação de datas e horários:
   Você pode formatar datas e horários em uma
string usando o método `strftime`:

   AS % SÃO AS DIRETIVAS

   EXISTEM DEZENAS:
   VERIFIQUE NO FINAL DA PÁGINA ALGUMAS OUTRAS DIRETIVAS
documentação:

https://docs.python.org/pt-br/3/library/datetime.html

   formatted_date = today.strftime("%Y-%m-%d")
   formatted_time = today.strftime("%H:%M:%S")
   print(formatted_date)
   print(formatted_time)


7. Analisando datas e horários a partir de strings:
   Você pode converter strings em objetos `datetime`
usando `strptime`:


   date_str = "2023-09-27"
   parsed_date = datetime.strptime(date_str, "%Y-%m-%d")
   print(parsed_date)

"""# DIRETIVAS

As diretivas da função `strftime` em Python são usadas para formatar objetos `datetime` em strings de acordo com um padrão específico. Aqui estão algumas das diretivas mais comuns que você pode usar com `strftime`:

- `%Y`: Ano com quatro dígitos (por exemplo, 2023).
- `%y`: Ano com dois dígitos (por exemplo, 23 para 2023).
- `%m`: Mês com zero à esquerda (por exemplo, 01 para janeiro).
- `%B`: Nome completo do mês (por exemplo, "January").
- `%b` ou `%h`: Nome abreviado do mês (por exemplo, "Jan").
- `%d`: Dia do mês com zero à esquerda (por exemplo, 05 para o dia 5).
- `%H`: Hora (00-23) com zero à esquerda.
- `%I`: Hora (01-12) com zero à esquerda.
- `%M`: Minuto com zero à esquerda.
- `%S`: Segundo com zero à esquerda.
- `%p`: AM ou PM (dependendo do horário).
- `%A`: Nome completo do dia da semana (por exemplo, "Sunday").
- `%a`: Nome abreviado do dia da semana (por exemplo, "Sun").
- `%j`: Dia do ano como um número decimal (001 a 366).
- `%U`: Número da semana no ano (00 a 53, onde a semana começa no domingo).
- `%W`: Número da semana no ano (00 a 53, onde a semana começa na segunda-feira).
- `%w`: Dia da semana como um número decimal (0 para domingo, 6 para sábado).
- `%Z`: Nome do fuso horário.
- `%z`: Offset do fuso horário (por exemplo, "+0200").

Aqui está um exemplo de como usar algumas dessas diretivas com `strftime`:
"""

from datetime import datetime

dt = datetime(2023, 9, 27, 14, 30, 0)

# Formatando a data e hora
formatted_datetime = dt.strftime("%Y-%m-%d %H:%M:%S")
print(formatted_datetime)  # Saída: "2023-09-27 14:30:00"

# Formatando apenas a data
formatted_date = dt.strftime("%A, %d de %B de %Y")
print(formatted_date)  # Saída: "Wednesday, 27 de September de 2023"

"""Essas diretivas permitem que você personalize a formatação de datas e horários de acordo com suas necessidades específicas."""

from datetime import datetime

data_nascimento = input("Digite sua data de nascimento (ano-mes-dia):")
nascimento = datetime.strptime(data_nascimento, "%Y-%m-%d")
idade = datetime.now() - nascimento

# Extrair apenas a parte dos anos da diferença de datas
anos = idade.days // 365

print(anos)





EXPLICAÇÃO DO CÓDIGO

from datetime import datetime:

Esta linha importa a classe datetime do módulo datetime.
Isso é necessário para criar objetos de data e hora e usar as
funcionalidades relacionadas a datas e horas fornecidas por esse módulo.
data_nascimento = input("Digite sua data de nascimento (ano-mes-dia):"):

solicitamos ao usuário que insira sua data de nascimento no formato
"ano-mes-dia" e armazenamos a entrada na variável data_nascimento.
nascimento = datetime.strptime(data_nascimento, "%Y-%m-%d"):

Usamos o método strptime da classe datetime para converter a string
data_nascimento em um objeto datetime. O segundo argumento "%Y-%m-%d"
indica o formato da string que estamos esperando, onde %Y representa o
ano com quatro dígitos, %m representa o mês e %d representa o dia.
idade = datetime.now() - nascimento:

calculamos a diferença entre a data e hora atual e a data de
nascimento, o que nos dá um objeto timedelta. Um objeto timedelta
representa a diferença entre duas datas e horas.
anos = idade.days // 365:

Para obter a idade em anos, dividimos o número de dias em idade.days
pelo número médio de dias em um ano (365). Isso nos dá uma estimativa da idade em anos completos.
print(anos):

Finalmente, exibimos a idade calculada em anos na tela usando a função print().

---------------------------------------------------------------




# from datetime import datetime

# data  = input("Digite sua data de nascimento (ano-mes-dia):")
# dat  = datetime.strptime(data, "%Y-%m-%d")

# data_atual  = datetime.now()

# age  =  data_atual.year - dat.year -
((data_atual.month, data_atual.day) < (dat.month, dat.day))

# print(age)




Esta linha importa a classe datetime do módulo datetime.
Isso é necessário para criar objetos de data e hora e usar as
funcionalidades relacionadas a datas e horas fornecidas por esse módulo.
data = input("Digite sua data de nascimento (AAAA-MM-DD): "):

Esta linha solicita ao usuário que digite sua data de nascimento no formato
"AAAA-MM-DD" (ano-mês-dia) e armazena a entrada do usuário em uma variável chamada data.
dat = datetime.strptime(data, "%Y-%m-%d"):

Aqui, estamos usando o método strptime da classe datetime para converter a
string data em um objeto datetime. O %Y-%m-%d é um formato de diretiva que indica
como a string deve ser interpretada. Y representa o ano com quatro dígitos,
m representa o mês e d representa o dia.
data_atual = datetime.now():

Essa linha cria um objeto datetime chamado data_atual que representa a data
e hora atuais. O método datetime.now() retorna a data e hora do sistema no momento
em que é chamado.
age = data_atual.year - dat.year - ((data_atual.month, data_atual.day) <
(dat.month, dat.day)):


((data_atual.month, data_atual.day) < (dat.month, dat.day))
compara as datas de nascimento e atual mês a mês e dia a dia.
Isso retorna True se a pessoa ainda não fez aniversário este ano
(ou seja, se o mês e o dia de nascimento ainda não ocorreram este ano)
e False caso contrário



Aqui, estamos calculando a idade da pessoa. Primeiro, subtraímos o ano
de nascimento (dat.year) do ano atual (data_atual.year) para obter a idade aproximada.
Em seguida, verificamos se o mês e o dia de nascimento já ocorreram no
ano atual. A expressão (data_atual.month, data_atual.day) < (dat.month, dat.day)
retorna True se o mês e o dia de nascimento ainda não ocorreram no ano atual,
o que significa que a pessoa ainda não fez aniversário este ano. Se essa condição
for verdadeira, subtrai 1 da idade, caso contrário, a idade permanece a mesma.
O resultado final é armazenado na variável age, que representa a idade da pessoa.

"""**EXERCÍCIOS 1**

1 - Peça ao usuário que insira seu ano de nascimento e calcule sua idade.

2 - Calcule e exiba a data e hora exatas daqui a 7 dias a partir de agora.

3 - Peça ao usuário para inserir um ano e, em seguida, exiba o ano atual.

4 - Calcule e exiba a data e hora atuais em um formato personalizado.
"""



from datetime import datetime

date = datetime.now()
print(date)

data = datetime(2022,05,11)
h = data.strftime())
print()

date = datetime(1988,2,28)
d = date.date()
print(d)

hora = datetime(22,1,2)
h = hora.time()
print(h)

date_str = "2023-09-27"
parsed_date = datetime.strptime(date_str, "%Y-%m-%d")
print(parsed_date)

DT = input('digite sua data de nascimento - AAAA-MM-DD>>')
DTF = datetime.strptime(DT, '%Y-%M-%d')
date_current = datetime.now()

nascimento = date_current - DTF
ANO = nascimento.days // 365
print(ANO)

