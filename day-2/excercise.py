
def calculate_average(numbers):
    return sum(numbers)/len(numbers)

#print(calculate_average([1,2,3,4,5]))

def calculate_total(*numbers):
    return sum(numbers)

#print(calculate_total(1,2,3,4,5))

def create_profile(**details):
    for key,value in details.items():
        print(f"{key}: {value}")
        
#create_profile(name="John", age=30, city="New York")




def divison(num1, num2):
    try:
        return num1/num2
    except Exception as e:
        print("Error:", e)
        return None

#print(divison(10, 0))



messages = [
    {
        "role": "system",
        "content": "You are a helpful assistant."
    },
    {
        "role": "user",
        "content": "Explain Python."
    },
    {
        "role": "assistant",
        "content": "Python is a programming language."
    },
    {
        "role": "user",
        "content": "What is FastAPI?"
    }
]



user_messages=[
    message
    for message in messages
    if message["role"]=="user"
    ]
#print(user_messages)


def create_message(role, content):
    return {
    "role": role,
    "content": content
}


message = create_message(
    "user",
    "Explain Docker"
)

print(message)

