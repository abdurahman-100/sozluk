word = input("Anlamadığınız bir kelime yazın (hepsini büyük harflerle yazın!):")

meme_dict = {
            "LOL" : "komik bir şeye verilen cevap",
            "CRINGE" : "garip ya da utandırıcı bir şey",
            "ROFL" : "bir şakaya karşılık cevap",
            "SHEESH" : "onaylamamak",
            "CREEPY" : "korkunç",
            "AGGRO" :"agresifleşmek/sinirlenmek"
            }


if word in meme_dict:
    print(meme_dict[word])
else:
    print("böle birşey bulunamamaktadır")
