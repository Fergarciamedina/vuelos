## Desafío

La aerolínea Andes Airlines desea evaluar si es posible realizar un check-in automático de sus pasajeros en países de Latinoamérica. El desafío consiste en crear un programa que simule el check-in mediante una API REST con un endpoint que permita consultar por el ID del vuelo y retornar la simulación. La base de datos contiene toda la información necesaria para la simulación.

## Lo que se tiene:

- La aerolínea cuenta con 2 aviones de distinta capacidad y distribución de asientos.
- Una base de datos (solo lectura) que contiene todos los datos necesarios para la simulación, con las credenciales de conexión a un servidor configurado para abortar conexiones inactivas por más de 5 segundos.

## A lo que se quiere llegar:

- Crear una API REST con un solo endpoint que permita consultar por el ID del vuelo y retornar la simulación del check-in.
- Asignar los asientos a cada tarjeta de embarque, teniendo en cuenta que los pasajeros menores de edad deben quedar al lado de al menos uno de sus acompañantes mayores de edad, tratar en lo posible que los asientos que se asignen estén juntos o muy cercanos, y que no se puede asignar un asiento de otra clase si la tarjeta de embarque pertenece a la clase “económica”.
- Transformar los nombres de los campos en Snake case de la base de datos a Camel case en la respuesta de la API.
- Contemplar buenas prácticas de programación y utilizar control de versiones.
- Entregar un archivo README.md con la documentación del proyecto, el código fuente en un repositorio privado de GitHub, y enviar la información solicitada mediante un formulario.

##### Estructura de la respuesta exitosa:
- Método: GET
- Ruta: /flights/:id/passengers

Respuesta:

```
{
  "code": 200,
  "data": {
    "flightId": 1,
    "takeoffDateTime": 1688207580,
    "takeoffAirport": "Aeropuerto Internacional Arturo Merino Benitez, Chile",
    "landingDateTime": 1688221980,
    "landingAirport": "Aeropuerto Internacional Jorge Cháve, Perú",
    "airplaneId": 1,
    "passengers": [
      {
        "passengerId": 90,
        "dni": 983834822,
        "name": "Marisol",
        "age": 44,
        "country": "México",
        "boardingPassId": 24,
        "purchaseId": 47,
        "seatTypeId": 1,
        "seatId": 1
      },
      {...}
    ]
  }
}
```

##### Estructura de respuesta en caso de vuelo no encontrado:
```
{
"code": 404,
"data": {}
}
```
##### Estructura de respuesta en caso de error:
```
{
"code": 400,
"errors": "could not connect to db"
}
```


- SQLAlchemy para manejar la interacción con la base de datos
- NumPy y Pandas para el análisis de datos y la creación de estadísticas
- FastAPI para la creación de la API web
- AWS para alojar la aplicación web

## Ejecución de la API:

1. Accede a la instancia de AWS donde se encuentra el código de la API.

2. Asegúrate de que todas las dependencias necesarias se encuentran instaladas en la instancia de AWS.

3. Abre una terminal en la instancia de AWS y navega hasta el directorio donde se encuentra el código de la API.

4. Ejecuta el siguiente comando para iniciar el servidor de la API:
```
uvicorn main:app --host 0.0.0.0 --port 80
```
En este comando, "main" se refiere al archivo principal de la API, y "app" se refiere a la instancia de la aplicación FastAPI que se ha creado en ese archivo.

5. El parámetro --host 0.0.0.0 especifica que la aplicación debe escuchar todas las solicitudes entrantes en todas las interfaces de red disponibles. El parámetro --port 80 especifica que la aplicación debe escuchar en el puerto 80, que es el puerto predeterminado para el tráfico HTTP.

6. Una vez que la API se esté ejecutando, podrás acceder a ella a través de una solicitud HTTP en el puerto 80. Para hacer esto, simplemente abre un navegador web y visita la dirección IP pública de la instancia de AWS en el puerto 80, seguida del endpoint de la API que se desea acceder.

## Pasos a seguir

1. Crear una instancia de una base de datos en AWS.
2. Crear un modelo de datos utilizando SQLAlchemy.
3. Utilizar FastAPI para crear una API web que permita a los usuarios ingresar información sobre sus compras y almacenarla en la base de datos.
4. Utilizar NumPy y Pandas para analizar los datos almacenados en la base de datos y crear estadísticas relevantes.
5. Desplegar la aplicación en un servidor de AWS.

Primero, se realiza la conexión a la base de datos (DB.py):

- Se importan las librerías necesarias para conectarse a una base de datos MySQL utilizando SQLAlchemy.
- Se establecen las credenciales necesarias para acceder a la base de datos.
Se crea una cadena de conexión utilizando las credenciales establecidas y la URL de la base de datos.
- Se crea un motor SQLAlchemy a partir de la cadena de conexión creada anteriormente.
- Se establece una conexión a la base de datos utilizando el motor SQLAlchemy creado.
- La conexión se guarda en una variable llamada "conn".

Segundo, se ubican los niños dentro del avión correspondiente a su tarjeta de embarque, para eso se realiza los siguientes pasos:

- Importar las librerías necesarias y el módulo DB.
- Definir consultas SQL para obtener información de los menores de edad y la información de los asientos reservados en el avión.
- Ejecutar la consulta SQL para obtener los menores de edad y almacenarlos en una variable.
- Ejecutar la consulta SQL para obtener los detalles de los asientos reservados en el avión y almacenarlos en una variable.
- Definir listas vacías para almacenar información de los menores de edad y los detalles de los asientos reservados.
- Recorrer la lista de los menores de edad y para cada menor de edad, recorrer la lista de los detalles de los asientos reservados en el avión. Si el menor de edad está en la lista de pasajeros en el asiento reservado, agregar información del menor de edad y la reserva del asiento
- Crear una lista de identificadores de compra únicos para los menores de edad que tienen asientos reservados.
- Crear una matriz de ceros de tamaño 16x6 para representar los asientos disponibles en el avión.
- Recorrer la lista de identificadores de compra de los menores de edad y, para cada identificador, encontrar los asientos reservados en la reserva. Luego, buscar un asiento disponible en la matriz de asientos disponible en el avión y reservarlo para el menor de edad.

Tercero, se ubican a los a los adultos al lado de los menores de edad, para eso:

- Se recorre la matriz buscando si tienen vecinos con el mismo purchase_id. Es decir, buscar si tienen numeros al su lado con el mismo valor.

Cuarto, se ubican a los demás pasajeros considerando juntos a los que tienen el mismo purchase_id:

- Se utiliza la matriz anterior y se comparan, ya no vecinos a la derecha o izquierda, sin o que vecinos en un kernel. Es decir, se evalua una matriz de 3x3 donde se ordena o se hace un sorting para que dentro de esa matriz de 3x3 se tenga los mismos valores posibles. Y así se itera con toda la matriz de los asientos. Se restringe a no cambiar a los niños y sus acompañantes ubicados anteriormente.

Quinto, se realizan estos pasos para los demás tipos de asientos, "Primera clase" y "Económico premium" y así como para el siguiente avion.

Sexto, se cambian las celdas de la matrices de purchase\_id a passenger\_id para poder asociar las filas y columnas de los asientos al passenger\_id.

Con estos datos, se crea un index.html (se usa tambien scss para el diseño de la tarjeta de embarque) para mostrar las tarjetas de embarques para cada pasajero según el codigo del pasajero.

Finalmente, en el web server AWS se suben todos los codigos y se crea el apiREST usand fastapi.

