import time
import random


def creature() -> str:
    evil_creatures = ["Baba Yaga", "Alp", "Banshee", "Chimera", "Manananggal", "Oni"]
    creature_ = random.choice(evil_creatures)
    return creature_


def printMessage(string_message: str, form: bool =False) -> None:
    the_cret = creature()
    if form is False:
        print(string_message)
        time.sleep(3)
    elif form is True:
        print(string_message.format(the_cret))
        time.sleep(3)


def WelcomeMessage() -> None:
    printMessage("Welcome to the the best or worst adventure of your lifetime")
    printMessage("The decisions you make can either make or mar you.")
    printMessage("Choose wisely")
    printMessage("N.B You have 30 seconds to pick an answer, else a random option will be picked for you")
    print("\n")


def InputAndValidation() -> str:
    random_action = ["a", "b"]
    while True:
        message_received = input("Select your preferred option: ").lower()
        if message_received not in random_action:
            print("Option not available")
        else:
            break
    return message_received


class Adventure:
    # random_action = ["a", "b"]

    def __init__(self) -> None:
        self.action_1 = ""
        self.action_2 = ""
        self.action_3 = ""
        self.action_4 = ""
        self.lose = False

    def TheWoods(self) -> str:
        printMessage("You get intrigued and wonder what is beyond the woods. For what it's worth,")
        printMessage("you're stranded on as island, and what better way to pass the time than to explore")
        printMessage("into the unknown in the hopes of finding a way out. As you get closer to the trees,")
        printMessage("your head hurts, and your gut tells you not to go in, but you've made up your mind.")
        printMessage("The leaves crunch as your feet walks on them, the atmosphere looked great and just as you")
        printMessage("begin to wonder why you didn't feel like going in there, you hear a loud shriek.")
        print("\n")
        printMessage("What do you do?")
        print("A. Run")
        print("B. Locate the source of the sound")
        self.action_2 = InputAndValidation()
        return self.action_2

    def Survival(self) -> bool:
        print("You wake up on a mysterious island all alone, you have no idea how you got there or what's")
        printMessage("happening.")
        print("You are surrounded by the most beautiful scenery you've ever seen. Behind you lies a grove of ")
        printMessage("trees, ")
        printMessage("Or so you think.")
        print("\n")
        printMessage("What do you do?")
        print("Option A: Search for your phone?")
        print("Option B: Get curious and walk into the trees.")
        action_1 = InputAndValidation()

        if action_1 == "a":
            time.sleep(1)
            printMessage("Your initial inclination is to go for your phone, and as you reach for your pockets, ")
            printMessage("you feel the edges of something and breathe a sigh of relief when you find it. I need")
            printMessage("to contact my mum. Your joy is short lived as you learn that your phone has no network bars")
            printMessage("You have no choice.")
            self.TheWoods()

        elif action_1 == "b":
            self.TheWoods()

        if self.action_2 == "b":
            printMessage("You swivel your head towards the source of the noise, wondering what type of animal would")
            printMessage("create such a noise, and you decide to investigate more. As you detour from your course and")
            printMessage("travel to the left, the leaves above you begin to shade off the sun beams. Nothing made a")
            printMessage("sound in the woods except your feet on the ground. You see something dart through the trees")
            printMessage("It was a {}.", True)
            printMessage("Your eyes can't quite make out what it was, so you make a dash back in the direction you")
            printMessage("came but you're too slow. When it comes up to you, it tears off your head.", True)
            self.lose = True
            print("GAME OVER!")
            return self.lose

        elif self.action_2 == "a":
            printMessage("You're not taking any chances, so you sprint full speed as you place one leg in front of")
            printMessage("the other. You sprint through the trees like an Olympic gold medallist in a 100m dash,")
            printMessage("but this time for your life or out of fear. Your heart thumps, and terror spreads like")
            printMessage("wildfire through you. The shriek resurfaces, this time sounding considerably close to you "
                         "than before.")
            printMessage("The beast after your life is a {}", True)
            printMessage("What do you do?")
            printMessage("A. You run into the cave and hide.")
            printMessage("B. You stand up and keep running.")

            self.action_3 = InputAndValidation()

            if self.action_3 == "b":
                printMessage("You soon jump back up and start to run again, but you end up stumbling on another")
                printMessage("stone after a few meters. It was as if terrible luck had been bestowed upon you.")
                printMessage("The beast, a {} catches up with you, and with a terrible yowl, it takes a clean")
                printMessage("swipe, and your head rolls right off your neck.")
                self.lose = True
                print("GAME OVER!")
                return self.lose

            elif self.action_3 == "a":
                printMessage("You dive inside the cave and take cover. Because the beast, a {} can't locate you, the",
                             True)
                print("cave gives momentary comfort and safety. You lock yourself up in the cave for an hour")

            print("What do you do?")
            print("A. Spend the night in the cave")
            print("B. Crawl out of the cave and make another run for it")

            action_4 = InputAndValidation()

            if action_4 == "a":
                printMessage("As time passes, the little light seeping into the cave dims, signalling the")
                printMessage("arrival of darkness. Your stomach is grumbling and your tongue is parched.")
                printMessage("You can't stand it any longer and decide to climb out of the cave in the hopes")
                printMessage("of finding something edible anywhere. As you seek for the cave's walls,")
                printMessage("you come into contact with something that stings you. It had slipped")
                printMessage("into the cave while you waited for nightfall, the sting is no ordinary sting.")
                printMessage("It's the sting from a {}.", True)
                printMessage("While you're trying to figure out what stung you, you convulse and die.")
                self.lose = True
                print("GAME OVER!")
                return self.lose

            elif action_4 == "b":
                printMessage("It was either you died inside the cave or you died trying to escape. You chose")
                printMessage("the latter, you climb your way out of the cave as soon as you were sure that it")
                printMessage("was nowhere near. On climbing out of the cave, you scan your surroundings to make")
                printMessage("it was safe and with the last energy in your body, you ran straight ahead")
                printMessage("not taking a look backwards. Your decision pays off as you burst out into the other")
                printMessage("side of the island. You see a boat waiting for you and you jump into it without a")
                printMessage("second thought as to why it was placed there or who placed it there.")
                printMessage("You row away to safety as you arrive at a beach with humans who come to your rescue.")
                print("YOU WIN!")


if __name__ == "__main__":
    message = Adventure()
    WelcomeMessage()
    play = message.Survival()
    if play is True:
        while True:
            play_again = input("Do you want to play again? y/n: ").lower()
            if play_again == "y":
                play = message.Survival()
            elif play_again == "n":
                print("We hope to see you again")
                break
