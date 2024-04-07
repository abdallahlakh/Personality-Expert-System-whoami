# Import libraries
import aima.utils
import aima.logic
def ask_selected_indirect_questions(KB, trait_matches):
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
            for personality in trait_matches:
                if list(aima.logic.fol_fc_ask(KB, aima.utils.expr(f'HasTrait(Walter, {question["trait2"]}) & {personality}(Walter)'))):
                    trait_matches[personality] += 1
                    break
        else:
            KB.tell(aima.utils.expr(f'Not({question["trait"]}(Walter))'))

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

    # Create a dictionary to keep track of the number of matching traits for each personality type
    trait_matches = {personality: 0 for personality in personality_types}

    # Ask the selected indirect questions and update trait_matches
    ask_selected_indirect_questions(KB, trait_matches)

    # Calculate the percentage match for each personality type
    for personality in personality_types:
        answer = aima.logic.fol_fc_ask(KB, aima.utils.expr(f'{personality}(Walter)'))
        print(trait_matches)
        percentage_match = (trait_matches[personality] / len(rules)) * 100
        print(f'Is Walter a {personality}?')
        print('True' if list(answer) else 'False')
        print(f'Percentage match: {percentage_match}%')

# Tell python to run main method
if __name__ == "__main__":
    main()