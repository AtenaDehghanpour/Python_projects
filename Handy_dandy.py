username = input("lotfan shomare daneshjoei khod ra vared konid:")
while username != ("1401230012"):
    print("shomare daneshjoei mord nazar yaft nashod!")
    username = input("lotfan shomare daneshjoei khod ra vared konid:")
print("shomare daneshjoei 'Atena Dehghanpour' yaft shod")
password = input("lotfan ramz obor khod ra vared konid:")
while password != ("0110491807"):
    print("ramz obor vared shode ghalat mibashad!")
    password = input("lotfan ramz obor khod ra vared konid")
print("ramz obor vared shode sahih mibashad")
print("khosh omadid")
emtiaz_player1 = 0
emtiaz_player2 = 0
while True :
    player_1 = input("lotfan entekhab konid : chap ya rast ?")
    player_1 = str.lower(player_1)
    if player_1 == "chap":
        print("player_1 : chap")
    elif player_1 == "rast":
        print("player_1 : rast ")
    else:
        print("entekhab shoma ghalat mibashad")
        player_1 = input("lotfan entekhab konid : chap ya rast ?")
    
    import random as rn
    randint = rn.randint(1 , 3)
    player_2 = randint
    if player_2 == 1:
        print("player_2 : chap")
    if player_2 ==2:
        print("player_2 : rast ")
    if player_1 == "chap" and player_2 == 1:
        print("barande : player_1")
        emtiaz_player1 += 1
        print("emtiaz_player1 =",emtiaz_player1)
        print("emtiaz_player2 =",emtiaz_player2)
    elif player_1 == "chap" and player_2 == 2 :
        print("barande : player_2")
        emtiaz_player2 += 1
        print("emtiaz_player1 =",emtiaz_player1)
        print("emtiaz_player2 =",emtiaz_player2)
    elif player_1 == "rast" and player_2 == 1 :
        print("barande : player_2")
        emtiaz_player2 += 1
        print("emtiaz_player1 =",emtiaz_player1)
        print("emtiaz_player2 =",emtiaz_player2)
    elif player_1 == "rast" and player_2 == 2 :
        print("barande : player_1")
        emtiaz_player1 += 1
        print("emtiaz_player1 =",emtiaz_player1)
        print("emtiaz_player2 =",emtiaz_player2)
    if emtiaz_player1 == 3 :
        print("VICTORY")
        break
    if emtiaz_player2 == 3 :
        print("GAME OVER")
        break