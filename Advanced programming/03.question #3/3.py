words = ['red', 'green', 'black', 'pink', 'black', 'white', 'black', 'eyes', 'white', 'black', 'orange', 'pink', 'pink', 'red', 'red', 'white', 'orange', 'white', "black", 'pink', 'green', 'green', 'pink', 'green', 'pink', 'white', 'orange', "orange", 'red'  ]
red,green,black,pink,white,eyes,orange = 0,0,0,0,0,0,0
for i in words:
    if i == 'red':
        red = red + 1
    if i == 'green':
        green = green + 1
    if i == 'black':
        black = black + 1
    if i == 'pink':
        pink = pink + 1
    if i == 'white':
        white = white + 1
    if i == 'eyes':
        eyes = eyes + 1
    if i == 'orange':
        orange = orange + 1
a  =  {}
a['red'] = red
a['green'] = green
a['black'] = black
a['pink'] = pink
a['white'] = white
a['eyes'] = eyes
a['orange'] = orange
for key,value in a.items():
    print(key,value)
print("****************************")
max = 0
min = 10000
key = ''
for key,value in a.items():
    if value >= max:
        max = value
        key1 = key
print("max : ",key1, "=>", "Repeated" , max , "time.")
for key,value in a.items():
    if value <= min:
        min = value
        key1 = key
print("min : " , key1,"=>","Repeated",min, "time.")

