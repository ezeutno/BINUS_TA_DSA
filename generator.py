import os
binusian, email, class_id, link = "","","",""
while True:
    os.system("cls")
    inp = input("SCORE DETAILS CREATOR\n[0] ADD\n[1] VIEW\n[OTHER]EXIT\nINPUT = ")
    if inp == "0":
        f = open("index.html","r")
        data = f.read().split("<!--SPLIT-->")
        details = int(data[1].split("\n")[2]) + 1
        f.close()
        while True:
            print("NO            : "+str(details))
            binusian     = input("BINUSIAN ID   : ")
            email        = input("EMAIL         : ")
            class_id     = input("CLASS(A|B|C)  : ")
            link         = input("LINK          : ")
            ok = input("CHECK(Y|N)")
            if ok in ["y","yes","Y","YES"] : break
        s = open("index.html","w")
        s.write(data[0])
        s.write("<tr>\n\t<td>"+str(details)+"</td>")
        s.write("\n\t<td>"+binusian+"</td>")
        s.write("\n\t<td>"+email+"</td>")
        s.write("\n\t<td>B2"+class_id+"C</td>")
        s.write("\n\t<td><a href=\""+link+"\">CLICK HERE</a></td>")
        s.write("\n</tr>\n")
        s.write("<!--SPLIT-->\n<!--\n"+ str(details) +"\n-->\n<!--SPLIT-->")
        s.write(data[2])
        s.close()
    elif inp == "1":
        os.system("index.html")
    else:
        break
os.system("cls")
 


