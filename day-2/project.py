messages = []


def add_message(role:str,content:str):
    messages.append({
        "role":role,
        "content":content
    })

def get_user_messages(user:str):
    user_message=[
        message
        for message in messages
        if(message["role"]=="user")
        ]
    return user_message

def get_all_messages():
    all_message=[message for message in messages]
    return all_message

def clear_messages():
    messages.clear()


add_message(
    "user",
    "What is Python?"
)

add_message(
    "assistant",
    "Python is a programming language."
)

print(get_all_messages())


