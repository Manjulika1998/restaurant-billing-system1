from tkinter import *
from tkinter import filedialog,messagebox
import random
import time
import requests

root = Tk()

root.geometry('1270x690+0+0')
root.resizable(0,0)

root.title('Restaurant management sytem')
root.config(bg='firebrick4')
topFreame= Frame(root, bd=10,relief=RIDGE)
topFreame.pack(side=TOP)

lableTtile= Label(topFreame, text='Restaurant management system', font=('arial',30,'bold'))
lableTtile.grid(row=0, column=0)

#frame
menuframe = Frame(root,bd=10, relief=RIDGE,bg='firebrick4')
menuframe.pack(side=LEFT)

costframe= Frame(menuframe,bd=4,relief=RIDGE,bg='firebrick4')
costframe.pack(side=BOTTOM,pady=10)

foodframe=LabelFrame(menuframe,text='food',font=('arial',19,'bold'),bd=10,relief=RIDGE,fg='red')
foodframe.pack(side= LEFT)

drinkframe=LabelFrame(menuframe,text='drinks',font=('arial',19,'bold'),bd=10,relief=RIDGE)
drinkframe.pack(side= LEFT)

cakeframe=LabelFrame(menuframe,text='cakes',font=('arial',19,'bold'),bd=10,relief=RIDGE)
cakeframe.pack(side= LEFT)

rightframe = Frame(root,bd=15,relief=RIDGE)
rightframe.pack(side = RIGHT)

calculatorframe= Frame(rightframe,bd=1,relief=RIDGE)
calculatorframe.pack()

receiptframe= Frame(rightframe,bd=4,relief=RIDGE)
receiptframe.pack()

buttonframe= Frame(rightframe,bd=3,relief=RIDGE)
buttonframe.pack()
#functions
#SAVE FUNCTION
def save():
    url=filedialog.asksaveasfile(mode='w',defaultextension='.txt')

    bill_data=textreceipt.get(1.0,END)
    url.write((bill_data))
    url.close()
    messagebox.showinfo('information','your bill is successfully saved')
#end save function
def roti():
    if var1.get()==1:
        textroti.config(state=NORMAL)
        textroti.delete(0,END)
        textroti.focus()
    else:
        textroti.config(state=DISABLED)
        e_roti.set('0')
def dal():
    if var2.get()==1:
        textdal.config(state=NORMAL)
        textdal.delete(0,END)
        textdal.focus()
    else:
        textdal.config(state=DISABLED)
        e_dal.set('0')
def fish():
    if var3.get()==1:
        textfish.config(state=NORMAL)
        textfish.delete(0,END)
        textfish.focus()
    else:
        textfish.config(state=DISABLED)
        e_fish.set('0')

def chicken():
    if var4.get()==1:
        textchicken.config(state=NORMAL)
        textchicken.delete(0,END)
        textchicken.focus()
    else:
        textchicken.config(state=DISABLED)
        e_chicken.set('0')

def paneer():
        if var5.get() == 1:
            textpaneer.config(state=NORMAL)
            textpaneer.delete(0, END)
            textpaneer.focus()
        else:
            textpaneer.config(state=DISABLED)
            e_paneer.set('0')
def mashroom():
    if var6.get()==1:
        textmashroom.config(state=NORMAL)
        textmashroom.delete(0,END)
        textmashroom.focus()
    else:
        textmashroom.config(state=DISABLED)
        e_mashroom.set('0')
def sabji():
    if var7.get()==1:
        textsabji.config(state=NORMAL)
        textsabji.delete(0,END)
        textsabji.focus()
    else:
        textsabji.config(state=DISABLED)
        e_sabji.set('0')
def biriyani():
    if var8.get()==1:
        textbiriyani.config(state=NORMAL)
        textbiriyani.delete(0,END)
        textbiriyani.focus()
    else:
        textbiriyani.config(state=DISABLED)
        e_biriyani.set('0')
def rice():
    if var9.get()==1:
        textrice.config(state=NORMAL)
        textrice.delete(0,END)
        textrice.focus()
    else:
        textrice.config(state=DISABLED)
        e_rice.set('0')

def egg():
    if var10.get()==1:
        textegg.config(state=NORMAL)
        textegg.delete(0,END)
        textegg.focus()
    else:
        textegg.config(state=DISABLED)
        e_egg.set('0')
#drink function
def lassi():
    if var11.get()==1:
        textlassi.config(state=NORMAL)
        textlassi.delete(0,END)
        textlassi.focus()
    else:
        textlassi.config(state=DISABLED)
        e_lassi.set('0')
def cofee():
    if var12.get()==1:
        textcofee.config(state=NORMAL)
        textcofee.delete(0,END)
        textcofee.focus()
    else:
        textcofee.config(state=DISABLED)
        e_cofee.set('0')
def faluda():
    if var13.get()==1:
        textfaluda.config(state=NORMAL)
        textfaluda.delete(0,END)
        textfaluda.focus()
    else:
        textfaluda.config(state=DISABLED)
        e_faluda.set('0')
def shikanji():
    if var14.get()==1:
        textshikanji.config(state=NORMAL)
        textshikanji.delete(0,END)
        textshikanji.focus()
    else:
        textshikanji.config(state=DISABLED)
        e_shikanji.set('0')
def cold():
    if var15.get()==1:
        textcold.config(state=NORMAL)
        textcold.delete(0,END)
        textcold.focus()
    else:
        textcold.config(state=DISABLED)
        e_cold.set('0')
def jaljeera():
    if var16.get()==1:
        textjaljeera.config(state=NORMAL)
        textjaljeera.delete(0,END)
        textjaljeera.focus()
    else:
        textjaljeera.config(state=DISABLED)
        e_jaljeera.set('0')
def masalatea():
    if var17.get()==1:
        textmasalatea.config(state=NORMAL)
        textmasalatea.delete(0,END)
        textmasalatea.focus()
    else:
        textmasalatea.config(state=DISABLED)
        e_masalatea.set('0')
def badammilk():
    if var18.get()==1:
        textbadammilk.config(state=NORMAL)
        textbadammilk.delete(0,END)
        textbadammilk.focus()
    else:
        textbadammilk.config(state=DISABLED)
        e_badammilk.set('0')
def tea():
    if var19.get()==1:
        texttea.config(state=NORMAL)
        texttea.delete(0,END)
        texttea.focus()
    else:
        texttea.config(state=DISABLED)
        e_tea.set('0')
def wine():
    if var20.get()==1:
        textwine.config(state=NORMAL)
        textwine.delete(0,END)
        textwine.focus()
    else:
        textwine.config(state=DISABLED)
        e_wine.set('0')
#cake function
def oreo():
    if var21.get()==1:
        textoreo.config(state=NORMAL)
        textoreo.delete(0,END)
        textoreo.focus()
    else:
        textoreo.config(state=DISABLED)
        e_oreo.set('0')
def apple():
    if var22.get()==1:
        textapple.config(state=NORMAL)
        textapple.delete(0,END)
        textapple.focus()
    else:
        textapple.config(state=DISABLED)
        e_apple.set('0')
def kitkat():
    if var23.get()==1:
        textkitkat.config(state=NORMAL)
        textkitkat.delete(0,END)
        textkitkat.focus()
    else:
        textkitkat.config(state=DISABLED)
        e_kitkat.set('0')
def vanilla():
    if var24.get()==1:
        textvanilla.config(state=NORMAL)
        textvanilla.delete(0,END)
        textvanilla.focus()
    else:
        textvanilla.config(state=DISABLED)
        e_vanilla.set('0')
def banana():
    if var25.get()==1:
        textbanana.config(state=NORMAL)
        textbanana.delete(0,END)
        textbanana.focus()
    else:
        textbanana.config(state=DISABLED)
        e_banana.set('0')
def brownie():
    if var26.get()==1:
        textbrownie.config(state=NORMAL)
        textbrownie.delete(0,END)
        textbrownie.focus()
    else:
        textbrownie.config(state=DISABLED)
        e_brownie.set('0')
def pineapple():
    if var27.get()==1:
        textpineapple.config(state=NORMAL)
        textpineapple.delete(0,END)
        textpineapple.focus()
    else:
        textpineapple.config(state=DISABLED)
        e_pineapple.set('0')
def chocolate():
    if var28.get()==1:
        textchocolate.config(state=NORMAL)
        textchocolate.delete(0,END)
        textchocolate.focus()
    else:
        textchocolate.config(state=DISABLED)
        e_chocolate.set('0')
def blackforest():
    if var29.get()==1:
        textblackforest.config(state=NORMAL)
        textblackforest.delete(0,END)
        textblackforest.focus()
    else:
        textblackforest.config(state=DISABLED)
        e_blackforest.set('0')
def strawberry():
    if var30.get()==1:
        textstrawberry.config(state=NORMAL)
        textstrawberry.delete(0,END)
        textstrawberry.focus()
    else:
        textstrawberry.config(state=DISABLED)
        e_strawberry.set('0')

#cost
def totalcost():
    global subtotalofitem
    global priceoffood
    global priceofdrink
    global priceofcake
    item1=int(e_roti.get())
    item2 = int(e_dal.get())
    item3 = int(e_fish.get())
    item4 = int(e_chicken.get())
    item5 = int(e_paneer.get())
    item6 = int(e_mashroom.get())
    item7 = int(e_sabji.get())
    item8 = int(e_biriyani.get())
    item9 = int(e_rice.get())
    item10 = int(e_egg.get())

    item11 = int(e_lassi.get())
    item12 = int(e_cofee.get())
    item13 = int(e_faluda.get())
    item14 = int(e_shikanji.get())
    item15 = int(e_cold.get())
    item16 = int(e_jaljeera.get())
    item17 = int(e_masalatea.get())
    item18 = int(e_badammilk.get())
    item19 = int(e_tea.get())
    item20 = int(e_wine.get())

    item21 = int(e_oreo.get())
    item22 = int(e_apple.get())
    item23 = int(e_kitkat.get())
    item24 = int(e_vanilla.get())
    item25 = int(e_banana.get())
    item26 = int(e_brownie.get())
    item27 = int(e_pineapple.get())
    item28 = int(e_chocolate.get())
    item29 = int(e_blackforest.get())
    item30 = int(e_strawberry.get())

    priceoffood=(item1*10)+(item2*60)+(item3*100)+(item4*150)+(item5*150)+(item6*130)+(item7*90)+(item8*200)+(item9*60)+(item10*80)
    priceofdrink=(item11*70)+(item12*120)+(item13*150)+(item14*60)+(item15*60)+(item16*60)+(item17*120)+(item18*130)+(item19*40)+(item20*300)
    priceofcake=(item21*300)+(item22*400)+(item23*500)+(item24*350)+(item25*450)+(item26*230)+(item27*290)+(item28*300)+(item29*360)+(item30*380)


    costoffood.set(str(priceoffood)+' Rs')
    costofdrink.set(str(priceofdrink)+' Rs')
    costofcake.set(str(priceofcake)+' Rs')

    subtotalofitem = priceoffood+priceofdrink+priceofcake
    costofsubtotal.set(str(subtotalofitem)+' Rs')

    costofservicetax.set('50 Rs')

    totalcost=subtotalofitem+50
    costoftotal.set(str(totalcost)+" Rs")
#send
def send():


    root2=Toplevel()

    root2.title("send bill")
    root2.config(bg='red4')
    root2.geometry('485x620+50+50')
    logoimage=PhotoImage(file='send1.png')
    label=Label(root2,image=logoimage,bg='red4')
    label.pack()

    numberlabel=Label(root2,text='Mobile number',font=('arial',18,'bold underline'),bg='red4',fg='white')
    numberlabel.pack(pady=5)

    numberfield=Entry(root2,font=('helvetica',22,'bold'),bd=3,width=24)
    numberfield.pack(pady=5)

    billlabel = Label(root2, text='Bill Details', font=('arial', 18, 'bold underline'), bg='red4', fg='white')
    billlabel.pack(pady=5)

    textarea=Text(root2,font=('arial',12,'bold'),bd=3,width=42,height=14)
    textarea.pack(pady=5)
    textarea.insert(END,'Receipt Ref:\t\t'+ billnumber+'\t\t'+date+'\n')

    if costoffood.get()!='0 Rs':
        textarea.insert(END,f'Cost Of Food\t\t\t{priceoffood}Rs\n')
    if costofdrink.get()!='0 Rs':
        textarea.insert(END, f'Cost Of Drinks\t\t\t{priceofdrink}Rs\n')
    if costofcake.get()!='0 Rs':
        textarea.insert(END, f'Cost Of Cakes\t\t\t{priceofcake}Rs\n')

    textarea.insert(END, f'Sub total\t\t\t{subtotalofitem}Rs\n')
    textarea.insert(END, f'Service tax\t\t\t{50}Rs\n')
    textarea.insert(END, f'Total cost\t\t\t{subtotalofitem + 50}Rs\n')

    sendbutton=Button(root2,text='SEND',font=('arial',19,'bold'),bg='white',fg='red4',bd=7,relief=GROOVE,command=send_msg())
    sendbutton.pack(pady=5)

    root2.mainloop()

#receipt
def receipt():
    global  billnumber,date
    textreceipt.delete(1.0,END)
    x=random.randint(100,10000)
    billnumber='BILL'+str(x)
    date=time.strftime('%d/%m/%Y')
    textreceipt.insert(END,'Receipt Ref:\t\t'+billnumber+'\t\t'+date+'\n')
    textreceipt.insert(END,'**************************************************************\n')
    textreceipt.insert(END,'item:\t\t Cost of Items(Rs)\n')
    textreceipt.insert(END, '************************************************************\n')









    if e_roti.get()!='0':
        textreceipt.insert(END,f'Roti\t\t\t{int(e_roti.get())*10}\n\n')
    if e_dal.get()!='0':
        textreceipt.insert(END,f'Dal\t\t\t{int(e_dal.get())*60}\n\n')
    if e_fish.get()!='0':
        textreceipt.insert(END,f'Fish\t\t\t{int(e_fish.get())*100}\n')
    if e_chicken.get()!='0':
        textreceipt.insert(END,f'Chicken\t\t\t{int(e_chicken.get())*150}\n')
    if e_paneer.get()!='0':
        textreceipt.insert(END,f'Paneer\t\t\t{int(e_paneer.get())*150}\n')
    if e_mashroom.get()!='0':
        textreceipt.insert(END,f'Mashroom\t\t\t{int(e_mashroom.get())*130}\n')
    if e_sabji.get()!='0':
        textreceipt.insert(END,f'Sabji\t\t\t{int(e_sabji.get())*90}\n')
    if e_biriyani.get()!='0':
        textreceipt.insert(END,f'Biriyani\t\t\t{int(e_biriyani.get())*200}\n')
    if e_rice.get()!='0':
        textreceipt.insert(END,f'Rice\t\t\t{int(e_rice.get())*60}\n')
    if e_egg.get()!='0':
        textreceipt.insert(END,f'Egg Masala\t\t\t{int(e_egg.get())*80}\n')


    if e_lassi.get()!='0':
        textreceipt.insert(END,f'Lassi\t\t\t{int(e_lassi.get())*70}\n')
    if e_cofee.get()!='0':
        textreceipt.insert(END,f'Cofee\t\t\t{int(e_cofee.get())*120}\n')
    if e_faluda.get()!='0':
        textreceipt.insert(END,f'Faluda\t\t\t{int(e_faluda.get())*150}\n')
    if e_shikanji.get()!='0':
        textreceipt.insert(END,f'Shikanji\t\t\t{int(e_shikanji.get())*60}\n')
    if e_cold.get()!='0':
        textreceipt.insert(END,f'Cold drinks\t\t\t{int(e_cold.get())*60}\n')
    if e_jaljeera.get()!='0':
        textreceipt.insert(END,f'Jal Jeera\t\t\t{int(e_jaljeera.get())*60}\n')
    if e_masalatea.get()!='0':
        textreceipt.insert(END,f'Masala Tea\t\t\t{int(e_masalatea.get())*120}\n')
    if e_badammilk.get()!='0':
        textreceipt.insert(END,f'Badam Milk\t\t\t{int(e_badammilk.get())*130}\n')
    if e_tea.get()!='0':
        textreceipt.insert(END,f'Tea\t\t\t{int(e_tea.get())*40}\n')
    if e_wine.get()!='0':
        textreceipt.insert(END,f'Wine\t\t\t{int(e_wine.get())*300}\n')



    if e_oreo.get() != '0':
        textreceipt.insert(END, f'Oreo\t\t\t{int(e_oreo.get()) * 300}\n')
    if e_apple.get() != '0':
        textreceipt.insert(END, f'Apple\t\t\t{int(e_apple.get()) * 400}\n')
    if e_kitkat.get() != '0':
        textreceipt.insert(END, f'Kitkat\t\t\t{int(e_kitkat.get()) * 500}\n')
    if e_vanilla.get() != '0':
        textreceipt.insert(END, f'Vanilla\t\t\t{int(e_vanilla.get()) * 350}\n')
    if e_banana.get() != '0':
        textreceipt.insert(END, f'Banana\t\t\t{int(e_banana.get()) * 450}\n')
    if e_brownie.get() != '0':
        textreceipt.insert(END, f'Brownie\t\t\t{int(e_brownie.get()) * 230}\n')
    if e_pineapple.get() != '0':
        textreceipt.insert(END, f'Pineapple\t\t\t{int(e_pineapple.get()) * 290}\n')
    if e_chocolate.get() != '0':
        textreceipt.insert(END, f'Chocolate\t\t\t{int(e_chocolate.get()) * 300}\n')
    if e_blackforest.get() != '0':
        textreceipt.insert(END, f'Blackforest\t\t\t{int(e_blackforest.get()) * 360}\n')
    if e_strawberry.get() != '0':
        textreceipt.insert(END, f'Strawberry\t\t\t{int(e_strawberry.get()) * 380}\n\n')

    textreceipt.insert(END, '************************************************************\n')
    if costoffood.get()!='0 Rs':
        textreceipt.insert(END,f'Cost Of Food\t\t\t{priceoffood}Rs\n')
    if costofdrink.get()!='0 Rs':
        textreceipt.insert(END, f'Cost Of Drinks\t\t\t{priceofdrink}Rs\n')
    if costofcake.get()!='0 Rs':
        textreceipt.insert(END, f'Cost Of Cakes\t\t\t{priceofcake}Rs\n')

    textreceipt.insert(END, '************************************************************\n')

    textreceipt.insert(END,f'Sub total\t\t\t{subtotalofitem}Rs\n')
    textreceipt.insert(END, f'Service tax\t\t\t{50}Rs\n')
    textreceipt.insert(END, f'Total cost\t\t\t{subtotalofitem+50}Rs\n')
    textreceipt.insert(END, '************************************************************\n')

#reset
def reset():
    textreceipt.delete(1.0,END)
    e_roti.set('0')
    e_dal.set('0')
    e_fish.set('0')
    e_chicken.set('0')
    e_paneer.set('0')
    e_mashroom.set('0')
    e_sabji.set('0')
    e_biriyani.set('0')
    e_rice.set('0')
    e_egg.set('0')
    e_oreo.set('0')
    e_apple.set('0')
    e_kitkat.set('0')
    e_vanilla.set('0')
    e_banana.set('0')
    e_brownie.set('0')
    e_pineapple.set('0')
    e_chocolate.set('0')
    e_blackforest.set('0')
    e_strawberry.set('0')
    e_oreo.set('0')
    e_apple.set('0')
    e_kitkat.set('0')
    e_vanilla.set('0')
    e_banana.set('0')
    e_brownie.set('0')
    e_pineapple.set('0')
    e_chocolate.set('0')
    e_blackforest.set('0')
    e_strawberry.set('0')

    textroti.config(state=DISABLED)
    textdal.config(state=DISABLED)
    textfish.config(state=DISABLED)
    textchicken.config(state=DISABLED)
    textpaneer.config(state=DISABLED)
    textmashroom.config(state=DISABLED)
    textsabji.config(state=DISABLED)
    textbiriyani.config(state=DISABLED)
    textrice.config(state=DISABLED)
    textegg.config(state=DISABLED)
    textlassi.config(state=DISABLED)
    textcofee.config(state=DISABLED)
    textfaluda.config(state=DISABLED)
    textshikanji.config(state=DISABLED)
    textcold.config(state=DISABLED)
    textjaljeera.config(state=DISABLED)
    textmasalatea.config(state=DISABLED)
    textbadammilk.config(state=DISABLED)
    texttea.config(state=DISABLED)
    textwine.config(state=DISABLED)
    textoreo.config(state=DISABLED)
    textapple.config(state=DISABLED)
    textkitkat.config(state=DISABLED)
    textvanilla.config(state=DISABLED)
    textbanana.config(state=DISABLED)
    textbrownie.config(state=DISABLED)
    textpineapple.config(state=DISABLED)
    textchocolate.config(state=DISABLED)
    textblackforest.config(state=DISABLED)
    textstrawberry.config(state=DISABLED)

    var1.set(0)
    var2.set(0)
    var3.set(0)
    var4.set(0)
    var5.set(0)
    var6.set(0)
    var7.set(0)
    var8.set(0)
    var9.set(0)
    var10.set(0)
    var11.set(0)
    var12.set(0)
    var13.set(0)
    var14.set(0)
    var15.set(0)
    var16.set(0)
    var17.set(0)
    var18.set(0)
    var19.set(0)
    var20.set(0)
    var21.set(0)
    var22.set(0)
    var23.set(0)
    var24.set(0)
    var25.set(0)
    var26.set(0)
    var27.set(0)
    var28.set(0)
    var29.set(0)
    var30.set(0)

    costoffood.set('')
    costofdrink.set('')
    costofcake.set('')
    costofsubtotal.set('')
    costofservicetax.set('')
    costoftotal.set('')









#variable
var1=IntVar()
var2=IntVar()
var3=IntVar()
var4=IntVar()
var5=IntVar()
var6=IntVar()
var7=IntVar()
var8=IntVar()
var9=IntVar()
var10=IntVar()

var11=IntVar()
var12=IntVar()
var13=IntVar()
var14=IntVar()
var15=IntVar()
var16=IntVar()
var17=IntVar()
var18=IntVar()
var19=IntVar()
var20=IntVar()

var21=IntVar()
var22=IntVar()
var23=IntVar()
var24=IntVar()
var25=IntVar()
var26=IntVar()
var27=IntVar()
var28=IntVar()
var29=IntVar()
var30=IntVar()

#entry variable
e_roti= StringVar()
e_dal= StringVar()
e_fish= StringVar()
e_chicken= StringVar()
e_paneer= StringVar()
e_mashroom= StringVar()
e_sabji= StringVar()
e_biriyani= StringVar()
e_rice= StringVar()
e_egg= StringVar()

e_roti.set('0')
e_dal.set('0')
e_fish.set('0')
e_chicken.set('0')
e_paneer.set('0')
e_mashroom.set('0')
e_sabji.set('0')
e_biriyani.set('0')
e_rice.set('0')
e_egg.set('0')

e_lassi= StringVar()
e_cofee= StringVar()
e_faluda= StringVar()
e_shikanji= StringVar()
e_cold= StringVar()
e_jaljeera= StringVar()
e_masalatea= StringVar()
e_badammilk= StringVar()
e_tea= StringVar()
e_wine= StringVar()

e_lassi.set('0')
e_cofee.set('0')
e_faluda.set('0')
e_shikanji.set('0')
e_cold.set('0')
e_jaljeera.set('0')
e_masalatea.set('0')
e_badammilk.set('0')
e_tea.set('0')
e_wine.set('0')

e_oreo= StringVar()
e_apple= StringVar()
e_kitkat= StringVar()
e_vanilla= StringVar()
e_banana= StringVar()
e_brownie= StringVar()
e_pineapple= StringVar()
e_chocolate= StringVar()
e_blackforest= StringVar()
e_strawberry= StringVar()

e_oreo.set('0')
e_apple.set('0')
e_kitkat.set('0')
e_vanilla.set('0')
e_banana.set('0')
e_brownie.set('0')
e_pineapple.set('0')
e_chocolate.set('0')
e_blackforest.set('0')
e_strawberry.set('0')

costoffood=StringVar()
costofdrink=StringVar()
costofcake=StringVar()
costofsubtotal=StringVar()
costofservicetax=StringVar()
costoftotal=StringVar()


#food
roti=Checkbutton(foodframe,text='roti',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var1,command=roti)
roti.grid(row=0,column=0,sticky=W)

dal=Checkbutton(foodframe,text='dal',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var2,command=dal)
dal.grid(row=1,column=0,sticky=W)

fish=Checkbutton(foodframe,text='fish',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var3,command=fish)
fish.grid(row=2,column=0,sticky=W)

chicken=Checkbutton(foodframe,text='chicken',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var4,command=chicken)
chicken.grid(row=3,column=0,sticky=W)

paneer=Checkbutton(foodframe,text='paneer',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var5,command=paneer)
paneer.grid(row=4,column=0,sticky=W)

mashroom=Checkbutton(foodframe,text='mashroom',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var6,command=mashroom)
mashroom.grid(row=5,column=0,sticky=W)

sabji=Checkbutton(foodframe,text='sabji',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var7,command=sabji)
sabji.grid(row=6,column=0,sticky=W)

biriyani=Checkbutton(foodframe,text='biriyani',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var8,command=biriyani)
biriyani.grid(row=7,column=0,sticky=W)

rice=Checkbutton(foodframe,text='rice',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var9,command=rice)
rice.grid(row=8,column=0,sticky=W)

egg=Checkbutton(foodframe,text='egg masala',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var10,command=egg)
egg.grid(row=9,column=0,sticky=W)

#entry for food
textroti=Entry(foodframe,font=('arial',15,'bold'),bd=7,width=6,state=DISABLED, textvariable= e_roti)
textroti.grid(row=0,column=1)

textdal=Entry(foodframe,font=('arial',15,'bold'),bd=7,width=6,state=DISABLED, textvariable= e_dal)
textdal.grid(row=1,column=1)

textfish=Entry(foodframe,font=('arial',15,'bold'),bd=7,width=6,state=DISABLED, textvariable= e_fish)
textfish.grid(row=2,column=1)

textchicken=Entry(foodframe,font=('arial',15,'bold'),bd=7,width=6,state=DISABLED, textvariable= e_chicken)
textchicken.grid(row=3,column=1)

textpaneer=Entry(foodframe,font=('arial',15,'bold'),bd=7,width=6,state=DISABLED, textvariable= e_paneer)
textpaneer.grid(row=4,column=1)

textmashroom=Entry(foodframe,font=('arial',15,'bold'),bd=7,width=6,state=DISABLED, textvariable= e_mashroom)
textmashroom.grid(row=5,column=1)

textsabji=Entry(foodframe,font=('arial',15,'bold'),bd=7,width=6,state=DISABLED, textvariable= e_sabji)
textsabji.grid(row=6,column=1)

textbiriyani=Entry(foodframe,font=('arial',15,'bold'),bd=7,width=6,state=DISABLED, textvariable= e_biriyani)
textbiriyani.grid(row=7,column=1)

textrice=Entry(foodframe,font=('arial',15,'bold'),bd=7,width=6,state=DISABLED, textvariable= e_rice)
textrice.grid(row=8,column=1)

textegg=Entry(foodframe,font=('arial',15,'bold'),bd=7,width=6,state=DISABLED, textvariable= e_egg)
textegg.grid(row=9,column=1)

#drinks
lassi=Checkbutton(drinkframe,text='Lassi',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var11,command=lassi)
lassi.grid(row=0,column=0,sticky=W)

cofee=Checkbutton(drinkframe,text='Cofee',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var12,command=cofee)
cofee.grid(row=1,column=0,sticky=W)

faluda=Checkbutton(drinkframe,text='Faluda',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var13,command=faluda)
faluda.grid(row=2,column=0,sticky=W)


shikanji=Checkbutton(drinkframe,text='Shikanji',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var14,command=shikanji)
shikanji.grid(row=3,column=0,sticky=W)

cold=Checkbutton(drinkframe,text='Cold drinks',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var15,command=cold)
cold.grid(row=4,column=0,sticky=W)

jaljeera=Checkbutton(drinkframe,text='Jal-Jeera',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var16,command=jaljeera)
jaljeera.grid(row=5,column=0,sticky=W)

masalatea=Checkbutton(drinkframe,text='Masala-Tea',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var17,command=masalatea)
masalatea.grid(row=6,column=0,sticky=W)

badammilk=Checkbutton(drinkframe,text='Badam-Milk',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var18,command=badammilk)
badammilk.grid(row=7,column=0,sticky=W)

tea=Checkbutton(drinkframe,text='Tea',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var19,command=tea)
tea.grid(row=8,column=0,sticky=W)

wine=Checkbutton(drinkframe,text='wine',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var20,command=wine)
wine.grid(row=9,column=0,sticky=W)

#entry for drinks
textlassi=Entry(drinkframe,font=('arial',15,'bold'),bd=7,width=6,state=DISABLED, textvariable= e_lassi)
textlassi.grid(row=0,column=1)

textcofee=Entry(drinkframe,font=('arial',15,'bold'),bd=7,width=6,state=DISABLED, textvariable= e_cofee)
textcofee.grid(row=1,column=1)

textfaluda=Entry(drinkframe,font=('arial',15,'bold'),bd=7,width=6,state=DISABLED, textvariable= e_faluda)
textfaluda.grid(row=2,column=1)

textshikanji=Entry(drinkframe,font=('arial',15,'bold'),bd=7,width=6,state=DISABLED, textvariable= e_shikanji)
textshikanji.grid(row=3,column=1)

textcold=Entry(drinkframe,font=('arial',15,'bold'),bd=7,width=6,state=DISABLED, textvariable= e_cold)
textcold.grid(row=4,column=1)

textjaljeera=Entry(drinkframe,font=('arial',15,'bold'),bd=7,width=6,state=DISABLED, textvariable= e_jaljeera)
textjaljeera.grid(row=5,column=1)

textmasalatea=Entry(drinkframe,font=('arial',15,'bold'),bd=7,width=6,state=DISABLED, textvariable= e_masalatea)
textmasalatea.grid(row=6,column=1)

textbadammilk=Entry(drinkframe,font=('arial',15,'bold'),bd=7,width=6,state=DISABLED, textvariable= e_badammilk)
textbadammilk.grid(row=7,column=1)

texttea=Entry(drinkframe,font=('arial',15,'bold'),bd=7,width=6,state=DISABLED, textvariable= e_tea)
texttea.grid(row=8,column=1)

textwine=Entry(drinkframe,font=('arial',15,'bold'),bd=7,width=6,state=DISABLED, textvariable= e_wine)
textwine.grid(row=9,column=1)

#cakes
oreo=Checkbutton(cakeframe,text='oreo',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var21,command=oreo)
oreo.grid(row=0,column=0,sticky=W)

apple=Checkbutton(cakeframe,text='Apple',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var22,command=apple)
apple.grid(row=1,column=0,sticky=W)


kitkat=Checkbutton(cakeframe,text='Kitkat',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var23,command=kitkat)
kitkat.grid(row=2,column=0,sticky=W)

vanilla=Checkbutton(cakeframe,text='Vanilla',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var24,command=vanilla)
vanilla.grid(row=3,column=0,sticky=W)

banana=Checkbutton(cakeframe,text='Banana',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var25,command=banana)
banana.grid(row=4,column=0,sticky=W)

brownie=Checkbutton(cakeframe,text='Brownie',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var26,command=brownie)
brownie.grid(row=5,column=0,sticky=W)

pineapple=Checkbutton(cakeframe,text='Pineapple',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var27,command=pineapple)
pineapple.grid(row=6,column=0,sticky=W)

chocolate=Checkbutton(cakeframe,text='Chocolate',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var28,command=chocolate)
chocolate.grid(row=7,column=0,sticky=W)

blackforest=Checkbutton(cakeframe,text='Blackforest',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var29,command=blackforest)
blackforest.grid(row=8,column=0,sticky=W)

strawberry=Checkbutton(cakeframe,text='Strawberry',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var30,command=strawberry)
strawberry.grid(row=9,column=0,sticky=W)

#entry for cakes
textoreo=Entry(cakeframe,font=('arial',15,'bold'),bd=7,width=6,state=DISABLED, textvariable= e_oreo)
textoreo.grid(row=0,column=1)

textapple=Entry(cakeframe,font=('arial',15,'bold'),bd=7,width=6,state=DISABLED, textvariable= e_apple)
textapple.grid(row=1,column=1)

textkitkat=Entry(cakeframe,font=('arial',15,'bold'),bd=7,width=6,state=DISABLED, textvariable= e_kitkat)
textkitkat.grid(row=2,column=1)

textvanilla=Entry(cakeframe,font=('arial',15,'bold'),bd=7,width=6,state=DISABLED, textvariable= e_vanilla)
textvanilla.grid(row=3,column=1)

textbanana=Entry(cakeframe,font=('arial',15,'bold'),bd=7,width=6,state=DISABLED, textvariable= e_banana)
textbanana.grid(row=4,column=1)

textbrownie=Entry(cakeframe,font=('arial',15,'bold'),bd=7,width=6,state=DISABLED, textvariable= e_brownie)
textbrownie.grid(row=5,column=1)

textpineapple=Entry(cakeframe,font=('arial',15,'bold'),bd=7,width=6,state=DISABLED, textvariable= e_pineapple)
textpineapple.grid(row=6,column=1)

textchocolate=Entry(cakeframe,font=('arial',15,'bold'),bd=7,width=6,state=DISABLED, textvariable= e_chocolate)
textchocolate.grid(row=7,column=1)

textblackforest=Entry(cakeframe,font=('arial',15,'bold'),bd=7,width=6,state=DISABLED, textvariable= e_blackforest)
textblackforest.grid(row=8,column=1)

textstrawberry=Entry(cakeframe,font=('arial',15,'bold'),bd=7,width=6,state=DISABLED, textvariable= e_strawberry)
textstrawberry.grid(row=9,column=1)

#cost labels & frames

labelcostoffood =Label(costframe,text='cost of food',font=('arial',16,'bold'),bg='firebrick4',fg='white')
labelcostoffood.grid(row=0,column=0)
textcostoffood=Entry(costframe,font=('arial',16,'bold'),bd=6,width=14,state='readonly',textvariable=costoffood)
textcostoffood.grid(row=0,column=1,padx=41)

labelcostofdrink =Label(costframe,text='cost of drink',font=('arial',16,'bold'),bg='firebrick4',fg='white')
labelcostofdrink.grid(row=1,column=0)
textcostofdrink=Entry(costframe,font=('arial',16,'bold'),bd=6,width=14,state='readonly',textvariable=costofdrink)
textcostofdrink.grid(row=1,column=1,padx=41)


labelcostofcake =Label(costframe,text='cost of cake',font=('arial',16,'bold'),bg='firebrick4',fg='white')
labelcostofcake.grid(row=2,column=0)
textcostofcake=Entry(costframe,font=('arial',16,'bold'),bd=6,width=14,state='readonly',textvariable=costofcake)
textcostofcake.grid(row=2,column=1,padx=41)

labelsubtotal =Label(costframe,text='sub total',font=('arial',16,'bold'),bg='firebrick4',fg='white')
labelsubtotal.grid(row=0,column=2)
textsubtotal=Entry(costframe,font=('arial',16,'bold'),bd=6,width=14,state='readonly',textvariable=costofsubtotal)
textsubtotal.grid(row=0,column=3,padx=41)

labelservicetax =Label(costframe,text='Service Tax',font=('arial',16,'bold'),bg='firebrick4',fg='white')
labelservicetax.grid(row=1,column=2)
textservicetax=Entry(costframe,font=('arial',16,'bold'),bd=6,width=14,state='readonly',textvariable=costofservicetax)
textservicetax.grid(row=1,column=3,padx=41)

labeltotalcost =Label(costframe,text='Total cost',font=('arial',16,'bold'),bg='firebrick4',fg='white')
labeltotalcost.grid(row=2,column=2)
texttotalcost=Entry(costframe,font=('arial',16,'bold'),bd=6,width=14,state='readonly',textvariable=costoftotal)
texttotalcost.grid(row=2,column=3,padx=41)

#buttons
buttontotal = Button(buttonframe,text='Total',font=('arial',14,'bold'),fg='white',bg='red4',bd=3,padx=5,command=totalcost)
buttontotal.grid(row=0,column=0)

buttonreceipt = Button(buttonframe,text='Receipt',font=('arial',14,'bold'),fg='white',bg='red4',bd=3,padx=5,command=receipt)
buttonreceipt.grid(row=0,column=1)

buttonsave = Button(buttonframe,text='Save',font=('arial',14,'bold'),fg='white',bg='red4',bd=3,padx=5,command=save)
buttonsave.grid(row=0,column=2)

buttonsend = Button(buttonframe,text='Send',font=('arial',14,'bold'),fg='white',bg='red4',bd=3,padx=5,command=send)
buttonsend.grid(row=0,column=3)

buttonreset = Button(buttonframe,text='Reset',font=('arial',14,'bold'),fg='white',bg='red4',bd=3,padx=5,command=reset)
buttonreset.grid(row=0,column=4)

#textarea of receipt
textreceipt = Text(receiptframe,font=('arial',12,'bold'),bd=3,width=42,height=14)
textreceipt.grid(row=0,column=0)

#calculator
operator=''
def buttonClick(numbers):
    global operator
    operator=operator+numbers
    calculatorfield.delete(0,END)
    calculatorfield.insert(END,operator)

def clear():
    global operator
    operator=''
    calculatorfield.delete(0,END)

def answer():
    global operator
    result=str(eval(operator))
    calculatorfield.delete(0,END)
    calculatorfield.insert(0,result)
    operator=''

calculatorfield=Entry(calculatorframe,font=('arial',14,'bold'),width=32,bd=4)
calculatorfield.grid(row=0,column=0,columnspan=4)

button7=Button(calculatorframe,text='7',font=('arial',16,'bold'),fg='yellow',bg='red4',bd=6,width=6,command=lambda :buttonClick('7'))
button7.grid(row=1,column=0)
button8=Button(calculatorframe,text='8',font=('arial',16,'bold'),fg='yellow',bg='red4',bd=6,width=6,command=lambda :buttonClick('8'))
button8.grid(row=1,column=1)
button9=Button(calculatorframe,text='9',font=('arial',16,'bold'),fg='yellow',bg='red4',bd=6,width=6,command=lambda :buttonClick('9'))
button9.grid(row=1,column=2)
buttonplus=Button(calculatorframe,text='+',font=('arial',16,'bold'),fg='yellow',bg='red4',bd=6,width=6,command=lambda :buttonClick('+'))
buttonplus.grid(row=1,column=3)
button4=Button(calculatorframe,text='4',font=('arial',16,'bold'),fg='yellow',bg='red4',bd=6,width=6,command=lambda :buttonClick('4'))
button4.grid(row=2,column=0)
button5=Button(calculatorframe,text='5',font=('arial',16,'bold'),fg='yellow',bg='red4',bd=6,width=6,command=lambda :buttonClick('5'))
button5.grid(row=2,column=1)
button6=Button(calculatorframe,text='6',font=('arial',16,'bold'),fg='yellow',bg='red4',bd=6,width=6,command=lambda :buttonClick('6'))
button6.grid(row=2,column=2)
buttonminus=Button(calculatorframe,text='-',font=('arial',16,'bold'),fg='yellow',bg='red4',bd=6,width=6,command=lambda :buttonClick('-'))
buttonminus.grid(row=2,column=3)
button1=Button(calculatorframe,text='1',font=('arial',16,'bold'),fg='yellow',bg='red4',bd=6,width=6,command=lambda :buttonClick('1'))
button1.grid(row=3,column=0)
button2=Button(calculatorframe,text='2',font=('arial',16,'bold'),fg='yellow',bg='red4',bd=6,width=6,command=lambda :buttonClick('2'))
button2.grid(row=3,column=1)
button3=Button(calculatorframe,text='3',font=('arial',16,'bold'),fg='yellow',bg='red4',bd=6,width=6,command=lambda :buttonClick('3'))
button3.grid(row=3,column=2)
buttonmul=Button(calculatorframe,text='*',font=('arial',16,'bold'),fg='yellow',bg='red4',bd=6,width=6,command=lambda :buttonClick('*'))
buttonmul.grid(row=3,column=3)
buttonans=Button(calculatorframe,text='Ans',font=('arial',16,'bold'),fg='yellow',bg='green',bd=6,width=6,command=answer)
buttonans.grid(row=4,column=0)
buttonclear=Button(calculatorframe,text='Clear',font=('arial',16,'bold'),fg='white',bg='red4',bd=6,width=6,command=clear)
buttonclear.grid(row=4,column=2)
button0=Button(calculatorframe,text='0',font=('arial',16,'bold'),fg='yellow',bg='red4',bd=6,width=6,command=lambda :buttonClick('0'))
button0.grid(row=4,column=1)
buttondiv=Button(calculatorframe,text='%',font=('arial',16,'bold'),fg='yellow',bg='red4',bd=6,width=6,command=lambda :buttonClick('%'))
buttondiv.grid(row=4,column=3)







root.mainloop()

