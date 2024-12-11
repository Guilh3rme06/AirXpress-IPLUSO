from src.models.flights import get_all_flights_db, insert_flight_db

def get_all_flights():
    return get_all_flights_db()

def add_flight(data):
    # Validação ou transformação dos dados
    validate_flight_data(data)
    insert_flight_db(data)
