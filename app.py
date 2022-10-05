def load_data(file_name):
    """
    A function that reads a text file of user data and returns a list of all users.

    Args:
        file_name (string): The file name.

    Returns:
           list: A list of all users
    """
    f = open(file_name, "r")
    user_list = f.readlines()
    f.close()

    return user_list


def login(user_list):
    """
    A function that prompts the user for the username and password, checks if they match an existing user, and returns a user dictionary.

    Args:
        user_list (list): All the users.

    Returns:
           dictionary: A user dictionary
    """
    usernameInput = input("Username: ")
    passwordInput = input("Password: ")
    found_user = {}
    for user in user_list:
        username, password, full_name, balance = user.strip().split(",")
        if usernameInput == username and passwordInput == password:
            found_user = {"Name": full_name, "Balance": float(balance)}

    return found_user


def display_user(user):
    """
    A function that displays the user information

    Args:
        user (dictionary): A user dictionary.
    """
    if user == {}:
        print("\nUser name and password not found")
    else:
        user_info = f'\nName: {user["Name"]}\nBalance: {user["Balance"]}'
        print(user_info)


user_list = load_data("data.txt")
user = login(user_list)
display_user(user)
