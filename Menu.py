from tkinter import *
from tkinter import font  as tkfont # python 3
import tkinter as tk



class Aplicativo(tk.Tk):

    def __init__(self, *args, **kwargs):
        
        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self)


        container.pack(side="top", fill="both", expand = True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (MENU,VENDAS,EXTRATO):

            frame = F(container, self)

            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(MENU)

    def show_frame(self, cont):

        frame = self.frames[cont]
        frame.tkraise()
        frame["bg"] = "BLUE"

class MENU(tk.Frame):

	def __init__(self, parent, controller):
		tk.Frame.__init__(self,parent)
		label = tk.Label(self, text="MENU")
		label.pack(pady=10,padx=10)

		button = tk.Button(self, text="VENDAS", command=lambda: controller.show_frame(VENDAS))
		button.place(x = 50 , y = 150)

		button2 = tk.Button(self, text="EXTRATO",command=lambda: controller.show_frame(EXTRATO))
		button2.place(x = 250 , y = 150)

		lb1 = tk.Label(self,text = "TOTAL")
		label.pack(pady = 20 , padx = 20)


class VENDAS(tk.Frame):

    def __init__(self, parent, controller):
        self.__petisco = 0
        self.__cerveja = 0 
        self.__refri = 0
        self.__total = 0

        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="VENDAS")
        label.pack(pady=10,padx=10)
        
        def somapetisco():
       	    self.__petisco += 7.00
        def somacerva():
            self.__cerveja += 5.00
        def somarefri():
            self.__refri += 6.00
        def totalcompra():
        	self.__total = self.__petisco + self.__cerveja + self.__refri ## quando voltar a tela fechar a compra 
   
       	
        
        button1 = tk.Button(self, text="VOLTAR",command=lambda: controller.show_frame(MENU))
        button1.pack()
		   
        button2 = tk.Button(self, text="Cerveja",command = lambda:somacerva()) ## Seleciona a quantidade de cervejas 
        button2.place(x = "250" , y = "150")

        precocerva = tk.Label(self , text = "5.00")
        precocerva.place(x = 330 , y = 150)
        
        button3 = tk.Button(self , text ="Petiscos",command = lambda:somapetisco()) ## Seleciona quantidade de  petiscos
        button3.place(x= "400" , y = "150")

        precopest = tk.Label(self , text = "7.00")
        precopest.place(x = 500 , y = 150) 

        button4 = tk.Button(self,text = "Refrigerantes",command = lambda:somarefri()) ## Seleciona quantidade de refrigerantes
        button4.place(x= "100" , y = "150")

        precorefri = tk.Label(self, text = "6.00")
        precorefri.place(x = 200 , y = 150)

        label = tk.Label(self, text="TOTAL")
        label.place(x=100,y=250)

        label = tk.Label(self,text ="18.00")
        label.place(x = 200 , y = 250)


        pag = tk.Label(self,text = "Pagamento")
        pag.place(x =100,y =350)

        op = tk.Label(self , text = "OPÇOES DE PAGAMENTO:")
        op.place(x = 100 , y = 450)

        cirpt = tk.Label(self,text="BTICOIN")
        cirpt.place(x = 100 ,y = 500)

        cirpt1 = tk.Label(self, text = "DASH")
        cirpt1.place(x = 200 , y=500)

        cirpt2 = tk.Label(self,text = "LITECOIN")
        cirpt2.place(x = 300 , y = 500)


class EXTRATO(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        label = tk.Label(self, text="EXTRATO")
        label.pack(pady=10,padx=10)

        button1 = tk.Button(self, text="VOLTAR",
                            command=lambda: controller.show_frame(MENU))
       	button1.pack()
        
        dia = tk.Label(self,text="22/09/2019")
       	dia.place(x = 100 , y = 150)       
        
        transaçao1 = tk.Label(self,text ="HORARIO: 18.00    |   PRODUTO(S): 1 UNIDADE(S) DE CERVEJA(S) 1 UNIDADE DE PESTISCO(S) 2 UNIDADE DE REFIGREANTE  |    VALOR : 18.00 REAIS | DASH : 0.04")
        transaçao1.place(x = 100 , y = 200)

        transaçao = tk.Label(self,text ="HORARIO: 19.00    |   PRODUTO(S): 3 UNIDADE DE PESTISCO(S)  |    VALOR : 21.00 REAIS | LITECOIN: 0.015")
        transaçao.place(x = 100 , y = 250)

        transaçao2 = tk.Label(self,text ="HORARIO: 20.00    |   PRODUTO(S): 4 UNIDADE DE PESTISCO(S)  1 UNIDADE(S) DE CERVEJA(S) | VALOR : 33.00 REAIS | BTC: 0.0008")
        transaçao2.place(x = 100 , y = 300)


        dia = tk.Label(self,text="21/09/2019")
       	dia.place(x = 100 , y = 350)       
        
        transaçao1 = tk.Label(self,text ="HORARIO: 20.00    |   PRODUTO(S): 1 UNIDADE(S) DE CERVEJA(S) 1 UNIDADE DE PESTISCO(S) 2 UNIDADE DE REFIGREANTE  |    VALOR : 18.00 REAIS | DASH : 0.04")
        transaçao1.place(x = 100 , y = 400)

        transaçao = tk.Label(self,text ="HORARIO: 21.00    |   PRODUTO(S): 3 UNIDADE DE PESTISCO(S)  |    VALOR : 21.00 REAIS | LITECOIN: 0.015")
        transaçao.place(x = 100 , y = 450)

        transaçao2 = tk.Label(self,text ="HORARIO: 22.00    |   PRODUTO(S): 4 UNIDADE DE PESTISCO(S)  1 UNIDADE(S) DE CERVEJA(S) | VALOR : 33.00 REAIS | BTC: 0.0008")
        transaçao2.place(x = 100 , y = 500)




app = Aplicativo()
app.mainloop()