def fol_fc_ask(kb, alpha):
    """
    [Figure 9.3]
    A simple forward-chaining algorithm.
    """
    # TODO: improve efficiency
    kb_consts = list({c for clause in kb.clauses for c in constant_symbols(clause)})

    def enum_subst(p):
        query_vars = list({v for clause in p for v in variables(clause)})
        for assignment_list in itertools.product(kb_consts, repeat=len(query_vars)):
            theta = {x: y for x, y in zip(query_vars, assignment_list)}
            yield theta

    # check if we can answer without new inferences
    for q in kb.clauses:
        phi = unify_mm(q, alpha)
        if phi is not None:
            yield phi
    rules_priority_0 = [
    "(LikesReading(x) ==> HasTrait(x, Openness))",
    "(Not(LikesReading(x)) ==> Not(HasTrait(x, Openness)))",
    "(LikesNewExperiences(x) ==> HasTrait(x, Openness))",
    "(Not(LikesNewExperiences(x)) ==> Not(HasTrait(x, Openness)))",
    "(IsOrganized(x) ==> HasTrait(x, Conscientiousness))",
    "(Not(IsOrganized(x)) ==> Not(HasTrait(x, Conscientiousness)))",
    "(IsCareful(x) ==> HasTrait(x, Conscientiousness))",
    "(Not(IsCareful(x)) ==> Not(HasTrait(x, Conscientiousness)))",
    "(IsSocial(x) ==> HasTrait(x, Extraversion))",
    "(Not(IsSocial(x)) ==> Not(HasTrait(x, Extraversion)))",
    "(LikesParties(x) ==> HasTrait(x, Extraversion))",
    "(Not(LikesParties(x)) ==> Not(HasTrait(x, Extraversion)))",
    "(IsSympathetic(x) ==> HasTrait(x, Agreeableness))",
    "(Not(IsSympathetic(x)) ==> Not(HasTrait(x, Agreeableness)))",
    "(LikesHelpingOthers(x) ==> HasTrait(x, Agreeableness))",
    "(Not(LikesHelpingOthers(x)) ==> Not(HasTrait(x, Agreeableness)))",
    "(GetsNervous(x) ==> HasTrait(x, Neuroticism))",
    "(Not(GetsNervous(x)) ==> Not(HasTrait(x, Neuroticism)))",
    "(WorriesALot(x) ==> HasTrait(x, Neuroticism))",
    "(Not(WorriesALot(x)) ==> Not(HasTrait(x, Neuroticism)))"
    ] 
    personality_types = ['Alpha(Walter)', 'Beta(Walter)', 'Sigma(Walter)', 'Omega(Walter)', 'GammaWalter', 'Delta(Walter)', 'Epsilon(Walter)', 'Zeta(Walter)', 'Theta(Walter)', 'Iota(Walter)']
   
    

    # Define the agenda
    agenda = []
    # Convert the rules in kb.clauses to strings
    kb_clauses_str = [str(rule) for rule in kb.clauses]

    for rule_str in kb_clauses_str:
        if rule_str in rules_priority_0:
            heapq.heappush(agenda, (0, rule_str))
        elif "Walter" in rule_str:
            heapq.heappush(agenda, (0, rule_str))
        else:
            heapq.heappush(agenda, (1, rule_str))

    while True:
        new = []
        for rule in kb.clauses:
            p, q = parse_definite_clause(rule)
            print(f"The value of Q ({q}) is due to the rule P ({p}).")
            if not p:  # This checks if p is an empty list
              if q in personality_types:
                exit(0)
            for theta in enum_subst(p):
                if set(subst(theta, p)).issubset(set(kb.clauses)):
                    q_ = subst(theta, q)
                    #print('Adding to KB:', q_)
                    if all([unify_mm(x, q_) is None for x in kb.clauses + new]):
                        new.append(q_)
                        phi = unify_mm(q_, alpha)
                        if phi is not None:
                            yield phi
        if not new:
            break
        for clause in new:
            print('Adding to KB:', clause)
            kb.tell(clause)
            if clause in personality_types:
                exit(0)
    return None

