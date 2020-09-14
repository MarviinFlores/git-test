from  tkinter  import ttk
from  tkinter  import *
import sqlite3


class Product:

    db_name ='database.db'
    def __init__(self, window ):
      self.wind = window
      self.wind.title('Products App') 
        #CREATE  CONTAINER FRAME
      frame = LabelFrame(self.wind, text = 'Register a New Prod') 
      frame.grid(row = 0, column= 0, columnspan = 3, pady = 20) 
       #NAME INPUT
      Label(frame, text ='Name: ').grid(row = 1, column = 0)
      self.name = Entry(frame)
      self.name.focus()
      self.name.grid(row = 1, column = 1)
      #PRICE INPUT
      Label(frame, text = 'Price: ').grid(row = 2, column = 0)
      self.price = Entry(frame)
      self.price.grid(row = 2, column= 1)
      #BUTTON ADD PRODUCT
      ttk.Button(frame, text= 'SaveProd',command = self.add_product).grid(row = 3,columnspan = 2, sticky = W+E)
      # TABLE
      self.tree = ttk.Treeview(height = 10, columns = 2)
      self.tree.grid(row= 4, column= 0, columnspan =2)
      self.tree.heading('#0',text ='Name',anchor = CENTER)
      self.tree.heading('#1',text ='Price',anchor = CENTER)

      self.get_products()

    def run_query(self,query,parameters =()):
      with sqlite3.connect(self.db_name) as conn:
        cursor = conn.cursor()
        result = cursor.execute(query,parameters)
        conn.commit() # ejecuta las consultas SQL
      return result  
    def get_products(self):  #  funcion  para traer los datos de la DBprod
      #limpiando la tabla
      records = self.tree.get_children() 
      for element in records:
        self.tree.delete(element)
        #consultando datos
      query = 'SELECT * FROM product ORDER BY name ASC'
      db_rows = self.run_query(query)
      
      for row in db_rows:
        #print(row)
        self.tree.insert('', 0, text = row[1], values = row[2])
    def validation(self):
      return len(self.name.get()) != 0 and len(self.price.get()) != 0 # valido datos y obtengo solo valores del Entry
    # agregando funcion de Input New Prod.
    def add_product(self):
      if self.validation():
        query = 'INSERT INTO product VALUES(NULL,?,?)'
        parameters = (self.name.get(), self.price.get())
        self.run_query(query,parameters)
        print('Data Saved')

       # impresion de valores ingresados en la Terminal sin guardarlos en la DB
       # print(self.name.get())
        #print(self.price.get())
      else:
        print('Name and Price is Requered') 
      self.get_products()   


      #print(db_rows)
        


if __name__ == '__main__':
 window = Tk()       
 application = Product(window)
 window.mainloop()







