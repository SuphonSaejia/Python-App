import tkinter as tk
from tkinter import messagebox
window = tk.Tk()
window.title("GameX.O.")
window.configure(background='#D9EDE7')
def ints(): #ประกาศตัวเเปลและเคลียร์ข้อมูล
     global i,j,i1,t1,t2,t3,t4,t5,t6,t7,t8,t9,x,y,z,x1,y1,z1,x2,y2,z2,g,c1,c2,c3,r1,r2,r3,xr,xl,oc1,oc2,oc3,or1,or2,or3,oxr,oxl,txtl,n,num
     g=0
     i=1
     i1=0
     t1=0
     t2=0
     t3=0
     t4=0
     t5=0
     t6=0
     t7=0
     t8=0
     t9=0
     
     c1=0
     c2=0
     c3=0
     r1=0
     r2=0
     r3=0
     xr=0
     xl=0
     
     oc1=0
     oc2=0
     oc3=0
     or1=0
     or2=0
     or3=0
     oxr=0
     oxl=0
     
     num=[]
def cr():  #เคลียร์หน้าจอใหม่
    global i,j,i1,t1,t2,t3,t4,t5,t6,t7,t8,t9,x,y,z,x1,y1,z1,x2,y2,z2
    x='[   1   ]'
    y='[   2   ]'
    z='[   3   ]'
    lbl1 = tk.Label(window,text=(""+x+y+z),font=("Arial Bold",30),bg='#D9EDE7',fg='#C9B7DB')
    lbl1.grid(column=0,row=4)
    x1='[   4   ]'
    y1='[   5   ]'
    z1='[   6   ]'
    lbl1 = tk.Label(window,text=(""+x1+y1+z1),font=("Arial Bold",30),bg='#D9EDE7',fg='#C9B7DB')
    lbl1.grid(column=0,row=5)
    x2='[   7   ]'
    y2='[   8   ]'
    z2='[   9   ]'
    lbl1 = tk.Label(window,text=(""+x2+y2+z2),font=("Arial Bold",30),bg='#D9EDE7',fg='#C9B7DB')
    lbl1.grid(column=0,row=6)
def cseckwin(): #หาผู้ชนะ
    global i,j,i1,t1,t2,t3,t4,t5,t6,t7,t8,t9,x,y,z,x1,y1,z1,x2,y2,z2,g,c1,c2,c3,r1,r2,r3,xr,xl,oc1,oc2,oc3,or1,or2,or3,oxr,oxl,txtl,n,num
    if(n==1):
        if(t1==0):
           t1=1
           if(j!=0):
              x='[   x   ]'
              c1=c1+1
              r1=r1+1
              xr=xr+1
           else:
              x='[   o   ]'
              oc1=oc1+1
              or1=or1+1
              oxr=oxr+1
           lbl1 = tk.Label(window,text=(""+x+y+z),font=("Arial Bold",30),bg='#D9EDE7',fg='#C9B7DB')
           lbl1.grid(column=0,row=4)
    if(n==2):
        if(t2==0):
           t2=1
           if(j!=0):
              y='[   x   ]'
              c2=c2+1
              r1=r1+1
           else:
              y='[   o   ]'
              oc2=oc2+1
              or1=or1+1
           lbl1 = tk.Label(window,text=(""+x+y+z),font=("Arial Bold",30),bg='#D9EDE7',fg='#C9B7DB')
           lbl1.grid(column=0,row=4)
    if(n==3):
         if(t3==0):
             t3=1
             if(j!=0):
                z='[   x   ]'
                c3=c3+1
                r1=r1+1
                xl=xl+1
             else:
                z='[   o   ]'
                oc3=oc3+1
                or1=or1+1
                oxl=oxl+1
             lbl1 = tk.Label(window,text=(""+x+y+z),font=("Arial Bold",30),bg='#D9EDE7',fg='#C9B7DB')
             lbl1.grid(column=0,row=4)
    if(n==4):
         if(t4==0):
           t4=1
           if(j!=0):
              x1='[   x   ]'
              c1=c1+1
              r2=r2+1
           else:
              x1='[   o   ]'
              oc1=oc1+1
              or2=or2+1
           lbl1 = tk.Label(window,text=(""+x1+y1+z1),font=("Arial Bold",30),bg='#D9EDE7',fg='#C9B7DB')
           lbl1.grid(column=0,row=5)
    if(n==5):
        if(t5==0):
           t5=1
           if(j!=0):
               y1='[   x   ]'
               
               c2=c2+1
               r2=r2+1
               xr=xr+1
               xl=xl+1
           else:
              y1='[   o   ]'
              
              oc2=oc2+1
              or2=or2+1
              oxr=oxr+1
              oxl=oxl+1
           lbl1 = tk.Label(window,text=(""+x1+y1+z1),font=("Arial Bold",30),bg='#D9EDE7',fg='#C9B7DB')
           lbl1.grid(column=0,row=5)
    if(n==6):
         if(t6==0):
             t6=1
             if(j!=0):
                z1='[   x   ]'
                c3=c3+1
                r2=r2+1
             else:
                z1='[   o   ]'
                oc3=oc3+1
                or2=or2+1
             lbl1 = tk.Label(window,text=(""+x1+y1+z1),font=("Arial Bold",30),bg='#D9EDE7',fg='#C9B7DB')
             lbl1.grid(column=0,row=5)
    if(n==7):
         if(t7==0):
           t7=1
           if(j!=0):
              x2='[   x   ]'
              c1=c1+1
              r3=r3+1
              xl=xl+1
           else:
              x2='[   o   ]'
              oc1=oc1+1
              or3=or3+1
              oxl=oxl+1
           lbl1 = tk.Label(window,text=(""+x2+y2+z2),font=("Arial Bold",30),bg='#D9EDE7',fg='#C9B7DB')
           lbl1.grid(column=0,row=6)
    if(n==8):
        if(t8==0):
           t8=1
           if(j!=0):
               y2='[   x   ]'
               c2=c2+1
               r3=r3+1
               
           else:
              y2='[   o   ]'
              oc2=oc2+1
              or3=or3+1
           lbl1 = tk.Label(window,text=(""+x2+y2+z2),font=("Arial Bold",30),bg='#D9EDE7',fg='#C9B7DB')
           lbl1.grid(column=0,row=6)
    if(n==9):
         if(t9==0):
             t9=1
             if(j!=0):
                z2='[   x   ]'
                c3=c3+1
                r3=r3+1
                xr=xr+1
             else:
                z2='[   o   ]'
                oc3=oc3+1
                or3=or3+1
                oxr=oxr+1
             lbl1 = tk.Label(window,text=(""+x2+y2+z2),font=("Arial Bold",30),bg='#D9EDE7',fg='#C9B7DB')
             lbl1.grid(column=0,row=6)          
             
    txtl=tk.Entry(window,text='',width=13)
    txtl.grid(column=0,row=8)       
    print(str(j))
    i=i+1
    if((i%2) == 0):
         lbl1 = tk.Label(window,text="O",font=("Arial Bold",25),bg='#D9EDE7',fg='gray')
         lbl1.grid(column=0,row=2)
    else :
         lbl1 = tk.Label(window,text="X",font=("Arial Bold",25),bg='#D9EDE7',fg='gray')
         lbl1.grid(column=0,row=2)
    if(c1==3 or c2==3 or c3==3 or r1==3 or r2==3 or r3==3 or xl==3 or xr==3):
        messagebox.showinfo("ผลการแข่งขัน","ผู้เล่น X เป็นผู้ชนะ")
        cr()
        ints()
    elif(oc1==3 or oc2==3 or oc3==3 or or1==3 or or2==3 or or3==3 or oxl==3 or oxr==3):
        messagebox.showinfo("ผลการแข่งขัน","ผู้เล่น O เป็นผู้ชนะ")
        cr()
        ints()
    elif(g==9):
        messagebox.showinfo("ผลการแข่งขัน","เสมอกันไม่มีผู้ชนะ")
        cr()
        ints()
def btn1_clicked():
    global i,j,i1,t1,t2,t3,t4,t5,t6,t7,t8,t9,x,y,z,x1,y1,z1,x2,y2,z2,g,c1,c2,c3,r1,r2,r3,xr,xl,oc1,oc2,oc3,or1,or2,or3,oxr,oxl,txtl,n,num
    try:
         n= int(txtl.get())
         for L in num:
              if(L==n):
                   L1=1
                   n=0
         if(n==1111):
            messagebox.showinfo("จัดทำโดย","นาย สุพล แซ่เจี่ย\n61030060")
         if(n>0 and n<10):
            g=g+1
            j=i%2
            num.append(n)
            cseckwin()
         else :
            txtl=tk.Entry(window,text='',width=13)
            txtl.grid(column=0,row=8)
            if(L1==1):
                 messagebox.showinfo("คำเตือน","หมายเลขนี้ถูกใช้ไปแล้ว")
            else:
                 messagebox.showerror("คำเตือน","กรุณาใส่เลข 1-9 ")
            n=0
            L1=0
    except:
        txtl=tk.Entry(window,text='',width=13)
        txtl.grid(column=0,row=8)
        messagebox.showerror("คำเตือน","กรุณาใส่เลข 1-9 ")
#...........ส่วนUI.............   
ints()
cr()
lbl1 = tk.Label(window,text="GameX.O.",fg="#FFB7B7",font=("Arial Bold",30),bg='#D9EDE7')
lbl1.grid(column=0,row=0)
lbl1 = tk.Label(window,text="Turn of Player",font=("Arial Bold",25),bg='#D9EDE7',fg='white')
lbl1.grid(column=0,row=1)
if((i%2) == 0):
    lbl1 = tk.Label(window,text="O",font=("Arial Bold",25),bg='#D9EDE7',fg='gray')
    lbl1.grid(column=0,row=2)
else :
    lbl1 = tk.Label(window,text="X",font=("Arial Bold",25),bg='#D9EDE7',fg='gray')
    lbl1.grid(column=0,row=2)

lbl1 = tk.Label(window,text="Number",font=("Arial Bold",15),bg='#D9EDE7',fg='gray')
lbl1.grid(column=0,row=7)
lbl1 = tk.Label(window,text="*สุพล แซ่เจี่ย  61030060",font=("Arial Bold",13),bg='#D9EDE7',fg="#FFB7B7")
lbl1.grid(column=0,row=10)
#...........ส่วนรับข้อมูล...........
txtl=tk.Entry(window,width=13)
txtl.grid(column=0,row=8)
btn = tk.Button(window,text='Enter',fg="black",bg="#AAD4E0",width=11,font=("Arial Bold",9),command=btn1_clicked)
btn.grid(column=0,row=9)
window.mainloop()
