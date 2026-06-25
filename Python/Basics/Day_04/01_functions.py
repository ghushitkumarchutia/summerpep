def animelist():
    print("1. Attack on Titan")
    print("2. One Piece")
    print("3. Naruto")
    print("4. Demon Slayer")
    print("5. Jujutsu Kaisen")

animelist()

def intro(name, course, university):
    print(f"Hello, My name is {name}. I am a student of {course} at {university}.")

intro("Alex", "BS in CS", "Carleton University")

def multiplication_table(number):
    for i in range(1,11):
        print(f"{number} * {i} = {number * i}")
    
multiplication_table(5)

def anime_dec(anime_name):
    if anime_name == "Attack on Titan":
        return "Humanity is on the brink of extinction due to the sudden appearance of giant, man-eating creatures called Titans."
    elif anime_name == "One Piece":
        return "Monkey D. Luffy, a young man whose body has gained the properties of rubber after inadvertently eating a Devil Fruit, sets sail from the East Blue Sea in search of the ultimate treasure known as the One Piece to become the next King of the Pirates."
    elif anime_name == "Naruto":
        return "Naruto Uzumaki, a mischievous and independent ninja, dreams of becoming the Hokage, the leader of his village, to earn the respect and recognition of his peers."
    elif anime_name == "Demon Slayer":
        return "Tanjiro Kamado, a kind-hearted boy whose family is massacred by demons, embarks on a perilous journey to find a cure for his sister Nezuko, who was transformed into a demon."
    elif anime_name == "Jujutsu Kaisen":
        return "Yuji Itadori, a high school student with extraordinary physical strength, inadvertently consumes a cursed object and becomes the host of a powerful curse, leading him to join a secret organization of Jujutsu Sorcerers."
    else:
        return "Anime not found."

print(anime_dec("Attack on Titan"))
    