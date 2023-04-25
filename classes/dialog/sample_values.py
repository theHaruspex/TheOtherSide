

sample_portrait_path = "resources/images/the_prophetess.jpg"
sample_background_path = "resources/images/dialogue_background.jpg"
prophetess_dialogue = {
    "start": {
        "text": "Welcome, traveler. You seek guidance?",
        "options": {
            "Yes": "guidance_response",
            "No": "farewell"
        }
    },
    "guidance_response": {
        "text": "Speak.",
        "options": {
            "What can you guide me on?": "guidance_description",
            "I seek a quest.": "quest"
        }
    },
    "guidance_description": {
        "text": "Direction.",
        "options": {
            "Can you be more specific?": "specific_guidance",
            "I decline.": "farewell"
        }
    },
    "specific_guidance": {
        "text": "Dangerous path ahead.",
        "options": {
            "Thank you.": "farewell",
            "Can you tell me more?": "specific_guidance_more"
        }
    },
    "specific_guidance_more": {
        "text": "Monsters.",
        "options": {
            "Thank you.": "farewell"
        }
    },
    "quest": {
        "text": "Journey.",
        "options": {
            "What quest?": "quest_description",
            "I decline.": "farewell"
        }
    },
    "quest_description": {
        "text": "Retrieve artifact.",
        "options": {
            "What artifact?": "artifact_description",
            "I decline.": "farewell"
        }
    },
    "artifact_description": {
        "text": "Lost amulet of power.",
        "options": {
            "Where was it lost?": "where_description",
            "I decline.": "farewell"
        }
    },
    "where_description": {
        "text": "Deep in forest.",
        "options": {
            "Can you mark it on my map?": "mark_map",
            "I decline.": "farewell"
        }
    },
    "mark_map": {
        "text": "Yes.",
        "options": {}
    },
    "farewell": {
        "text": "Farewell.",
        "options": {}
    }
}