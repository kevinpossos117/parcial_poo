categorias= []


categorias = int(input("en que categoria se encuentra el libro: 1.(terror) 2.(accion) 3.(fantacia): "))
if categorias == 1:
     print("el libro se añadio a terror")
elif categorias == 2:
    print("el libro se agrego a accion")
elif categorias == 3:
    print("el libro se agrefo a fantacia")
else:
    print("entrada invalida")