def strTobin(input_string):
    res = ''.join(format(ord(i), '08b') for i in input_string)
    return res


def binTostr(input_string):
    input_string=int(input_string, 2);
 
    #Obtain the total number of bytes
    Total_bytes= (input_string.bit_length() +7) // 8
    
    #Convert these bits to bytes
    input_array = input_string.to_bytes(Total_bytes, "big")
    
    #Convert the bytes to an ASCII value and display it on the output screen
    ASCII_value=input_array.decode()
    return ASCII_value

def server():
    
    if __name__=="__main__":
    # print(binTostr("0100100001100101011011000110110001101111"))
    # str = input("Enter message : ");
    # print(str)
    # str = strTobin(str)
    # print(str)
    # str = binTostr(str)
    # print(str)