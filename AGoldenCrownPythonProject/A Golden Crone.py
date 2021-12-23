#Kingdoms and Emblems Dictonary
kingdoms_and_Emblems_dict = {"LAND" : "PANDA", "AIR" :"OWL", "WATER" : "OCTOPUS","FIRE":"DRAGON","ICE":"MAMMOTH"}

#Message Wheel
wheel = []
for i in range(65 , 91):
    wheel.append(chr(i)) 
message_sended_kingdomes_list = "SPACE " 

#Reading Number of Inputs
number_of_input=[]
while(True):
        try:
            a=input()
        except Exception as e:
            break
        number_of_input.append(a)
for each in number_of_input:
    input_list = each.split()
    ruler_list = input_list[0]
    ruler = ruler_list.upper()
    emblem_list = ''
    for word in input_list[1:]:
        emblem_list += word
        emblem = emblem_list.upper()
    #Decrypted message Letters List 
    decrypt_msg_letter_list = []
    
    three_rulers_match_or_not = []
    #King Own By Send Message to 3 kingdomes that condition
    if (len(number_of_input) < 3):
        print("NONE")
    else:
        for each in emblem:
           ruler_length = len(kingdoms_and_Emblems_dict[ruler])
           decrypt_msg_letter_list.append(wheel[wheel.index(each) - ruler_length])
        #Checking Wether Decrypted Letters in  given message
        for each in kingdoms_and_Emblems_dict[ruler]:
            if (each in decrypt_msg_letter_list):
                three_rulers_match_or_not.append("Yes")
            else:
                three_rulers_match_or_not.append("No")
        if ("No" in three_rulers_match_or_not):
            message_sended_kingdomes_list += ''
        else: 
            message_sended_kingdomes_list += ruler + " "

kindoms_length = len(message_sended_kingdomes_list.split())
#King Own By Send Message to 3 kingdomes that condition
if (kindoms_length <= 3):
    print("NONE")
else:
    print(message_sended_kingdomes_list)