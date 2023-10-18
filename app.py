class Reserva:
    def __init__(self):
        self.nombre = input("Por favor, ingresa tu nombre completo: ")
        self.email = input("Por favor, ingresa tu dirección de correo electrónico: ")
        self.telefono = input("Por favor, ingresa tu número de teléfono: ")
        self.cm_tatuaje = input("Por favor, ingresa el tamaño del tatuaje en centímetros: ")
        self.zona_tatuar = input("Por favor, ingresa la zona del cuerpo donde se realizará el tatuaje: ")
        self.img_url = input("Opcional: Si tienes una imagen o URL del diseño del tatuaje, ingrésala aquí (o presiona Enter para omitir): ")

class Agenda: 
    def __init__(self):
        self.reservaciones  = []
        
    def agregar_reserva(self, reserva):
        self.reservaciones.append(reserva)
        print("-" * 30)
        print("Se agregó una reserva") 
        
    def eliminar_reserva(self, reserva):
    
        if 0 <= reserva < len(self.reservaciones):
            reserva_eliminar = self.reservaciones[reserva]
            self.reservaciones.remove(reserva_eliminar)
            print("Reserva eliminada correctamente.")
        else:
            print("Número de reserva inválido.")
            
    def editar_reserva(self, reserva):

        if 0 <= reserva < len(self.reservaciones):
            reserva = self.reservaciones[reserva]
            print("¿Qué te gustaría editar?")
            print("1. Nombre")
            print("2. Email")
            print("3. Teléfono")
            print("4. Tamaño del tatuaje")
            print("5. Zona a tatuar")
            print("6. Imagen/URL")
            opcion_edit = input("Selecciona una opción: ")

            if opcion_edit == "1":
                reserva.nombre = input("Nuevo nombre: ")
            elif opcion_edit == "2":
                reserva.email = input("Nuevo email: ")
            elif opcion_edit == "3":
                reserva.telefono = input("Nuevo teléfono: ")
            elif opcion_edit == "4":
                reserva.cm_tatuaje = input("Nuevo tamaño del tatuaje en centímetros: ")
            elif opcion_edit == "5":
                reserva.zona_tatuar = input("Nueva zona a tatuar: ")
            elif opcion_edit == "6":
                reserva.img_url = input("Nueva imagen/URL (o presiona Enter para omitir): ")
            else:
                print("Opción inválida.")
        else:
            print("Número de reserva inválido.")
    
    def mostrar_reservas(self):
        reservas_dict_list = []  # Lista para almacenar los diccionarios de reservas
    
        for idx, reserva in enumerate(self.reservaciones):
            reserva_dict = {
                "Reserva": idx,
                "Nombre": reserva.nombre,
                "Email": reserva.email,
                "Teléfono": reserva.telefono,
                "Tamaño del tatuaje (cm)": reserva.cm_tatuaje,
                "Zona a tatuar": reserva.zona_tatuar,
                "Imagen/URL": reserva.img_url or 'No especificada'
            }
            reservas_dict_list.append(reserva_dict)

        
        for reserva in reservas_dict_list:
            print("-" * 30)
            for key, value in reserva.items():
                print(f"{key}: {value}")
            print("-" * 30) 

agenda = Agenda()

while True:
    print("1. Agregar reserva")
    print("2. Editar reserva")
    print("3. Eliminar reserva")
    print("4. Mostrar reservas")
    print("5. Salir")
    opcion = input("Ingresa una opción: ")
     
    if opcion == "1":
        nueva_reserva = Reserva()
        agenda.agregar_reserva(nueva_reserva)
    elif opcion == "2":
        agenda.mostrar_reservas()
        numero_reserva = int(input("Selecciona el número de reserva a editar: "))
        agenda.editar_reserva(numero_reserva)
    elif opcion == "3":
        agenda.mostrar_reservas()
        numero_reserva = int(input("Selecciona el número de reserva a eliminar: "))
        agenda.eliminar_reserva(numero_reserva)
    elif opcion == "4":
        agenda.mostrar_reservas()
    elif opcion == "5":
        print("Gracias por usar el sistema de reservas.")
        break
    else:    
        print("Opción inválida. Por favor, selecciona una opción válida.")
 