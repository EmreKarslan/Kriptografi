import hashlib

def md5(fname,sayac):
    hash_md5 = hashlib.md5()
    with open(fname, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    liste.append(hash_md5.hexdigest()[7])
    md5string(hash_md5.hexdigest(),sayac-1)

def md5string(md5str,sayac):
    if(sayac>0):
        hash_md5_2 = hashlib.md5()
        hash_md5_2.update(md5str.encode("utf-8"))
        liste.append(hash_md5_2.hexdigest()[7])
        md5string(hash_md5_2.hexdigest(),sayac-1)
    else:
        str1 = ''.join(liste)
        print("Hexadecimal = ", str1)
        print("Decimal = ", int(str1, 16))


a=input("Kac Basamakli Olcak?")
liste=[]
md5("Deneme.txt",int(a))

