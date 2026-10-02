def create_message(role, content):
    return {"role": role, "content": content}

print(create_message(role="user", content="Hello"))  