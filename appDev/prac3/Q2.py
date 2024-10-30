while True:
    name = input('Enter name: ')
    weight = float(input('Enter weight (kg): '))
    height = float(input('Enter height(m): '))

    bmi = weight/height**2
    print(bmi)

    command = input('Store your bmi to file? (Y/N): ')
    if command.upper() == 'Y':
        bmi_File = open('bmi.txt', 'w')
        bmi_File.write(name+','+ str(bmi) +'\n')
        bmi_File.close()
      
    command = input('Do you want to continue? (Y/N): ')
    if command.upper() == 'N':
        command = input('Do you want view BMI record in file? (Y/N): ')
        if command.upper() == 'Y':
            bmi_File = open('bmi.txt', 'r')
            contents = bmi_File.read()
            print(contents)
            bmi_File.close()
            break
    
        

