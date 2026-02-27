users = {
    1: {
        "email": "admin@system.com",
        "role": "administrator",
        "active": True
    },
    2: {
        "email": "jan@email.com",
        "role": "user",
        "active": True
    },
    3: {
        "email": "guest@email.com",
        "role": "guest",
        "active": False
    }
}

try:
    user_id = int(input("Enter user to search info: "))
    user = users.get(user_id)
except:
    print("\nUser not found")
else:
    print("\n==== User Info ====")
    print(f"Email: {user.get('email', 'N/A')}")
    print(f"Role: {user.get('role', 'N/A')}")
    print(f"Active: {user.get('active', 'N/A')}")
finally:
    print("\nSearch finished")