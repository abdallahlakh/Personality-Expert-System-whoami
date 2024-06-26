# **Personality Expert System** #**whoami**
## **Topic Description:**
The chosen topic is a Personality Expert System based on the Big Five personality traits. I've used the expertise from the book  **"Introduction to the Big Five Personality Test" by William R . Dimas** that tells us how to detect them with an indirect question quiz to know if a person LikesReading, IsOrganized, IsSocial, IsSympathetic, GetsNervous... This information is used to decide their matching to the Big Five personality types mentioned in the book (Openness, Conscientiousness, Extraversion, Agreeableness, Neuroticism). Then, according to these personalities, the system makes a decision about the type of your main personality (alpha, sigma, gamma, beta, etc.) using the previous decisions then display facts about this types. The system uses First-Order Logic (FOL) and the forward-chaining inference algorithm to infer personality types.

## **Problem Formulation:**
The problem was formulated into different Expert System (ES) elements as follows:

### **Knowledge Base:**
The knowledge base consists of a set of rules that map certain combinations of traits to personality types (Alpha, Beta, Sigma, etc.) and the matching of input personalities (LikesReading, IsOrganized, IsSocial, IsSympathetic, GetsNervous) to the Big Five types (Openness, Conscientiousness, Extraversion, Agreeableness, Neuroticism). These rules are expressed in First-Order Logic (FOL). The knowledge base also includes facts, which are the answers to indirect questions, for example:
LikesReading(Mourad)
Not(IsOrganized(Mourad))
Not(IsSocial(Mourad))
Not(IsSympathetic(Mourad))
Not(GetsNervous(Mourad))
These can be used to infer the presence or absence of certain traits.

### **Inference Engine:**
The inference engine uses the forward-chaining inference algorithm. It starts with the known facts from the inputs of users, for example:
LikesReading(Mourad)
Not(IsOrganized(Mourad))
Not(IsSocial(Mourad))
Not(IsSympathetic(Mourad))
Not(GetsNervous(Mourad))
Then it applies the rules to infer new facts, for example:
HasTrait(Mourad, Openness)
Not(HasTrait(Mourad, Conscientiousness))
Not(HasTrait(Mourad, Extraversion))
Not(HasTrait(Mourad, Agreeableness))
Not(HasTrait(Mourad, Neuroticism))
Sigma(Mourad)
This process is repeated for all the main types (alpha, beta, etc.) until no more new facts can be inferred. The inference engine is provided by the aima.logic library.

### **User Interface:**
I've integrated the model into a Flask web app to make it easy for the normal user to use the model by submitting the inputs. The app also processes the model and displays the output from the browser#for simplicity#, showing how the inference process happens. It asks the user indirect questions, reads the answers from a JSON file, and updates the knowledge base accordingly. It also prints the inferred personality types and the matching percentages.

### **Explanation System:**
The explanation system is implicit in the output of the inference engine. It shows which personality types match the inferred traits and explains to the user why they get the results of the rule. It calculates a matching percentage for each personality type and explains why?.

### **Agenda:**
In the Agenda part, I've divided the execution of rules into two parts. The first with priority of 0 are rules that calculate the Big Five types (Openness, Conscientiousness, Extraversion, Agreeableness, Neuroticism). Then it's the turn of the rules with priority of 1 to be executed using the new facts reached by rules of priority 0 to determine the main type of personality (alpha, sigma, beta, etc.).

### **Working Memory:**
In the working memory, I've used LIFO (Last In, First Out). Each new fact reached is pushed there. When new facts come, I pop this LIFO from the old facts and push the new facts. Then I print the state of my working memory.

## **In conclusion,**
 this Personality Inference System is a simple but powerful application of Expert Systems in the field of psychology. It could be extended with more traits, personality types, and indirect questions, and the input and output could be integrated with a user interface or a database.



## **The potential applications of this system in various industries are vast.**
 In human resources, it could be used to assess the personality traits of job applicants, aiding in the selection of candidates who are the best fit for the company culture and job requirements. In marketing, it could be used to understand customer behavior and preferences, enabling more targeted and effective campaigns. In mental health services, it could be used as a tool for psychological assessment, providing valuable insights that can guide treatment plans. In the military domain, the system could be used for personnel selection and team formation, ensuring that individuals with the right traits are assigned to roles that suit their personalities. It could also be used for psychological profiling in intelligence and security operations.

These are just a few examples of how this system could be utilized. With further development and integration, the Personality Inference System has the potential to revolutionize how we understand and interact with people in various professional contexts.

## **"Every man has three characters - that which he exhibits, that which he has, and that which he thinks he has." - Alphonse Karr**


