def request():
    gender = input("Enter Gender:")
    rbc_count = input("Enter Red Blood Cell Count:")
    (RBC(rbc_count, gender))
    wbc_count = input("Enter White Blood Cell Count:")
    plt_count = input("Enter Platelets Count:")
    hct_count = input("Enter Hematocrit Count:")
    hgb_count = input("Enter Hemoglobin Count:")




def RBC(rbc_count, gender):
    if (str (gender) == "Male" and float(rbc_count)>=4.2 and float(rbc_count)<=6.0):
        print ("RBC Count= Normal")
    elif(str(gender)== "Male" and float(rbc_count)<4.2):
        print("RBC Count= Low/Anemia")
    elif(str(gender)== "Male" and float(rbc_count)>6.0):
        print ("RBC Count= High/Polycythemia")




request()