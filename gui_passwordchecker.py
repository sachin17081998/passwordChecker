import tkinter as g
from tkinter import font
from PIL import ImageTk, Image
import requests
import hashlib



root=g.Tk()
root.minsize(height=550,width=750)
root.maxsize(height=550,width=750)
root.configure(background='#1f1f1f')
root.title('Passsword Checker')

#image reference
im = ImageTk.PhotoImage(Image.open("images/hj2.jpg"))
#function to check the password
def checkpassword():
       
    password=content.get()
    
    
    if(len(password)<1):
        con.config(text='please enter your password so that we can check it')
    else:
        
        try:
            

            # function to find hash of our password

            def hashcaluclate(password):
                #we have to encode our password with sha1 hashing algorithm and utf-8 because the api stores tha password in 
                #in this format.
                return hashlib.sha1(password.encode('utf-8')).hexdigest()

            # code to split calculated hash into two parts,head=first five char and tail=remaining char
            sha1pass = hashcaluclate(password)
            head, tail = sha1pass[:5], sha1pass[5:]
            head = head.upper()
            tail = tail.upper()

            # code for requesting password checker api
            url = 'https://api.pwnedpasswords.com/range/'+head
            res = requests.get(url)
            res.encoding = 'utf-8'

            apiresult = res.text  # .text conversts the result into a string
            list_of_api_hash = apiresult.splitlines(False)

            # function to check if the tail of user password matches with any of the password returned by api
            def checker(list_of_api_hash, tail):
                flg = True
                for item in list_of_api_hash:
                    if tail == item[:35]:
                        con.config(text='your password is leaked')
                        
                        flg = False
                        break
                    else:
                        flg = True
                return flg

            if checker(list_of_api_hash, tail):
                    con.config(text=' ')
                    con.config(text='your password is safe')
                        
                    


        except TypeError:
            con.config(text='there is a type error')
        except ConnectionError:        
            con.config(text='please connect to an internet')
        except:
            con.config(text='there is some issue with your connection')


  


#font objects 
fnew=font.Font(family='verdana',size=13,weight='bold')
f=font.Font(family='verdana',size=25,weight='bold')


    


g.Label(bd=5,height=200,width=360,image=im).place(height=200,width=180,relx=0.0,rely=0.1)
g.Label(text='Check Your password Here.',font=f,fg='#CACBC1',bg='#1f1f1f').place(relx=0.26,rely=0.25)

#password section
g.Label(text='enter your password',font=fnew,bg='#1f1f1f',fg='#CACBC1').place(relx=0.07,rely=0.6)
content=g.StringVar()
passw=g.Entry(text='enter your password',font=f,textvariable=content)
passw.place(relwidth=0.5,relheight=0.05,relx=0.37,rely=0.6)
g.Button(command=checkpassword,text='Check',relief='ridge',cursor='circle',font=fnew,fg='#CACBC1',bg='#1f1f1f',height=1,width=10,activebackground='#3d3d3d',highlightbackground='#3d3d3d').place(rely=0.7,relx=0.7)

#result label
con=g.Label(text='', font=fnew,fg='red',bg='#1f1f1f')
con.place(relx=0.1,rely=0.8)

if __name__ == "__main__":
    root.mainloop()
