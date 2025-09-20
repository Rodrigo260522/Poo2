class InventarioTienda:
    def __init__(self, nombre_tienda):
        self.nombre_tienda = nombre_tienda
        self.productos = []

    def agregar_producto(self, nombre, precio, cantidad):
        producto = {'nombre': nombre, 'precio': precio, 'cantidad': cantidad}
        self.productos.append(producto)

    def vender_producto(self, nombre, cantidad):
        for producto in self.productos:
            if producto['nombre'] == nombre:
                if producto['cantidad'] >= cantidad:
                    producto['cantidad'] -= cantidad
                    print(f"Venta realizada: {cantidad} unidades de '{nombre}'")
                else:
                    print(f"No hay suficientes productos de '{nombre}'")
                return
        print(f"El producto '{nombre}' no esta en el inventario")

    def mostrar_inventario(self):
        print(f"Inventario de {self.nombre_tienda}: ")
        for producto in self.productos:
            print(f"- {producto['nombre']}: ${producto['precio']} ({producto['cantidad']} unidades)")

    def producto_mas_caro(self):
        if not self.productos:
            return None
        producto_caro = max(self.productos, key=lambda p: p['precio'])
        return (producto_caro['nombre'], producto_caro['precio'])
    
tienda = InventarioTienda("Tienda")

while True:
    print("1. Agregar producto")
    print("2. Vender producto")
    print("3. Ver inventario")
    print("4. Consultar producto mas caro")
    print("5. Salir")
    opcion = input("Selecciona una opcion: ")

    if opcion == "1":
        nombre = input("Nombre del producto: ")
        try:
            precio = float(input("Precio del producto: "))
            cantidad = int(input("Cantidad disponible: "))
            # Validación de precio y cantidad
            if precio <= 0 or cantidad <= 0:
                print("Error: El precio y la cantidad deben ser positivos.")
            else:
                tienda.agregar_producto(nombre, precio, cantidad)
                print("Producto agregado correctamente.")
        except ValueError:
            print("Error: precio y cantidad deben ser numeros.")
    elif opcion == "2":
        nombre = input("Nombre del producto a vender: ")
        try:
            cantidad = int(input("Cantidad a vender: "))
            # Validación de cantidad
            if cantidad <= 0:
                print("Error: La cantidad a vender debe ser un numero positivo.")
            else:
                tienda.vender_producto(nombre, cantidad)
        except ValueError:
            print("Error: la cantidad debe ser un numero entero.")
    elif opcion == "3":
        tienda.mostrar_inventario()
    elif opcion == "4":
        resultado = tienda.producto_mas_caro()
        if resultado:
            print(f"Producto mas caro: {resultado[0]} (${resultado[1]})")
        else:
            print("No hay productos en el inventario.")
    elif opcion == "5":
        print("Saliendo")
        break
    else:
        print("Opcion invalida, intenta de nuevo.")
