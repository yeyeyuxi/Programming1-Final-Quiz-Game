import random

# ------------------------------
# QUESTIONS (1-100)
# ------------------------------
questions = [
    "Solve for x: 2x + 5 = 15",
    "What is the value of 7 × (8 − 3)?",
    "Simplify: 18 ÷ 3 × 2",
    "If x = 4, what is x² − 3x?",
    "What is 25% of 200?",
    "Solve: 3(x − 2) = 12",
    "What is the next number: 2, 4, 8, 16, ___?",
    "Simplify: (5² − 3²)",
    "If a = 3 and b = 5, find ab + b",
    "What is the square root of 144?",
    "Solve: x / 4 = 6",
    "What is the value of 9³?",
    "Simplify: 6 + 2 × 5",
    "What is 3/4 as a decimal?",
    "If x + 7 = 20, x = ?",
    "Find the perimeter of a square with side 6",
    "What is the value of 2⁴?",
    "Simplify: 15 − 3²",
    "If y = 10, find 2y − 4",
    "What is the sum of angles in a triangle?",
    "Solve: 5x = 45",
    "What is the median of 2, 5, 7?",
    "Simplify: (10 − 4)²",
    "If a rectangle has length 8 and width 3, area = ?",
    "What is 1/5 of 100?",
    "What planet is known as the Red Planet?",
    "What gas do plants absorb from the atmosphere?",
    "What is the basic unit of life?",
    "Which organ pumps blood throughout the human body?",
    "What force keeps us on the ground?",
    "What part of the plant is responsible for photosynthesis?",
    "What is H₂O commonly known as?",
    "Which planet is the largest in the solar system?",
    "What type of animal is a frog?",
    "What gas do humans breathe in to survive?",
    "What part of the human body is responsible for thinking?",
    "What energy source comes directly from the Sun?",
    "Which scientist is known for the theory of evolution?",
    "What do you call animals that eat only plants?",
    "What planet do we live on?",
    "What is the boiling point of water (at sea level)?",
    "Which part of the body helps in breathing?",
    "What kind of energy is stored in food?",
    "Which planet is closest to the Sun?",
    "What tool is used to measure temperature?",
    "What system controls the body using nerves?",
    "What gas makes up most of Earth’s atmosphere?",
    "What do we call animals that eat both plants and meat?",
    "What layer of the Earth do we live on?",
    "What part of the eye controls how much light enters?",
    "Who was the first President of the United States?",
    "What year did World War II end?",
    "Who discovered America in 1492?",
    "What ancient civilization built the pyramids?",
    "Who was known as the Iron Lady?",
    "What war was fought between the North and South regions of the United States?",
    "Who was the first man to walk on the Moon?",
    "What empire was ruled by Julius Caesar?",
    "What wall fell in 1989 symbolizing the end of the Cold War?",
    "Who wrote the Declaration of Independence?",
    "What ship sank after hitting an iceberg in 1912?",
    "Who was the leader of Nazi Germany?",
    "What country was formerly known as Siam?",
    "Who was the first Emperor of Rome?",
    "What revolution began in 1789?",
    "Who led India to independence through nonviolent resistance?",
    "What was the main trade route connecting Asia and Europe called?",
    "What ancient city was destroyed by a volcanic eruption in AD 79?",
    "Who was the first woman to fly solo across the Atlantic?",
    "What empire was ruled by Genghis Khan?",
    "What document limited the power of the English king in 1215?",
    "Who was the first President of the Philippines?",
    "What war was triggered by the assassination of Archduke Franz Ferdinand?",
    "Who was the famous queen of ancient Egypt?",
    "What period is known as the Middle Ages?",
    "What is the capital city of Japan?",
    "Which country has the largest population in the world?",
    "What is the official language of Brazil?",
    "Which continent has the most countries?",
    "What currency is used in most European Union countries?",
    "Which country is known as the Land of the Rising Sun?",
    "What is the longest river in the world?",
    "Which country hosted the 2016 Summer Olympics?",
    "What international organization was founded after World War II to promote peace?",
    "Which country is famous for the Eiffel Tower?",
    "What is the largest ocean on Earth?",
    "Which country has the maple leaf on its flag?",
    "What city is known as the financial capital of the United States?",
    "Which country is both in Europe and Asia?",
    "What is the tallest mountain in the world?",
    "Which country invented paper?",
    "What is the capital of Australia?",
    "Which country is known for the Great Wall?",
    "What sea separates Europe and Africa?",
    "Which country is the smallest in the world by land area?",
    "What is the main religion in the Middle East?",
    "Which country has the most time zones?",
    "What international court is based in The Hague?",
    "Which country is known as the Pearl of the Orient?",
    "What is the largest hot desert in the world?"
]

# ------------------------------
# CHOICES (1-100)
# ------------------------------
choices = [
    # PART 1: MATH (1–25)
    ["A. 3", "B. 5", "C. 10", "D. 15"],
    ["A. 15", "B. 35", "C. 56", "D. 40"],
    ["A. 3", "B. 6", "C. 12", "D. 18"],
    ["A. 4", "B. 8", "C. 16", "D. 28"],
    ["A. 25", "B. 40", "C. 50", "D. 75"],
    ["A. 2", "B. 4", "C. 6", "D. 8"],
    ["A. 18", "B. 24", "C. 32", "D. 64"],
    ["A. 4", "B. 10", "C. 16", "D. 25"],
    ["A. 15", "B. 18", "C. 20", "D. 30"],
    ["A. 10", "B. 11", "C. 12", "D. 14"],
    ["A. 10", "B. 18", "C. 24", "D. 30"],
    ["A. 27", "B. 81", "C. 243", "D. 729"],
    ["A. 16", "B. 20", "C. 40", "D. 60"],
    ["A. 0.25", "B. 0.50", "C. 0.75", "D. 1.25"],
    ["A. 11", "B. 12", "C. 13", "D. 14"],
    ["A. 12", "B. 18", "C. 24", "D. 36"],
    ["A. 10", "B. 16", "C. 32", "D. 64"],
    ["A. 6", "B. 9", "C. 12", "D. 18"],
    ["A. 12", "B. 14", "C. 16", "D. 20"],
    ["A. 90°", "B. 180°", "C. 270°", "D. 360°"],
    ["A. 7", "B. 8", "C. 9", "D. 10"],
    ["A. 2", "B. 5", "C. 6", "D. 7"],
    ["A. 12", "B. 16", "C. 36", "D. 100"],
    ["A. 11", "B. 22", "C. 24", "D. 48"],
    ["A. 5", "B. 10", "C. 15", "D. 20"],

    # PART 2: SCIENCE (26–50)
    ["A. Venus", "B. Mars", "C. Jupiter", "D. Saturn"],
    ["A. Oxygen", "B. Nitrogen", "C. Carbon Dioxide", "D. Hydrogen"],
    ["A. Atom", "B. Cell", "C. Tissue", "D. Organ"],
    ["A. Lungs", "B. Brain", "C. Heart", "D. Liver"],
    ["A. Magnetism", "B. Gravity", "C. Friction", "D. Pressure"],
    ["A. Root", "B. Stem", "C. Flower", "D. Leaf"],
    ["A. Salt", "B. Hydrogen Peroxide", "C. Water", "D. Oxygen"],
    ["A. Earth", "B. Mars", "C. Jupiter", "D. Neptune"],
    ["A. Reptile", "B. Mammal", "C. Amphibian", "D. Fish"],
    ["A. Carbon Dioxide", "B. Oxygen", "C. Nitrogen", "D. Helium"],
    ["A. Heart", "B. Brain", "C. Lungs", "D. Stomach"],
    ["A. Wind", "B. Fossil Fuel", "C. Solar", "D. Nuclear"],
    ["A. Isaac Newton", "B. Albert Einstein", "C. Charles Darwin", "D. Galileo Galilei"],
    ["A. Carnivores", "B. Omnivores", "C. Herbivores", "D. Insectivores"],
    ["A. Mars", "B. Venus", "C. Earth", "D. Mercury"],
    ["A. 50°C", "B. 75°C", "C. 100°C", "D. 150°C"],
    ["A. Heart", "B. Kidneys", "C. Lungs", "D. Intestines"],
    ["A. Mechanical", "B. Chemical", "C. Electrical", "D. Thermal"],
    ["A. Venus", "B. Earth", "C. Mars", "D. Mercury"],
    ["A. Barometer", "B. Thermometer", "C. Hygrometer", "D. Anemometer"],
    ["A. Digestive", "B. Circulatory", "C. Nervous", "D. Respiratory"],
    ["A. Oxygen", "B. Carbon Dioxide", "C. Nitrogen", "D. Hydrogen"],
    ["A. Herbivores", "B. Carnivores", "C. Omnivores", "D. Predators"],
    ["A. Core", "B. Mantle", "C. Crust", "D. Magma"],
    ["A. Retina", "B. Cornea", "C. Iris", "D. Optic Nerve"],

    # PART 3: HISTORY (51–75)
    ["A. Abraham Lincoln", "B. George Washington", "C. Thomas Jefferson", "D. John Adams"],
    ["A. 1943", "B. 1944", "C. 1945", "D. 1946"],
    ["A. Ferdinand Magellan", "B. Marco Polo", "C. Christopher Columbus", "D. Amerigo Vespucci"],
    ["A. Romans", "B. Greeks", "C. Egyptians", "D. Mayans"],
    ["A. Queen Elizabeth I", "B. Margaret Thatcher", "C. Angela Merkel", "D. Indira Gandhi"],
    ["A. Revolutionary War", "B. Civil War", "C. World War I", "D. Cold War"],
    ["A. Buzz Aldrin", "B. Yuri Gagarin", "C. Neil Armstrong", "D. Michael Collins"],
    ["A. Greek", "B. Roman", "C. Ottoman", "D. Persian"],
    ["A. Great Wall", "B. Berlin Wall", "C. Hadrian’s Wall", "D. Western Wall"],
    ["A. George Washington", "B. Benjamin Franklin", "C. Thomas Jefferson", "D. John Hancock"],
    ["A. Lusitania", "B. Britannic", "C. Titanic", "D. Queen Mary"],
    ["A. Joseph Stalin", "B. Adolf Hitler", "C. Benito Mussolini", "D. Winston Churchill"],
    ["A. Myanmar", "B. Cambodia", "C. Thailand", "D. Laos"],
    ["A. Julius Caesar", "B. Augustus", "C. Nero", "D. Caligula"],
    ["A. American", "B. Industrial", "C. French", "D. Russian"],
    ["A. Jawaharlal Nehru", "B. Mahatma Gandhi", "C. Subhas Bose", "D. Indira Gandhi"],
    ["A. Spice Route", "B. Silk Road", "C. Amber Road", "D. Tea Route"],
    ["A. Athens", "B. Troy", "C. Pompeii", "D. Carthage"],
    ["A. Amelia Earhart", "B. Sally Ride", "C. Valentina Tereshkova", "D. Bessie Coleman"],
    ["A. Roman", "B. Ottoman", "C. Mongol", "D. Chinese"],
    ["A. Constitution", "B. Magna Carta", "C. Bill of Rights", "D. Treaty of Versailles"],
    ["A. Manuel L. Quezon", "B. Emilio Aguinaldo", "C. Jose P. Laurel", "D. Sergio Osmeña"],
    ["A. World War I", "B. World War II", "C. Cold War", "D. Crimean War"],
    ["A. Nefertiti", "B. Cleopatra", "C. Hatshepsut", "D. Isis"],
    ["A. Ancient", "B. Medieval", "C. Renaissance", "D. Modern"],

    # PART 4: INTERNATIONAL (76–100)
    ["A. Kyoto", "B. Osaka", "C. Tokyo", "D. Hiroshima"],
    ["A. USA", "B. India", "C. China", "D. Russia"],
    ["A. Spanish", "B. Portuguese", "C. French", "D. English"],
    ["A. Asia", "B. Europe", "C. Africa", "D. South America"],
    ["A. Pound", "B. Dollar", "C. Euro", "D. Franc"],
    ["A. China", "B. South Korea", "C. Japan", "D. Thailand"],
    ["A. Amazon", "B. Nile", "C. Yangtze", "D. Mississippi"],
    ["A. China", "B. UK", "C. Brazil", "D. Japan"],
    ["A. NATO", "B. ASEAN", "C. United Nations", "D. EU"],
    ["A. Italy", "B. Spain", "C. France", "D. Germany"],
    ["A. Atlantic", "B. Indian", "C. Arctic", "D. Pacific"],
    ["A. Australia", "B. Canada", "C. USA", "D. UK"],
    ["A. Los Angeles", "B. Chicago", "C. New York City", "D. Washington D.C."],
    ["A. Greece", "B. Italy", "C. Turkey", "D. Egypt"],
    ["A. K2", "B. Mount Everest", "C. Kilimanjaro", "D. Fuji"],
    ["A. India", "B. Egypt", "C. China", "D. Greece"],
    ["A. Sydney", "B. Melbourne", "C. Canberra", "D. Perth"],
    ["A. Japan", "B. Mongolia", "C. China", "D. South Korea"],
    ["A. Black Sea", "B. Red Sea", "C. Mediterranean", "D. Caspian"],
    ["A. Monaco", "B. Vatican City", "C. Malta", "D. Singapore"],
    ["A. Christianity", "B. Buddhism", "C. Islam", "D. Hinduism"],
    ["A. USA", "B. Russia", "C. China", "D. France"],
    ["A. International Criminal Court", "B. Supreme Court", "C. European Court", "D. World Trade Court"],
    ["A. Thailand", "B. Philippines", "C. Indonesia", "D. Vietnam"],
    ["A. Gobi", "B. Arabian", "C. Kalahari", "D. Sahara"]
]

# ------------------------------
# ANSWERS (A/B/C/D) (1-100)
# ------------------------------
answers = [
    # PART 1: MATH (1–25)
    "C","B","C","B","C",
    "B","C","C","B","C",
    "C","C","A","C","C",
    "C","B","A","C","B",
    "C","B","C","C","B",

    # PART 2: SCIENCE (26–50)
    "B","C","B","C","B",
    "D","C","C","C","B",
    "B","C","C","C","C",
    "C","C","B","D","B",
    "C","C","C","C","C",

    # PART 3: HISTORY (51–75)
    "B","C","C","C","B",
    "B","C","B","B","C",
    "C","B","C","B","C",
    "B","B","C","A","C",
    "B","B","A","B","B",

    # PART 4: INTERNATIONAL (76–100)
    "C","B","B","C","C",
    "C","B","C","C","C",
    "D","B","C","C","B",
    "C","C","C","C","B",
    "C","B","A","B","D"
]

# ------------------------------
# SHUFFLE block (safe; uses combined list)
# ------------------------------
shuffle_choice = input("Shuffle questions? (Y/N): ").strip().upper()

if shuffle_choice == "Y":
    combined = []
    for i in range(len(questions)):
        combined.append((questions[i], choices[i], answers[i], i+1))
    random.shuffle(combined)

    # overwrite lists with shuffled order
    questions = []
    choices = []
    answers = []
    original_numbers = []
    for item in combined:
        questions.append(item[0])
        choices.append(item[1])
        answers.append(item[2])
        original_numbers.append(item[3])
else:
    original_numbers = []
    for i in range(len(questions)):
        original_numbers.append(i+1)

# ------------------------------
# GAME LOOP (no def)
# ------------------------------
lives = 3
score = 0
missed = []

print("\n🎮 WELCOME TO THE QUIZ GAME 🎮")
print("You have 3 lives.")
print("Type Q anytime to quit.\n")

i = 0
while i < len(questions) and lives > 0:
    print(f"\nQuestion {i+1}/{len(questions)}")
    print(questions[i])

    for option in choices[i]:
        print(option)

    answer = ""
    while answer not in ["A", "B", "C", "D", "Q"]:
        answer = input("Your answer (A/B/C/D or Q): ").strip().upper()

    if answer == "Q":
        print("\nYou quit the game.")
        break

    if answer == answers[i]:
        score += 1
        print("✅ Correct!")
    else:
        lives -= 1
        print("❌ Wrong!")
        print(f"Lives left: {lives}")
        missed.append((original_numbers[i], answer, answers[i]))

    i += 1

print("\n🎯 GAME OVER 🎯")
print(f"Final Score: {score}/{i}")

if len(missed) > 0:
    print("\n📋 Missed Questions:")
    for item in missed:
        print(f"Question {item[0]} — Your answer: {item[1]} | Correct: {item[2]}")
else:
    print("\nPerfect run! No missed questions 🎉")
