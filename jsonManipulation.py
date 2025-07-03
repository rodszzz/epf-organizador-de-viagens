import json

with open("ida.json") as f:
    data_ida = json.load(f)

with open("volta.json") as f:
    data_volta = json.load(f)

top_voos_ida = data_ida.get("best_flights", [])
top_voos_volta = data_volta.get("best_flights", [])

def processar_voos(lista_voos):
    voos_processados = []

    for voo in lista_voos:
        trechos = []

        for flight in voo["flights"]:
            partida = flight["departure_airport"]
            chegada = flight["arrival_airport"]

            trecho_info = {
                "companhia": flight["airline"],
                "numero_voo": flight["flight_number"],
                "classe": flight["travel_class"],
                "saida_nome": partida["name"],
                "saida_codigo": partida["id"],
                "saida_hora": partida["time"],
                "chegada_nome": chegada["name"],
                "chegada_codigo": chegada["id"],
                "chegada_hora": chegada["time"],
                "duracao": flight["duration"]
            }

            trechos.append(trecho_info)

        info = {
            "tipo": voo.get("type"),
            "preco_total": voo["price"],
            "total_duration": voo.get("total_duration"),
            "trechos": trechos
        }

        voos_processados.append(info)
    
    return voos_processados


voos_ida = processar_voos(top_voos_ida)
voos_volta = processar_voos(top_voos_volta)


print("\n" + "="*10 + " ITINERÁRIOS COMPLETOS " + "="*10)
for i, (voo_ida, voo_volta) in enumerate(zip(voos_ida, voos_volta), 1):
    print("\n IDA:")
    print(f"Preço: R$ {voo_ida['preco_total']:.2f}")
    print(f"Duração total: {voo_ida['total_duration']} min")

    for j, trecho in enumerate(voo_ida["trechos"], 1):
        print(f"\n  Trecho {j}:")
        print(f"    Companhia: {trecho['companhia']}")
        print(f"    Número do voo: {trecho['numero_voo']}")
        print(f"    Classe: {trecho['classe']}")
        print(f"    Saída: {trecho['saida_nome']} ({trecho['saida_codigo']}) às {trecho['saida_hora']}")
        print(f"    Chegada: {trecho['chegada_nome']} ({trecho['chegada_codigo']}) às {trecho['chegada_hora']}")
        print(f"    Duração: {trecho['duracao']} minutos")

    print("\n VOLTA:")
    print(f"Preço: R$ {voo_volta['preco_total']:.2f}")
    print(f"Duração total: {voo_volta['total_duration']} min")

    for j, trecho in enumerate(voo_volta["trechos"], 1):
        print(f"\n  Trecho {j}:")
        print(f"    Companhia: {trecho['companhia']}")
        print(f"    Número do voo: {trecho['numero_voo']}")
        print(f"    Classe: {trecho['classe']}")
        print(f"    Saída: {trecho['saida_nome']} ({trecho['saida_codigo']}) às {trecho['saida_hora']}")
        print(f"    Chegada: {trecho['chegada_nome']} ({trecho['chegada_codigo']}) às {trecho['chegada_hora']}")
        print(f"    Duração: {trecho['duracao']} minutos")

    print("\n" + "-"*50)
