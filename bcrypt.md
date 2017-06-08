1. Update app.py to setup Bcrypt
2. Update the user model to hash the password
3. Apply model changes to the database with a db migration
4. Delete all user data in the users table within the postgres (or sqlite3) shell
5. Add new users to the table
6. Manually test to ensure passwords are hashed.
