def binSum(a,b,length_of_AC):
    sum = bin(int(a,2)+int(b,2))#binary sum hua yahan abhi (python wala binary aka "0b" wali kabwass)
    sum = int(sum,2) #binary ko decimal me convert krdia.
    alpha = "{0:b}".format(sum) # normal human-ic binary me kar dia 
    

    #now we are dealing with overflow
    #now ye kr rahe hai ki say output = 10 bits ka hai 
    #but length of ac ( = length of reister)... pata nhi ho gaya deal . extra bit ko ignore kr dia 

    if len(alpha) > length_of_AC:
        x = len(alpha) - length_of_AC
        beta = alpha[x:]
        return beta
    
    #we have dealt with overflow

    # ye just in case agar hamara sum ki length less than AC hai 
    # toh sum ke peeche "0"(zero) laga do taaki woh equal to
    # length of  AC ho jaye
    if len(alpha) < length_of_AC:
        x = length_of_AC - len(alpha)
        beta = "0"*x + alpha
        return beta
    #end of above if


    # ye normal hai maanlo dono me se koi "if" nahi chala 
    #mtlb ki length of output == length of AC

    if len(alpha)==length_of_AC:
        return alpha # this is only when len(alpha) == length_of_ac . 
        #mtlb no of reg bits ke barbar hai 

def ASR(AC,Q,Q_pika):
    str1 = AC+Q+Q_pika
    new_st = AC[0]+str1[0:len(str1)-1]
    return new_st


def oneComp(number_in_str):
    updated_num = ""
    for i in range(len(number_in_str)):
        if number_in_str[i]=="0":
            updated_num+="1"
        else:
            updated_num+="0"

    return updated_num

def twoComp(number_in_str):
    x = oneComp(number_in_str)
    alpha = int(x,2) #converts x(jo binary me tha) to decimal/integer
    alpha = alpha +1 # adding 1 to the one's complimenet

    beta = "{0:b}".format(alpha)
    return beta


def dectoBin(number,reg_bits):
    alpha = "{0:b}".format(int(number))

    if len(alpha)< reg_bits:
        beta = alpha.zfill(reg_bits)
        return beta

counter_for_a_negative_number = 0
input1 = 0


reg_bits = int(input("enter no of reg bits  "))

checkpoint1 = input("is your first number positive? (Y/N) ")
if checkpoint1 =="Y":
    no1 = input("enter first +ve decimal +ve(M) number  ") #number input lia
    x1 = dectoBin(no1,reg_bits)
    input1 = x1
    print("first numb in binary",x1)

    #decimal to binary with 
    #length equal to "NO OF REGISTER BITS"
else:
    no1 = input("enter first -ve decimal (M) number  ") #number input lia
    temp = int(no1)*-1 # input ko positive kr dia
    neg_binary = dectoBin(temp,reg_bits) #ye krne se lets se 
    # -5 tha mere paas . toh mene abhi usko "5" bana dia
    #then uska binary = 101 kra dia
    #and maybe zfill se equal to no of reg bits ke equal bit kr dia 

    neg_binary_2comp = twoComp(neg_binary)
    print("first number in binary ",neg_binary_2comp)
    input1 = neg_binary_2comp
    x1 =input1

    counter_for_a_negative_number +=1


# """ Q = input2"""
#therefore 
Q = 0

checkpoint2 = input("is your second number positive? (Y/N) ")
if checkpoint2 =="Y":    
    no2 = input("enter second +ve decimal(Q) number  ")
    x2 = dectoBin(no2,reg_bits)
    print("second number in binary ",x2)
    Q = x2
else:
    no2 = input("enter second-ve decimal(Q) number  ")
    temp = int(no2) *-1
    neg_binary = dectoBin(temp,reg_bits)
    neg_binary_2comp = twoComp(neg_binary)
    print("second numb in binary",neg_binary_2comp)
    Q = neg_binary_2comp
    counter_for_a_negative_number+=1

#now INPUT3 is the 2's comp of first input.
input3 = twoComp(x1)
no_of_reg_bits  = reg_bits
AC = "0"*no_of_reg_bits
Q_pika = "0" # meaning (Q-1)
new_str="" #empty string 

for i in range(1,no_of_reg_bits+1):
    print(" \n ")
    print("step ",i)
    if Q[-1]+Q_pika == "10":

        print("--------------------------------------------------------------------------------------------------------")


        x = binSum(AC,input3,no_of_reg_bits) #sum of AC and "-M" .. input3 = -M
        AC = x #AC = AC+(-M)
        print("Operation performed : AC = AC + (-M)")
        print("AC = " + AC)

        #now we'll do ASR
        print("Operation perfomed : Arithmetic Right Shift")
        new_str = ASR(AC,Q,Q_pika) # new_str me new_str poora concatenate hoke aaya hai 
        print("AC+Q+(Q-) = "+ new_str +"                           (String concatenated and printed for reference only)")


        AC = new_str[:no_of_reg_bits] 
        Q=new_str[no_of_reg_bits:no_of_reg_bits+no_of_reg_bits]
        Q_pika = new_str[-1]

        print("AC = " + AC)
        print("Q = " + Q)
        print("(Q-) = " + Q_pika)

        print("--------------------------------------------------------------------------------------------------------")

    elif Q[-1]+Q_pika=="01":

        print("--------------------------------------------------------------------------------------------------------")


        x = binSum(AC,input1,no_of_reg_bits) #sum of AC and"+M" ...input1 is my "+M"
        AC=x # AC = AC+M
        print("Operation performed : AC = AC +M ")
        
        print("AC = " + AC)

        #now we'll do ASR
        new_str = ASR(AC,Q,Q_pika)
        print("Operation perfomed : Arithmetic Right Shift")
        print("AC+Q+(Q-) = "+ new_str +"                           (String concatenated and printed for reference only)")

        AC = new_str[:no_of_reg_bits]
        Q =new_str[no_of_reg_bits:no_of_reg_bits+no_of_reg_bits]
        Q_pika = new_str[-1]

        print("AC = " + AC)
        print("Q = " + Q)
        print("(Q-) = " + Q_pika)


        print("--------------------------------------------------------------------------------------------------------")


    else: # if "00" or "11" hua toh 
    
        print("--------------------------------------------------------------------------------------------------------")


        #here now we'll do only ASR
        print("Operation perfomed : Arithmetic Right Shift")
        new_str = ASR(AC,Q,Q_pika)
        print("AC = " + AC)
        print("AC+Q+(Q-) = "+ new_str +"                           (String concatenated and printed for reference only)")

        AC = new_str[:no_of_reg_bits]
        Q =new_str[no_of_reg_bits:no_of_reg_bits+no_of_reg_bits]
        Q_pika = new_str[-1]

        print("AC = " + AC)
        print("Q = " + Q)
        print("(Q-) = " + Q_pika)


        print("--------------------------------------------------------------------------------------------------------")



if (counter_for_a_negative_number == 1): # meaning ki ek number negative tha(dono number me se) toh ans negtive me aya hoga na 

    print("final ans in binary is " + (AC+Q))
    output = twoComp(AC+Q)
    fin_output = int(output,2)
    finaloutput = fin_output*-1
    print("final ans in decimal is " , finaloutput)
else:
    print("final ans in binary is " + (AC +Q))
    omega = int(AC+Q,2)
    print("final ans in decimal is "+ str(omega))
