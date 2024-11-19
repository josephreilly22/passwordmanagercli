Pass Manage

How it works:
1. Set a password that is hashed with SHA256
2. That hash of the password is the AES key to encrypt passwords
3. The hash of the password is AES encrypted using itself
4. To add or get passwords, you need the master password's hash

To use:
1. git clone https://github.com/josephreilly22/passwordmanagercli.git
2. Run "python passmanage.py" or "python3 passmanage.py"
3. Set master password
4. All ready to set and retrieve passwords
