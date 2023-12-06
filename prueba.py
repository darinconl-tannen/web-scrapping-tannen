lineas = ['20:00', '05 Dic', 'EE.UU (F)', '1.062', '8.50', 'China (F)', '26.00', '41', '22:00', '05 Dic', 'Canadá (F)', '1.85', '3.35', 'Australia (F)', '3.55', '11']

hora = list()
fecha = list()
local_team = list()
local_bet = list()
draw_bet = list()
vis_team = list()
vis_bet = list()
market_amount = list()

for i in range(0, len(lineas), 8):
    hora.append(lineas[i])
    fecha.append(lineas[i+1])
    local_team.append(lineas[i+2])
    local_bet.append(lineas[i+3])
    draw_bet.append(lineas[i+4])
    vis_team.append(lineas[i+5])
    vis_bet.append(lineas[i+6])
    market_amount.append(lineas[i+7])

print(lineas)