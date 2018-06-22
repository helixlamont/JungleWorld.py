# short text adventure rpg
# Andrew Brown
# 6/18/2018
import time
import sys

t = time.sleep


def endcredits():
    t(1)
    micro_delay_print("THE OUTLET\n\n")
    t(1)
    micro_delay_print("Made by Andrew Brown\n")
    t(1)
    micro_delay_print("...\n...\n...")
    t(1)
    macro_delay_print("Pt. 2 coming soon .....")


def macro_delay_print(text):
    for x in text:
        print(x, end="")
        sys.stdout.flush()
        t(0.4)


def micro_delay_print(text2):
    for y in text2:
        print(y, end="")
        sys.stdout.flush()
        t(0.035)


t(0.5)
micro_delay_print("Welcome To the Outlet\n\n")
t(1.2)
macro_delay_print("......\n\n")
t(0.5)
name = input("What will you call yourself?\n")
t(1)
name2 = input("How bout your girl/guy?\n")
t(1)
micro_delay_print("Okay " + name + "\n\n")
t(1)
answer = input("Are you ready?(yes/no, then enter)\n")

if answer == 'yes':
    t(0.5)
    micro_delay_print("Activating\n")
    time.sleep(1)
    print("...")
    time.sleep(1)
    print("...")
    time.sleep(1)
    print("...")
    time.sleep(1)
    print("To make a choice, input the letter of your answer and then press ENTER")
    time.sleep(1)
    print("...")
    time.sleep(1)
    print("...")
    time.sleep(1)
    print("...")
    time.sleep(1)
else:
    micro_delay_print("Fine then\n")
    t(1)
    micro_delay_print("I guess you aren't ready yet\n")
    t(1)
    endcredits()

micro_delay_print("     '.... Ugh,' you grunt as you awake from your sleep. \n"
                  "A piercing light shines from a hole in the ceiling. \n"
                  "The old church you're in is filled with dust and plants growing in every corner of the room. \n"
                  "You glance to your side to see your girlfriend sleeping. \n\n")

choice = input("Do you:\n(a) Wake her up?\n(b) Quietly get out of bed?\n")

if choice == "a":
    t(0.5)
    micro_delay_print("     YAWNNNN ... Baby? Last night was crazy .... how did we survive?\n")
    input()
    t(0.5)
    micro_delay_print("     'heh .. I knew you'd say that. can you unplug me?' You reach over and take out the cord \n"
                      "connected to her back. her eyes glow a bright green and she gives a sigh of relief. \n"
                      "You check your limb navigator. 'Money's all here.' She smiles. 'By the time Kikai realizes \n"
                      "we're gone, we'll be on a beach somewhere in Jakarta.' 'I've never seen a beach you know. \n"
                      "I hear the water is so clear, and so beautiful, it's like looking through glass.' \n"
                      "'Well, we'll just have to find out won't we?' Her smiles reminds you of home. \n"
                      "A gentler time, far from the cold desolation of The Outlet. \n\n"
                      "     Suddenly a gas canister flies through the window and starts to spew out noxious chemicals! \n"
                      "Bullets rain through the door as men in tactical gear enter the church and \n"
                      "begin to shoot at you! '" + name2 + " run! Get to the bikes!' \n\n"
                      "     You burst through the back exit with " + name2 + ". as you run towards your bikes. \n"
                      "However, an android awaits you. It readies itself for battle\n\n")

    choice = input("Do you:\n(a) Shoot at it?\n(b) Engage it in hand to hand combat?\n\n")

    if choice == "a":
        t(0.5)
        micro_delay_print("     'It's over, " + name + ". If you surrender now, I may let the girl live.' 'EAT LEAD K!' \n"
                          "You open fire on Kikai's android, but the bullets are useless against it's \n"
                          "metal exterior. It launches a small rocket at you which you're able to block \n"
                          "with your gamma shield at the last second causing you to fly backwards. \n"
                          "The android walks towards you and aims at your head.\n"
                          "Goodbye, " + name + ". 'KRITCSCHH--' A vibrant blue plasma sword rips \n"
                          "through the android's chest. The android begins to malfunction as " + name2 + " stands fiercely \n"
                          "behind it. It turns it's head 180 degrees though as it dies and fires a round striking \n"
                          "" + name2 + " in the chest. She falls to the floor. 'No!' You scream. '" + name2 +"!' \n"
                          "It's okay " + name + ", I wouldn't take anything back.' You stare into her eyes as they \n"
                          "glaze over and so, your heart with it. 'He's back here!' \n\n"
                          "     You jump on your motorcycle and head towards the dock. Kikai's goons are not far behind. \n"
                          "You blaze towards your friend Dave's boat. You call him up on your interface \n"
                          "'START THE BOAT DAVE, START THE BOAT!'. Bullets whizz past your head as you \n"
                          "navigate the pier. You're not sure you're going to make it. You fly up the loading ramp \n"
                          "and soar through the sky as the sun glistens off your black helmet. \n"
                          "You crash land onto the boat as it speeds away. 'Now that's how you make an exit! \n"
                          "Where's " + name2 + "?' She didn't make it.' Dave gives a silent look of acknowledgement \n"
                          "and returns to the helm. You stare back at shore and gaze at your former city, The Outlet.\n\n")
        endcredits()

    elif choice == "b":
        t(0.5)
        micro_delay_print("     You run towards the android and engage it with judo. It's an older model, but\n"
                          "it's reaction times are off the charts. You go for a roundhouse kick but it grabs you\n"
                          "by the legs and throws you down to the ground. It goes for a hammer fist but you roll\n"
                          "out of the way as the earth cracks where your head once laid. 'I'm going to kill you\n"
                          "" + name +", Then I'm going to make " + name2 + " a slave!' The android goes for a jab but you\n"
                          "manage to dodge and armbar, then climb on back. You reach under it's neck cover and pull\n"
                          "out it's circuits. 'Shoot'em now" + name2 +"!. She takes the shot and it's dead on.\n"
                          "The android drops as you hear kikai yells out 'This isn't the last of me! You hop on your\n"
                          "Motorcycles and race to the boat. Dave is waiting for you there. 'Whoooo! Let's go man!' \n"
                          "'Where are we headed?' ...... Jakarta'\n\n")

        endcredits()


elif choice == "b":
    t(0.5)
    micro_delay_print("     You get up off of the floor and quietly walk towards your armour. \n"
                      "You glance back to see your if " + name2 +" is sleeping and remove a small key \n"
                      "from your mouth. You unlock a secret compartment in your armour to reveal a hand-drawn map. \n"
                      "'It won't be long now,' you whisper to yourself. A sly grin spreads across your face as your \n"
                      "girlfriend calls you. Baby ... what's that? \n\n")


    choice = input("You respond:\n(a) Ahhh, it's nothing ... How did you sleep?\n(b) You show it to her\n")
    if choice == "a":
        t(0.5)
        micro_delay_print("     'Good. I was dreaming of us relaxing on the beach, sun shining down on us. \n"
                        "It's all coming together baby. It's really gonna happen.' You look her in the eyes as \n"
                        "she walks towards you. 'No more babe. No more suffering. \n"
                        "No more killing. No more running around in this god forsaken city. \n"
                        "The Outlet has taken a lot from me ... But sometimes you have to lose something in order to gain.' \n\n"
                        "You pack up your things and get on your motorcycle. 'Let's go' \n"
                        "You arrive at the dock. "+ name2 + " begins loading the boat. As she finishes you\n\n")


        choice = input("(a) Pull a gun on her \n(b) Give her a hug\n")
        if choice == "a":
            t(0.5)
            micro_delay_print("     As she finishes boarding her things, you draw your draw your amrpistol H557 and\n"
                          "press it against her side. 'Baby ... what?' 'I'm sorry " + name2 + ". I can't take\n"
                          "Any chances.' 'You mean the world to me ... but you're too big of a risk. He'll go \n"
                          "to the ends of the earth for his flesh and blood.' 'Tears begin to well up in her eyes\n"
                          "So it was all a lie, huh? Everything you said? Just words?' 'No, I meant it.' You lift\n"
                          "The gun to her head and tighten your grip on the trigger. 'I have no choice-' \n\n"
                          "     You close your eyes and begin to squeeze when a shot rings out and hits you in the shoulder!\n"
                          "You wince in pain. 'Dammit!' You scream. You see Kikai's men running towards your location. " + name2 +" \n"
                          "ducks behind a pallet for cover as you exchange gunfire with Kikai's goons. You hop in \n"
                          "The helm of the boat and peel off. 'Wheww, that was close.' You start to check your \n"
                          "mixture of flesh and metal when you hear a beeping sound. 'Beep beep beep.' You pull out\n"
                          "a small object embedded in your shoulder. ' .... - A Lithium rou- BOOOOOOOM!' Your body and \n"
                          "boat are strewn about the wind. So close, so close.")

            endcredits()


        elif choice == "b":
            t(0.5)
            micro_delay_print("     'This is it babe, our new life.' " + name + "'s eyes begin to well up. 'What's wrong?'\n"
                          "'You were always a believer weren't you?' You feel something plunge into your stomach.\n"
                          "The deep blue glow of her plasma sword eminates from within you. She pulls it out of you\n"
                          "as you drop to your knees. 'How- ... h-how did you know?' You gaze into her eyes as she\n"
                          "slips her hand into your chest cavity and withdraws the map. 'I always knew. What did\n"
                          "you think? I was some fool? That I didn't know what you were hiding?' 'But- your father?\n"
                          "He'll -, kill you for -that map.' 'I don't think we'll have to worry about Kikai anymore.\n"
                          "I'm in charge now.' Your last images are of the maginificence of the city they call The Outlet. You fall to your side\n"
                          "and leak out the clear fluid that flows through your vein. You smile to yourself. Almost made it.")

            endcredits()



    elif choice == "b":
        t(0.5)
        micro_delay_print("     'I wanted to wait until later .. but I guess I'll show you now.' You walk over to your\n"
                          "girlfriend " + name2 + ", and show her the map to la Fancia. 'This is a shipwreck right\n"
                          "off the coast of Jakarta. It was a pirate ship that sunk back in the 23rd century,\n"
                          "Rumored to be carrying one of the oracles answers. I know, I know, I said yesterday was\n"
                          "the last time, but this is one of the Oracles answers baby! There are only seven in the \n"
                          "world! Imagine what we could get for this! We'll be rich!\n\n"
                          "     A look of disbelief begins to crawl over her face. 'Baby, why?' .. 'What do you mean?'\n"
                          " 'It's fine! We'll be long by the time Kikai ever real-' ... 'Wait-wait-wait,\n"
                          "You took this from Kikai? He'll kill us! We have to put this back baby,\n"
                          "Yeah we'll just put it right back where you found it, and it'll all be good.'\n"
                          "'What? NO WAY, we can't do that, plus this is just too valuable .. look we'll be fine'\n"
                          "'Fine? You know how powerful Kikai is. He can find us anywhere! He'll track us down\n"
                          "and sell us for prosthetics! This is not how this was supposed to be baby! .... You have a choice\n"
                          "give me the map or I walk.'\n\n")

        choice = input("Do You:\n(a) Give her the map \n(b) Keep the map?\n")
        if choice == "a":
            t(0.5)
            micro_delay_print("     'I-I ... Here'. She holds it up to her lighter and burns it. 'I'm doing this \n"
                              "Because I love you.' You pack your things and head to the dock where Dave awaits you\n"
                              "'So, guess this is it for Outlet City huh? You off to a new life?' 'The Outlet\n"
                              "will always go with me, wherever I go. It's part of me." + name2 + " Smiles and heads \n"
                              "into the cabin. 'Yup, all up here.'")

            endcredits()


        elif choice == "b":
            t(0.5)
            micro_delay_print("    Well. I'm not surprised. You always loved this kind of life too much\n"
                              "I guess I was just kidding myself believing you'd leave it behind\n"
                              "'You don't have to go.' 'I know.' You watch as " + name2 + " leaves. You wonder to\n"
                              "yourself if this is all worth it. Maybe not, but then again, you never really had\n"
                              "much choice in the matter, did you?")

            endcredits()


