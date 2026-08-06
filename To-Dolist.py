import json
import datetime

def menu():
    print("===== MENÚ =====")
    print("1. Agregar tarea")
    print("2. Mostrar tarea")
    print("3. Completar tarea")
    print("4. Eliminar tarea")
    print("5. salir")
    opcion = int(input("Seleccione una opción: "))
    return  opcion

def agregar():

   tarea= input("escribe la tarea que deseas guardar: ")
   
   fechaCorrecta = False
   while not fechaCorrecta:
      fecha_usuario = input("Ingrese fecha (AAAA-MM-DD): ")
      try:
         fecha = datetime.date.fromisoformat(fecha_usuario)
         fechaCorrecta = True
      except  ValueError:
         print("Fecha inválida")
   tareas.append(
       {"tareaGuardada" : tarea,
        "completada": False,
        "fecha" :  fecha_usuario
       }
    )
   guardar()
   print("su tarea ha sido guardada")

def mostrar():
    if not tareas:
     print("la lista esta vacia")
        
    else:
        print ("===== TAREAS =====")
        for i in range(len(tareas)):
         if tareas[i]["completada"]:
            print( "[X]", i + 1, ".", tareas[i]["tareaGuardada"])
            print( "Tarea completada")

         else:
            fecha_tarea = datetime.date.fromisoformat(tareas[i]["fecha"])
            print( "[ ]", i + 1, ".", tareas[i]["tareaGuardada"])
            vencimiento(fecha_tarea)
            
def completar():

    tareaEditar = int(input("escribe el numero de la tarea que completaste: "))
      
    for i in range(len(tareas)):
        if i+ 1 == tareaEditar:
            print ("tarea encontrado ")
            confirmar = input("¿Completaste la tarea ?" \
             "1. si " \
             "2. no  ")
            if confirmar == "1":
               tareas[i]["completada"] = True
               print("Tarea completada correctamente.")
               guardar()
            else:
               print("velvemos a menu")
            break
    else:
        print("la tarea no existe.")

def eliminar():
    tareaEliminar = int(input("Escribe el numero de la tarea que deseas eliminar: "))
   
    for i in range(len(tareas)):
        if i+1 == tareaEliminar:
         print ("tarea encontrado ")
         confirmar = input("¿seguro que quieres eliminar la tarea ?" \
         "1. si " \
         "2. no  ")
         if confirmar == "1":
            tareas.pop(i)
            print("Tarea eliminada correctamente.")
            guardar()
         else:
            print("velvemos a menu")
         break
    else:
      print("La tarea no existe.")

def guardar():
   with open("pruebas.json", "w") as archivo:
       json.dump(tareas, archivo, indent=4)

def cargar():
    global tareas

    try:
        with open("pruebas.json", "r") as archivo:
            tareas = json.load(archivo)

    except FileNotFoundError:
        tareas = []

        with open("pruebas.json", "w") as archivo:
            json.dump(tareas, archivo, indent=4)

def vencimiento(fecha_tarea):
    hoy = datetime.date.today()
    diferencia = fecha_tarea - hoy 
    dias = diferencia.days
    if dias > 0:
        print("Faltan:", dias, "días")
    elif dias == 0:
        print("la tareas vence hoy")
    else:
        print("la tarea vencio hace ", abs(dias), "dias" )  

tareas = []
ejecutando = True
cargar()

while ejecutando:
    
    opcion = menu()
    match opcion:
     case 1:
        agregar()

     case 2:
        mostrar()

     case 3:
        completar()
      
     case 4:
          eliminar()
     
     case 5:
        print("Chaoooo")
        ejecutando = False

     case _:
        print("Opción inválida vuelve a intentar.")
