# Import libraries
import re
import aima.utils
import aima.logic
from facts import personality_facts
import json
def ask_selected_indirect_questions(KB):
    selected_indirect_questions = [
    {"question": "Would you enjoy spending a quiet afternoon immersed in a novel?", "trait": "LikesReading", "trait2": "Openness"},
    {"question": "Do you often find yourself rearranging your workspace to keep it tidy?", "trait": "IsOrganized", "trait2": "Conscientiousness"},
    {"question": "Would you enjoy attending a large social gathering?", "trait": "IsSocial", "trait2": "Extraversion"},
    {"question": "Do you feel sympathy when you hear about someone's misfortune?", "trait": "IsSympathetic", "trait2": "Agreeableness"},
    {"question": "Do you usually feel nervous when something unexpected happens?", "trait": "GetsNervous", "trait2": "Neuroticism"}
    ]
    
    # Load answers from input.json
    with open('input.json', 'r') as f:
        answers = json.load(f)

    # Tell the knowledge base based on the answers
    for question in selected_indirect_questions:
        answer = answers.get(question["trait"], "no")
        if answer.lower() == "yes":
            KB.tell(aima.utils.expr(f'{question["trait"]}(Mourad)'))
        else:
            KB.tell(aima.utils.expr(f'Not({question["trait"]}(Mourad))'))



output = {}

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
    # Ask the selected indirect questions and update trait_matches
    ask_selected_indirect_questions(KB)
    #declare to me a list of max 4 length
    walter_traits = []
    # Calculate the percentage match for each personality type
    for personality in personality_types:
        if personality not in output:
           output[personality] = []  # Initialize the key with an empty list
        # part 1 check if Mourad is a personality
        answer = aima.logic.fol_fc_ask(KB, aima.utils.expr(f'{personality}(Mourad)'))
        if list(answer):
           output[personality] = []
           print('\n\n\n\n\n\n\n\n\n\n\n\n\n')
           print(f'Mourad is {personality} ')
           for p in personality_facts:
             if p['type'] == personality:
                print("Facts:")
                for fact in p['facts']:
                    print(fact)
                    output[personality] = []
                    for p in personality_facts:
                        if p['type'] == personality:
                            output['facts']=p['facts']
                            output['Mourad'] = personality
   
           
   




























        # part 2 calculate the matching percentage       
        walter_traits = []
        
        for k in KB.clauses:
            # Check if the clause matches the format HasTrait(Mourad, Trait) or Not(HasTrait(Mourad, Trait))
            if str(k).startswith("HasTrait(Mourad") or str(k).startswith("Not(HasTrait(Mourad"):
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
                
                # Replace 'x' with 'Mourad' in the required traits
                required_traits = [re.sub(r'\(x,', '(Mourad,', trait) for trait in required_traits]
        
        # Calculate the matching percentage after the loop
        matching_traits = set(required_traits).intersection(set(walter_traits))
        matching_percentage = (len(matching_traits) / len(required_traits)) * 100
        print('\n\n\n\n\n\n\n\n\n\n\n\n\n')
        print(f"Matching percentage for {personality}: {matching_percentage}%")  
        output[personality]=({'Matching percentage': str(matching_percentage)+"%"})
        print('\n\n\n\n\n\n\n\n\n\n\n\n\n')
if __name__ == "__main__":
    main()

    with open('output.json', 'w') as f:
        json.dump(output, f)

    
    data = []
    
    with open('infrenceprocess.json', 'r') as f:
        for line in f:
            data.append(json.loads(line))
    
    # Wrap the objects in a list
    data = [data]
    
    # Write the result back to the JSON file
    with open('infrenceprocess.json', 'w') as f:
        json.dump(data, f, indent=4)