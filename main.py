import json
from datetime import datetime,timezone #importación para generar la fecha
def Abrirpagos():#función para abrir el archivo json
    datos=[]
    with open("pagos.json", encoding="utf8") as openfile:
        datos=json.load(openfile)
        return datos
def guardarpagos(midato):#función para guardar cambios en el json
    with open("pagos.json", "w") as mifile:
        json.dump(midato,mifile)
        
def Abrirpedidos():#función para abrir el archivo json
    datos=[]
    with open("pedidos.json", encoding="utf8") as openfile:
        datos=json.load(openfile)
        return datos
def guardarpedidos(midato):#función para guardar cambios en el json
    with open("pedidos.json", "w") as mifile:
        json.dump(midato,mifile)

def Abrirmenu():#función para abrir el archivo json
    datos=[]
    with open("menu.json", encoding="utf8") as openfile:
        datos=json.load(openfile)
        return datos
def guardarmenu(midato):#función para guardar cambios en el json
    with open("menu.json", "w") as mifile:
        json.dump(midato,mifile)


def opciones():
    print("--------MOLIPOLLITO--------")
    print("1. HACER PEDIDO")
    print("2. VER PEDIDOS")
def categorias():
    print("----Categorias----\n")
    print("1. entrada")
    print("2. Plato fuerte")
    print("3. Bebidas")
    print("4. terminar pedido")
def mostrar_pedidos():
    print("""
    --------VER PEDIDOS-------
    1. Todos los pedidos
    2. Ver pedido especifico
    3. volver
    """)
pagos=Abrirpagos()
guardarpagos(pagos)


bucle=True
while bucle==True:
    opciones()
    opc=input("Escoje una opción: ")
    if opc=="1":
        menu=Abrirmenu()
        pedidos=Abrirpedidos()
        nombre_cliente=input("Nombre del cliente: ")
        lista_pedido=[]
        booleano=True
        while booleano==True:
            categorias()
            opc_categoria=input("de que categoría: ")
            if opc_categoria=="1":
                for i in menu["menu"]:
                    if i["categoria"]=="entrada":
                        print("--------------------------")
                        print("Nombre: ",i["nombre"])
                        print("Precio: ",i["precio"])
                        print("--------------------------")
                bool=True
                while bool==True:
                    plato_pedido=input("nombre de lo que pediste: ")      
                    for i in menu["menu"]:
                        if plato_pedido==i["nombre"] and i["categoria"]=="entrada":
                            lista_pedido.append({"categoria":i["categoria"],"nombre":i["nombre"],"precio":i["precio"]})
                            bool=False

            if opc_categoria=="2":
                for i in menu["menu"]:
                    if i["categoria"]=="plato_fuerte":
                        print("--------------------------")
                        print("Nombre: ",i["nombre"])
                        print("Precio: ",i["precio"])
                        print("--------------------------")

                bool=True
                while bool==True:
                    plato_pedido=input("nombre de lo que pediste: ")      
                    for i in menu["menu"]:
                        if plato_pedido==i["nombre"] and i["categoria"]=="plato_fuerte":
                            lista_pedido.append({"categoria":i["categoria"],"nombre":i["nombre"],"precio":i["precio"]})
                            bool=False

            if opc_categoria=="3":
                for i in menu["menu"]:
                    if i["categoria"]=="bebida":
                        print("--------------------------")
                        print("Nombre: ",i["nombre"])
                        print("Precio: ",i["precio"])
                        print("--------------------------")
                bool=True
                while bool==True:
                    plato_pedido=input("nombre de lo que pediste: ")      
                    for i in menu["menu"]:
                        if plato_pedido==i["nombre"] and i["categoria"]=="bebida":
                            lista_pedido.append({"categoria":i["categoria"],"nombre":i["nombre"],"precio":i["precio"]})
                            bool=False

            if opc_categoria=="4":
                booleano=False
        estado=input("Estado del pedido: ")
        pedidos["pedidos"].append({"cliente":nombre_cliente, "items":lista_pedido,"estado":estado})
        guardarpedidos(pedidos)
    if opc=="2":
        pedidos=Abrirpedidos()
        bool=True
        while bool==True:
            mostrar_pedidos()
            opc_pedidos=input("escoje una opción: ")
            if opc_pedidos=="1":
                for i in pedidos["pedidos"]:
                    print("///////////////////////////////")
                    print("cliente: ",i["cliente"])
                    contador=0
                    for x in i["items"]:
                        contador+=1
                        print("-------------------------------")
                        print("item #",contador)
                        print("Categiria: ",x["categoria"])
                        print("Nombre: ",x["nombre"])
                        print("Precio: ",x["precio"])
                        print("-------------------------------")
                    print("Estado: ",i["estado"])
                    print("///////////////////////////////")
            if opc_pedidos=="2":
                pedidos=Abrirpedidos()
                print("------VER PEDIDO ESPECIFICO-----")
                bool=True
                while bool==True:
                    nombre=input("Nombre del cliente que realizó el pedido: ")
                    con=0
                    for i in pedidos["pedidos"]:
                        if i["cliente"]==nombre:
                            con+=1
                            print("///////////////////////////////")
                            print("cliente: ",i["cliente"])
                            contador=0
                            for x in i["items"]:
                                contador+=1
                                print("-------------------------------")
                                print("item #",contador)
                                print("Categiria: ",x["categoria"])
                                print("Nombre: ",x["nombre"])
                                print("Precio: ",x["precio"])
                                print("-------------------------------")
                            print("Estado: ",i["estado"])
                            print("///////////////////////////////")
                    if con==0:
                        print("no existe este cliente o los escribiste mal")
                        print("vuelve a intentarlo")
                    else:
                        x1=True
                        while x1==True:
                            print("1. Ver otro pedido")
                            print("2. salir")
                            salir=input("Ingrea tu opción: ")
                            if salir=="1":
                                x1=False
                            if salir=="2":
                                bool=False
                                x1=False