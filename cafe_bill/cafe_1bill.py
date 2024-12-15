from tkinter import *
from tkinter import messagebox
import random
# import os
import tempfile
import webbrowser
import urllib.parse
from datetime import datetime

#calculation
def total():
    #coffee's price
    global Americano_price,Espresso_price,Cappuccino_price,Latte_price,Macchiato_price,Black_coffee
    
    Americano_price=int(Americano_entry.get())*150
    Espresso_price=int(Espresso_entry.get())*100
    Cappuccino_price=int(Cappuccino_entry.get())*150
    Latte_price=int(Latte_entry.get())*150
    Macchiato_price=int(Macchiato_entry.get())*140
    Black_coffee=int(Black_coffee_entry.get())*100
    
    total_coffee=Americano_price+Espresso_price+Cappuccino_price+Latte_price+Macchiato_price+Black_coffee
    costofcoffe_entry.delete(0,END)
    costofcoffe_entry.insert(0,total_coffee+.00)
    
    #Non-coffee's price
    global Chocolate_price,Green_Tea_Latte_price,Milk_Tea_price,Matcha_price,Matcha_Latte_price,Vanilla_Latte_price
    
    Chocolate_price=int(Chocolate_entry.get())*180
    Green_Tea_Latte_price=int(Green_Tea_Latte_entry.get())*180
    Milk_Tea_price=int(Milk_Tea_entry.get())*50
    Matcha_price=int(Matcha_entry.get())*180
    Matcha_Latte_price=int(Matcha_Latte_entry.get())*180
    Vanilla_Latte_price=int(Vanilla_Latte_entry.get())*180

    total_non_coffee=Chocolate_price+Green_Tea_Latte_price+Milk_Tea_price+Matcha_price+Matcha_Latte_price+Vanilla_Latte_price
    costofnoncoffe_entry.delete(0,END)
    costofnoncoffe_entry.insert(0,total_non_coffee+.00)   

    #subtotal
    global sub_total_price
    sub_total_price=total_coffee+total_non_coffee
    subtotal_entry.delete(0,END)
    subtotal_entry.insert(0,sub_total_price+.00)
    
    #tax
    global paidtax_total
    paidtax_total=sub_total_price*5/100
    paidtax_entry.delete(0,END)
    paidtax_entry.insert(0,paidtax_total)

    #grandtotal
    global grand_total
    grand_total=sub_total_price+paidtax_total
    totalbutton_entry.delete(0,END)
    totalbutton_entry.insert(0,grand_total+.00)
    
def bill_area():
    name = nameEntry.get().strip()
    phone = phoneEntry.get().strip()
    coffee = costofcoffe_entry.get().strip()
    non_coffee =costofnoncoffe_entry.get().strip()
    sub_total= subtotal_entry.get().strip()
    paid_tax = paidtax_entry.get().strip()
    if not name or not phone:
        messagebox.showerror("Error", "Customer details are required")
    elif not coffee and not non_coffee and not sub_total and not paid_tax:
        messagebox.showerror("Error", "Products details are required")
    else:
        textarea.delete(1.0,END)
        textarea.tag_configure("center", justify='center')
        textarea.tag_configure("large_font", font=("DejaVu Sans Mono",10)) 
        textarea.tag_configure("bold_font", font=("DejaVu Sans Mono",11,"bold")) 
        textarea.insert(END,"WELCOME TO OUR $CAF`E CLICK\n","center")
        textarea.insert(END, f"\nDate & Time: {now}\n","large_font")
        textarea.insert(END,f"Bill number : {billnumber}","large_font")
        textarea.insert(END,f"\nCustomer : {nameEntry.get()}","large_font")
        textarea.insert(END,f"\nPhone number : {phoneEntry.get()}","large_font")
        textarea.insert(END,f"\n==========================================================")
        textarea.insert(END,"\nITEMS\t\t\tQUANTITY\t\t\tPRICE","large_font")
        textarea.insert(END,f"\n==========================================================")
        if Americano_entry.get()!="0":
            textarea.insert(END,f"\t\nAmericano\t\t\t{Americano_entry.get()}\t\t\t{Americano_price}.00","large_font")
        if Espresso_entry.get()!="0":
            textarea.insert(END,f"\t\nEspresso\t\t\t{Espresso_entry.get()}\t\t\t{Espresso_price}.00","large_font")
        if Cappuccino_entry.get()!="0":
            textarea.insert(END,f"\t\nCappuccino\t\t\t{Cappuccino_entry.get()}\t\t\t{Cappuccino_price}.00","large_font")
        if Latte_entry.get()!="0":
            textarea.insert(END,f"\t\nLatte\t\t\t{Latte_entry.get()}\t\t\t{Latte_price}.00","large_font")
        if Macchiato_entry.get()!="0":
            textarea.insert(END,f"\t\nMacchiato\t\t\t{Macchiato_entry.get()}\t\t\t{Macchiato_price}.00","large_font")
        if Black_coffee_entry.get()!="0":
            textarea.insert(END,f"\t\nBlack Coffee\t\t\t{Black_coffee_entry.get()}\t\t\t{Black_coffee}.00","large_font")
        if Chocolate_entry.get()!="0":
            textarea.insert(END,f"\t\nChocolate\t\t\t{Chocolate_entry.get()}\t\t\t{Chocolate_price}.00","large_font")
        if Green_Tea_Latte_entry.get()!="0":
            textarea.insert(END,f"\t\nGreen Tea Latte\t\t\t{Green_Tea_Latte_entry.get()}\t\t\t{Green_Tea_Latte_price}.00","large_font")
        if Milk_Tea_entry.get()!="0":
            textarea.insert(END,f"\t\nMilk Tea\t\t\t{Milk_Tea_entry.get()}\t\t\t{Milk_Tea_price}.00","large_font")
        if Matcha_entry.get()!="0":
            textarea.insert(END,f"\t\nMatcha\t\t\t{Matcha_entry.get()}\t\t\t{Matcha_price}.00","large_font")
        if Matcha_Latte_entry.get()!="0":
            textarea.insert(END,f"\t\nMatcha Latte\t\t\t{Matcha_Latte_entry.get()}\t\t\t{Matcha_Latte_price}.00","large_font")
        if Vanilla_Latte_entry.get()!="0":
            textarea.insert(END,f"\t\nVanilla Latte\t\t\t{Vanilla_Latte_entry.get()}\t\t\t{Vanilla_Latte_price}.00","large_font")
        textarea.insert(END,f"\n----------------------------------------------------------")
        if subtotal_entry.get():
            textarea.insert(END,f"\t\nTOTAL\t\t\t\t\t\t{sub_total_price}.00","large_font")
        if paidtax_entry.get():
            textarea.insert(END,f"\t\nSSGT @ 9%\t\t\t\t\t\t{paidtax_total/2}","large_font")
        if paidtax_entry.get():
            textarea.insert(END,f"\t\nCSGT @ 9%\t\t\t\t\t\t{paidtax_total/2}","large_font")
        if totalbutton_entry.get():
            textarea.insert(END,f"\t\n\nNET AMOUNT\t\t\t\t\t\t{grand_total}","bold_font")
        textarea.insert(END,f"\n**********************************************************\n")
        textarea.insert(END,"'Thank you visit again'\n","center")
        textarea.insert(END,"'Happiness is a warm cup of coffee'\n","center")


# if not os.path.exists("bills"):
#     os.mkdir("bills")
    
def save_bill():
    global billnumber
    result=messagebox.askyesno("Confirm","Do you want to save the bill")
    if result:
        bill_content=textarea.get(1.0,END)
        file=open(f"bills/ {billnumber}.txt","w")
        file.write(bill_content)
        file.close()
        messagebox.showinfo("Success",f"{billnumber} is saved Successfully")
        
def print_bill():
    if textarea.get(1.0,END)=="\n":
        messagebox.showerror("Error","Your bill is empty")
    else:
        file=tempfile.mktemp(".txt")
        open(file,"w").write(textarea.get(1.0,END))
        

def share_on_whatsapp():
    phone_number = phoneEntry.get().strip()
    if not phone_number:
        messagebox.showerror("Error", "Phone number is required")
        return
    # Get the content of the bill
    bill_content = textarea.get(1.0, END).strip()
    if not bill_content:
        messagebox.showerror("Error", "Bill content is empty")
        return
    # Encode the bill content
    encoded_bill_content = urllib.parse.quote(bill_content)
    # Create the WhatsApp URL
    whatsapp_url = f"https://wa.me/{phone_number}?text={encoded_bill_content}"
    # Open the WhatsApp URL
    webbrowser.open(whatsapp_url)

def clear_all():
    Americano_entry.delete(0,END)
    Espresso_entry.delete(0,END)
    Cappuccino_entry.delete(0,END)
    Latte_entry.delete(0,END)
    Macchiato_entry.delete(0,END)
    Black_coffee_entry.delete(0,END)
    
    Chocolate_entry.delete(0,END)
    Green_Tea_Latte_entry.delete(0,END)
    Milk_Tea_entry.delete(0,END)
    Matcha_entry.delete(0,END)
    Matcha_Latte_entry.delete(0,END)
    Vanilla_Latte_entry.delete(0,END)

    Americano_entry.insert(0,0)
    Espresso_entry.insert(0,0)
    Cappuccino_entry.insert(0,0)
    Latte_entry.insert(0,0)
    Macchiato_entry.insert(0,0)
    Black_coffee_entry.insert(0,0)
    
    Chocolate_entry.insert(0,0)
    Green_Tea_Latte_entry.insert(0,0)
    Milk_Tea_entry.insert(0,0)
    Matcha_entry.insert(0,0)
    Matcha_Latte_entry.insert(0,0)
    Vanilla_Latte_entry.insert(0,0)
    
    costofcoffe_entry.delete(0,END)
    costofnoncoffe_entry.delete(0,END)
    subtotal_entry.delete(0,END)
    paidtax_entry.delete(0,END)

    nameEntry.delete(0,END)
    phoneEntry.delete(0,END)
    totalbutton_entry.delete(0,END)
    textarea.delete(1.0,END)

#root
billnumber=random.randint(500,3000)
root=Tk()
root.title("Billing System")
# root.iconbitmap("bill.ico")
now = datetime.now()
# Maximize window size
root.state('zoomed')

#title
head=Label(root,text="$CAF`E CLICK",font=("ARIAL BLACK",25),bg="#6F4E37",fg="white",bd=8,relief=GROOVE)
head.pack(fill=X)

#billing area
items4=Frame(root)
items4.pack(side=RIGHT)
billing=Frame(items4,bd=8,relief=GROOVE)
billing.pack(side=TOP, fill=BOTH, expand=True)
#root
bill=Label(billing,text="BILLING AREA",font=("Segoe UI",15,"bold"),bd=8,relief=GROOVE)
bill.pack(side=TOP, fill=X)

#scrollbar for bill area
scroll=Scrollbar(billing,orient=VERTICAL) #scrollbar
scroll.pack(side=RIGHT,fill=Y)
textarea=Text(billing,height=31,width=58,yscrollcommand=scroll.set)
textarea.pack(side=LEFT, fill=BOTH, expand=True)
scroll.config(command=textarea.yview)

#customer info
customer=LabelFrame(root,text="CUSTOMER DETAILS",font=("Segoe UI",15,"bold"),fg="black",bd=8,relief=SUNKEN,bg="#F1E5D1")
customer.pack(fill=X)

name=Label(customer,text="NAME",font=("Segoe UI",15,"bold"),bg="#F1E5D1")
name.grid(row=1,column=0,padx=10,pady=10)
nameEntry=Entry(customer,font=("ARIAL",15,"bold"),bd=7,width=18)
nameEntry.grid(row=1,column=1,padx=25)

phone=Label(customer,text="PHONE NUMBER",font=("Segoe UI",15,"bold"),bg="#F1E5D1")
phone.grid(row=1,column=2,padx=10,pady=10)
phoneEntry=Entry(customer,font=("ARIAL",15,"bold"),bd=7,width=18)
phoneEntry.grid(row=1,column=3,padx=25)

#items info
items=Frame(root)
items.pack(fill=X)

items1=LabelFrame(items,text=" C O F F E E",font=("Segoe UI",18,"bold"),fg="black",bg="#F1E5D1")
items1.grid(row=0,column=1,padx=10)

#coffee items
Americano=Label(items1,text="Americano",font=("Segoe UI",15,"bold"),bg="#F1E5D1")
Americano.grid(row=1,column=0,padx=30)
Americano_entry=Entry(items1,font=("ARIAL",15,"bold"),width=10,bd=5)
Americano_entry.grid(row=1,column=1,padx=40,pady=5)
Americano_entry.insert(0,0)

Espresso=Label(items1,text="Espresso",font=("Segoe UI",15,"bold"),bg="#F1E5D1")
Espresso.grid(row=2,column=0,padx=30)
Espresso_entry=Entry(items1,font=("ARIAL",15,"bold"),width=10,bd=5)
Espresso_entry.grid(row=2,column=1,padx=40,pady=5)
Espresso_entry.insert(0,0)

Cappuccino=Label(items1,text="Cappuccino",font=("Segoe UI",15,"bold"),bg="#F1E5D1")
Cappuccino.grid(row=3,column=0,padx=30)
Cappuccino_entry=Entry(items1,font=("ARIAL",15,"bold"),width=10,bd=5)
Cappuccino_entry.grid(row=3,column=1,padx=40,pady=5)
Cappuccino_entry.insert(0,0)

Latte=Label(items1,text="Latte",font=("Segoe UI",15,"bold"),bg="#F1E5D1")
Latte.grid(row=4,column=0,padx=30)
Latte_entry=Entry(items1,font=("ARIAL",15,"bold"),width=10,bd=5)
Latte_entry.grid(row=4,column=1,padx=40,pady=5)
Latte_entry.insert(0,0)

Macchiato=Label(items1,text="Macchiato",font=("Segoe UI",15,"bold"),bg="#F1E5D1")
Macchiato.grid(row=5,column=0,padx=30)
Macchiato_entry=Entry(items1,font=("ARIAL",15,"bold"),width=10,bd=5)
Macchiato_entry.grid(row=5,column=1,padx=40,pady=5)
Macchiato_entry.insert(0,0)

Black_coffee=Label(items1,text="Black Coffee",font=("Segoe UI",15,"bold"),bg="#F1E5D1")
Black_coffee.grid(row=6,column=0,padx=30)
Black_coffee_entry=Entry(items1,font=("ARIAL",15,"bold"),width=10,bd=5)
Black_coffee_entry.grid(row=6,column=1,padx=40,pady=10)
Black_coffee_entry.insert(0,0)

#non-coffee items
items2=LabelFrame(items,text="N O N - C O F F E E",font=("Segoe UI",18,"bold"),fg="black",bg="#F1E5D1")
items2.grid(row=0,column=3,padx=2)

Chocolate=Label(items2,text="Chocolate",font=("Segoe UI",15,"bold"),bg="#F1E5D1")
Chocolate.grid(row=7,column=0,padx=30)
Chocolate_entry=Entry(items2,font=("ARIAL",15,"bold"),width=10,bd=5)
Chocolate_entry.grid(row=7,column=1,padx=0,pady=5)
Chocolate_entry.insert(0,0)

Green_Tea_Latte=Label(items2,text="Green Tea Latte",font=("Segoe UI",15,"bold"),bg="#F1E5D1")
Green_Tea_Latte.grid(row=8,column=0,padx=30)
Green_Tea_Latte_entry=Entry(items2,font=("ARIAL",15,"bold"),width=10,bd=5)
Green_Tea_Latte_entry.grid(row=8,column=1,padx=40,pady=5)
Green_Tea_Latte_entry.insert(0,0)

Milk_Tea=Label(items2,text="Milk Tea",font=("Segoe UI",15,"bold"),bg="#F1E5D1")
Milk_Tea.grid(row=9,column=0,padx=30)
Milk_Tea_entry=Entry(items2,font=("ARIAL",15,"bold"),width=10,bd=5)
Milk_Tea_entry.grid(row=9,column=1,padx=40,pady=5)
Milk_Tea_entry.insert(0,0)

Matcha=Label(items2,text="Matcha",font=("Segoe UI",15,"bold"),bg="#F1E5D1")
Matcha.grid(row=10,column=0,padx=30)
Matcha_entry=Entry(items2,font=("ARIAL",15,"bold"),width=10,bd=5)
Matcha_entry.grid(row=10,column=1,padx=40,pady=5)
Matcha_entry.insert(0,0)

Matcha_Latte=Label(items2,text="Matcha Latte",font=("Segoe UI",15,"bold"),bg="#F1E5D1")
Matcha_Latte.grid(row=11,column=0,padx=30)
Matcha_Latte_entry=Entry(items2,font=("ARIAL",15,"bold"),width=10,bd=5)
Matcha_Latte_entry.grid(row=11,column=1,padx=40,pady=5)
Matcha_Latte_entry.insert(0,0)

Vanilla_Latte=Label(items2,text="Vanilla Latte",font=("Segoe UI",15,"bold"),bg="#F1E5D1")
Vanilla_Latte.grid(row=12,column=0,padx=30)
Vanilla_Latte_entry=Entry(items2,font=("ARIAL",15,"bold"),width=10,bd=5)
Vanilla_Latte_entry.grid(row=12,column=1,padx=40,pady=10)
Vanilla_Latte_entry.insert(0,0)

#billing section
billsect=LabelFrame(root,font=("Segoe UI",15,"bold"),fg="black",bg="#F1E5D1")
billsect.pack(fill=X)

costofcoffee=Label(billsect,text="COST OF COFFEE'S",font=("Segoe UI",11,"bold"),bg="#F1E5D1")
costofcoffee.grid(row=0,column=0,padx=5)
costofcoffe_entry=Entry(billsect,font=("ARIAL",17,"bold"),width=12,bd=4)
costofcoffe_entry.grid(row=0,column=1,padx=5,pady=10)

costofnoncoffee=Label(billsect,text="COST OF NON-COFFEE'S",font=("Segoe UI",11,"bold"),bg="#F1E5D1")
costofnoncoffee.grid(row=1,column=0,padx=5)
costofnoncoffe_entry=Entry(billsect,font=("ARIAL",17,"bold"),width=12,bd=4)
costofnoncoffe_entry.grid(row=1,column=1,padx=5,pady=10)

subtotal=Label(billsect,text="SUB TOTAL",font=("Segoe UI",11,"bold"),bg="#F1E5D1")
subtotal.grid(row=0,column=2,padx=5)
subtotal_entry=Entry(billsect,font=("ARIAL",17,"bold"),width=12,bd=4)
subtotal_entry.grid(row=0,column=3,padx=5,pady=10)

paidtax=Label(billsect,text="PAID TAX",font=("Segoe UI",11,"bold"),bg="#F1E5D1")
paidtax.grid(row=1,column=2,padx=5)
paidtax_entry=Entry(billsect,font=("ARIAL",17,"bold"),width=12,bd=4)
paidtax_entry.grid(row=1,column=3,padx=5,pady=10)

#total
billsect2=LabelFrame(root,font=("Segoe UI",15,"bold"),fg="black",bg="#F1E5D1")
billsect2.pack(fill=X)

totalbutton=Button(billsect2,text="TOTAL",font=("Segoe UI",12,"bold"),bd=5,bg="#6F4E37",fg="white",width=17,relief=GROOVE,command=total)
totalbutton.grid(row=0,column=1,padx=5)
grandtotal=Label(billsect2,text="GRAND TOTAL",font=("Segoe UI",15,"bold"),bg="#F1E5D1")
grandtotal.grid(row=0,column=2,padx=5)
totalbutton_entry=Entry(billsect2,font=("ARIAL",20,"bold"),width=22,bd=5)
totalbutton_entry.grid(row=0,column=3,padx=5,pady=15)

#button
buttonframe=LabelFrame(items4,font=("Segoe UI",15,"bold"),fg="black",bg="#F1E5D1",bd=5)
buttonframe.pack(fill=X)

button_bill=Button(buttonframe,text="BILL",font=("Segoe UI",12,"bold"),bd=5,bg="#6F4E37",fg="white",width=8,relief=GROOVE,command=bill_area)
button_bill.grid(row=0, column=1,padx=10,pady=10)

button_print=Button(buttonframe,text="PRINT",font=("Segoe UI",12,"bold"),bd=5,bg="#6F4E37",fg="white",width=8,relief=GROOVE,command=print_bill)
button_print.grid(row=0, column=2,padx=10,pady=10)

button_share=Button(buttonframe,text="SHARE ON WA",font=("Segoe UI",12,"bold"),bd=5,bg="#6F4E37",fg="white",width=12,relief=GROOVE,command=share_on_whatsapp)
button_share.grid(row=0, column=3,padx=10,pady=10)

button_clear=Button(buttonframe,text="CLEAR",font=("Segoe UI",12,"bold"),bd=5,bg="#6F4E37",fg="white",width=8,relief=GROOVE,command=clear_all)
button_clear.grid(row=0, column=4,padx=10,pady=10)

footer = Label(root, text="© 2024 $CAF`E CLICK | Contact us at info@$CAF`E CLICK.com", bg="#F1E5D1", fg="black", font=("Segoe UI", 12,"bold"), pady=10,relief=GROOVE,bd=2)
footer.pack(side=BOTTOM, fill=X)

root.mainloop()