from re import M


messages = []

def add_message(role,content):
    messages.append({"role":role,"content":content})
    # print(messages)

def get_user_messages(role):
    ans=[]
    for message in messages:
        if(message["role"]==role):
            ans.append(message)
    
    print(messages)

    

def get_all_messages():
    ans=[]
    for message in messages:
        ans.append(message)

    print(messages)


def clear_messages():
    messages.clear()
    print(messages)





add_message(
    "user",
    "What is Python?"
)

add_message(
    "assistant",
    "Python is a programming language."
)

# print(messages)

# get_user_messages("user")
get_all_messages()
# clear_messages()

