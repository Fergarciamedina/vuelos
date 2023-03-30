from DB import *
import collections
import numpy as np

# Queries
query_children = """ 
    SELECT passenger_id FROM passenger WHERE age < 18
"""

query_air_1_seat_1 = """
    SELECT boarding_pass.purchase_id, GROUP_CONCAT(boarding_pass.passenger_id SEPARATOR ', ') AS passenger_ids, boarding_pass.seat_type_id, boarding_pass.seat_id
    FROM flight
    INNER JOIN airplane ON flight.airplane_id = airplane.airplane_id
    INNER JOIN boarding_pass ON flight.flight_id = boarding_pass.flight_id
    WHERE airplane.airplane_id = 1 AND boarding_pass.seat_type_id = 1
    GROUP BY purchase_id;
"""
query_air_1_seat_2 = """
    SELECT boarding_pass.purchase_id, GROUP_CONCAT(boarding_pass.passenger_id SEPARATOR ', ') AS passenger_ids, boarding_pass.seat_type_id, boarding_pass.seat_id
    FROM flight
    INNER JOIN airplane ON flight.airplane_id = airplane.airplane_id
    INNER JOIN boarding_pass ON flight.flight_id = boarding_pass.flight_id
    WHERE airplane.airplane_id = 1 AND boarding_pass.seat_type_id = 2
    GROUP BY purchase_id;
"""

query_air_1_seat_3 = """
    SELECT boarding_pass.purchase_id, GROUP_CONCAT(boarding_pass.passenger_id SEPARATOR ', ') AS passenger_ids, boarding_pass.seat_type_id, boarding_pass.seat_id
    FROM flight
    INNER JOIN airplane ON flight.airplane_id = airplane.airplane_id
    INNER JOIN boarding_pass ON flight.flight_id = boarding_pass.flight_id
    WHERE airplane.airplane_id = 1 AND boarding_pass.seat_type_id = 3
    GROUP BY purchase_id;
"""

query_air_2_seat_1 = """
    SELECT boarding_pass.purchase_id, GROUP_CONCAT(boarding_pass.passenger_id SEPARATOR ', ') AS passenger_ids, boarding_pass.seat_type_id, boarding_pass.seat_id
    FROM flight
    INNER JOIN airplane ON flight.airplane_id = airplane.airplane_id
    INNER JOIN boarding_pass ON flight.flight_id = boarding_pass.flight_id
    WHERE airplane.airplane_id = 2 AND boarding_pass.seat_type_id = 1
    GROUP BY purchase_id;
"""
query_air_2_seat_2 = """
    SELECT boarding_pass.purchase_id, GROUP_CONCAT(boarding_pass.passenger_id SEPARATOR ', ') AS passenger_ids, boarding_pass.seat_type_id, boarding_pass.seat_id
    FROM flight
    INNER JOIN airplane ON flight.airplane_id = airplane.airplane_id
    INNER JOIN boarding_pass ON flight.flight_id = boarding_pass.flight_id
    WHERE airplane.airplane_id = 2 AND boarding_pass.seat_type_id = 2
    GROUP BY purchase_id;
"""

query_air_2_seat_3 = """
    SELECT boarding_pass.purchase_id, GROUP_CONCAT(boarding_pass.passenger_id SEPARATOR ', ') AS passenger_ids, boarding_pass.seat_type_id, boarding_pass.seat_id
    FROM flight
    INNER JOIN airplane ON flight.airplane_id = airplane.airplane_id
    INNER JOIN boarding_pass ON flight.flight_id = boarding_pass.flight_id
    WHERE airplane.airplane_id = 2 AND boarding_pass.seat_type_id = 3
    GROUP BY purchase_id;
"""

# Kids
res_children = conn.execute(text(query_children))
arr_res_ch = res_children.fetchall()
arr_res_ch_int = [int(row[0]) for row in arr_res_ch]

# purchase - passenger
res_group_purch_pass = conn.execute(text(query_air_1_seat_3))
arr_group_purch_pass = res_group_purch_pass.fetchall()
# arr_group_purch_pass_int = [int(row[0]) for row in arr_group_purch_pass]

arr_var_kid_passenger_id = []
arr_var_group_pur_id = []
arr_var_kids_boarding_pass_id = []
arr_purchase_id = []
arr_seat_type_id = []

for i in arr_res_ch_int:

    for row in arr_group_purch_pass:
        group_kid_purchase_id = row[0]
        passenger_ids_str  = row[1]
        seat_type_id = row[2]

        passenger_ids  = [int(num) for num in passenger_ids_str .split(', ')]

        if i in passenger_ids:
            print(f"The kids' purchase_id {group_kid_purchase_id} and the passenger_id {i}")
            arr_var_kid_passenger_id.append(i)
            arr_var_group_pur_id.append(group_kid_purchase_id)
            arr_purchase_id.append(passenger_ids_str)
            arr_seat_type_id.append(seat_type_id)

            break
        
    else:
        print(f"The kids' passenger_id {i} is not in any purchase_id")


for element in arr_purchase_id:
    numbers = element.replace(',', '').split()
    count = len(numbers)

unique_array_pur_id_kids_group = list(set(arr_var_group_pur_id))


# Asignación de sitios a los menores de edad - economico avion 1 - ubicando por el purchase_id

seat_row = range(19, 35)
seat_column = ['A', 'B', 'C', 'E', 'F', 'G']
valores = list(range(1, 17))

matriz = np.zeros((len(seat_row), len(seat_column)), dtype=int)

i = 0  # índice para recorrer la lista arr_var_kid_passenger_id
for j in range(len(seat_column)):
    for k in range(len(seat_row)):
        if matriz[k][j] == 0:  # si la celda está vacía
            if i < len(arr_var_group_pur_id):
                matriz[k][j] = arr_var_group_pur_id[i]
                i += 1
            else:
                break  # si ya no hay más datos, salir del bucle interno
    if i == len(arr_var_group_pur_id):
        break  # si ya se han asignado todos los datos, salir del bucle externo

matriz[0][1] = 165
print(matriz)


filas = len(matriz)
columnas = len(matriz[0])

for i in range(filas):
    for j in range(columnas - 1):
        if matriz[i][j] >= 1 and matriz[i][j+1] >= 1 and matriz[i][j] == matriz[i][j+1]:
            print(f"El número {matriz[i][j]} en la fila {i} y columna {j} tiene un vecino igual a su derecha.")
        # else:
        #     matriz[i][j+1] = 
        #     asignar un adulto con el mismo purchase_id al lado del menor de edad




