import time
import random


def print_pause(message, seconds):
    print(message)
    time.sleep(seconds)


def play_ball():
    pitch = []
    oppo_team = ["Franklin Fury", "Washington Warriors", "Carthage "
                 "Cavaliers", "Georgetown Giants"]
    intro(oppo_team)
    pitch_one(pitch)
    pitch_two(pitch)


def intro(oppo_team):
    print_pause("It's the bottom of the ninth inning.", 3)
    print_pause("You're pitching for the Springfield Redbirds.", 3)
    print_pause("The game is tight. You're winning by two runs, BUT...", 3)
    print_pause("the " + random.choice(oppo_team) +
                " have loaded the bases.", 3)
    print_pause("If that's not bad enough, there's only one out.", 3)
    print_pause("The ballpark thunders with excitement.", 3)
    print_pause("All three hits this inning have come off your fastball.", 3)


def pitch_one(pitch):
    print_pause("You look at the catcher to select your next pitch.", 3)
    pitch_1 = input("Enter 1 to select fastball or\n"
                    "Enter 2 to select change-up:\n")
    if pitch_1 == "1":
        print_pause("You hurl a fastball towards homeplate.", 2)
        print_pause("CRACK!! The slugger sends the ball sailing "
                    "with homerun distance!!", 3)
        print_pause("Thankfully, it hooks foul just inches away "
                    "from the foul pole!!", 3)
        pitch.append("fastball")

    elif pitch_1 == "2":
        print_pause("You windup and throw a well-executed change-up.", 3)
        print_pause("\"STRRRRRRIIIIIKE!!\", the Slugger swings the bat way "
                    "ahead of the pitch for strike one.", 3)
        pitch.append("change-up")

    else:
        pitch_one(pitch)


def pitch_two(pitch):
    print_pause("You look at the catcher to select your next pitch.", 3)
    pitch_2 = input("Enter 1 to select your fastball or\n"
                    "Enter 2 to select your change-up:\n")
    if pitch_2 == "1":
        if "fastball" in pitch:
            print_pause("You throw a fastball right down "
                        "the heart of the plate.", 2)
            print_pause("KA-BOOM!! The Slugger launches the ball over the "
                        "center field wall for a GRANDSLAM!!", 3)
            print_pause("You walk off the field in disbelief.", 2)
            print_pause("It's a crushing defeat.", 2)
            play_again()
        else:
            print_pause("You hurl a poorly thrown fastball.", 2)
            print_pause("CRACK!! The Slugger hits a hard line drive "
                        "into the right field corner for a triple.", 3)
            print_pause("Three runs score on a walk-off triple.", 2)
            print_pause("Your team loses and your sent "
                        "back to the Minor Leagues.", 2)
            play_again()
    elif pitch_2 == "2":
        if "change-up" in pitch:
            print_pause("The Slugger grounds hard to the short stop "
                        "who throws to second base for an out", 3)
            print_pause("and then the second baseman throws "
                        "to firstbase for a DOUBLEPLAY!!", 3)
            print_pause("Phewwwww! You escape the jam and win the game!", 3)
            play_again()
        else:
            print_pause("The Slugger hits a hard linedrive, "
                        "but it's caught by the third baseman for one out.", 3)
            print_pause("He quickly steps on thirdbase before the baserunner "
                        "can make it back for an unassisted DOUBLEPLAY!", 3)
            print_pause("You win the game, and buy your "
                        "third baseman a steak dinner.", 3)
            play_again()

    else:
        pitch_two(pitch)


def play_again():
    play = input("Do you want to play again? Type \"y\" or \"n\". \n")
    if play == "y":
        play_ball()
    elif play == "n":
        print("Thanks for playing!!")
    else:
        play_again()


play_ball()
