import datetime

# Datos estáticos (Cuentas de ejemplo que cree)
cuentas = {
    "1234": {"pin": "1111", "saldo": 5000, "movimientos": [], "limite_diario": 5000, "retiros_hoy": 0},
    "5678": {"pin": "2222", "saldo": 10000, "movimientos": [], "limite_diario": 5000, "retiros_hoy": 0},
    "7777": {"pin": "3456", "saldo": 4300, "movimientos": [], "limite_diario": 5000, "retiros_hoy": 0},
    "8989": {"pin": "8965", "saldo": 9700, "movimientos": [], "limite_diario": 5000, "retiros_hoy": 0},
}

# Validacion de cuentaUsuario
def validar_usuario(numero_cuenta, pin):
    if numero_cuenta in cuentas and cuentas[numero_cuenta]["pin"] == pin:
        return True
    return False

# Generación de comprobante
def generar_comprobante(numero_cuenta, operacion, detalles):
    nombre_archivo = f"comprobante_{numero_cuenta}_{operacion}_{datetime.datetime.now().strftime('%Y%m%d%H%M%S')}.txt"
    with open(nombre_archivo, "w") as archivo:
        archivo.write(f"--- COMPROBANTE DE {operacion.upper()} ---\n")
        archivo.write(f"Fecha: {datetime.datetime.now().strftime('%d/%m/%Y')}\n")
        archivo.write(f"Número de cuenta: {numero_cuenta}\n")
        archivo.write(f"Detalles: {detalles}\n")
    print(f"Comprobante generado: {nombre_archivo}")

# Retiro de efectivo
def retirar_efectivo(numero_cuenta, monto):
    cuenta = cuentas[numero_cuenta]
    if monto % 100 != 0:
        return "El monto debe ser múltiplo de 100."
    if monto > cuenta["saldo"]:
        return "Fondos insuficientes."
    if monto > cuenta["limite_diario"] - cuenta["retiros_hoy"]:
        return f"Excede el límite diario permitido. Límite restante: ${cuenta['limite_diario'] - cuenta['retiros_hoy']}."
    
    cuenta["saldo"] -= monto
    cuenta["retiros_hoy"] += monto
    cuenta["movimientos"].append(f"Retiro: -${monto}")
    generar_comprobante(numero_cuenta, "retiro", f"Retiraste ${monto}. Saldo actual: ${cuenta['saldo']}")
    return f"Retiro exitoso. Nuevo saldo: ${cuenta['saldo']}"

# Depósito de efectivo
def depositar_efectivo(numero_cuenta, billetes):
    if any(billete % 100 != 0 for billete in billetes):
        return "Todos los billetes deben ser múltiplos de 100."
    
    monto = sum(billetes)
    cuenta = cuentas[numero_cuenta]
    cuenta["saldo"] += monto
    cuenta["movimientos"].append(f"Depósito: +${monto}")
    generar_comprobante(numero_cuenta, "deposito", f"Depositaste ${monto}. Saldo actual: ${cuenta['saldo']}")
    return f"Depósito exitoso. Nuevo saldo: ${cuenta['saldo']}"

# Pago de servicios
def pagar_servicio(numero_cuenta, servicio, monto, referencia):
    cuenta = cuentas[numero_cuenta]
    if referencia not in ["1111", "2222", "3333"]:
        return "Número de referencia incorrecto."
    if monto > cuenta["saldo"]:
        return "Fondos insuficientes para pagar el servicio."
    cuenta["saldo"] -= monto
    cuenta["movimientos"].append(f"Pago de {servicio}: -${monto}")
    generar_comprobante(numero_cuenta, "pago_servicio", f"Pago de {servicio} por ${monto}. Saldo actual: ${cuenta['saldo']}")
    return f"Pago exitoso de {servicio}. Nuevo saldo: ${cuenta['saldo']}"

# Consultar saldo
def consultar_saldo(numero_cuenta):
    return f"Saldo actual: ${cuentas[numero_cuenta]['saldo']}"

# Consultar movimientos
def consultar_movimientos(numero_cuenta, tipo=None):
    movimientos = cuentas[numero_cuenta]["movimientos"]
    if tipo:
        movimientos = [mov for mov in movimientos if tipo in mov]
    if not movimientos:
        return "No hay movimientos recientes."
    generar_comprobante(numero_cuenta, "consulta_movimientos", "\n".join(movimientos[-5:]))
    return "Últimos movimientos:\n" + "\n".join(movimientos[-5:])

# Validar la entrada num
def pedir_numero(mensaje):
    while True:
        try:
            return int(input(mensaje))
        except ValueError:
            print("Por favor, ingrese un número válido.")

# Menú de entrada vaya el inicial
def menu():
    print("Bienvenido al Cajero")
    numero_cuenta = input("Ingrese su número de cuenta: ")
    pin = input("Ingrese su PIN: ")

    if not validar_usuario(numero_cuenta, pin):
        print("Número de cuenta o PIN incorrecto.")
        return

    while True:
        print("\n1. Retirar efectivo\n2. Consultar saldo\n3. Consultar movimientos\n4. Depositar efectivo\n5. Pagar servicio\n6. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            monto = pedir_numero("Ingrese el monto a retirar: ")
            print(retirar_efectivo(numero_cuenta, monto))
        elif opcion == "2":
            print(consultar_saldo(numero_cuenta))
        elif opcion == "3":
            tipo = input("¿Deseas filtrar por algún tipo de movimiento? (retiro, deposito, pago) o presiona Enter para todos: ")
            print(consultar_movimientos(numero_cuenta, tipo if tipo else None))
        elif opcion == "4":
            billetes = input("Ingrese la lista de billetes separados por coma (Ej: 100,200,500): ")
            billetes = [int(b) for b in billetes.split(",")]
            print(depositar_efectivo(numero_cuenta, billetes))
        elif opcion == "5":
            servicio = input("Ingrese el nombre del servicio (agua, luz, internet): ")
            referencia = input("Ingrese el número de referencia: ")
            monto = pedir_numero(f"Ingrese el monto a pagar para {servicio}: ")
            print(pagar_servicio(numero_cuenta, servicio, monto, referencia))
        elif opcion == "6":
            print("Gracias por usar el cajero. ¡Adiós!")
            break
        else:
            print("Opción no válida.")

menu()