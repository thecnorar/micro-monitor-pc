import customtkinter as ctk
import psutil

# Estilo Oscuro Minimalista
ctk.set_appearance_mode("dark")

class MicroMonitor(ctk.CTk):
    def __init__(self):
        super().__init__()

        # Ventana compacta estilo Widget (Ancho x Alto)
        self.title("PERF")
        self.geometry("260x220")
        self.resizable(False, False)
        self.configure(fg_color="#0d0e15") # Fondo azul noche ultra oscuro
        
        # Truco pro: Hace que la ventana se quede SIEMPRE arriba de tus juegos o apps
        self.attributes("-topmost", True)

        # FUENTE ESTILO COMPACTO
        fuente_titulo = ("Arial", 12, "bold")
        fuente_datos = ("Arial", 11, "bold")

        # --- SECCIÓN CPU ---
        self.lbl_cpu = ctk.CTkLabel(self, text="CPU: 0%", font=fuente_datos, text_color="#00ffcc") # Verde Neón
        self.lbl_cpu.pack(anchor="w", padx=20, pady=(15, 2))
        
        self.bar_cpu = ctk.CTkProgressBar(self, width=220, height=6, progress_color="#00ffcc", fg_color="#1a1c29")
        self.bar_cpu.set(0)
        self.bar_cpu.pack(padx=20, pady=(0, 12))

        # --- SECCIÓN RAM ---
        self.lbl_ram = ctk.CTkLabel(self, text="RAM: 0%", font=fuente_datos, text_color="#ff007f") # Rosa Neón
        self.lbl_ram.pack(anchor="w", padx=20, pady=(0, 2))
        
        self.bar_ram = ctk.CTkProgressBar(self, width=220, height=6, progress_color="#ff007f", fg_color="#1a1c29")
        self.bar_ram.set(0)
        self.bar_ram.pack(padx=20, pady=(0, 12))

        # --- SECCIÓN DISCO D ---
        self.lbl_disco = ctk.CTkLabel(self, text="DISCO D: 0%", font=fuente_datos, text_color="#39ff14") # Verde Eléctrico
        self.lbl_disco.pack(anchor="w", padx=20, pady=(0, 2))
        
        self.bar_disco = ctk.CTkProgressBar(self, width=220, height=6, progress_color="#39ff14", fg_color="#1a1c29")
        self.bar_disco.set(0)
        self.bar_disco.pack(padx=20, pady=(0, 15))

        # Bucle de actualización rápida (Cada 500ms = Medio segundo)
        self.actualizar()

    def actualizar(self):
        # CPU
        uso_cpu = psutil.cpu_percent()
        self.lbl_cpu.configure(text=f"CPU: {uso_cpu}%")
        self.bar_cpu.set(uso_cpu / 100)

        # RAM
        ram = psutil.virtual_memory()
        self.lbl_ram.configure(text=f"RAM: {ram.percent}% ({round(ram.used/(1024**3), 1)}GB)")
        self.bar_ram.set(ram.percent / 100)

        # DISCO D
        try:
            disco = psutil.disk_usage('D:\\')
            self.lbl_disco.configure(text=f"DISCO D: {disco.percent}%")
            self.bar_disco.set(disco.percent / 100)
        except:
            self.lbl_disco.configure(text="DISCO D: ---")
            self.bar_disco.set(0)

        # Se actualiza el doble de rápido que antes para que sea más responsivo
        self.after(500, self.actualizar)

if __name__ == "__main__":
    app = MicroMonitor()
    app.mainloop()