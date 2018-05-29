def shoelace (tightness):
    if tightness==1:
        return "The tightness of your shoelaces is one"
    elif tightness==2:
        return "The tightness of your shoelaces is two"
    elif tightness==3:
        return "The tightness of your shoelaces is three"
    elif tightness==4:
        return "The tightness of your shoelaces is four"
    elif tightness==5:
        return "The tightness of your shoelaces is five"
    elif tightness==6:
        return "The tightness of your shoelaces is six"
    elif tightness==7:
        return "The tightness of your shoelaces is seven"
    elif tightness==8:
        return "The tightness of your shoeslaces is eight"
    elif tightness==9:
        return "The tightness of your shoelaces is nine"
    elif tightness==10:
        return "The tightness of your shoelaces is ten"
    else:
        return "Please put in a number from 1 to 10"
print(shoelace(int(input("From a scale of 1 to 10, how would you want the tightness of your shoes to be?"))))