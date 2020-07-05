import pymysql

print("Welcome to State Bank of India")
print("Are you existing customer ?")
choice=input("Press Y to continue N to stop\n")
if choice=='y' or choice=='Y':
    ip1=input("Enter user name:\n")
    ip2=int(input("Enter PIN:\n"))
    

    conn=pymysql.connect(host='localhost',user='root',password='',database='sbi')
    cur=conn.cursor()

    query="select * from user_details where name='%s' and pin='%d'"%(ip1,ip2)

    cur.execute(query)

    row=cur.rowcount

    if row>0:
        print("User Identified")
        for r in cur.fetchall():
            print("Welcome",r[0])
            op=float(input("Press \n1. Withdraw \n2. Deposit \n3. Balance Check\n"))
            if op==1:
                amt=int(input("ENter amount to withdraw\n"))
                if (r[3]-amt)>1000:
                    rem = r[3]-amt
                    cur.execute("update user_details set bal = '%f' where name = '%s' and pin = '%d'"%(float(rem),ip1,ip2))
                    print("amount %d withdrawn, balnace is %d"%(amt,rem))
                else:
                    print("Insufficient balance to withdraw")
                
            elif op==2:
                amt=float(input("ENter amount to deposit\n"))
                cur_bal = r[3]+amt
                cur.execute("update user_details set bal = '%f' where name = '%s' and pin = '%d'"%(float(cur_bal),ip1,ip2))
                print("amount %f depsoited, balnace is %f"%(amt,cur_bal))
            elif op==3:
                print("Balnace is",r[3])
            else:
                print("Wrong choice!")
    else:
        print("User Name or PIN maybe wrong. Kindly check once !!!")
        
elif choice=='n' or choice=='N':
    print("Sorry for inconvinience, visit nearest branch to avail ATM services")

else:
    print("Invalid input !!!")
