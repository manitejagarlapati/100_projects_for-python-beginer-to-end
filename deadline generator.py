# 🗓️ Deadline Generator – A simple Python script for beginners

# Displaying a welcome message
print("THIS IS YOUR SAMPLE DEADLINE GENERATOR:")

# Asking the user for input and storing it in variables
company = input("Enter the name of your company: ")      # Company name
type = input("Enter the type of your company: ")         # Company type (e.g., startup, NGO, etc.)
deadline = input("Enter the deadline for your company: ")# Submission deadline

# Combining the inputs into a final message using string concatenation
print("The " + company + " of " + type + " needs to submit on " + deadline)