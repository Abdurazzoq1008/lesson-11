cars = ['totoya', 'Mazda', 'hyundai', 'gm', 'kia']
for car in cars:
    if car != '':
        print(car.capitalize())

while True:
    buyruq1 = input('Login: ')
    if buyruq1 == "Abdurazzoq":
         yosh = int(input('Parolni kiriting: '))
    # else:
    #     print("Noto'g'ri login kiritildi. Loginni qayta kiriting.")
    else:
          buyruq = ["stop"]
          davom = input("Noto'g'ri login kiritildi. Loginni qayta kiriting.")
          if davom.lower() == buyruq[0]:
               break

    while True:
           if yosh == 5078:
              print("xush kelibsiz!")
           else:
             buyruq = ["stop"]
             davom = input("Noto'g'ri parol kiritildi.Parolni qayta kiritiing. ")
             if davom.lower() == buyruq[0]:
                               break