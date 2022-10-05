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


# ------------------------------------------------------------------------------------

# STRETCH GOALS:

# ------------------------------------------------------------------------------------


def write_data(file_name, data):
    f = open(file_name, "w")
    f.writelines(data)
    f.close()


# accrue interest
# The accrue interest function takes an interest rate as a parameter.
# When called it loops over all users in the list and adds an amount
# to their balance equal to the current balance times the rate.


def accrue_interest(rate, user_list):
    updated_user_list = []
    for user in user_list:
        user = user.strip().split(",")
        balance = float(user.pop())
        balance = balance + balance * rate
        user.append(f"{str(balance)}\n")
        updated_user_list.append(",".join(user))
    write_data("data2.txt", updated_user_list)


accrue_interest(0.13, user_list)


# Deposit
# Write a deposit function. This function should take the user name, password, and amount.
# It should search the list of users for the username and verify the password.
# If it finds a user it should add the amount to that user's account balance.
def deposit(usernameInput, passwordInput, amount):
    updated_user_list = []
    found_user = {}
    # search for user in user list
    for user in user_list:
        user = user.strip().split(",")
        if usernameInput == user[0] and passwordInput == user[1]:
            # deposit amount
            user[3] = int(user[3]) + amount
            user[3] = str(user[3])
            found_user = user
        user[3] = f"{user[3]}\n"
        updated_user_list.append(",".join(user))
    if found_user == {}:
        print("\nUser name and password not found")
    write_data("data3.txt", updated_user_list)


deposit("aman", "password", 5)
deposit("aman", "1234", 5)


# Withdrawl function
# This function takes the user name, password, and amount.
# It should find the user name, verify the password and attempt to subtract the amount from the user's balance.
# If the amount is greater than the balance it should print an error.
# Otherwise, the amount is subtracted and the new balance is printed.
def withdrawl(usernameInput, passwordInput, amount):
    updated_user_list = []
    found_user = {}
    # search for user in user list
    for user in user_list:
        user = user.strip().split(",")
        if usernameInput == user[0] and passwordInput == user[1]:
            # check if there are enough funds
            if int(user[3]) < amount:
                print("Not enough funds.")
            else:
                # deduct amount from balance
                user[3] = int(user[3]) - amount
                user[3] = str(user[3])
            found_user = user
        user[3] = f"{user[3]}\n"
        updated_user_list.append(",".join(user))
    if found_user == {}:
        print("\nUser name and password not found")
    write_data("data4.txt", updated_user_list)


withdrawl("aman", "password", 1005)
withdrawl("aman", "1234", 5)

# Transfer
# The transfer function takes a username, password, amount, and a second username.
# It should search for a user name, verify the password, subtract the amount from the first user's balance.
# If the amount is greater than the balance it should display an error.
# Otherwise, it finds the second user name in the list and adds the amount to their balance.
