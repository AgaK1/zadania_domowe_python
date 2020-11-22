#1.
print("Hello World!")

#2
name = "Aga"
print("Hello " + name)

#3
nickname = "Aga"
cd = 20
new_cd = 5
print("Hej, " + nickname)
print("Masz " + str(cd) + " płyt.")
print("Ostatnio kupiłaś " + str(new_cd) + " nowych.")

#4
marka = "Kia"
m = marka.upper()
print(m)

n = marka.lower()
print(n)

#5
name1 = "Ala"
animal = "kot"
count = int(input())

if count == 1:
    print('{0} ma {1}a'.format(name1, animal))
elif count <= 4:
    print('{0} ma {1} {2}y'.format(name1, count, animal))
else:
    print("Za duzo kotow")

#6
music = ["rock", "metal", "kpop", "classic", "posthardcore"]
for m in music:
    print(m)

for idx in range(len(music)):
    print("idx: " + str(idx) + " : " + music[idx])
print(music[3])
print(",".join(music))
del music[2]
print(music)
