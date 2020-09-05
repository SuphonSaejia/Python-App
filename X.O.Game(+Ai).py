import tkinter as tk
from tkinter import messagebox
window = tk.Tk()
window.title("GameX.O.")
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
lbl1 = tk.Label(window,text="GameX.O.",font=("Arial Bold",30))
lbl1.grid(column=0,row=0)
lbl1 = tk.Label(window,text="Number:",font=("Arial Bold",15))
lbl1.grid(column=0,row=7)
txtl=tk.Entry(window,width=13)
txtl.grid(column=0,row=8)
def cr():
    global i,j,i1,t1,t2,t3,t4,t5,t6,t7,t8,t9,x,y,z,x1,y1,z1,x2,y2,z2
    x='[   1   ]'
    y='[   2   ]'
    z='[   3   ]'
    lbl1 = tk.Label(window,text=(""+x+y+z),font=("Arial Bold",30))
    lbl1.grid(column=0,row=4)
    x1='[   4   ]'
    y1='[   5   ]'
    z1='[   6   ]'
    lbl1 = tk.Label(window,text=(""+x1+y1+z1),font=("Arial Bold",30))
    lbl1.grid(column=0,row=5)
    x2='[   7   ]'
    y2='[   8   ]'
    z2='[   9   ]'
    lbl1 = tk.Label(window,text=(""+x2+y2+z2),font=("Arial Bold",30))
    lbl1.grid(column=0,row=6)

cr()
def btn1_clicked():
    global i,j,i1,t1,t2,t3,t4,t5,t6,t7,t8,t9,x,y,z,x1,y1,z1,x2,y2,z2,g,c1,c2,c3,r1,r2,r3,xr,xl,oc1,oc2,oc3,or1,or2,or3,oxr,oxl
    n= int(txtl.get())
    g=g+1
    i=i+1
    j=i%2
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
           lbl1 = tk.Label(window,text=(""+x+y+z),font=("Arial Bold",30))
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
           lbl1 = tk.Label(window,text=(""+x+y+z),font=("Arial Bold",30))
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
             lbl1 = tk.Label(window,text=(""+x+y+z),font=("Arial Bold",30))
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
           lbl1 = tk.Label(window,text=(""+x1+y1+z1),font=("Arial Bold",30))
           lbl1.grid(column=0,row=5)
    if(n==5):
        if(t5==0):
           t5=1
           if(j!=0):
               y1='[   x   ]'
               c1=c1+1
               c2=c2+1
               c3=c3+1
               r1=r1+1
               r2=r2+1
               r3=r3+1
               xr=xr+1
               xl=xl+1
           else:
              y1='[   o   ]'
              oc1=oc1+1
              oc2=oc2+1
              oc3=oc3+1
              or1=or1+1
              or2=or2+1
              or3=or3+1
              oxr=oxr+1
              oxl=oxl+1
           lbl1 = tk.Label(window,text=(""+x1+y1+z1),font=("Arial Bold",30))
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
             lbl1 = tk.Label(window,text=(""+x1+y1+z1),font=("Arial Bold",30))
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
           lbl1 = tk.Label(window,text=(""+x2+y2+z2),font=("Arial Bold",30))
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
           lbl1 = tk.Label(window,text=(""+x2+y2+z2),font=("Arial Bold",30))
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
             lbl1 = tk.Label(window,text=(""+x2+y2+z2),font=("Arial Bold",30))
             lbl1.grid(column=0,row=6)          
             
    txtl=tk.Entry(windowt,width=13)
    txtl.grid(column=0,row=8)       
    print(str(j))
    if(c1==3 or c2==3 or c3==3 or r1==3 or r2==3 or r3==3 or xl==3 or xr==3):
        messagebox.showinfo("Messag title","ผู้เล่น X เป็นผู้ชนะ")
    elif(oc1==3 or oc2==3 or oc3==3 or or1==3 or or2==3 or or3==3 or oxl==3 or oxr==3):
        messagebox.showinfo("Messag title","ผู้เล่น O เป็นผู้ชนะ")
    elif(g==9):
        messagebox.showinfo("Messag title","เสมอกันไม่มีผู้ชนะ")
        cr()
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
    
btn = tk.Button(window,text=' กด ',width=13,command=btn1_clicked)
btn.grid(column=0,row=9)
window.mainloop()
