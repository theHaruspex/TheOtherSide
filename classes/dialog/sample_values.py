sample_dialogue = (
    "Lorem ipsum dolor sit amet, consectetuer adipiscing elit, sed diam nonummy nibh euismod tincidunt ut "
    "laoreet dolore magna aliquam erat volutpat. Ut wisi enim ad minim veniam, quis nostrud exerci tation "
    "ullamcorper.")

sample_portrait_path = "resources/the_prophetess.jpg"
sample_background_path = "resources/dialogue_background.jpg"
sample_adj_list = {
    "start": {
        "text": "Hello there! How are you doing today?",
        "options": {
            "Good": "good_response",
            "Not great": "not_great_response"
        }
    },
    "good_response": {
        "text": "That's great to hear! Is there anything I can help you with?",
        "options": {
            "Yes": "yes_help_response",
            "No": "no_help_response"
        }
    },
    "not_great_response": {
        "text": "Oh no, I'm sorry to hear that. Is there anything I can do to help?",
        "options": {
            "Yes": "yes_help_response",
            "No": "no_help_response"
        }
    },
    "yes_help_response": {
        "text": "Sure thing! What do you need help with?",
        "options": {
            "Technical issue": "tech_help_response",
            "Billing question": "billing_help_response"
        }
    },
    "no_help_response": {
        "text": "Okay, no problem. Let me know if you need anything later!",
        "options": {}
    },
    "tech_help_response": {
        "text": "I'm sorry, I'm not equipped to handle technical issues. Please contact our technical support department.",
        "options": {}
    },
    "billing_help_response": {
        "text": "For billing inquiries, please contact our billing department.",
        "options": {}
    }
}
