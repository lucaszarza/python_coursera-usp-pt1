print("**Bem-vindo ao conversor de segundos!!**")
totalSeconds = int(input("Digite quantos segundos deseja converter: "))

days = totalSeconds // (60*60*24)
remainingSeconds = totalSeconds % (60*60*24)

hours = remainingSeconds // (60*60)
remainingSecs = remainingSeconds % (60*60)

minutes = remainingSecs // 60

lastRemainingSecs = remainingSecs % 60

print(days, "dias, ", hours, "horas, ", minutes, "minutos e ", lastRemainingSecs, "segundos")
