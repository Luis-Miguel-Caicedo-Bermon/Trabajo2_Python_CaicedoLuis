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
    print("2. ")
def categorias():
    print("----Categorias----\n")
    print("1. entrada")
    print("2. Plato fuerte")
    print("3. Bebidas")
    print("4. terminar pedido")
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
        bool=True
        while bool==True:
            categorias()
            opc_categoria=input("de que categoría: ")
            if opc_categoria=="1":
                for i in menu["menu"]:
                    if i["categoria"]=="entrada":
                        print("--------------------------")
                        print("Nombre: ",i["nombre"])
                        print("Precio: ",i["precio"])
                        print("--------------------------")
                for i in menu["menu"]:
                    plato_pedido=input("nombre de lo que pediste: ")
                    if plato_pedido==i["nombre"] and i["categoria"]=="plato_fuerte":
                        lista_pedido.append({"categoria":i["categoria"],"nombre":i["nombre"],"precio":i["precio"]})
                    else:
                        print("este producto no existe")
                        print("o lo escribiste mal")

            if opc_categoria=="2":
                for i in menu["menu"]:
                    if i["categoria"]=="plato_fuerte":
                        print("--------------------------")
                        print("Nombre: ",i["nombre"])
                        print("Precio: ",i["precio"])
                        print("--------------------------")
                        
                for i in menu["menu"]:
                    plato_pedido=input("nombre de lo que pediste: ")
                    if plato_pedido==i["nombre"] and i["categoria"]=="plato_fuerte":
                        lista_pedido.append({"categoria":i["categoria"],"nombre":i["nombre"],"precio":i["precio"]})
                    else:
                        print("este producto no existe")
                        print("o lo escribiste mal")

            if opc_categoria=="3":
                for i in menu["menu"]:
                    if i["categoria"]=="bebidas":
                        print("--------------------------")
                        print("Nombre: ",i["nombre"])
                        print("Precio: ",i["precio"])
                        print("--------------------------")
                for i in menu["menu"]:
                    plato_pedido=input("nombre de lo que pediste: ")
                    if plato_pedido==i["nombre"] and i["categoria"]=="plato_fuerte":
                        lista_pedido.append({"categoria":i["categoria"],"nombre":i["nombre"],"precio":i["precio"]})
                    else:
                        print("este producto no existe")
                        print("o lo escribiste mal")

            if opc_categoria=="4":
                bool=False
        pagado=input("El pedido se pagó?")
            