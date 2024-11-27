import os


while True:
    # lista dei file presenti nella cartella NetworksDefaultTypes
    files = os.listdir("NetworksDefaultTypes")
    print("Lista dei file presenti nella cartella NetworksDefaultTypes:")
    for i in range(len(files)):
        print(str(i) + " - " + files[i])

    # chiedo all'utente quale file vuole runnare
    index = int(input("Quale rete si vuole creare? "))
    os.system("python NetworksDefaultTypes/" + files[index])
