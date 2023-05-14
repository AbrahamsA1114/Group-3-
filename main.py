def request():
    gender = input("Enter Gender:")
    rbc_count = input("Enter Red Blood Cell Count:")
    (RBC(rbc_count, gender))
    wbc_count = input("Enter White Blood Cell Count:")
    (WBC(wbc_count, gender))
    plt_count = input("Enter Platelets Count:")
    (PLT(plt_count, gender))
    hct_count = input("Enter Hematocrit Count:")
    hgb_count = input("Enter Hemoglobin Count:")


def RBC(rbc_count, gender):
    if (str (gender) == "male" and float(rbc_count)>=4.2 and float(rbc_count)<=6.0):
        print ("RBC Count= Normal")
    elif(str(gender)== "male" and float(rbc_count)<4.2):
        print("RBC Count= Low/Anemia")
    elif(str(gender)== "male" and float(rbc_count)>6.0):
        print ("RBC Count= High/Polycythemia")
    elif (str (gender) == "female" and float(rbc_count)>=3.8 and float(rbc_count)<=5.2):
        print ("RBC Count= Normal")
    elif(str(gender)== "female" and float(rbc_count)<3.8):
        print("RBC Count= Low/Anemia")
    elif(str(gender)== "female" and float(rbc_count)>5.2):
        print ("RBC Count= High/Polycythemia")

def WBC (wbc_count, gender):
    if (str(gender)== "male" and float(wbc_count)>=3.6 and float(wbc_count)<=10.6):
        print("WBC Count = Normal")
    elif (str(gender)== "male" and float(wbc_count)>10.6):
        print("WBC Count = High/Leukocytosis")
    elif(str(gender)=="male" and float(wbc_count)<3.6):
        print("WBC Count = Low/Leukopenia")
    elif (str(gender)=="female" and float(wbc_count)>=3.6 and float(wbc_count)<=10.6):
        print("WBC Count = Normal")
    elif (str(gender)== "female" and float(wbc_count)>10.6):
        print ("WBC Count = High/Leukocytosis")
    elif (str(gender)== "female" and float(wbc_count)<3.6):
        print("WBC Count = Low/Leukopenia")

def PLT (plt_count , gender):
    if (str (gender)== "male"  and float(plt_count)>=150 and float(plt_count)<=450):
        print("PLT Count = Normal")
    elif (str(gender)=="male" and float(plt_count)>450):
        print("PLT Count = High/Thrombocytosis")
    elif (str(gender)== "male" and float(plt_count)<150):
        print("PLT Count = Low/Thrombocytopenia")
    elif (str(gender)== "female" and float(plt_count)>=150 and float(plt_count)<=450):
        print("PLT Count = Normal")
    elif (str(gender)== "female" and float(plt_count)>450):
        print("PLT Count = High/Thrombocytosis")
    elif (str(gender)== "female" and float(plt_count)<150):
        print("PLT Count = Low/Thrombocytopenia")
request()



