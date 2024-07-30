import json
import re

def get_stored_user_data(filename):
    """Load the user data if it has been stored previously."""
    try:
        with open(filename) as f_obj:
            user_data = json.load(f_obj)
            return user_data
    except FileNotFoundError:
        return {}
    except json.JSONDecodeError:
        print("Error: The file is not in the correct format. It will be overwritten.")
        return {}
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return {}

def store_user_data(filename, user_data):
    """Store the user data in a file."""
    try:
        with open(filename, 'w') as f_obj:
            json.dump(user_data, f_obj)
    except Exception as e:
        print(f"An unexpected error occurred while saving the user data: {e}")

def validate_phone_number(phone_number):
    """Validate the phone number using a regular expression."""
    pattern = re.compile(r"^\+?\d{10,15}$")
    return pattern.match(phone_number) is not None