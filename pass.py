# important libraries 
import string 
import random 
import sqlite3 # for databse

pas=sqlite3.connect('Pass.db')
cur=pas.cursor()

def create():
    query='CREATE TABLE Pass_Word(ACC_NAME TEXT NOT NULL,PASSWORD TEXT NOT NULL);'
    cur.execute(query)
# to generate passwords
def want(nm1,nm2):
    an=str(input("Enter the name of the account for which you want a password : -"))
    while True :
        rann=random.randint(1,len(nm1))
        name=nm1[0:rann]
        rann=random.randint(1,len(nm2))
        sur=nm2[0:rann]
        digit=str(random.randint(0,10))+str(random.randint(0,10))+str(random.randint(0,10))
        pw=''.join(name)+''.join(sur)+''.join(digit)
        print("Your password is ....  "+pw)
        inp=str(input("\n Satisfied ....? (y/n)"))
        if inp=='y':
            break
    insert='INSERT INTO Pass_Word(ACC_NAME , PASSWORD) VALUES(?,?);'
    cur.execute(insert,(an,pw,))
# to see all of your passwords
def show():
    squery='SELECT * FROM Pass_Word ;'
    cur.execute(squery)
    while True:
        record=cur.fetchone()
        if record==None:
            break
        print(record[0]+' : '+record[1])
    return
# to insert an existing password
def insert():
    an=str(input("Enter Account name : - "))
    pw=str(input("Enter Password : - "))
    insert='INSERT INTO Pass_Word(ACC_NAME , PASSWORD) VALUES(?,?);'
    cur.execute(insert,(an,pw,))
# to search a password
def search():
    acc=str(input("Enter the name account name your are seaching for :- "))
    query1="SELECT * FROM Pass_Word WHERE ACC_NAME='{}';".format(acc)
    cur.execute(query1)
    while True:
        record=cur.fetchone()
        if record==None:
            break
        print(record[0]+' : '+record[1])
    return
yc=int(input("\t\t\t\tWelcome Back !!!!\n1-Want new password ? ,\n2- Want to see All of your passwords ,\n3- Forgot any Password , want to search, \n4-Want to insert Existing account's password?\n"))
if yc==1:
    nm1=input(str("Enter your first name : "))
    nm2=input(str("Enter your second name : "))
    want(nm1,nm2)
    print('\n Have a good Day !!')
elif yc==2:
    
    show()
    print('\n Have a good Day !!')
elif yc==3:
    search()
    print('\n Have a good Day !!')
elif yc==4:
    insert()
    print('\n Have a good Day !!')
pas.commit()
pas.close()
