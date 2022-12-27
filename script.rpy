init python:
    import random

    MIN_ABILITY = 1
    MAX_ABILITY = 10

    # # Define lists of first and last names to use for generating random names
    first_names_male = ['Bob', 'Charlie', 'David', 'Frank']
    first_names_female = ['Alice', 'Emily', "Karen", "Susan"]
    last_names = ['Smith', 'Johnson', 'Williams', 'Jones', 'Brown', 'Davis']
    maids_names = [
    "Cassandra", "Emma", "Dot", "Valerie", "Yumeko", "Kei", "Emilia", "Anna",
    "Mary", "Kate", "Veronica", "Nina", "Molly"
    ]



    class Maid:
        def __init__(self, name, cleaning, cooking, hospitality, gardening, status, level, xp, hired):
            self.name = name
            self.cleaning = cleaning
            self.cooking = cooking
            self.hospitality = hospitality
            self.gardening = gardening
            self.status = status
            self.level = level
            self.xp = xp
            self.hired = hired
    
    class Customer:
        def __init__(self, name, age, gender, requests):
            self.name = name
            self.age = age
            self.gender = gender
            self.requests = requests

    # # Create a list to hold the customer instances
    customers = []

    # # Generate 10 random customers

    for i in range(10):
    #   # Generate a random gender using a 50/50 chance
        gender = 'male' if random.randint(0, 1) == 0 else 'female'

        if gender == "male":
            first_name = random.choice(first_names_male)
            last_name = random.choice(last_names)
        else:
            first_name = random.choice(first_names_female)
            last_name = random.choice(last_names)

        name = f"{first_name} {last_name}"

    #   # Generate a random age between 18 and 99
        age = random.randint(18, 99)



    #   # Generate a random list of requests (could be empty)
        requests = []

        num_requests = random.randint(0, 3)

        for j in range(num_requests):
            requests.append(f"Request {j+1}")

    #   # Create a new Customer instance with the random values
        customer = Customer(name, age, gender, requests)

    #   # Add the customer to the list
        customers.append(customer)


    class Task:
        def __init__(self, name, difficulty, time, skills, base_payment):
            self.name = name
            self.difficulty = difficulty
            self.time = time
            self.skills = skills
            self.base_payment = base_payment

    tasks = []

    # # Create task instances for various tasks
    vacuuming = Task('Vacuuming', 3, 30, 'cleaning', 50)
    dusting = Task('Dusting', 2, 20, 'cleaning', 30)
    washing_dishes = Task('Washing Dishes', 3, 45, 'cleaning', 20)
    babysitting = Task('Babysitting', 4, 60, 'hospitality', 60)
    gardening = Task('Gardening', 3, 45, 'gardening', 70)
    welcoming_guests = Task('Welcoming Guests', 2, 30, 'hospitality', 80)

    # # Add the tasks to the list
    tasks.extend([
    vacuuming, dusting, washing_dishes, babysitting, gardening, welcoming_guests
    ])



    firstMaid = Maid("Makoto", 6, 7, 8, 9, "available", 1, 0, True)
    secondMaid = Maid("Cassandra", 6, 7, 8, 9, "available", 1, 0, False)
    thirdMaid = Maid("Emily", 6, 7, 8, 9, "available", 1, 0, False)
    fourthMaid = Maid("Rebecca", 6, 7, 8, 9, "available", 1, 0, False)

    maidsList = [firstMaid, secondMaid, thirdMaid, fourthMaid]
    hiredMaidsList = [firstMaid.name]

    def maidSkillCheck(maid, skill):
        global skillChecked
        skillChecked = getattr(maid, skill)
        return skillChecked

    SkillChecked = 0

    money = 0


    
    


define m = Character("[maidName]")
define pov = Character("[povname]")
# The game starts here.

image MaidNeutral:
    "makoto maid.png"
    zoom .5 pos (1017, 1170)

image outside:
    "home out day.png"

image outsideNight:
    "home out night.png"

image CassandraNeutral:
    "cassandra neutral.png"

image EmilyNeutral:
    "emily neutral.png"

# if clock_status == 1:
#     image outside:
#         "home out day.png"
# else:
#     image outside:
#         "home out night.png"


label start:

    scene outside

    show MaidNeutral

    python:
        povname = renpy.input("What is your name?", length=32)
        povname = povname.strip()

        if not povname:
            povname = "Pat Smith"

    pov "My name is [povname]!"
    

    python:
        maidName = renpy.input("Hello [povname]! Would you like to choose a name for me?", length=32)
        maidName = maidName.strip()
 

        if not maidName:
            maidName = firstMaid.name

        firstMaid.name = maidName
    # These display lines of dialogue.

    m "Great! My name will be [maidName] from now on!"

    python:
        maidSkillCheck(firstMaid, "cleaning")
        SkillCleaning = skillChecked
        maidSkillCheck(firstMaid, "cooking")
        SkillCooking = skillChecked
        maidSkillCheck(firstMaid, "hospitality")
        Skillhospitality = skillChecked
        maidSkillCheck(firstMaid, "gardening")
        Skillgardening = skillChecked
    m "My name is [maidName] and my skills are: [SkillCleaning] cleaning, [SkillCooking] cooking, [Skillhospitality] hospitality and [Skillgardening] gardening."

    pov "Sorry, [maidName], but it doesn't sound much..."

    m "I know, I am a bit rusty, I had to take care of the managment before you show up"

    m "But now that you're here I can focus on what I do best, being a maid"

    menu:

        m "You want to know more about any of these skills?"

        "Cleaning":

            jump cleaningExplained

        "Cooking":

            jump cookingExplained

        "Hospitality":

            jump hospitalityExplained

        "Gardening":

            jump gardeningExplained

        "No, I already know what I need to Know":

            jump aftertutorial

label cleaningExplained:
    m "Cleaning is how about good the maid is at... Cleaning."
    m "It's essencial for any good maid. Especially for tasks like vacuuming, Dusting, washing dishes, etc."

    menu:

        m "You want to know more about any of these skills?"

        "Cleaning":

            jump cleaningExplained

        "Cooking":

            jump cookingExplained

        "Hospitality":

            jump hospitalityExplained

        "Gardening":

            jump gardeningExplained

        "No, I already know what I need to Know":

            jump aftertutorial

label cookingExplained:
    m "The higher the cooking skill, the higher the quality and the taste of the food the maid makes."

    menu:

        m "You want to know more about any of these skills?"

        "Cleaning":

            jump cleaningExplained

        "Cooking":

            jump cookingExplained

        "Hospitality":

            jump hospitalityExplained

        "Gardening":

            jump gardeningExplained

        "No, I already know what I need to Know":

            jump aftertutorial

label hospitalityExplained:
    m "Hospitality is friendly, welcoming behaviour towards guests or people in general."
    m "A maid needs to be well very charismatic to welcome guests or to babysitt."

    menu:

        m "You want to know more about any of these skills?"

        "Cleaning":

            jump cleaningExplained

        "Cooking":

            jump cookingExplained

        "Hospitality":

            jump hospitalityExplained

        "Gardening":

            jump gardeningExplained

        "No, I already know what I need to Know":

            jump aftertutorial

label gardeningExplained:
    m "Some maids have a green thumb, others not so much."
    m "Sometimes the maid's duty also involves taking care of the plants inside and outside the home."

    menu:

        m "You want to know more about any of these skills?"

        "Cleaning":

            jump cleaningExplained

        "Cooking":

            jump cookingExplained

        "Hospitality":

            jump hospitalityExplained

        "Gardening":

            jump gardeningExplained

        "No, I already know what I need to Know":

            jump aftertutorial

label aftertutorial:

    m "Our money currently is: $[money]"

    pov "So we're broke?"

    m "For now... But things will get better as soon as we get our first job!"

    "some time later"

    m "Look! We have a customer!"

    m "It's [customers[0].name]!"

    python:
        index = random.randint(0, len(tasks)-1)
        customerIndex = random.randint(0, len(customers)-1)

        if customers[0].gender == "male":
            customerPronoun = "He"
        else:
            customerPronoun = "She"

        index = int(index)

        taskName = tasks[index].name

    m "[customerPronoun] needs us to [taskName]"


    python:
        firstMaid.status = "tired"
        money += 100
    m "We just did our first job! Now we have: $[money]"

        

    m "But now we need to rest, talk to you tomorrow!"

    jump endday

label endday:

    scene outsideNight

    python:
        firstMaid.status = "available"
        secondMaid.status = "available"
        thirdMaid.status = "available"


    "The day ends and you and the maids rest."

    jump managermenu
    # This ends the game.

label managermenu:

    scene outside

    show MaidNeutral

    python:
        maidStatus = firstMaid.status
    m "Good morning! Now I am [maidStatus]"
    menu:

        m "What do you want to do now?\n
        we have $[money]"

        "Look for jobs":

            jump tasksMenu

        "Manage Maids":

            jump maidManagment1

        "Hire new maids":

            jump hireMaids

        "Upgrade maids":

            jump construction

        "Maid School":

            jump construction

        "rest for the day":

            jump endday

        "quit the game":

            jump quit


label tasksMenu:
    python:
        index = random.randint(0, len(tasks)-1)
        taskName = tasks[index].name

    menu:
        m "Let's see what is available!"

        "[taskName]":
            jump taskDescription
        
        "Go back":
            jump managermenu

label taskDescription:
    python:
        customerIndex = random.randint(0, len(customers)-1)
        customerIndex = int(customerIndex)

        customerHiring = customers[customerIndex].name


    hide MaidNeutral with dissolve

    menu:
        m "[customerHiring] needs us to do [taskName]. Lets see who is available"

        "[maidName]" if maidsList[0].status == "available":
            show MaidNeutral with dissolve
            $ chosen_maid = maidName
            $ requirement = firstMaid
            $ maidsList[0].status = "unavailable"
            jump taskResolution

        "[maidsList[1].name]" if maidsList[1].status == "available" and maidsList[1].name in hiredMaidsList:
            show CassandraNeutral with dissolve
            $ chosen_maid = maidsList[1].name
            $ requirement = secondMaid
            $ maidsList[1].status = "unavailable"
            jump taskResolution

        "[maidsList[2].name]" if maidsList[2].status == "available" and maidsList[2].name in hiredMaidsList:
            show EmilyNeutral with dissolve
            $ chosen_maid = maidsList[2].name
            $ requirement = thirdMaid
            $ maidsList[2].status = "unavailable"
            jump taskResolution

        "[maidsList[3].name]" if maidsList[3].status == "available" and maidsList[3].name in hiredMaidsList:
            show EmilyNeutral with dissolve
            $ chosen_maid = maidsList[3].name
            $ requirement = thirdMaid
            $ maidsList[3].status = "unavailable"
            jump taskResolution


        "Go back":
            jump managermenu



label taskResolution:
    python:
        meets_requirement = True

        skill_name = tasks[index].skills
        skill_level = getattr(requirement, skill_name)
        if skill_level >= tasks[index].difficulty:
            meets_requirement = True
        else:
            meets_requirement = False

        if meets_requirement:
            taskPayment = tasks[index].base_payment
            taskPayment = taskPayment + (taskPayment * (skill_level / 10))
            money += taskPayment
            ResolutionText = f"Great! {chosen_maid} was successful! We got payed ${taskPayment}. Now we have ${money}"
        else:
            ResolutionText = f"{chosen_maid} wasn't able to peform the task!"


    m "[ResolutionText]"

    jump managermenu


label maidManagment1:

    m "Sorry, this hasn't been implametaded yet"

    jump managermenu

label hireMaids:

    hide MaidNeutral with dissolve

    python:
        maidCost = 100

        def hiring_process(id, cost):
            global money
            if money >= cost:
                money -= cost
                maidsList[id].hired = True
                hiredMaidsList.append(maidsList[id].name)
                return True
            else:
                return False

    menu:
        m "Each new Maid costs $[maidCost]. Which maid you want to hire?"

        "[maidsList[1].name]" if maidsList[1].hired == False:
            show CassandraNeutral with dissolve
            $ maidId = 1
            if hiring_process(maidId, maidCost):
                m "Congrats! You hired [maidsList[1].name]"
            else:
                m "Sorry, you don't have enough money"
            jump hireMaids

        "[maidsList[2].name]" if maidsList[2].hired == False:
            show EmilyNeutral with dissolve

            jump hireMaids

        "[maidsList[3].name]" if maidsList[3].hired == False:
            show EmilyNeutral with dissolve

            jump hireMaids


        "Go back":
            jump managermenu



label construction:

    m "Sorry, this hasn't been implametaded yet"

    jump managermenu






label quit:

    m "bye, bye! See you next time!"

    return
