import random  # Importing Random for shuffling questions
import english_grammar, general_knowledge, mathematics, physics, chemistry, programming  # Importing category modules

# Dictionary to map category names to their respective modules
categories = {
    "English Grammar": english_grammar,
    "General Knowledge": general_knowledge,
    "Mathematics": mathematics,
    "Physics": physics,
    "Chemistry": chemistry,
    "Programming": programming
}


# Function to ask a question and validate the answer
def ask_question(question, options, answer):
    print("\n" + question)
    
    index = 1  # Manual index variable
    for option in options:
        print(f" {option}")
        index += 1  # Increment index manually

    
    while True:
        try:
            user_input = (input("Enter your choice (A,B,C,D): ")).strip().upper()
            if  user_input in ["A","B","C","D"]:
                break
            else:
                print("Invalid choice, please enter valid option between (A,B,C,D)")
        except ValueError:
            print("Invalid input! Please enter an alphabet.")

    return user_input == answer   # Return True if correct, else False

# Function to run the quiz
def start_quiz():
    print("Welcome to the Quiz Game!\n")
    
    # # Display categories

    print("\tSelect a category:\n")

    index = 1  # Initialize manual index
    category_list = [f"{index + i}. {category}" for i, category in zip(range(len(categories)), categories.keys())]

    print(*category_list, sep="\n")

    while True:
        try:
            category_choice = int(input("\nEnter category number: "))
            if 1 <= category_choice <= len(categories):
                selected_category = list(categories.keys())[category_choice - 1]
                break
            else:
                print("Invalid category choice.")
        except ValueError:
            print("Please enter a valid number.")

    # Display difficulty levels
    print("\nSelect difficulty level:\n")
    difficulty_levels = ["easy", "medium", "hard"]
    for i, level in enumerate(difficulty_levels, 1):
        print(f"{i}. {level.capitalize()}")

    while True:
        try:
            difficulty_choice = int(input("\nEnter difficulty number: "))
            if 1 <= difficulty_choice <= len(difficulty_levels):
                selected_difficulty = difficulty_levels[difficulty_choice - 1]
                break
            else:
                print("Invalid difficulty choice.")
        except ValueError:
            print("Please enter a valid number.")

    # Fetch the selected category questions
    category_module = categories[selected_category]
    questions = category_module.questions[selected_difficulty]

    # Shuffle and select 10 questions
    random.shuffle(questions)
    questions = questions[:10]

    # Start quiz
    score = 0
    for q in questions:
        if ask_question(q["question"], q["options"], q["answer"]):
            print("Correct!\n")
            score += 1
        else:
            print(f"Wrong! The Correct Answer was: {q['answer']}\n")

    # Display final score
    print(f"Quiz Over! Your Score: {score}/10")

# Run the quiz
if __name__ == "__main__":
    start_quiz()
