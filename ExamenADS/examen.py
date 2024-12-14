# Datos estáticos (Cuentas de ejemplo)
cuentas = {
    "1234": {"pin": "1111", "saldo": 5000, "movimientos": []},
    "5678": {"pin": "2222", "saldo": 10000, "movimientos": []},
    "7777": {"pin": "3456", "saldo": 4300, "movimientos": []},
    "8989": {"pin": "8965", "saldo": 9700, "movimientos": []},
}

# Validar usuario
def validar_usuario(numero_cuenta, pin):
    if numero_cuenta in cuentas and cuentas[numero_cuenta]["pin"] == pin:
        return True
    return False

# Retiro de efectivo
def retirar_efectivo(numero_cuenta, monto):
    cuenta = cuentas[numero_cuenta]
    if monto % 100 != 0:
        return "El monto debe ser múltiplo de 100."
    if monto > cuenta["saldo"]:
        return "Fondos insuficientes."
    cuenta["saldo"] -= monto
    cuenta["movimientos"].append(f"Retiro: -${monto}")
    return f"Retiro exitoso. Nuevo saldo: ${cuenta['saldo']}"

# Depósito de efectivo
def depositar_efectivo(numero_cuenta, monto):
    if monto <= 0:
        return "El monto a depositar debe ser mayor a 0."
    cuenta = cuentas[numero_cuenta]
    cuenta["saldo"] += monto
    cuenta["movimientos"].append(f"Depósito: +${monto}")
    return f"Depósito exitoso. Nuevo saldo: ${cuenta['saldo']}"

# Pago de servicios
def pagar_servicio(numero_cuenta, servicio, monto):
    cuenta = cuentas[numero_cuenta]
    if monto > cuenta["saldo"]:
        return "Fondos insuficientes para pagar el servicio."
    if monto <= 0:
        return "El monto debe ser mayor a 0."
    cuenta["saldo"] -= monto
    cuenta["movimientos"].append(f"Pago de {servicio}: -${monto}")
    return f"Pago exitoso de {servicio}. Nuevo saldo: ${cuenta['saldo']}"

# Consultar saldo
def consultar_saldo(numero_cuenta):
    return f"Saldo actual: ${cuentas[numero_cuenta]['saldo']}"

# Consultar movimientos
def consultar_movimientos(numero_cuenta):
    movimientos = cuentas[numero_cuenta]["movimientos"]
    if not movimientos:
        return "No hay movimientos recientes."
    return "Últimos movimientos:\n" + "\n".join([f"- {mov}" for mov in movimientos[-5:]])

# Validar entrada de num
def pedir_numero(mensaje):
    while True:
        try:
            return int(input(mensaje))
        except ValueError:
            print("Por favor, ingrese un número válido.")

# Menú inicual
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
            print(consultar_movimientos(numero_cuenta))
        elif opcion == "4":
            monto = pedir_numero("Ingrese el monto a depositar: ")
            print(depositar_efectivo(numero_cuenta, monto))
        elif opcion == "5":
            servicio = input("Ingrese el nombre del servicio (agua, luz, internet): ")
            monto = pedir_numero(f"Ingrese el monto a pagar para {servicio}: ")
            print(pagar_servicio(numero_cuenta, servicio, monto))
        elif opcion == "6":
            print("Gracias por usar el cajero. ¡Adiós!")
            break
        else:
            print("Opción no válida.")


menu()