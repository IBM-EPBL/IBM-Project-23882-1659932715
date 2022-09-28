
import random
while(True):
    temp=random.randrange(0,100)
    humid=random.randrange(0,100)
    if (temp>90 or temp<80) and humid>60:
        print("Alert, Please Make Precautions")
    else:
	  print("safe with extra water bodies")
