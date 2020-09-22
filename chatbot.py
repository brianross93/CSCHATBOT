from random import choice 




def chat_init(user_response):
    pickup_line = ["Let's rock and roll rockstar!", "Giddy up!", "What's up buttercup?",
    "What's cookin good lookin?", "Holy guacamole!"]

    pickup_line_alternate = ["I say we make like a banana and split", 
    "How about you and me go dance with destiny", "Let's make like a bee and buzz outta here"]

    if user_response == "Wow what a hunk":
        return "Say okay and we go away!"
    elif user_response == "What?":
        return choice(pickup_line_alternate)
    elif user_response == "Stop":
        return "Say go away and I make like hay and go away"
    else:
        return choice(pickup_line)

    



user_response = ""

while True:
    user_response = input("Woah momma! ")
  
    if user_response == 'Go away':
        break
    if user_response == "Okay":
        user_other_response = "Cmon hunny lets blow this joint"
        print(user_other_response)
        break

    pickup_response = chat_init(user_response)
    print(pickup_response)