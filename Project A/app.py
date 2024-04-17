#module app

#import module
import dev
hasil = dev.getUser(Nama="Budi", Umur="30", Kota="Jakarta")
print(hasil)

#cara lain import module
from dev import getUser
hasil = getUser(Nama="Budi", Umur="30", Kota="Jakarta")
print(hasil)


#cara lain import module
import pkgA.module1

#panggil function di dev
hasil3 = pkgA.module1.getUser(Nama="Budi", Umur="30", Kota="Jakarta")
print(hasil3)



from pkgA.module1 import perkenalan

hasil4 = perkenalan(Nama="Budi", Umur="30", Kota="Jakarta")
print(hasil4)