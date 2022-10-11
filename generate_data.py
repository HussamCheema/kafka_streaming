import random
import string

user_ids = list(range(1,101))
recepient_ids = list(range(1,101))

def generate_message() -> dict:
    random_user_id = random.choice(user_ids)
    recepient_ids_copy = recepient_ids.copy()

    # So that user can't message himself
    recepient_ids_copy.remove(random_user_id)

    random_recepient_id = random.choice(recepient_ids_copy)

    # Generate a random message
    message = "".join(random.choice(string.ascii_letters) for i in range(32))

    return {
        "user-id": random_user_id,
        "recepient-id": random_recepient_id,
        "message": message
    }
