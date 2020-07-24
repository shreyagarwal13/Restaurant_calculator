from tkinter import *
from csv import DictWriter
import os
import random
import time

rest = Tk()
rest.geometry("1600x800+0+0")
rest.title("Restaurant Bill Calculator ")
rest.configure(background = "gray26")

text_input= StringVar()
operator=""

tops= Frame(rest, width=1600, height=50, relief="raise", bd=10)
tops.pack(side=TOP)

f1= Frame(rest, width=800, height=700, bg="gray26", relief="raise",bd=5)
f1.pack(side=LEFT)

f2= Frame(rest, width=800, height=700, bg="gray26", relief="raise", bd=5)
f2.pack(side=RIGHT)

#=================TIME=========================================================================================================================
localtime = time.asctime(time.localtime(time.time()))

#=================TOP==============================================================================================================
heading= Label(tops,font=("lucida console",40,'bold'),text="Restaurant Bill Calculator",
               fg="dark turquoise", bd=10, anchor='w')
heading.grid(row=0,column=0)
heading= Label(tops,font=("lucida console",15,'bold'), text=localtime,
               fg="dark turquoise", bd=10, anchor='w')
heading.grid(row=1,column=0)

#==================CALCULATOR=============================================================================================================
def btnclick(numbers):
    global operator
    operator = operator+ str(numbers)
    text_input.set(operator) 

def btnclearf():
    global operator
    operator=""
    text_input.set(operator)

def btnequalf():
    global operator
    ans=str(eval(operator)) #will directly calculate the result from the numbers and operators in string
    text_input.set(ans)
    operator=""

def Ref():
    x= random.randint(1200,5000)
    randomref = str(x)
    rand.set(randomref)

    cof = 80 * float(fries.get())
    cod = 150 * float(softdrink.get())
    covb = 100 * float(vburger.get())
    cocb =  120 * float(cburger.get())
    convb = 140 * float(nvburger.get())
    cocc = 180 * float(ccoffee.get())

    total = cof+cod+covb+cocb+convb+cocc
    taxx = "₹" , str("%.2f" % ((total*12)/100))
    servicetaxx ="₹" , str("%.2f" % ((total*5)/100))
    tax.set(taxx)
    servicetax.set(servicetaxx)
    costt="₹" , str("%.2f" % (total + (total*5)/100+ (total*12)/100))
    cost.set(costt)

    friesdata = fries.get()
    softdrinkdata = softdrink.get()
    vburgerdata = vburger.get()
    cburgerdata = cburger.get()
    nvburgerdata = nvburger.get()
    ccoffeedata = ccoffee.get()
    taxdata = str("%.2f" % ((total*12)/100))
    servicetaxdata = str("%.2f" % ((total*5)/100))
    costdata = str("%.2f" % (total + (total*5)/100+ (total*12)/100))

    with open("restaurant_orders.csv","a") as f:

        dw = DictWriter(f,fieldnames=["Reference Number","Number of Fries","Number of Soft Drinks","Number of Veg Burgers",
                        "Number of Cheese Burgers","Number of Non Veg Burgers",
                        "Number of Iced Lattes","Service Tax","Tax","Total Bill"])

        if os.stat("restaurant_orders.csv").st_size==0 :
            dw.writeheader()

        dw.writerow({"Reference Number":randomref,"Number of Fries":friesdata,"Number of Soft Drinks":softdrinkdata,
                     "Number of Veg Burgers":vburgerdata,"Number of Cheese Burgers":cburgerdata,
                     "Number of Non Veg Burgers":nvburgerdata,"Number of Iced Lattes":ccoffeedata,
                     "Service Tax":servicetaxdata,"Tax":taxdata,"Total Bill": costdata })







    

def qexit():
    rest.destroy()

def reset():
    rand.set("")
    fries.set("")
    vburger.set("")
    cburger.set("")
    nvburger.set("")
    cost.set("")
    tax.set("")
    servicetax.set("")
    ccoffee.set("")
    softdrink.set("")
    

result = Entry(f2,font=("lucida console",25,'bold'),fg="turquoise", textvariable=text_input,
               bd=15, insertwidth=4,bg="gray26", justify='right')
result.grid(columnspan=4)

#789+-------------------------------------------------------------------------------------------
btn7 = Button(f2,padx=16,pady=16,bd=8,bg="gray26",fg="turquoise",text="7",
              font=("lucida console",20),command=lambda:btnclick(7)).grid(row=2,column=0)

btn8 = Button(f2,padx=16,pady=16,bd=8,bg="gray26",fg="turquoise",text="8",
              font=("lucida console",20),command=lambda:btnclick(8)).grid(row=2,column=1)

btn9 = Button(f2,padx=16,pady=16,bd=8,bg="gray26",fg="turquoise",text="9",
              font=("lucida console",20),command=lambda:btnclick(9)).grid(row=2,column=2)

add = Button(f2,padx=16,pady=16,bd=8,bg="gray26",fg="turquoise",text="+",
              font=("lucida console",20),command=lambda:btnclick("+")).grid(row=2,column=3)


#456--------------------------------------------------------------------------------------------
btn4 = Button(f2,padx=16,pady=16,bd=8,bg="gray26",fg="turquoise",text="4",
              font=("lucida console",20),command=lambda:btnclick(4)).grid(row=3,column=0)

btn5 = Button(f2,padx=16,pady=16,bd=8,bg="gray26",fg="turquoise",text="5",
              font=("lucida console",20),command=lambda:btnclick(5)).grid(row=3,column=1)

btn6 = Button(f2,padx=16,pady=16,bd=8,bg="gray26",fg="turquoise",text="6",
              font=("lucida console",20),command=lambda:btnclick(6)).grid(row=3,column=2)

subtract = Button(f2,padx=16,pady=16,bd=8,bg="gray26",fg="turquoise",text="-",
              font=("lucida console",20),command=lambda:btnclick("-")).grid(row=3,column=3)

#123*-------------------------------------------------------------------------------------------
btn1 = Button(f2,padx=16,pady=16,bd=8,bg="gray26",fg="turquoise",text="1",
              font=("lucida console",20),command=lambda:btnclick(1)).grid(row=4,column=0)

btn2 = Button(f2,padx=16,pady=16,bd=8,bg="gray26",fg="turquoise",text="2",
              font=("lucida console",20),command=lambda:btnclick(2)).grid(row=4,column=1)

btn3 = Button(f2,padx=16,pady=16,bd=8,bg="gray26",fg="turquoise",text="3",
              font=("lucida console",20),command=lambda:btnclick(3)).grid(row=4,column=2)

multiply = Button(f2,padx=16,pady=16,bd=8,bg="gray26",fg="turquoise",text="*",
              font=("lucida console",20),command=lambda:btnclick("*")).grid(row=4,column=3)

#0c=/-------------------------------------------------------------------------------------------
btn0 = Button(f2,padx=16,pady=16,bd=8,bg="gray26",fg="turquoise",text="0",
              font=("lucida console",20),command=lambda:btnclick(0)).grid(row=5,column=0)

btnclear = Button(f2,padx=16,pady=16,bd=8,bg="gray26",fg="turquoise",text="C",
              font=("lucida console",20),command=btnclearf).grid(row=5,column=1)

btnequal = Button(f2,padx=16,pady=16,bd=8,bg="gray26",fg="turquoise",text="=",
              font=("lucida console",20),command=btnequalf).grid(row=5,column=2)

division = Button(f2,padx=16,pady=16,bd=8,bg="gray26",fg="turquoise",text="/",
              font=("lucida console",20),command=lambda:btnclick("/")).grid(row=5,column=3)

#ENDofCALCULATOR---------------------------------------------------------------------------------

#===MENU===========================================================================================================================

rand = StringVar()
fries = StringVar()
vburger = StringVar()
cburger = StringVar()
nvburger = StringVar()
cost = StringVar()
tax = StringVar()
servicetax = StringVar()
ccoffee = StringVar()
softdrink = StringVar()


lblreference = Label(f1,bg="gray26",fg="turquoise",font=("lucida console",16),
                     text="Reference",bd=16,anchor='w').grid(row=0,column=0)

textreference = Entry(f1,bg="gray20",fg="turquoise",font=("lucida console",16),
                      textvariable=rand, bd=10, insertwidth=4,
                      justify='right').grid(row=0,column=1)

lblfries = Label(f1,bg="gray26",fg="turquoise",font=("lucida console",16),
                 text="Fries",bd=16,anchor='w').grid(row=1,column=0)

textfries = Entry(f1,bg="gray20",fg="turquoise",font=("lucida console",16),
                  textvariable=fries, bd=10, insertwidth=4,
                  justify='right').grid(row=1,column=1)

lblvburger = Label(f1,bg="gray26",fg="turquoise",font=("lucida console",16),
                     text="Aloo Patty Burger",bd=16,anchor='w').grid(row=2,column=0)

textvburger = Entry(f1,bg="gray20",fg="turquoise",font=("lucida console",16),
                      textvariable=vburger, bd=10, insertwidth=4,
                    justify='right').grid(row=2,column=1)

lblcburger = Label(f1,bg="gray26",fg="turquoise",font=("lucida console",16),
                 text="Cheese Burger",bd=16,anchor='w').grid(row=3,column=0)

textcburger = Entry(f1,bg="gray20",fg="turquoise",font=("lucida console",16),
                  textvariable=cburger, bd=10, insertwidth=4,
                  justify='right').grid(row=3,column=1)

lblnvburger = Label(f1,bg="gray26",fg="turquoise",font=("lucida console",16),
                     text="Chicken Burger",bd=16,anchor='w').grid(row=4,column=0)

textnvburger = Entry(f1,bg="gray20",fg="turquoise",font=("lucida console",16),
                     textvariable=nvburger, bd=10, insertwidth=4,
                     justify='right').grid(row=4,column=1)

lblccoffee = Label(f1,bg="gray26",fg="turquoise",font=("lucida console",16),
                 text="Iced Latte",bd=16,anchor='w').grid(row=0,column=2)

textccoffee = Entry(f1,bg="gray20",fg="turquoise",font=("lucida console",16),
                  textvariable=ccoffee, bd=10, insertwidth=4,
                  justify='right').grid(row=0,column=3)

lblsoftdrink = Label(f1,bg="gray26",fg="turquoise",font=("lucida console",16),
                     text="Soft Drink",bd=16,anchor='w').grid(row=1,column=2)

textsoftdrink = Entry(f1,bg="gray20",fg="turquoise",font=("lucida console",16),
                      textvariable=softdrink, bd=10, insertwidth=4,
                      justify='right').grid(row=1,column=3)

lbltax = Label(f1,bg="gray26",fg="turquoise",font=("lucida console",16),
                 text="Tax",bd=16,anchor='w').grid(row=2,column=2)

texttax = Entry(f1,bg="gray20",fg="turquoise",font=("lucida console",16),
                  textvariable=tax, bd=10, insertwidth=4,
                  justify='right').grid(row=2,column=3)

lblservicetax = Label(f1,bg="gray26",fg="turquoise",font=("lucida console",16),
                     text="Service Tax",bd=16,anchor='w').grid(row=3,column=2)

textservicetax = Entry(f1,bg="gray20",fg="turquoise",font=("lucida console",16),
                      textvariable=servicetax, bd=10, insertwidth=4,
                       justify='right').grid(row=3,column=3)

lblcost = Label(f1,bg="gray26",fg="turquoise",font=("lucida console",16),
                 text="Total Cost",bd=16,anchor='w').grid(row=4,column=2)

textcost = Entry(f1,bg="gray20",fg="turquoise",font=("lucida console",16),
                  textvariable=cost, bd=10, insertwidth=4,
                  justify='right').grid(row=4,column=3)

#===Button============================================================================================================

lbltemp= Label(f1,bg="gray26",font=("lucida console",10)).grid(row=5,column=0)

btntotal = Button(f1, padx=16, pady=8,text="Total",bd=16,bg="gray49",fg="turquoise",
                  font=("lucida console",20), width=10, command=Ref).grid(row=6,column=1)

btnreset = Button(f1, padx=16, pady=8,text="Reset",bd=16,bg="gray49",fg="turquoise",
                  font=("lucida console",20), width=10, command=reset).grid(row=6,column=2)

btnexit = Button(f1, padx=16, pady=8,text="Exit",bd=16,bg="gray49",fg="turquoise",
                  font=("lucida console",20), width=10, command=qexit).grid(row=6,column=3)




rest.mainloop()
