import datetime
import pytz
d =datetime.date(2024,8,31)
print(d)
print(datetime.date.today())

data_hora =datetime.datetime(2023,8,31,18,23,45)
print(data_hora)
hora = datetime.time(21,23,54)
print(hora)

#trabalhando com datas

# operacoes de soma e subtracao de datas

data_atual = datetime.datetime.now()
data_somada =data_atual + datetime.timedelta(minutes=50)
print(data_atual)
print(data_somada)

# formatando datas usando strftime e strptime
mascara_dt_tm = "%d/%m/%Y"
mascara_dt_parse = "%Y-%m-%d %H:%M"
print(data_atual.strftime(mascara_dt_tm))
dt_str = "2024-08-31 04:13"

# criando uma data a partir de um string com strptime
print(datetime.datetime.strptime(dt_str,mascara_dt_parse))

#trabalhando com timezones 
data_normal = datetime.datetime.now(pytz.timezone("Europe/Oslo"))
data_normal2 = datetime.datetime.now(pytz.timezone("America/Sao_paulo"))
print(data_normal)
print(data_normal2)