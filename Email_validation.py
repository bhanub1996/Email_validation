from validate_email_address import validate_email
import csv, os


# with open(os.path.join(os.path.dirname(os.path.realpath(__file__)),'1.csv'), encoding="utf-8-sig") as file_obj:
with open(os.path.join(os.getcwd(),'1.csv'), encoding="utf-8-sig") as file_obj:
    reader = csv.reader(file_obj)
    i = 0
    threshold = 5
    lst = []


    for row in reader: 
        
        i = i + 1
        
        isExists = validate_email(row[0], verify=True)
        if isExists == None or isExists == False:
            isExists = validate_email(row[0], verify=True)
            if isExists == None or isExists == False:
                lst.append([i,row[0],False])
            else:
                lst.append([i,row[0],isExists])
        else:
            lst.append([i,row[0],isExists])

        if i == threshold:
            print(lst)
            with open(os.path.join(os.getcwd(),'2.csv'), 'a', encoding="utf-8-sig", newline='') as csvfile: 

                csvwriter = csv.writer(csvfile) 

                csvwriter.writerows(lst)
            
            lst = []
            threshold = threshold+5



            

        



        

    
    




