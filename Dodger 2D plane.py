#pip install libraries pygame and mysql connector before execution
import pygame 
import random  
import mysql.connector as mys  # This module is used to link the databases with game

conn_object = mys.connect(
    host="localhost",      #please change the credentials to the local mySQL server
    user="root",
    passwd="athish22",
    database="game")  # This is the initialisation of connection object
if conn_object.is_connected():
    # This block is to make sure that connection is established
    print("Succesfully connected to database")
    print()


cursor = conn_object.cursor()



def infofetch(a):
    cursor.execute(a)
    b = cursor.fetchone()
    return b


blue = (0, 0, 255)
black = (0, 0, 0)
red = (255, 0, 0)
print("Welcome to Dodger 2D")
print()
r = input("Press P to start the game,else press Enter ")
print()

while r == "P":
    x, y, s, t, o, u, w, z ,xi = 900, 425, 0, 0, 0, 800, 0, 0, 0
    print("Have Fun in playing Dogder 2D")
    print()
    ins = input("To know about instructions press Y,else press enter ")
    print()

    if ins == "Y":
        print(
            "The objective of game is to dodge the obstacles using WASD  keys.")
        print("The obstacles will be moving towards left with some time delay.")
        print("Crossing each obstacle awards you a point.")
        print("To exit game in middle press e")
        print()
    n = input("Lets start the Game,for difficulty Easy press E,Hard press H ")
    print()
    screen = pygame.display.set_mode((800, 800))

    if n == "H":
        t = 3500
    elif n == "E":
        t = 4200
    else:
        z = "over"
        print("Thank You")
        print()

    while z != "over":
        a = random.randrange(0, 100)
        b = random.randrange(100, 200)
        c = random.randrange(200, 300)
        d = random.randrange(400, 500)
        e = random.randrange(500, 600)
        f = random.randrange(600, 700)
        g = random.randrange(700, 800)
        h = random.randrange(800, 900)

        while 3 < x:

            if c - b < 50:
                b -= 25
                c += 25
            elif e - d < 50:
                e += 25
                d -= 25
            elif g - f < 50:
                g += 25
                f -= 25

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_w:
                        if y < 25:
                            z = "over"
                            break
                        else:
                            y -= 25
                    elif event.key == pygame.K_s:
                        if y > 775:
                            z = "over"
                            break
                        else:
                            y += 25
                    elif event.key == pygame.K_a:
                        if xi < 0:
                            z = "over"
                            break
                        else:
                            xi -= 25
                    elif event.key == pygame.K_d:
                        if xi > 750:
                            z = "over"
                            break
                        else:
                            xi += 25
                    elif event.key == pygame.K_e:
                        z = "over"
                        break
            screen.fill(black)
            pygame.draw.rect(screen, red, [xi, y, 50, 50])

            for i in range(t):
                i += 1
            if t > 2500:
                t -= 1
            pygame.draw.line(screen, blue, (x, a), (x, b), 5)
            pygame.draw.line(screen, blue, (x, c), (x, d), 5)
            pygame.draw.line(screen, blue, (x, e), (x, f), 5)
            pygame.draw.line(screen, blue, (x, g), (x, h), 5)
            x -= 1
            pygame.display.update()

            if (
                (
                    (y > a and y < b)
                    or (y > c and y < d)
                    or (y > e and y < f)
                    or (y > g and y < h)
                    or (y + 50 > a and y + 50 < b)
                    or (y + 50 > c and y + 50 < d)
                    or (y + 50 > e and y + 50 < f)
                    or (y + 50 > g and y + 50 < h)
                )
                 and (xi+50>=x and xi<=x)
                or z == "over"
            ):
                z = "over"

                for w in range(0, 801):
                    pygame.draw.line(screen, red, (w, o), (w + 1, o + 1), 5)
                    pygame.draw.line(screen, red, (u, o), (u - 1, o + 1), 5)
                    o += 1
                    u -= 1
                    pygame.display.update()
                print("Better luck next time")
                print()
                break

        else:
            x = 800
            s += 1
    pygame.display.quit()
    print("Your score is ", s)
    print()
    v = input("If you want to store your score press Y,else press enter ")
    print()
  
    if v == "Y":
        nam = input("Enter your alias name ")
        print()
        command1 = "select alias_name from score where alias_name = '{}'".format(
           nam,)
        name = infofetch(command1)
 
        if name is None:
           con = input("The entered alias name is not found in the database,if you want to create new alias name press Y,else press enter ")
           print()
  
           if con == "Y":
               nam = input("Enter the new alias name ")
               print()
               cursor.execute(
                  "insert into score values ('{}',{},curdate())".format(
                      nam, s))
        else:
           command2 = "select highscore from score where alias_name = '{}'".format(
               nam,)
           score = infofetch(command2)
           update = "update score set highscore={} ,date_of_highscore=curdate() where alias_name = '{}' and highscore < {}".format(s, nam, s)
           cursor.execute(update)
    lead = input("If you want to see the leaderboard press Y,else press enter ")
    print()
 
    if lead == "Y":
        command3 = "Select * from score order by highscore desc"
        cursor.execute(command3)
        stats = cursor.fetchall()
        print("LEADERBOARD")
        print()
 
        for i in stats:
           print(i)
    wish = input(
        "If you want to see your last highscore press Y,else press enter ")
    print()
 
    if wish == "Y":
        nam = input("Enter your alias name ")
        print()
        command1 = "select highscore from score where alias_name = '{}'".format(
                  nam,)
        score = infofetch(command1)
        print("Your high score is ", score)
        print()
    delete = input(
        "If you want to delete any alias press Y,else press enter ")
    print()
 
    if delete == "Y":
        delname = input("Enter the alias name that you want to delete ")
        print()
        command3 = "delete from score where alias_name = '{}'".format(delname,)
        cursor.execute(command3)
    conn_object.commit()
    r = input("To play the game again press P,else press Enter ")
    print()
print("Thank You")
conn_object.close()

