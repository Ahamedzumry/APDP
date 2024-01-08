class User:
    def _init_(self, username, password):
        self.username = username
        self.password = password

def authenticate(username, password, users):
    for user in users:
        if user.username == username and user.password == password:
            return True
    return False

# Example usage:
user1 = User("john_doe", "password123")
user2 = User("alice_smith", "securepass")

user_list = [user1, user2]

input_username = input("Enter your username: ")
input_password = input("Enter your password: ")

if authenticate(input_username, input_password, user_list):
    print("Authentication successful!")
else:
    print("Authentication failed.")