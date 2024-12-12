from bookings import *


def print_listar_reservas_cliente(fk_cliente):
    reservas = listar_reservas_cliente()

    if reservas:
        for reserva in reservas:
            print(f"Reserva ID: {reserva[0]}, Voo: {reserva[1]} -> {reserva[2]}, Data: {reserva[3]}")
    else:
        print(f"Cliente {fk_cliente} não possui reservas.")

def print_cancelar_reserva():
    eliminar=input("Digite o id da reserva:")
    eliminar_reserva(eliminar)

def print_adicionar_reserva():
    voo=input("qual é o voo que quer ")