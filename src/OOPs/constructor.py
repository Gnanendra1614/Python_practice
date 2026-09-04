class School:
    schl_name='KES'
    schl_loc="MPL"
    schl_principal="ABC"
    def __init__(self,stname,stage,stc):
        self.stname=stname
        self.stage=stage
        self.stc=stc
school1=School("Gnanendra",22,10)
print("School Name:", school1.schl_name)
print("School Location:", school1.schl_loc)
print("Principal:", school1.schl_principal)
print("Student Name:", school1.stname)
print("Student Age:", school1.stage)
print("Student Class:", school1.stc)