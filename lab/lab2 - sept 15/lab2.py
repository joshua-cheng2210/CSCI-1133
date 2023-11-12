num = int(input("Enter a 4 digit number: ")) #missing a closing bracket
ones = num % 10 # unessesary quotations
print("Ones digit is", ones) #missing quotations
tens = (num // 10) % 10 #assignment error
print("Tens digit is", tens) #missing brackets
hunds = (num // 100) % 10 #formula error
print("Hundreds digit is", hunds) # missing variable, "hunds"
thous = (num // 1000) % 10 # formula error
print("Thousands digit is", thous) #missing print
rev = 1000*ones+100 *tens+10*hunds+thous #concatinating error
print("Original number reversed is", rev) # missing the variable "rev"
