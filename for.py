# Import libraries
import re
import aima.utils
import aima.logic

# Explanation Unit
def explain(rule, fact):
    print(f"The rule {rule} was fired because of the fact {fact}.")

# Working Memory
working_memory = []

# Agenda
agenda = []
def ask_selected_indirect_questions(KB):
    # Define the selected indirect questions
    selected_indirect_questions = [
        {"question": "Do you enjoy reading books?", "trait": "LikesReading", "trait2": "Openness"},
        {"question": "Do you find it easy to stay organized?", "trait": "IsOrganized", "trait2": "Conscientiousness"},
        {"question": "Do you enjoy being around people?", "trait": "IsSocial", "trait2": "Extraversion"},
        {"question": "Do you often feel sympathy for others?", "trait": "IsSympathetic", "trait2": "Agreeableness"},
        {"question": "Do you often feel nervous?", "trait": "GetsNervous", "trait2": "Neuroticism"},
    ]
        # Ask the selected indirect questions
    for question in selected_indirect_questions:
        answer = input(question["question"] + " (yes/no): ")
        if answer.lower() == "yes":
            KB.tell(aima.utils.expr(f'{question["trait"]}(Walter)'))
            working_memory.append(f'{question["trait"]}(Walter)')
            explain(f'{question["trait"]}(Walter)', f'{question["trait2"]}(Walter)')
        else:
            KB.tell(aima.utils.expr(f'Not({question["trait"]}(Walter))'))
            working_memory.append(f'Not({question["trait"]}(Walter)')
            explain(f'Not({question["trait"]}(Walter)', f'Not({question["trait2"]}(Walter)')


# The main entry point for this module
def main():
    # Create an array to hold clauses
    clauses = []

    # Add first-order logic clauses (rules and fact)
    personality_types = ['Alpha', 'Beta', 'Sigma', 'Omega', 'Gamma', 'Delta', 'Epsilon', 'Zeta', 'Theta', 'Iota']
    rules = [
        'HasTrait(x, Extraversion) & Not(HasTrait(x, Neuroticism)) & HasTrait(x, Conscientiousness) & HasTrait(x, Openness) & Not(HasTrait(x, Agreeableness)) ==> Alpha(x)',
        'Not(HasTrait(x, Extraversion)) & HasTrait(x, Agreeableness) & HasTrait(x, Neuroticism) & Not(HasTrait(x, Openness)) & Not(HasTrait(x, Conscientiousness)) ==> Beta(x)',
        'HasTrait(x, Openness) & Not(HasTrait(x, Agreeableness)) & Not(HasTrait(x, Conscientiousness)) & Not(HasTrait(x, Extraversion)) & Not(HasTrait(x, Neuroticism)) ==> Sigma(x)',
        'Not(HasTrait(x, Openness)) & Not(HasTrait(x, Conscientiousness)) & HasTrait(x, Neuroticism) & Not(HasTrait(x, Extraversion)) & Not(HasTrait(x, Agreeableness)) ==> Omega(x)',
        'HasTrait(x, Openness) & HasTrait(x, Conscientiousness) & Not(HasTrait(x, Extraversion)) & HasTrait(x, Agreeableness) & Not(HasTrait(x, Neuroticism)) ==> Gamma(x)',
        'HasTrait(x, Openness) & HasTrait(x, Conscientiousness) & HasTrait(x, Extraversion) & HasTrait(x, Agreeableness) & Not(HasTrait(x, Neuroticism)) ==> Delta(x)',
        'Not(HasTrait(x, Openness)) & Not(HasTrait(x, Conscientiousness)) & Not(HasTrait(x, Extraversion)) & Not(HasTrait(x, Agreeableness)) & Not(HasTrait(x, Neuroticism)) ==> Epsilon(x)',
        'HasTrait(x, Openness) & Not(HasTrait(x, Conscientiousness)) & HasTrait(x, Extraversion) & Not(HasTrait(x, Agreeableness)) & Not(HasTrait(x, Neuroticism)) ==> Zeta(x)',
        'HasTrait(x, Agreeableness) & HasTrait(x, Extraversion) & Not(HasTrait(x, Neuroticism)) & Not(HasTrait(x, Conscientiousness)) & Not(HasTrait(x, Openness)) ==> Theta(x)',
        'HasTrait(x, Conscientiousness) & Not(HasTrait(x, Extraversion)) & Not(HasTrait(x, Neuroticism)) & Not(HasTrait(x, Agreeableness)) & Not(HasTrait(x, Openness)) ==> Iota(x)'
    ]
     # Add indirect questions
    indirect_questions = [
    'LikesReading(x) ==> HasTrait(x, Openness)',
    'Not(LikesReading(x)) ==> Not(HasTrait(x, Openness))',
    'LikesNewExperiences(x) ==> HasTrait(x, Openness)',
    'Not(LikesNewExperiences(x)) ==> Not(HasTrait(x, Openness))',
    'IsOrganized(x) ==> HasTrait(x, Conscientiousness)',
    'Not(IsOrganized(x)) ==> Not(HasTrait(x, Conscientiousness))',
    'IsCareful(x) ==> HasTrait(x, Conscientiousness)',
    'Not(IsCareful(x)) ==> Not(HasTrait(x, Conscientiousness))',
    'IsSocial(x) ==> HasTrait(x, Extraversion)',
    'Not(IsSocial(x)) ==> Not(HasTrait(x, Extraversion))',
    'LikesParties(x) ==> HasTrait(x, Extraversion)',
    'Not(LikesParties(x)) ==> Not(HasTrait(x, Extraversion))',
    'IsSympathetic(x) ==> HasTrait(x, Agreeableness)',
    'Not(IsSympathetic(x)) ==> Not(HasTrait(x, Agreeableness))',
    'LikesHelpingOthers(x) ==> HasTrait(x, Agreeableness)',
    'Not(LikesHelpingOthers(x)) ==> Not(HasTrait(x, Agreeableness))',
    'GetsNervous(x) ==> HasTrait(x, Neuroticism)',
    'Not(GetsNervous(x)) ==> Not(HasTrait(x, Neuroticism))',
    'WorriesALot(x) ==> HasTrait(x, Neuroticism)',
    'Not(WorriesALot(x)) ==> Not(HasTrait(x, Neuroticism))'
    ]

    
    for rule in rules + indirect_questions:
        clauses.append(aima.utils.expr(rule))

    # Create a first-order logic knowledge base (KB) with clauses
    KB = aima.logic.FolKB(clauses)
    trait_matches = {personality: 0 for personality in personality_types}

    # Create a dictionary to keep track of the number of matching traits for each personality type
    trait_matches = {personality: 0 for personality in personality_types}
    # Ask the selected indirect questions and update trait_matches
    ask_selected_indirect_questions(KB, trait_matches)
    #declare to me a list of max 4 length
    walter_traits = []
    # Calculate the percentage match for each personality type
    for personality in personality_types:
        # part 1 check if Walter is a personality
        answer = aima.logic.fol_fc_ask(KB, aima.utils.expr(f'{personality}(Walter)'))
        print(f'Walter is {personality} ' if list(answer) else f'Walter is not {personality} ')
        




























        # part 2 calculate the matching percentage       
        walter_traits = []
        
        for k in KB.clauses:
            # Check if the clause matches the format HasTrait(Walter, Trait) or Not(HasTrait(Walter, Trait))
            if str(k).startswith("HasTrait(Walter") or str(k).startswith("Not(HasTrait(Walter"):
                # If it does, add it to the list of Walter's traits
                walter_traits.append(str(k))
                # If the list already has four traits, break the loop
                if len(walter_traits) == 4:  
                    break
                    
            # Check if the clause implies the current personality
            if f"=> {personality}(x)" in str(k):
                
                # Extract the traits required for the current personality
                required_traits_str = str(k).split("==>")[0]
                required_traits = re.findall(r'(HasTrait\(x, \w+\)|Not\(HasTrait\(x, \w+\)\))', required_traits_str)
                
                # Replace 'x' with 'Walter' in the required traits
                required_traits = [re.sub(r'\(x,', '(Walter,', trait) for trait in required_traits]
        
        # Calculate the matching percentage after the loop
        matching_traits = set(required_traits).intersection(set(walter_traits))
        matching_percentage = (len(matching_traits) / len(required_traits)+0.2) * 100
        print(f"Matching percentage for {personality}: {matching_percentage}%")  


if __name__ == "__main__":
    main()