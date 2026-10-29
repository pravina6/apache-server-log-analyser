
import os
import csv

ip = []
http_status = []

path = "C:\\Users\\USER\\OneDrive\\Desktop\\apache_server_log_analyser"
filename = "mylog.log"


## opening file and read line by line and split it 
with open(os.path.join(path, filename)) as f:
    for each_line in f:
        mylist = each_line.split(" ")

        ip.append(mylist[0])
        http_status.append(mylist[8])
    
    print(http_status)
    # print(ip)

# frequency 
def frequency(mylist):
    mydict = {}

    for each in mylist:
        if each not in mydict:
            mydict[each] = 1
        else:
            mydict[each] += 1

    return mydict

#print(frequency(http_status))
#print(frequency(ip))

# converting to csv file 
def write_to_csv(mydict, filename):
    with open(os.path.join(path, filename), "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["Sno", "Value", "Frequency"])

        Sno = 1
        for each in mydict:
            writer.writerow([Sno, each, mydict[each]])
            Sno += 1

rest1 = frequency(ip)
rest2 = frequency(http_status)

write_to_csv(rest1, "ip_frequency.csv")
write_to_csv(rest2, "http_status_frequency.csv")

print("CSV files created successfully")
