import json
import os
from config import Config

# Representa uma única viagem guardada por um utilizador
class Trip:
    def __init__(self, ida, volta, total_price, total_duration_hm):
        self.ida = ida
        self.volta = volta
        self.total_price = total_price
        self.total_duration_hm = total_duration_hm

# Gira o ficheiro trips.json
class TripModel:
    FILE_PATH = os.path.join(Config.DATA_PATH, 'trips.json')

    def __init__(self):
        self.trips_by_user = self._load()

    def _load(self):
        """ Carrega as viagens do ficheiro JSON. A estrutura é um dicionário onde a chave é o user_id. """
        if not os.path.exists(self.FILE_PATH):
            return {}
        try:
            with open(self.FILE_PATH, 'r', encoding='utf-8') as f:
                data = json.load(f)
                # Garante que os dados carregados sejam um dicionário
                return data if isinstance(data, dict) else {}
        except (json.JSONDecodeError, FileNotFoundError):
            return {}

    def _save(self):
        """ Guarda o dicionário de viagens de volta no ficheiro JSON. """
        with open(self.FILE_PATH, 'w', encoding='utf-8') as f:
            json.dump(self.trips_by_user, f, indent=4, ensure_ascii=False)

    def get_trips_by_user_id(self, user_id):
        """ Retorna a lista de viagens para um utilizador específico. """
        return self.trips_by_user.get(str(user_id), [])

    def add_trip_for_user(self, user_id, trip: Trip):
        """ Adiciona uma nova viagem à lista de um utilizador. """
        user_id_str = str(user_id)
        if user_id_str not in self.trips_by_user:
            self.trips_by_user[user_id_str] = []
        
        # --- CÓDIGO CORRIGIDO AQUI ---
        # Cria um dicionário com os detalhes da viagem para ser guardado
        trip_data = {
            'ida': {
                'partida': f"{trip.ida.legs[0].departure_airport_name} ({trip.ida.legs[0].departure_airport_code})",
                'chegada': f"{trip.ida.legs[-1].arrival_airport_name} ({trip.ida.legs[-1].arrival_airport_code})",
                'duracao_total': trip.ida.total_duration_hm,
                'preco': trip.ida.price,
                'booking_token': trip.ida.booking_token  # Adicionado
            },
            'volta': {
                'partida': f"{trip.volta.legs[0].departure_airport_name} ({trip.volta.legs[0].departure_airport_code})",
                'chegada': f"{trip.volta.legs[-1].arrival_airport_name} ({trip.volta.legs[-1].arrival_airport_code})",
                'duracao_total': trip.volta.total_duration_hm,
                'preco': trip.volta.price,
                'booking_token': trip.volta.booking_token  # Adicionado
            },
            'preco_total': trip.total_price,
            'duracao_total_viagem': trip.total_duration_hm
        }


        def delete_trip_for_user(self, user_id, trip_index):
            user_id_str = str(user_id)
            # Verifica se o utilizador e a viagem existem
            if user_id_str in self.trips_by_user and 0 <= trip_index < len(self.trips_by_user[user_id_str]):
                # Remove a viagem da lista
                del self.trips_by_user[user_id_str][trip_index]
                # Se o utilizador ficar sem viagens, removemos a entrada dele
                if not self.trips_by_user[user_id_str]:
                    del self.trips_by_user[user_id_str]
                self._save()
                return True
            return False
        # --- FIM DA CORREÇÃO ---
        
        self.trips_by_user[user_id_str].append(trip_data)
        self._save()