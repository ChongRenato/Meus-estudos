from datetime import datetime, timedelta


agora = datetime.now()
print(agora)

print(agora.strftime('%d/%m/%y %H:%M:%S'))

amanha = agora + timedelta(days=3)

print(amanha.strftime('%d/%m/%y'))
