import adduser as x
import fetchall as y
import fatchone as z
import update as p
import delete as q


print("1.adduser"  "2.fetchall"  "3.fetchone"   "4.update"  "5.delete")
option=int(input("enter ur option"))

if option==1:
    x.add_user()
elif option==2:
    y.fetch_all()
elif option==3:
    z.fatch_one(id)
elif option==4:
    p.update()
elif option==5:
    q.delete()
else:
    print("enter valid option")
