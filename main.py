# 1 - Pərakəndə:
# Məhsulun adı və qiyməti üçün istifadəçidən məlumat alan, sonra detalları formatlaşdırılmış şəkildə çap edən Python proqramı yazın. Proqram 6 dəfə məlumat almalıdır.


product_list=[]

for x in range(6):
    name=input("Mehsulun adinin daxil edin :")
    price=int(input("Mehsulun qimetini daxil edin :"))
    product={
        "name":name,
        "price":price,
    }
    product_list.append(product)
print(product_list)


# 2 - Maliyyə:
# Səhm portfelinin ümumi dəyərini hesablayan Python proqramı yaradın. Proqram sahib olduğu səhmlərin sayı və onların müvafiq qiymətləri ilə bağlı məlumatları qəbul etməli, sonra ümumi dəyəri çıxarmalıdır. Proqram 3 dəfə məlumat almalıdır.

stock_list=[]

for x in range(3):
    number=int(input("Sehmin sayini daxil edin :"))
    price=int(input("Sehmin qimetini daxil edin :"))
    worth=number*price
    stock={
        "number":number,
        "price":price,
        "worth":worth
    }
    stock_list.append(stock)
print(stock_list)


# 3 - Səhiyyə:
# Xəstə adı və yaşı üçün istifadəçidən məlumat alan, sonra detalları formatlaşdırılmış şəkildə çap edən Python proqramı yazın. Proqram 5 dəfə məlumat almalıdır.

patients_list=[]

for x in range(5):
    name=input("Xestenin adinin daxil edin :")
    age=int(input("Xestenin yasini daxil edin :"))
    patients={
        "name":name,
        "age":age,
    }
    patients_list.append(patients)
print(patients_list)


# 4 - Təhsil :
# Tələbə adı və yaşı üçün istifadəçidən məlumat alan, sonra detalları formatlaşdırılmış şəkildə çap edən Python proqramı yazın. Proqram 8 dəfə məlumat almalıdır.


stundets_list=[]

for x in range(2):
    name=input("Telebenin adinin daxil edin :")
    age=int(input("Telebenin yasini daxil edin :"))
    student={
        "name":name,
        "age":age,
    }
    stundets_list.append(student)
print(stundets_list)



# 5 - Restoran:
# Qida məhsullarının adı və qiyməti üçün istifadəçidən məlumat alan, sonra detalları formatlaşdırılmış şəkildə çap edən Python proqramı yazın. Proqram 4 dəfə məlumat almalıdır.


menu_list=[]

for x in range(4):
    name=input("Mehsulun adinin daxil edin :")
    price=int(input("Mehsulun qimetini daxil edin :"))
    product={
        "name":name,
        "price":price,
    }
    menu_list.append(product)
print(menu_list)


# 6 - Texnologiya:
# Proqram tərtibatçılarının adı, yaşı və istifadə etdiyi proqram dili üçün istifadəçidən məlumat alan, sonra detalları formatlaşdırılmış şəkildə çap edən Python proqramı yazın. Proqram 4 dəfə məlumat almalıdır.


developers_list=[]

for x in range(4):
    name=input("Adinizi daxil edin :")
    age=input("Yasinizi daxil edin :")
    program_lang=input("Isletdiyiniz Program dilini daxil edin :")
    developer={
        "name":name,
        "age":age,
        "program_lang":program_lang,
    }
    developers_list.append(developer)
print(developers_list)


# 7 - Nəqliyyat:
# Qət olunmuş məsafəyə və alınan vaxta əsasən avtomobilin orta sürətini hesablayan Python proqramı yaradın. İstifadəçini daxil etməyi təklif edin və hesablanmış orta sürəti göstərin.




distance=int(input("Qet olunmus mesafeni daxil edin :"))
time=int(input("Getdiyiniz vaxti daxil edin :"))
speed=distance/time
transportation={
        "distance":distance,
        "time":time,
        'speed':speed,
    }

print(transportation)




# 8 - Əyləncə:
# Filmlərin adı və istehsal tarixi üçün istifadəçidən məlumat alan, sonra detalları formatlaşdırılmış şəkildə çap edən Python proqramı yazın. Proqram 4 dəfə məlumat almalıdır.



movies_list=[]

for x in range(4):
    name=input("Filmin adinin daxil edin :")
    date=input("Filmin cixma tarixini daxil edin :")
    movie={
        "name":name,
        "date":date,
    }
    movies_list.append(movie)
print(movies_list)


# 9 - Daşınmaz Əmlak:
# Evin kvadratı sahəsi və qiyməti üçün istifadəçidən məlumat alan, sonra detalları formatlaşdırılmış şəkildə çap edən Python proqramı yazın. Proqram 4 dəfə məlumat almalıdır.


houses_list=[]

for x in range(4):
    squera=input("Evin nece kvadrat metr oldugunu daxil edin :")
    price=input("Evin qiymetini daxil edin :")
    home={
        "squera":squera,
        "price":price,
    }
    houses_list.append(home)
print(houses_list)



# 10 - Elektron ticarət:
# Məhsulun adı və qiyməti üçün istifadəçidən məlumat alan, sonra detalları formatlaşdırılmış şəkildə çap edən Python proqramı yazın. Proqram 7 dəfə məlumat almalıdır.


shoppig_list=[]

for x in range(7):
    name=input("Mehsulun daxil edin :")
    price=input("Mehsulun qiymeti daxil edin :")
    product={
        "name":name,
        "price":price,
    }
    shopping_list.append(product)
print(shoppig_list)


# 11 - Kənd Təsərrüfatı:
# Tərəvəzin adı və qiyməti üçün istifadəçidən məlumat alan, sonra detalları formatlaşdırılmış şəkildə çap edən Python proqramı yazın. Proqram 2 dəfə məlumat almalıdır.


agriculture_list=[]
for x in range(2):
    name=input("Terevezin adin daxil edin :")
    price=input("Terevezin qiymetini daxil edin :")
    vegetablet={
        "name":name,
        "price":price,
    }
    agriculture_list.append(vegetable)
print(agriculture_list)




# 12 - Telekommunikasiya:
# Telefonun adı və qiyməti üçün istifadəçidən məlumat alan, sonra detalları formatlaşdırılmış şəkildə çap edən Python proqramı yazın. Proqram 6 dəfə məlumat almalıdır.


phones_list=[]
for x in range(6):
    name=input("Telefonun adin daxil edin :")
    price=input("Telefonun qiymetini daxil edin :")
    phone={
        "name":name,
        "price":price,
    }
    phones_list.append(phone)
print(phones_list)



# 13 - Səyahət Sənayesi:
# Aviabilet, otel və avtomobil icarəsi daxil olmaqla səyahətin ümumi dəyərini hesablayan Python proqramı yazın. Proqram hər bir xərc üçün məlumatı götürməli və ümumi dəyəri çap etməlidir.


plane_ticket=int(input("Ucus qiymetini daxil edin :"))
hotel=int(input("Otelin qiymetini daxil edin :"))
rent_car=int(input("Avtomobil icare qiymetini daxil edin :"))
total_worth=plane_ticket+hotel+rent_car
travel={
        "plane_ticket":plane_ticket,
        "hotel":hotel,
        "rent_car":rent_car,
        "total_worth":total_worth
}

print(travel)




# 14 - Tikinti sənayesi:
# Tikinti layihəsi üçün lazım olan materialların ümumi dəyərini hesablayan Python proqramını hazırlayın. Proqram hər bir materialın kəmiyyəti və qiyməti ilə bağlı məlumatları daxil etməli və sonra ümumi dəyəri çap etməlidir. 1 ev üçün taxta , sement, qum və dəmir inputları olacaq



wood=int(input("Taxtanin olcusunu daxil edin:"))
wood_price=int(input("Taxtanin degeri daxil edin:"))
cement=int(input("Sementin cekisini daxil edin :"))
cement_price=int(input("Sementin degeri daxil edin :"))
sand=int(input("Qumun cekisini  daxil edin :"))
sand_price=int(input("Qumun degerini  daxil edin :"))
iron=int(input("Demirin cekisini  daxil edin :"))
iron_price=int(input("Demirin degerini  daxil edin :"))
total_worth=wood_price*wood+cement_price*cement+sand*sand_price+iron*iron
home={
        "wood":wood,
        "cement":cement,
        'sand':sand,
        "iron":iron,
        "total_worth":total_worth,
    }

print(home)
