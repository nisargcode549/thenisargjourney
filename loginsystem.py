# Simple login system

saved_user = "admin"
saved_pass = "1234"

a = input("Enter login name: ")
b = input("Enter password: ")

if a == saved_user and b == saved_pass:
    print("✅ Successfully logged in")
else:
    print("❌ Permission denied")
