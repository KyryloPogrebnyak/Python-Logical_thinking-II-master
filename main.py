#1

def show_registration(username, password, modulename):
    for user in users:
        if username == user['name'] and password == user['password'] and user['type'] == 'Student':
            for use in user['modules']:
                if modulename == use['title']:
                    return f'You are registered to the module {modulename}'
                elif modulename != use['title']:
                    return f"You did not register to the module {modulename}"
        elif username == user['name'] and password == user['password'] and user['type'] == 'Teacher':
            return "You are a teacher"                        
            
def has_completed_module(username, password, modulename):
    for user in users:
        if username == user['name'] and password == user['password'] and user['type'] == 'Student':
            for use in user['modules']:
                if modulename == use['title'] and use['completed'] == True:
                    return f"You have completed the module {modulename}."
                elif modulename == use['title'] and use['completed'] == False:
                    return f"You did not complete the module {modulename}."
        elif username == user['name'] and password == user['password'] and user['type'] == 'Teacher':
            return "You are a teacher"

def is_anonymus(username):
    for user in users:
        if username != user['name']:
            return True

def has_no_requirement(modulename):
    for module in modules:
        if modulename == module['name']:
            if 'requirement' not in module:
                return True

def is_registered(username, password, modulename):
    for user in users:
        if username == user['name'] and password == user['password'] and user['type'] == 'Student':
            for use in user['module']:
                if modulename == user['title']:
                    return True

def is_completed(username, password, modulename):
    for user in users:
        if username == user['name'] and password == user['password'] and user['type'] == 'Student':
            for use in user['module']:
                if modulename == use['title']:
                    if use['completed']:
                        return True

def is_registered_and_completed(username, password, modulename):
    return is_registered(username, password, modulename) and is_completed(username, password, modulename)

def meets_requirement(username, password, modulename):
    for module in modules:
        if modulename == module['name'] and module['requirement']:
            return is_registered_and_completed(username, password, modulename)

def may_enroll(username, password, modulename):
    if is_anonymus(username):
        return has_no_requirement(modulename)
    else:
        return is_registered(username, password, modulename) and (has_no_requirement(modulename) or meets_requirement(username, password, modulename))

users = [
    {
        "name": "Holly",
        "type": "Student",
        "password": "hunter",
        "modules": [
            {
                "title": "Computer basics",
                "completed": True
            },
            {
                "title": "Python basics",
                "completed": False
            }
        ]
    },
    {
        "name": "Peter",
        "type": "Student",
        "password": "pan",
        "modules": [
            {
                "title": "Computer basics",
                "completed": False
            }
        ]
    },
    {
        "name": "Luke",
        "type": "Student",
        "password": "skywalker",
        "modules": [
            {
                "title": "Computer basics",
                "completed": True
            }
        ]
    },
    {
        "name": "Janis",
        "type": "Teacher",
        "password": "joplin"
    }
]
modules = [
    {
        "name": "Computer basics"
    },
    {
        "name": "Python basics",
        "requirement": "Computer basics"
    },
    {
        "name": "Django",
        "requirement": "Python basics"
    }
]
username = input("What is your name? ")
password = input(f"Enter a pssword for {username}: ")
modulename = input("What module do you want to check? ")

print(show_registration(username, password, modulename))
#2
print(has_completed_module(username, password, modulename))
#3
if may_enroll(username, password, modulename):
    print(f"You may register to the module {modulename}.")
else:
    print(f"You may not register to the module {modulename}.")





