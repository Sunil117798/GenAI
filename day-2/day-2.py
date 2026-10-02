import numbers


def addNumbers(*numbers):
    ans=0
    for num in numbers:
        ans+=num
    return ans

# print(addNumbers(1, 2, 3, 4, 5))
# print(addNumbers(10, 20, 30))


def userDefined(**userDetails):
    print(userDetails)
    print(type(userDetails))

#userDefined(name="John", age=25, city="New York")


numbers=[1, 2, 3, 4, 5]

square=[num*num 
for num in numbers
if num%2==0
]
#print(square)


messages = [
    {
        "role": "user",
        "content": "Explain Python"
    },
    {
        "role": "assistant",
        "content": "Python is..."
    },
    {
        "role": "user",
        "content": "Explain Docker"
    }
]

user_messages =[message["content"] for message in messages 
if message["role"] == "user"]
#print(user_messages)

numbers = [1, 2, 3, 4, 5]

# squares={
# x:x*x 
# for x in numbers}
# print(squares)

squares=lambda x:x*x
print(squares(5))

sum=lambda x,y:x+y
print(sum(1,2))




