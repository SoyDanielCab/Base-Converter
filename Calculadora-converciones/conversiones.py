from tkinter import Tk,Text,Button,END

class interface:

    #Función que ayuda a crear Las diferetes pantallas y botones de la interfaz
    def __init__(self, screen):

        #Inicia nuestra ventana principal
        self.screen = screen
        self.screen.title("Conversión de Bases")

        #Crea las diferentes pantallas de la calculadora:
        #Pantalla principal
        self.pantalla = Text(
            self.screen,
            borderwidth=0,  
            state="disabled", 
            width=40, 
            height=3, 
            bg="SlateGray1", 
            foreground="gray1", 
            font=("Segoe UI",15)
            )
        
        #Pantalla de base Decimal
        self.pantallaDecimal = Text(
            self.screen,
            borderwidth=0, 
            state="disabled", 
            width=40, 
            height=1, 
            bg="SlateGray2", 
            foreground="gray1", 
            font=("Segoe UI",15)
            )


        #Pantalla de base binario
        self.pantallaBinaria = Text(
            self.screen,
            borderwidth=0, 
            state="disabled", 
            width=40, 
            height=1, 
            bg="SlateGray2", 
            foreground="gray1", 
            font=("Segoe UI",15)
            )

        #Pantalla de base Octal
        self.pantallaOctal = Text(
            self.screen,
            borderwidth=0, 
            state="disabled", 
            width=40, 
            height=1, 
            bg="SlateGray2", 
            foreground="gray1", 
            font=("Segoe UI",15)
            )

        #Pantalla de base Hexadecimal
        self.pantallaHexadecimal = Text(
            self.screen,
            borderwidth=0, 
            state="disabled", 
            width=40,
            height=1, 
            bg="SlateGray2", 
            foreground="gray1", 
            font=("Segoe UI",15)
            )


        #Definimos valores para posicionar a cada pantalla en 
        # el lugar que le corresponde
        self.pantalla.grid(
            row = 0, 
            column = 0, 
            columnspan = 5, 
            padx = 5, 
            pady = 5
            )

        self.pantallaDecimal.grid(
            row = 1, 
            column = 0, 
            columnspan = 4, 
            padx = 5, 
            pady = 5
            )

        self.pantallaBinaria.grid(
            row = 2, 
            column = 0, 
            columnspan = 4, 
            padx = 5, 
            pady = 5
            )


        self.pantallaOctal.grid(
            row = 3, 
            column = 0, 
            columnspan = 4, 
            padx = 5, 
            pady = 5
            )


        self.pantallaHexadecimal.grid(
            row = 4, 
            column = 0, 
            columnspan = 4, 
            padx = 5, 
            pady = 5
            )


        #Declaramos la variable number con la que podremos obtener los datos mostrados en pantalla
        self.number = ""

        #Declaramos los botones para la calculadora
        button1=self.createButton("A")
        button2=self.createButton("B")
        button3=self.createButton("C")
        button4=self.createButton("D")
        button5=self.createButton(7)
        button6=self.createButton(8)
        button7=self.createButton(9)
        button8=self.createButton("E")
        button9=self.createButton(4)
        button10=self.createButton(5)
        button11=self.createButton(6)
        button12=self.createButton("F")
        button13=self.createButton(1)
        button14=self.createButton(2)
        button15=self.createButton(3)
        button16=self.createButton(0)

        #Los Botones que definen la base de conversión no se tienen que mostrar por pantalla 
        button17=self.createButton("Dec",show=False)
        button18=self.createButton("Bin",show=False)
        button19=self.createButton("Oct",show=False)
        button20=self.createButton("Hex",show=False)
        button21=self.createButton(u"\u232B",show=False, width=40)


        #Pocicionar los botones en el grid
        cont = 0

        buttons =   [
            button1, button2, button3, button4, button5, 
            button6, button7, button8, button9, button10, 
            button11, button12, button13, button14, button15, 
            button16, button17, button18, button19, button20,button21
            ]

        for row in range(5,10):
            for column in range(4):
                buttons[cont].grid(row = row, column = column)
                cont+=1

        #Ubicar el último botón al final
        buttons[20].grid(row = 10,column = 0,columnspan = 4)

        return

##############################################################################################################################

    #Definimos los parametros para el diseño de los botones
    def createButton(self, value, show = True, width = 9, height = 1):

        return Button(self.screen,borderwidth = 0, text = value, width = width, height = height,
         background = "SlateGray3", activebackground = "SlateGray4",  padx = 6, pady = 5, font = ("Segoe UI",15),
          command = lambda:self.click(value,show))


    #Agregamos un una función que detecte el evento "Click"
    def click(self, op, show):

        #Si 'show' es True, entonces el valor del boton se muestra en pantalla. Si es False, no.
        if not show:

            #Detectamos el tipo de converición que el usuario preciona

            #Cuando la base es decimal
            if op == "Dec" : 
                

                dec = self.number
                convb = bin(int(dec))
                convo = oct(int(dec))
                convh = hex(int(dec))

                self.number = ""
                self.mostrarDecimal(dec)
                self.mostrarBinario(convb[2:])
                self.mostrarOctal(convo[2:])
                self.mostrarHexadecimal(convh[2:])


            #Cuando la base es Binaria
            elif op == "Bin":
                
                bn = self.number
                num = int(bn,2) 
                convo = oct(num)
                convh = hex(num)

                self.number = ""
                self.mostrarDecimal(num)
                self.mostrarBinario(bn)
                self.mostrarOctal(convo[2:])
                self.mostrarHexadecimal(convh[2:]) 


            #Cuando la base es Octal
            elif op == "Oct":

                ot = self.number
                num = int(ot,8) 
                convb = bin(num)
                convh = hex(num)

                self.number = ""
                self.mostrarDecimal(num)
                self.mostrarBinario(convb[2:])
                self.mostrarOctal(ot)
                self.mostrarHexadecimal(convh[2:])
                

            #Cuando la base es Hexadecimal
            elif op == "Hex":

                hx = self.number
                num = int(hx,16) 
                convb = bin(num)
                convo = oct(num)

                self.number = ""
                self.mostrarDecimal(num)
                self.mostrarBinario(convb[2:])
                self.mostrarOctal(convo[2:])
                self.mostrarHexadecimal(hx)
                    

            #Si preciona limpiar pantalla
            elif op == u"\u232B":

                self.number = ""
                self.limpiarPantalla()

        #Mostrar por pantalla el numero o letra precionado
        else:

            self.number += str(op)
            self.mostrarEnPantalla(op)

        return
    

    #Boton que limpia la pantalla
    def limpiarPantalla(self):

        #pantalla principal
        self.pantalla.configure(state = "normal")
        self.pantalla.delete("1.0", END)
        self.pantalla.configure(state = "disabled")

        #Pantalla decimal
        self.pantallaDecimal.configure(state = "normal")
        self.pantallaDecimal.delete("1.0", END)
        self.pantallaDecimal.configure(state = "disabled")
        self.mostrarDecimal("Dec: ")

        #Pantalla Binaria
        self.pantallaBinaria.configure(state = "normal")
        self.pantallaBinaria.delete("1.0", END)
        self.pantallaBinaria.configure(state = "disabled")
        self.mostrarBinario("Bin: ")

        #Pantalla Ocal
        self.pantallaOctal.configure(state = "normal")
        self.pantallaOctal.delete("1.0", END)
        self.pantallaOctal.configure(state = "disabled")
        self.mostrarOctal("Oct: ")

        #Pantalla Hexadecimal
        self.pantallaHexadecimal.configure(state = "normal")
        self.pantallaHexadecimal.delete("1.0", END)
        self.pantallaHexadecimal.configure(state = "disabled")
        self.mostrarHexadecimal("Hex: ")

        return
    
    #Muestra el resultado de la conversión en las diferentes pantallas
    def mostrarEnPantalla(self, value):

        self.pantalla.configure(state = "normal")
        self.pantalla.insert(END, value)
        self.pantalla.configure(state = "disabled")

        return

    #Pantala Decimal
    def mostrarDecimal(self, value):

        self.pantallaDecimal.configure(state = "normal")
        self.pantallaDecimal.insert(END, value)
        self.pantallaDecimal.configure(state = "disabled")

        return

    #Pantala Binaria
    def mostrarBinario(self, value):

        self.pantallaBinaria.configure(state = "normal")
        self.pantallaBinaria.insert(END, value)
        self.pantallaBinaria.configure(state = "disabled")

        return

    #Pantala Octal
    def mostrarOctal(self, value):

        self.pantallaOctal.configure(state = "normal")
        self.pantallaOctal.insert(END, value)
        self.pantallaOctal.configure(state = "disabled")

        return

    #Pantala Hexadecimal    
    def mostrarHexadecimal(self, value):


        self.pantallaHexadecimal.configure(state = "normal")
        self.pantallaHexadecimal.insert(END, value)
        self.pantallaHexadecimal.configure(state = "disabled")

        return


index = Tk()
index.config(bg="SlateGray1" )
conversion = interface(index)
index.mainloop()