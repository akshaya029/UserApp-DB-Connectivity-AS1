import mysql.connector

#Step 1: Connect to MySQL Database
def connect_db():
    try:
        conn = mysql.connector.connect(
            host="127.0.0.1",      
            user="root",           
            password="Admin@123",  
            database="user_app"   
        )
        return conn
    except mysql.connector.Error as err:
        print(f" Database connection failed: {err}")
        exit()

# Step 2: User Authentication
def login(cursor):
    print("\n--- LOGIN ---")
    username = input("Enter username: ")
    password = input("Enter password: ")

    cursor.execute("SELECT * FROM users WHERE username=%s AND password=%s", (username, password))
    user = cursor.fetchone()

    if user:
        print(f"\n Welcome, {username}! Login successful.")
        return user
    else:
        print("\n Access Denied: Invalid username or password.")
        return None

# Step 3: Show Profile
def show_profile(user):
    if user:
        print("\n--- YOUR PROFILE ---")
        print(f"Username: {user[1]}")
        print(f"Email: {user[3]}")
        print(f"Bio: {user[4]}")
    else:
        print("\n Access Denied. Please log in first.")

#Step 4: Edit Profile (Only Logged-In Users)
def edit_profile(cursor, conn, user):
    if user:
        print("\n--- EDIT PROFILE ---")
        new_email = input("Enter new email: ")
        new_bio = input("Enter new bio: ")

        cursor.execute("UPDATE users SET email=%s, bio=%s WHERE username=%s",
                       (new_email, new_bio, user[1]))
        conn.commit()
        print("\n Profile updated successfully!")
    else:
        print("\n Access Denied. Please log in to edit your profile.")

#Step 5: Main Application
def main():
    conn = connect_db()
    cursor = conn.cursor()

    print("=== Welcome to Python MySQL User App ===")
    user = login(cursor)

    while True:
        print("\nOptions:")
        print("1. View Profile")
        print("2. Edit Profile")
        print("3. Logout")

        choice = input("Enter your choice: ")

        if choice == '1':
            show_profile(user)
        elif choice == '2':
            edit_profile(cursor, conn, user)
        elif choice == '3':
            print("\n Logged out successfully.")
            break
        else:
            print("Invalid choice, try again.")

    cursor.close()
    conn.close()

if __name__ == "__main__":
    main()
