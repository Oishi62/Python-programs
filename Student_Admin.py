import csv

def write_into_csv(info_list):
    with open("student_info.csv","a",newline="") as csv_file:
        writer=csv.writer(csv_file)
        if (csv_file.tell()==0): # Signifies whether the csv file is empty or not
            writer.writerow(["Name","Age","Contact Number","Email ID"])
        writer.writerow(info_list)

condition=True
student_num=1
while(condition):
    student_info=input("Enter some student information for student {} in the following format (Name Age Contact_No Email_ID) ".format(student_num))
    student_info_list=student_info.split(" ")
    write_into_csv(student_info_list)
    condition_check=input("Do you want to input details of another student (yes/no) ")
    if(condition_check=='yes'):
        condition=True
        student_num=student_num+1
    else:
        condition=False
