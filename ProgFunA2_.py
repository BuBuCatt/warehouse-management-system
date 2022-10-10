#warehouse management system

"""class Customer"""

class Customer():
    def __init__(self,ID,name):
        self.__ID=ID
        self.__name=name

    def getID(self):  #get customer ID
        return self.__ID 
    def get_name(self): #get customer name
        return self.__name
    def get_discount(self,price): #get customer price
        self.price=price
        return self.price

"""class RetailCustomer"""

class RetailCustomer(Customer):

    customers_list=[]

    def __init__(self,ID,name,discount_rate,price):
        import csv
        super().__init__(ID,name)
        self.discount_rate=0.9
        self.price=price

        customer_file=csv.reader(open("customers.txt.csv", "r"), delimiter=",")
        self.customers_list+=customer_file
        for y in self.customers_list:
            cs=",".join(y)
            print(cs)

    def get_discount(self,price):
        retail_discount=self.price*self.discount_rate
        print("It returns 10% percent discount","--Total Price include discount: ",retail_discount)


    def displayCustomer(self):
        try:
            for row in self.customers_list:
                if row[2]=="R":
                    cs=",".join(row)
                    print(cs)
        except Exception as e:
            print(None)


    def setRate(self):
        import csv
        setrate_r = input("Please Enter the rate you would like to change: ")

        try:
            for row in self.customers_list:
                if row[2]=="R":
                    row[3]=setrate_r
        
            with open ("customers.txt.csv","w",newline="") as update_customer:
                newlist=csv.writer(update_customer)
                for i in self.customers_list:
                    newlist.writerow(i)
        except:
            None

"""class WholesaleCustomer"""

class WholesaleCustomer(Customer):
    wholesale_list=[]

    def __init__(self,ID,name,discount_rate_wholesale_A,discount_rate_wholesale_B,price):
        import csv

        customer_file=csv.reader(open("customers.txt.csv", "r"), delimiter=",")
        self.wholesale_list+=customer_file
        for y in self.wholesale_list:
            cs=",".join(y)
            print(cs)


        super().__init__(ID,name)
        self.discount_rate_wholesale_A=0.9
        self.discount_rate_wholesale_B=0.85
        self.price=price

        

    def get_discount(self,price):
        self.price=price
        if self.price<=1000:
            print(self.price*self.discount_rate_wholesale_A)
        elif self.price>1000:
            print(self.price*self.discount_rate_wholesale_B)

    def displaycustomer_wholesale(self):
        try:
            for row in self.wholesale_list:
                if row[2]=="W":
                    cs=",".join(row)
                    print(cs)
        except Exception as e:
            print(None)




    def setRate_wholesale(self):
        import csv
        setrate_r = float(input("Please Enter the rate you would like to change: "))
        try:
            for row in self.wholesale_list:
                if row[2]=="W" and int(row[4])>1000:
                        row[3]=(setrate_r-0.05)
                elif row[2]=="W" and int(row[4])<=1000:
                    row[3]=setrate_r       
            with open ("customers.txt.csv","w",newline="") as update_customer:
                newlist=csv.writer(update_customer)
                for i in self.wholesale_list:
                    newlist.writerow(i)
        except:
            for row in self.wholesale_list:
                if row[2]=="W" and int(row[4])>1000:
                    row[3]=(setrate_r-0.05)
                elif row[2]=="W" and int(row[4])<=1000:
                    row[3]=setrate_r 
                else:
                    break      
            with open ("customers.txt.csv","w",newline="") as update_customer:
                newlist=csv.writer(update_customer)
                for i in self.wholesale_list:
                    newlist.writerow(i)            

"""Products"""

class Product():

    product_list=[]

    def __init__(self,product_ID,product_name,product_price,product_stock):
        self.ID=product_ID
        self.product_name=product_name
        self.product_price=product_price
        self.product_stock=product_stock
        import csv

        product_file=csv.reader(open("products.txt.csv", "r"), delimiter=",")
        self.product_list+=product_file

        

    def readproducts(self):

        for r in self.product_list:
            product_content=",".join(r)
            print(product_content)

    def change_productPrice(self):
        import csv
        product_id= input("For changing price of product, Please Enter product's ID[P1,P2,P3,P4 or P5]: ")
        newprice = input("Please Enter the price of this product, you would like to change: ")
  
        for row in self.product_list:
            if product_id == row[0]:
                row[2]=newprice

        with open ("products.txt.csv","w",newline="") as update_price:
            newlist=csv.writer(update_price)
            for i in self.product_list:
                newlist.writerow(i)
    
    def change_stocks(self):
        import csv
        product_id= input("For changing price of product, Please Enter product's ID[P1,P2,P3,P4 or P5]: ")
        new_stocks = input("Please Enter the inventory of this product, you would like to change: ")

        for row in self.product_list:
            if product_id==row[0]:
                row[3]=new_stocks
        with open ("products.txt.csv","w",newline="") as update_stock:
            newlist=csv.writer(update_stock)
            for i in self.product_list:
                newlist.writerow(i)


    
"""Orders"""

class Order():
    order_list=[]
    customer_list=[]
    product_list=[]

    def __init__(self,customer_name,product_id,product_price,quantity):
        self.customer_name=customer_name
        self.product_id=product_id
        self.product_price=product_price
        self.quanity=quantity



        import csv

        print("----------------------------------------------------------------------------")
        print("{} {} {} {}".format("id","name","price_per_unit","in_stock_quantity"))
        print("----------------------------------------------------------------------------")       

        customer_file=csv.reader(open("customers.txt.csv", "r"), delimiter=",")
        self.customer_list=customer_file
        for y in self.customer_list:
            cs=",".join(y)
            print(cs)

        print("----------------------------------------------------------------------------")
        print("----------------------------------------------------------------------------")


        print("{} {} {} {} {}".format("id","name","retail_or_wholesale","discount_rate","total_value"))
        print("----------------------------------------------------------------------------")
        product_file=csv.reader(open("products.txt.csv", "r"), delimiter=",")
        self.product_list=product_file
        for x in self.product_list:
            prod=",".join(x)
            print(prod)
        print("----------------------------------------------------------------------------")
        print("----------------------------------------------------------------------------")


    def ordering_list(self):
        customer_name=input("Please Enter Customer Name: ")
        product_name=input("Please Enter the product name, you would like to order: ")
        quantity_of_product=input("Please Enter the quantity, you would like to order: ")

        for row in self.customer_list:
            if row[1]==customer_name:
                discount_rate=float(row[3])
            else:
                pass

        for x in self.product_list:
            if x[1]==product_name:
                total_price_order=(int(x[2])*int(quantity_of_product)*float(discount_rate))
                print('{:^8}--'.format(customer_name),"purchased",'{:^5}'.format(quantity_of_product),"x",'{:^5}'.format(product_name)
                ,"\n Unit Price: ",'{:^10}'.format(x[2]),"\n Total Price: ",'{:^10}'.format(total_price_order))
            else:
                pass


        for y in self.product_list:
            if y[1] in product_name:
                y[3]=int(y[3])-int(quantity_of_product)
                print(product_name,"still have",y[3],"in stocks")
                import csv       
                with open ("products.txt.csv","w",newline="") as product_file:
                    newlist=csv.writer(product_file)
                    for i in self.product_list:
                        newlist.writerow(i)
            

        



"""class records"""

class Record():
    def __init__(self,list_of_existing_customers,list_of_existing_products):
        self.list_of_existing_customers="customers.txt.csv"
        self.list_of_existing_products="products.txt.csv"

    def readCustomers(self):
        with open(self.list_of_existing_customers)as cs:
            content=cs.readlines()
        for line in content:
            print(line)
    def listCustomers(self):
        print("------------------------------List of Customers-------------------------------")
        print("------------------------------------------------------------------------------")
        return self.readCustomers()
    def findcustomer(self):
        import csv
        customer_id_name = input("For searching customers, Please Enter customer's ID or name : ")
        csv_file=csv.reader(open("customers.txt.csv", "r"), delimiter=",")
        try:
            for row in csv_file:
                if customer_id_name in row[0:2]:
                    customers_list=",".join(row)
                    return customers_list

        except Exception as e:
            print(None)

    def readProducts(self):
        with open(self.list_of_existing_products)as pd:
            content=pd.readlines()
        for line in content:
            print(line)     
    def listProducts(self):
        print("--------------------------------List of Poducts-------------------------------")

        print("--------------------------------------------------------------------------------")
        return self.readProducts()    
    
    def findProduct(self):
        import csv
        products_id_name = input("For searching item, Please Enter products's ID or name: ")
        csv_file=csv.reader(open("products.txt.csv", "r"), delimiter=",")
        try:
            for row in csv_file:
                if products_id_name in row[0:2]:
                    products_list=",".join(row)
                    return products_list
        except Exception as e:
            return None
        


"""Main Menu"""

# #######main menu
# customer_list=[]
# product_list=[]
def menu():  

    print("1. Records") # display 
    print("2. Making Order")# this dic also stored the new one we entered
    print("3. Quit!")# input inventory of products,price and new products
    print("========================================================")

    try:
        import csv
        customer_list=[]
        product_list=[]
        print("----------------------------------------------------------------------------")
        print("{} {} {} {} {}".format("id","name","retail_or_wholesale","discount_rate","total_value"))
        print("----------------------------------------------------------------------------")       

        customer_file=csv.reader(open("customers.txt.csv", "r"), delimiter=",")
        customer_list+=customer_file
        for y in customer_list:
            cs=",".join(y)
            print(cs)

        print("----------------------------------------------------------------------------")
        print("----------------------------------------------------------------------------")

        print("{} {} {} {}".format("id","name","price_per_unit","in_stock_quantity"))
        print("----------------------------------------------------------------------------")
        product_file=csv.reader(open("products.txt.csv", "r"), delimiter=",")
        product_list+=product_file
        for x in product_list:
            product=",".join(x)
            print(product)
        print("----------------------------------------------------------------------------")
        print("----------------------------------------------------------------------------")
    except:
        ("Error")
        


    menu_option=int(input("Please Enter the shopmenu option 1-5: "))
    record=Record("customers.txt.csv","products.txt.csv")
    order=Order("Tom","book",20,30)

    while True:

            if menu_option==1:
                print(f"\n----------Welcome To Warehouse Manegemant System---------\n")
                data=input("Please Enter the funtion---[C]list_customers---[P]list_products---[FC]find_cutomers---[FP]find_products: ")
                if data =="C":
                    record.listCustomers()
                    menu()
                elif data =="P":
                    record.listProducts()
                    menu()
                elif data=="FC":
                    print(record.findcustomer())
                    menu()
                elif data=="FP":
                    print(record.findProduct())
                    menu()
                else:
                    print("Try again!")
                    menu()
            
            elif menu_option==2:
                print(f"\n----------Welcome To Warehouse Manegemant System---------\n")
                data=input("Please Enter the funtion---[O]Making an Order: ")
                if data=="O":
                    order.ordering_list()
                    menu()
                # else:
                #     print("try again!")
                #     menu()
            elif menu_option==3:
                print("bye bye")
                break 

menu()