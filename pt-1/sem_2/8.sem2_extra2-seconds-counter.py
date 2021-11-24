total_seconds = int(input("Por favor, entre com o número de segundos que deseja converter: "))

days = total_seconds // (60*60*24)
remaining_seconds_days = total_seconds % (60*60*24)

hours = remaining_seconds_days // (60*60)
remaining_seconds_hours = remaining_seconds_days % (60*60)

minutes = remaining_seconds_hours // 60
seconds = remaining_seconds_hours % 60

print(f'{days} dias, {hours} horas, {minutes} minutos e {seconds} segundos.')