import tkinter as tk
from tkinter import messagebox
import datetime

# Datos estáticos (Cuentas de ejemplo que cree)
cuentas = {
    "1234": {"pin": "1111", "saldo": 5000, "movimientos": [], "limite_diario": 5000, "retiros_hoy": 0, "tarjeta_credito": {"saldo": 4000,"limite": 20000}},
    "5678": {"pin": "2222", "saldo": 10000, "movimientos": [], "limite_diario": 5000, "retiros_hoy": 0, "tarjeta_credito": {"saldo": 8900,"limite": 25000}},
    "7777": {"pin": "3456", "saldo": 4300, "movimientos": [], "limite_diario": 5000, "retiros_hoy": 0, "tarjeta_credito": {"saldo": 15000,"limite": 20000}},
    "8989": {"pin": "8965", "saldo": 9700, "movimientos": [], "limite_diario": 5000, "retiros_hoy": 0, "tarjeta_credito": {"saldo": 1000,"limite": 5000}}
}

class Cajero(tk.Tk):
    def __init__(self):
        super().__init__()
        self.__setup_window()
        self.__create_login_widgets()
        
    def __setup_window(self):
        self.title("Cajero Automático")
        self.geometry("600x800")
        self.configure(bg='#f0f0f0')
        
    def __create_login_widgets(self):
        self.frame_login = tk.Frame(self, bg='#f0f0f0')
        self.frame_login.pack(padx=20, pady=20)
        
        # Logo simulado
        logo_frame = tk.Frame(self.frame_login, bg='#1a5f7a', height=90, width=200)
        logo_frame.pack(pady=(0, 20))
        logo_frame.pack_propagate(False)
        
        # Botones para operaciones sin cuenta
        frame_sin_cuenta = tk.Frame(self.frame_login, bg='#f0f0f0')
        frame_sin_cuenta.pack(fill='x', pady=(0, 30))
        
        tk.Label(frame_sin_cuenta,
                text="Operaciones sin cuenta",
                font=('Arial', 14, 'bold'),
                bg='#f0f0f0',
                fg='#1a5f7a').pack(pady=(0, 10))
                
        tk.Button(frame_sin_cuenta,
                text="Realizar Depósito",
                command=self.__mostrar_deposito_sin_cuenta,
                bg='#1a5f7a',
                fg='white',
                font=('Arial', 12),
                width=20,
                cursor='hand2').pack(pady=5)
        
        tk.Button(frame_sin_cuenta,
         text="Pagar Servicios",
         command=self.__mostrar_pago_servicio_sin_cuenta,
         bg='#1a5f7a',
         fg='white',
         font=('Arial', 12),
         width=20,
         cursor='hand2').pack(pady=5)
                
        tk.Label(frame_sin_cuenta,
                text="───────── o ─────────",
                bg='#f0f0f0',
                fg='#666666').pack(pady=20)
        
        titulo = tk.Label(self.frame_login, 
                         text="Bienvenido al Cajero",
                         font=('Arial', 24, 'bold'),
                         bg='#f0f0f0',
                         fg='#1a5f7a')
        titulo.pack(pady=20)
        
        frame_entradas = tk.Frame(self.frame_login, bg='#f0f0f0')
        frame_entradas.pack(fill='x', padx=20)
        
        tk.Label(frame_entradas, 
                text="Número de Cuenta:",
                bg='#f0f0f0',
                font=('Arial', 12)).pack(anchor='w')
        self.entrada_cuenta = tk.Entry(frame_entradas,
                                     font=('Arial', 14),
                                     justify='center')
        self.entrada_cuenta.pack(fill='x', pady=(5, 15))
        
        tk.Label(frame_entradas,
                text="PIN:",
                bg='#f0f0f0',
                font=('Arial', 12)).pack(anchor='w')
        self.entrada_pin = tk.Entry(frame_entradas,
                                  show="•",
                                  font=('Arial', 14),
                                  justify='center')
        self.entrada_pin.pack(fill='x', pady=(5, 20))
        
        btn_ingresar = tk.Button(frame_entradas,
                                text="INGRESAR",
                                command=self.__validar_login,
                                bg='#1a5f7a',
                                fg='white',
                                font=('Arial', 12, 'bold'),
                                width=20,
                                height=2,
                                cursor='hand2')
        btn_ingresar.pack(pady=20)
        
        # Mensaje de ayuda
      #  tk.Label(self.frame_login,
       #         text="Para pruebas usar:\nCuenta: 1234, PIN: 1111",
        #        bg='#f0f0f0',
         #       fg='#666666',
          #      font=('Arial', 10)).pack(pady=(20, 0))
        
        # Validacion de cuentaUsuario        
    def __validar_login(self):
        self.cuenta_actual = self.entrada_cuenta.get()
        pin = self.entrada_pin.get()
        
        if self.cuenta_actual in cuentas and cuentas[self.cuenta_actual]["pin"] == pin:
            self.__show_menu()
        else:
            messagebox.showerror("Error", "Cuenta o PIN incorrecto")
            
    def __show_menu(self):
        self.frame_login.destroy()
        
        self.frame_menu = tk.Frame(self, bg='#f0f0f0')
        self.frame_menu.pack(padx=20, pady=20, fill='both', expand=True)
        
        tk.Label(self.frame_menu,
                text=f"Bienvenido\nCuenta: {self.cuenta_actual}",
                font=('Arial', 16, 'bold'),
                bg='#f0f0f0',
                fg='#1a5f7a').pack(pady=(0, 30))
        
        opciones = [
            ("Retirar Efectivo", self.__mostrar_retiro),
            ("Consultar Saldo", self.__consultar_saldo),
            ("Consultar Movimientos", self.__consultar_movimientos),
            ("Depositar Efectivo", self.__mostrar_deposito),
            ("Pagar Servicio", self.__mostrar_pago_servicio),
            ("Pagar Tarjeta", self.__mostrar_pago_tarjeta),
            ("Salir", self.__salir)
        ]
        
        for texto, comando in opciones:
            tk.Button(self.frame_menu,
                     text=texto,
                     command=comando,
                     bg='#1a5f7a',
                     fg='white',
                     font=('Arial', 12),
                     width=20,
                     height=2,
                     cursor='hand2').pack(pady=5)
                     
    def __mostrar_retiro(self):
        ventana = tk.Toplevel(self)
        ventana.title("Retiro de Efectivo")
        ventana.geometry("300x250")
        ventana.configure(bg='#f0f0f0')
        ventana.resizable(False, False)
        ventana.transient(self)
        ventana.grab_set()
        
        frame = tk.Frame(ventana, bg='#f0f0f0', padx=20, pady=20)
        frame.pack(fill='both', expand=True)
        
        tk.Label(frame,
                text="Monto a retirar:",
                bg='#f0f0f0',
                font=('Arial', 12)).pack(pady=10)
                
        entrada_monto = tk.Entry(frame,
                               font=('Arial', 14),
                               justify='center')
        entrada_monto.pack(pady=5)
        
        def realizar_retiro():
            try:
                monto = int(entrada_monto.get())
                cuenta = cuentas[self.cuenta_actual]
                
                if monto % 100 != 0:
                    messagebox.showerror("Error", "El monto debe ser múltiplo de 100")
                    return
                    
                if monto > cuenta["saldo"]:
                    messagebox.showerror("Error", "Fondos insuficientes")
                    return
                    
                if monto > cuenta["limite_diario"] - cuenta["retiros_hoy"]:
                    messagebox.showerror("Error", 
                                       f"Excede el límite diario. Disponible: ${cuenta['limite_diario'] - cuenta['retiros_hoy']}")
                    return
                
                cuenta["saldo"] -= monto
                cuenta["retiros_hoy"] += monto
                cuenta["movimientos"].append(f"Retiro: -${monto}")
                self.__generar_comprobante("retiro", f"Retiro por ${monto}")
                messagebox.showinfo("Éxito", f"Retiro exitoso. Nuevo saldo: ${cuenta['saldo']}")
                ventana.destroy()
                
            except ValueError:
                messagebox.showerror("Error", "Por favor ingrese un monto válido")
                
        tk.Button(frame,
                 text="Retirar",
                 command=realizar_retiro,
                 bg='#1a5f7a',
                 fg='white',
                 font=('Arial', 12),
                 width=20,
                 height=2,
                 cursor='hand2').pack(pady=20)

    def __mostrar_deposito(self):
        ventana = tk.Toplevel(self)
        ventana.title("Depósito de Efectivo")
        ventana.geometry("300x250")
        ventana.configure(bg='#f0f0f0')
        ventana.resizable(False, False)
        ventana.transient(self)
        ventana.grab_set()
        
        frame = tk.Frame(ventana, bg='#f0f0f0', padx=20, pady=20)
        frame.pack(fill='both', expand=True)
        
        tk.Label(frame,
                text="Ingrese los billetes separados por coma\n(Ej: 100,200,500):",
                bg='#f0f0f0',
                font=('Arial', 12)).pack(pady=10)
                
        entrada_billetes = tk.Entry(frame,
                                  font=('Arial', 14),
                                  justify='center')
        entrada_billetes.pack(pady=5)
        
        def realizar_deposito():
            try:
                billetes = [int(b.strip()) for b in entrada_billetes.get().split(",")]
                
                if any(billete % 100 != 0 for billete in billetes):
                    messagebox.showerror("Error", "Todos los billetes deben ser múltiplo de 100")
                    return
                    
                monto = sum(billetes)
                cuenta = cuentas[self.cuenta_actual]
                cuenta["saldo"] += monto
                cuenta["movimientos"].append(f"Depósito: +${monto}")
                self.__generar_comprobante("deposito", f"Depósito por ${monto}")
                messagebox.showinfo("Éxito", f"Depósito exitoso. Nuevo saldo: ${cuenta['saldo']}")
                ventana.destroy()
                
            except ValueError:
                messagebox.showerror("Error", "Por favor ingrese billetes válidos")
                
        tk.Button(frame,
                 text="Depositar",
                 command=realizar_deposito,
                 bg='#1a5f7a',
                 fg='white',
                 font=('Arial', 12),
                 width=20,
                 height=2,
                 cursor='hand2').pack(pady=20)
        
    def __mostrar_deposito_sin_cuenta(self):
        ventana = tk.Toplevel(self)
        ventana.title("Depósito a Cuenta")
        ventana.geometry("350x450")
        ventana.configure(bg='#f0f0f0')
        ventana.resizable(False, False)
        ventana.transient(self)
        ventana.grab_set()
        
        frame = tk.Frame(ventana, bg='#f0f0f0', padx=20, pady=20)
        frame.pack(fill='both', expand=True)
        
        # Número de cuenta destino
        tk.Label(frame,
                text="Número de Cuenta Destino:",
                bg='#f0f0f0',
                font=('Arial', 12)).pack(pady=5)
        entrada_cuenta = tk.Entry(frame,
                                font=('Arial', 14),
                                justify='center')
        entrada_cuenta.pack(pady=5)
        
        # Billetes a depositar
        tk.Label(frame,
                text="Ingrese los billetes separados por coma\n(Ej: 100,200,500):",
                bg='#f0f0f0',
                font=('Arial', 12)).pack(pady=10)
        entrada_billetes = tk.Entry(frame,
                                font=('Arial', 14),
                                justify='center')
        entrada_billetes.pack(pady=5)
        
        # Nombre del depositante
        tk.Label(frame,
                text="Nombre del Depositante:",
                bg='#f0f0f0',
                font=('Arial', 12)).pack(pady=5)
        entrada_nombre = tk.Entry(frame,
                                font=('Arial', 14),
                                justify='center')
        entrada_nombre.pack(pady=5)
        
        def realizar_deposito():
            try:
                cuenta_destino = entrada_cuenta.get()
                nombre_depositante = entrada_nombre.get()
                
                # Validar cuenta
                if cuenta_destino not in cuentas:
                    messagebox.showerror("Error", "La cuenta ingresada no existe")
                    return
                    
                if not nombre_depositante.strip():
                    messagebox.showerror("Error", "Ingrese el nombre del depositante")
                    return
                
                # Procesar billetes
                billetes_texto = entrada_billetes.get()
                try:
                    billetes = [int(b.strip()) for b in billetes_texto.split(",")]
                except:
                    messagebox.showerror("Error", "Formato de billetes inválido")
                    return
                    
                if any(billete % 100 != 0 for billete in billetes):
                    messagebox.showerror("Error", "Todos los billetes deben ser múltiplo de 100")
                    return
                    
                monto = sum(billetes)
                
                # Realizar depósito
                cuenta = cuentas[cuenta_destino]
                cuenta["saldo"] += monto
                cuenta["movimientos"].append(f"Depósito de {nombre_depositante}: +${monto}")
                
                # Generar comprobante
                fecha = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
                nombre_archivo = f"comprobante_deposito_{cuenta_destino}_{fecha}.txt"
                
                with open(nombre_archivo, "w") as archivo:
                    archivo.write("--- COMPROBANTE DE DEPÓSITO ---\n")
                    archivo.write(f"Fecha: {datetime.datetime.now().strftime('%d/%m/%Y %H:%M:%S')}\n")
                    archivo.write(f"Cuenta destino: {cuenta_destino}\n")
                    archivo.write(f"Depositante: {nombre_depositante}\n")
                    archivo.write(f"Monto depositado: ${monto}\n")
                    archivo.write(f"Billetes: {', '.join(map(str, billetes))}\n")
                
                messagebox.showinfo("Éxito", 
                                f"Depósito realizado con éxito\n" +
                                f"Monto: ${monto}\n" +
                                f"Se ha generado su comprobante: {nombre_archivo}")
                ventana.destroy()
                
            except ValueError:
                messagebox.showerror("Error", "Por favor verifique los datos ingresados")
        
        # Botones
        frame_botones = tk.Frame(frame, bg='#f0f0f0')
        frame_botones.pack(pady=20, fill='x')
        
        tk.Button(frame_botones,
                text="Realizar Depósito",
                command=realizar_deposito,
                bg='#1a5f7a',
                fg='white',
                font=('Arial', 12),
                width=20,
                height=2,
                cursor='hand2').pack(pady=5)
                
        tk.Button(frame_botones,
                text="Regresar",
                command=ventana.destroy,
                bg='#666666',
                fg='white',
                font=('Arial', 12),
                width=20,
                cursor='hand2').pack(pady=5)

    def __mostrar_pago_servicio(self):
        ventana = tk.Toplevel(self)
        ventana.title("Pago de Servicios")
        ventana.geometry("300x400")
        ventana.configure(bg='#f0f0f0')
        ventana.resizable(False, False)
        ventana.transient(self)
        ventana.grab_set()
        
        frame = tk.Frame(ventana, bg='#f0f0f0', padx=20, pady=20)
        frame.pack(fill='both', expand=True)
        
        # Servicio
        tk.Label(frame,
                text="Servicio (agua, luz, internet):",
                bg='#f0f0f0',
                font=('Arial', 12)).pack(pady=5)
        entrada_servicio = tk.Entry(frame,
                                  font=('Arial', 14),
                                  justify='center')
        entrada_servicio.pack(pady=5)
        
        # Referencia
        tk.Label(frame,
                text="Número de referencia:",
                bg='#f0f0f0',
                font=('Arial', 12)).pack(pady=5)
        entrada_referencia = tk.Entry(frame,
                                    font=('Arial', 14),
                                    justify='center')
        entrada_referencia.pack(pady=5)
        
        # Monto
        tk.Label(frame,
                text="Monto:",
                bg='#f0f0f0',
                font=('Arial', 12)).pack(pady=5)
        entrada_monto = tk.Entry(frame,
                               font=('Arial', 14),
                               justify='center')
        entrada_monto.pack(pady=5)
        
        def realizar_pago():
            try:
                servicio = entrada_servicio.get()
                referencia = entrada_referencia.get()
                monto = int(entrada_monto.get())
                cuenta = cuentas[self.cuenta_actual]
                
                if referencia not in ["1111", "2222", "3333"]:
                    messagebox.showerror("Error", "Número de referencia incorrecto")
                    return
                    
                if monto > cuenta["saldo"]:
                    messagebox.showerror("Error", "Fondos insuficientes")
                    return
                    
                cuenta["saldo"] -= monto
                cuenta["movimientos"].append(f"Pago de {servicio}: -${monto}")
                self.__generar_comprobante("pago_servicio", f"Pago de {servicio} por ${monto}")
                messagebox.showinfo("Éxito", f"Pago exitoso. Nuevo saldo: ${cuenta['saldo']}")
                ventana.destroy()
                
            except ValueError:
                messagebox.showerror("Error", "Por favor ingrese datos válidos")
                
        tk.Button(frame,
                 text="Pagar",
                 command=realizar_pago,
                 bg='#1a5f7a',
                 fg='white',
                 font=('Arial', 12),
                 width=20,
                 height=2,
                 cursor='hand2').pack(pady=20)
        
    def __mostrar_pago_servicio_sin_cuenta(self):
        ventana = tk.Toplevel(self)
        ventana.title("Pago de Servicios")
        ventana.geometry("400x600")
        ventana.configure(bg='#f0f0f0')
        ventana.resizable(False, False)
        ventana.transient(self)
        ventana.grab_set()
        
        frame = tk.Frame(ventana, bg='#f0f0f0', padx=20, pady=20)
        frame.pack(fill='both', expand=True)
        
        # Tipo de servicio
        tk.Label(frame,
                text="Seleccione el servicio:",
                bg='#f0f0f0',
                font=('Arial', 12)).pack(pady=5)
                
        servicios = {
            "Agua": ["1111"],
            "Luz": ["2222"],
            "Internet": ["3333"],
            "Teléfono": ["4444"],
            "Gas": ["55555"]
        }
        
        servicio_var = tk.StringVar(value="Agua")
        for servicio in servicios:
            tk.Radiobutton(frame,
                        text=servicio,
                        variable=servicio_var,
                        value=servicio,
                        bg='#f0f0f0',
                        font=('Arial', 11)).pack(pady=2)
        
        # Número de referencia
        tk.Label(frame,
                text="Número de referencia:",
                bg='#f0f0f0',
                font=('Arial', 12)).pack(pady=5)
        entrada_referencia = tk.Entry(frame,
                                    font=('Arial', 14),
                                    justify='center')
        entrada_referencia.pack(pady=5)
        
        # Monto a pagar
        tk.Label(frame,
                text="Monto a pagar:",
                bg='#f0f0f0',
                font=('Arial', 12)).pack(pady=5)
        entrada_monto = tk.Entry(frame,
                            font=('Arial', 14),
                            justify='center')
        entrada_monto.pack(pady=5)
        
        # Nombre del pagador
        tk.Label(frame,
                text="Nombre:",
                bg='#f0f0f0',
                font=('Arial', 12)).pack(pady=5)
        entrada_nombre = tk.Entry(frame,
                                font=('Arial', 14),
                                justify='center')
        entrada_nombre.pack(pady=5)
        
        def realizar_pago():
            try:
                servicio = servicio_var.get()
                referencia = entrada_referencia.get()
                nombre = entrada_nombre.get().strip()
                
                if not nombre:
                    messagebox.showerror("Error", "Ingrese el nombre del pagador")
                    return
                    
                if referencia not in servicios[servicio]:
                    messagebox.showerror("Error", 
                                    "Número de referencia inválido para este servicio")
                    return
                
                try:
                    monto = float(entrada_monto.get())
                    if monto <= 0:
                        raise ValueError
                except ValueError:
                    messagebox.showerror("Error", "Ingrese un monto válido")
                    return
                
                # Generar comprobante
                fecha = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
                nombre_archivo = f"comprobante_servicio_{servicio}_{fecha}.txt"
                
                with open(nombre_archivo, "w") as archivo:
                    archivo.write("--- COMPROBANTE DE PAGO DE SERVICIO ---\n")
                    archivo.write(f"Fecha: {datetime.datetime.now().strftime('%d/%m/%Y %H:%M:%S')}\n")
                    archivo.write(f"Servicio: {servicio}\n")
                    archivo.write(f"Referencia: {referencia}\n")
                    archivo.write(f"Pagador: {nombre}\n")
                    archivo.write(f"Monto pagado: ${monto:.2f}\n")
                
                messagebox.showinfo("Éxito", 
                                f"Pago realizado con éxito\n" +
                                f"Servicio: {servicio}\n" +
                                f"Monto: ${monto:.2f}\n" +
                                f"Se ha generado su comprobante: {nombre_archivo}")
                ventana.destroy()
                
            except Exception as e:
                messagebox.showerror("Error", "Por favor verifique los datos ingresados")
        
        # Botones
        frame_botones = tk.Frame(frame, bg='#f0f0f0')
        frame_botones.pack(pady=20, fill='x')
        
        tk.Button(frame_botones,
                text="Realizar Pago",
                command=realizar_pago,
                bg='#1a5f7a',
                fg='white',
                font=('Arial', 12),
                width=20,
                height=2,
                cursor='hand2').pack(pady=5)
                
        tk.Button(frame_botones,
                text="Regresar",
                command=ventana.destroy,
                bg='#666666',
                fg='white',
                font=('Arial', 12),
                width=20,
                cursor='hand2').pack(pady=5)    
        
        
        
    def __mostrar_pago_tarjeta(self):
        ventana = tk.Toplevel(self)
        ventana.title("Pago de Tarjeta de Crédito")
        ventana.geometry("300x400")
        ventana.configure(bg='#f0f0f0')
        ventana.resizable(False, False)
        ventana.transient(self)
        ventana.grab_set()
        
        frame = tk.Frame(ventana, bg='#f0f0f0', padx=20, pady=20)
        frame.pack(fill='both', expand=True)
        
        cuenta = cuentas[self.cuenta_actual]
        tarjeta = cuenta["tarjeta_credito"]
        saldo_actual = tarjeta["saldo"]
        
        # Mostrar información de la tarjeta
        tk.Label(frame,
                text=f"Saldo pendiente: ${saldo_actual}",
                bg='#f0f0f0',
                font=('Arial', 12, 'bold')).pack(pady=10)
        
        # Radio buttons para selección de tipo de pago
        tipo_pago = tk.StringVar(value="parcial")
        
        tk.Radiobutton(frame,
                    text="Pago Parcial",
                    variable=tipo_pago,
                    value="parcial",
                    bg='#f0f0f0',
                    font=('Arial', 11)).pack(pady=5)
                    
        tk.Radiobutton(frame,
                    text="Pago Total",
                    variable=tipo_pago,
                    value="total",
                    bg='#f0f0f0',
                    font=('Arial', 11)).pack(pady=5)
        
        # Entry para monto personalizado
        tk.Label(frame,
                text="Monto a pagar:",
                bg='#f0f0f0',
                font=('Arial', 12)).pack(pady=5)
        entrada_monto = tk.Entry(frame,
                            font=('Arial', 14),
                            justify='center')
        entrada_monto.pack(pady=5)
        
        def realizar_pago():
            try:
                if tipo_pago.get() == "total":
                    monto = saldo_actual
                else:
                    monto = float(entrada_monto.get())
                
                if monto <= 0:
                    messagebox.showerror("Error", "Ingrese un monto válido")
                    return
                    
                if monto > saldo_actual:
                    messagebox.showerror("Error", "El monto excede el saldo de la tarjeta")
                    return
                    
                if monto > cuenta["saldo"]:
                    messagebox.showerror("Error", "Fondos insuficientes en cuenta")
                    return
                
                # Realizar el pago
                cuenta["saldo"] -= monto
                tarjeta["saldo"] -= monto
                cuenta["movimientos"].append(f"Pago a tarjeta: -${monto}")
                
                self.__generar_comprobante("pago_tarjeta", 
                                        f"Pago a tarjeta por ${monto}\nSaldo restante: ${tarjeta['saldo']}")
                messagebox.showinfo("Éxito", 
                                f"Pago realizado con éxito\nNuevo saldo pendiente: ${tarjeta['saldo']}")
                ventana.destroy()
                
            except ValueError:
                messagebox.showerror("Error", "Por favor ingrese un monto válido")
        
        tk.Button(frame,
                text="Realizar Pago",
                command=realizar_pago,
                bg='#1a5f7a',
                fg='white',
                font=('Arial', 12),
                width=20,
                height=2,
                cursor='hand2').pack(pady=20)

    def __consultar_saldo(self):
        cuenta = cuentas[self.cuenta_actual]
        messagebox.showinfo("Saldo", f"Saldo actual: ${cuenta['saldo']}")
       #self.__generar_comprobante("consulta_saldo", f"Saldo actual: ${cuenta['saldo']}")
        
    def __consultar_movimientos(self):
        cuenta = cuentas[self.cuenta_actual]
        movimientos = cuenta["movimientos"]
        if not movimientos:
            messagebox.showinfo("Movimientos", "No hay movimientos recientes")
            return
            
        ultimos = movimientos[-5:]  # Últimos 5 movimientos
        mensaje = "Últimos movimientos:\n" + "\n".join(ultimos)
        messagebox.showinfo("Movimientos", mensaje)
       # self.__generar_comprobante("consulta_movimientos", mensaje)
        
        # Generación de comprobante
    def __generar_comprobante(self, operacion, detalles):
        fecha = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
        nombre_archivo = f"comprobante_{self.cuenta_actual}{operacion}{fecha}.txt"
        
        with open(nombre_archivo, "w") as archivo:
            archivo.write(f"--- COMPROBANTE DE {operacion.upper()} ---\n")
            archivo.write(f"Fecha: {datetime.datetime.now().strftime('%d/%m/%Y')}\n")
            archivo.write(f"Número de cuenta: {self.cuenta_actual}\n")
            archivo.write(f"Detalles: {detalles}\n")
            
    def __salir(self):
        if messagebox.askyesno("Confirmar", "¿Desea cerrar sesión?"):
                self.frame_menu.destroy()
                self.cuenta_actual = None
                self.__create_login_widgets()
            #self.quit()

if __name__ == "__main__":
    app = Cajero()
    app.mainloop()
