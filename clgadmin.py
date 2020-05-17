import csv

def csv_writer(info_list):
    with open('student_information.csv','a', newline='')as csv_file:
        writer=csv.writer(csv_file)

        if csv_file.tell()==0 :
            writer.writerow(["NAME","AGE","PHONE NO.","EMAIL-ID"])
        writer.writerow(info_list)
if __name__ == '__main__':
    condition=True
    entry_no=1
    while(condition):
        print("format:name age phone_no email-id")
        input_info=input("enter the details of the student #{} ".format(entry_no))
        ip_info_list=input_info.split(' ')
        print("entered information is: \nNAME= {}\nAGE= {}\nPHONE NO.= {}\nEMAIL-ID= {}".format(ip_info_list[0],ip_info_list[1],ip_info_list[2],ip_info_list[3]))
        check = input("do u wish to continue with above entry (yes/no)")
        if check=="yes":
            csv_writer(ip_info_list)
            entry_no+=1
            condition_check=input("do you want to make another entry (yes/no)")
            if condition_check=="yes":
                condition=True
            elif condition_check=="no":
                condition=False
        elif check=="no":

            print("please re-enter the details agian")
            condition=True
