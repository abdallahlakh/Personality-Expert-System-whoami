# Import libraries
import aima.utils
import aima.logic

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
        'LikesNewExperiences(x) ==> HasTrait(x, Openness)',
        'IsOrganized(x) ==> HasTrait(x, Conscientiousness)',
        'IsCareful(x) ==> HasTrait(x, Conscientiousness)',
        'IsSocial(x) ==> HasTrait(x, Extraversion)',
        'LikesParties(x) ==> HasTrait(x, Extraversion)',
        'IsSympathetic(x) ==> HasTrait(x, Agreeableness)',
        'LikesHelpingOthers(x) ==> HasTrait(x, Agreeableness)',
        'GetsNervous(x) ==> HasTrait(x, Neuroticism)',
        'WorriesALot(x) ==> HasTrait(x, Neuroticism)'
    ]

    
    for rule in rules + indirect_questions:
        clauses.append(aima.utils.expr(rule))

    # Create a first-order logic knowledge base (KB) with clauses
    KB = aima.logic.FolKB(clauses)

    # Add facts with tell
    KB.tell(aima.utils.expr("HasTrait(John, Openness)"))
    KB.tell(aima.utils.expr("HasTrait(John, Conscientiousness)"))
    KB.tell(aima.utils.expr("HasTrait(John, Extraversion)"))
    KB.tell(aima.utils.expr("Not(HasTrait(John, Agreeableness))"))
    KB.tell(aima.utils.expr("Not(HasTrait(John, Neuroticism))"))

    # Get information from the knowledge base with ask
    for personality in personality_types:
        answer = aima.logic.fol_fc_ask(KB, aima.utils.expr(f'{personality}(John)'))
        print(f'Is John a {personality}?')
        print('True' if list(answer) else 'False')

# Tell python to run main method
if __name__ == "__main__":
    main()