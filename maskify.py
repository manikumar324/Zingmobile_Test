def maskify(number):
    masked_number="#"*(len(number)-3)+number[-3:]
    print(masked_number)
maskify("6302585352")