turns = 0

start = '''
You wake up one morning and find that you aren't in your bed; you aren't even in your room.
You're in the middle of a giant maze.
A sign is hanging from the ivy: "You have one hour. Don't touch the walls."
There is a hallway to your right and to your left.
'''

print(start)
while True turns < 4:
    print("Type 'left' to go left or 'right' to go right.") # Update to match your story.
    user_input = input()
    if user_input == "left":
        print("You decide to go left") # Update to match your story.

        # Continue code to finish story.

    elif user_input == "right":
        print("You choose to go right") # Update to match your story.

    turns +=1
if user_input == "right":
    print("Go straight")
    print("you won")

if user_input == "left":
    print("No more moves")
    print("you lost")
