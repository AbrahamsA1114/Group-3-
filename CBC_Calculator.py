def request():
    gender = input("Enter Gender:")
    rbc_count = input("Enter Red Blood Cell Count:")
    (RBC(rbc_count, gender))
    wbc_count = input("Enter White Blood Cell Count:")
    (WBC(wbc_count, gender))
    plt_count = input("Enter Platelets Count:")
    (PLT(plt_count, gender))
    hct_count = input("Enter Hematocrit Count:")
    (HCT(hct_count, gender))
    hgb_count = input("Enter Hemoglobin Count:")
    (HGB(hgb_count, gender))


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
        print("WBC Count = High")
    elif(str(gender)=="male" and float(wbc_count)<3.6):
        print("WBC Count = Low/Leukopenia")
    elif (str(gender)=="female" and float(wbc_count)>=3.6 and float(wbc_count)<=10.6):
        print("WBC Count = Normal")
    elif (str(gender)== "female" and float(wbc_count)>10.6):
        print ("WBC Count = High")
    elif (str(gender)== "female" and float(wbc_count)<3.6):
        print("WBC Count = Low")

def PLT (plt_count , gender):
    if (str (gender)== "male"  and float(plt_count)>=150 and float(plt_count)<=450):
        print("PLT Count = Normal")
    elif (str(gender)=="male" and float(plt_count)>450):
        print("PLT Count = High")
    elif (str(gender)== "male" and float(plt_count)<150):
        print("PLT Count = Low")
    elif (str(gender)== "female" and float(plt_count)>=150 and float(plt_count)<=450):
        print("PLT Count = Normal")
    elif (str(gender)== "female" and float(plt_count)>450):
        print("PLT Count = High")
    elif (str(gender)== "female" and float(plt_count)<150):
        print("PLT Count = Low")


def HCT(hct_count, gender):
    if(str(gender)=="male" and float(hct_count)>=0.40 and float(hct_count)<=0.54):
        print("HCT Count = Normal")
    elif(str(gender)=="male" and float(hct_count)<0.40):
        print("HCT Count = Low/Anemia")
    elif(str(gender)=="male" and float(hct_count)>0.54):
        print("HCT Count = High/Polycythemia")
    elif(str(gender)=="female" and float(hct_count)>=0.35 and float(hct_count)<=0.49):
        print("HCT Count = Normal")
    elif(str(gender)=="female" and float(hct_count)<0.35):
        print("HCT Count = Low/Anemia")
    elif(str(gender)=="female" and float(hct_count)>0.49):
        print("HCT Count = High/Polycythemia")

def HGB(hgb_count, gender):
    if(str(gender)=="male" and float(hgb_count)>=135 and float(hgb_count)<180):
        print("HGB Count = Normal")
    elif(str(gender)=="male" and float(hgb_count)<135):
        print("HGB Count = Low/Anemia")
    elif(str(gender)=="male" and float(hgb_count)>180):
        print("HGB Count = High/Polycythemia")
    elif(str(gender)=="female" and float(hgb_count)>=120 and float(hgb_count)<=150):
        print("HGB Count = Normal")
    elif(str(gender)=="female" and float(hgb_count)<120):
        print("HGB Count = Low/Anemia")
    elif(str(gender)=="female" and float(hgb_count)>150):
        print("HGB Count = High/Polycythemia")



request()