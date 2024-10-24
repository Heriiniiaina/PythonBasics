def get_input(word_type:str):
    user_input:str = input(f"Entrer a {word_type}: ") 
    return user_input

noun1 = get_input("noun")
adjective1 = get_input("adjactive")
verb1 = get_input("verb")
 
story = f"""
    Once upon a time, there was a {adjective1} {noun1} who loved to {verb1} all day.
    
"""