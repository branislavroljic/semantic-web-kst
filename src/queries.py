from owlready2 import *

def find_students():
    query = f"""
        PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
        PREFIX owl: <http://www.w3.org/2002/07/owl#>
        PREFIX ks: <http://www.semanticweb.org/legion/ontologies/2023/11/ks_ontology#>

        SELECT DISTINCT ?fullname
        WHERE {{
          ?student rdf:type ks:Student.
            ?student ks:hasFullName ?fullname.
        }}
    """
    students = list(default_world.sparql(query))

    for student in students:
        print(student[0])
    return students

def find_problems():
    query = f"""
        PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
        PREFIX owl: <http://www.w3.org/2002/07/owl#>
        PREFIX ks: <http://www.semanticweb.org/legion/ontologies/2023/11/ks_ontology#>

        SELECT DISTINCT ?title
        WHERE {{
           ?problem rdf:type ks:Problem.
            ?problem ks:hasTitle ?title.
        }}
    """
    problems = list(default_world.sparql(query))

    for problem in problems:
        print(problem[0])
    return [problem[0] for problem in problems]


def find_students_for_problem(problem_title):
    query = f"""
        PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
        PREFIX owl: <http://www.w3.org/2002/07/owl#>
        PREFIX ks: <http://www.semanticweb.org/legion/ontologies/2023/11/ks_ontology#>

        SELECT DISTINCT ?fullname
        WHERE {{
          ?assessmentTest rdf:type ks:AssessmentTest.
          ?student rdf:type ks:Student.
          ?studentAssessmentTest rdf:type ks:StudentAssessmentTest.
          ?problem rdf:type ks:Problem.

          ?assessmentTest part:hasPart ?question.
          ?question part:hasPart ?correctAnswer.
          ?correctAnswer ks:hasCorrect true.

          ?student ks:hasFullName ?fullname.
          ?student ks:hasAssessmentTest ?studentAssessmentTest.
          ?studentAssessmentTest ks:belongsToTest ?assessmentTest.
          ?studentAssessmentTest part:hasPart ?studentAnswer.

          ?problem part:hasPart ?question.
          ?problem ks:hasTitle ?title

          FILTER(?studentAnswer = ?correctAnswer && ?title = "{problem_title}")
        }}
    """
    results = list(default_world.sparql(query))

    for result in results:
        print(result[0])

def find_students_for_knowladge_state(problems):
    problem_values = " ".join(f'"{problem}"' for problem in problems)
    print(problem_values)
    query = f"""
            PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
            PREFIX owl: <http://www.w3.org/2002/07/owl#>
            PREFIX ks: <http://www.semanticweb.org/legion/ontologies/2023/11/ks_ontology#>

            SELECT DISTINCT ?student
            WHERE {{
            ?student rdf:type ks:Student.
            ?problem rdf:type ks:Problem.
            ?problem ks:hasTitle ?title.
            
            FILTER (
                EXISTS {{
                VALUES ?title {{
                  {problem_values}
                }}
                ?assessmentTest rdf:type ks:AssessmentTest.
                ?studentAssessmentTest rdf:type ks:StudentAssessmentTest.

                ?assessmentTest part:hasPart ?question.
                ?problem part:hasPart ?question.
                
                ?question part:hasPart ?correctAnswer.
                ?correctAnswer ks:hasCorrect true.

                ?studentAssessmentTest ks:belongsToTest ?assessmentTest.
                ?studentAssessmentTest part:hasPart ?studentAnswer.
                ?studentAnswer rdf:type ks:Answer.
                FILTER(?studentAnswer = ?correctAnswer)
                }}
            )
            }}
            """
    results = list(default_world.sparql(query))

    for result in results:
            print(result[0])


def find_knowledge_state_for_student(student_name):
    query = f"""
        PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
        PREFIX owl: <http://www.w3.org/2002/07/owl#>
        PREFIX ks: <http://www.semanticweb.org/legion/ontologies/2023/11/ks_ontology#>

        SELECT distinct ?title
        WHERE {{
        ?assessmentTest rdf:type ks:AssessmentTest.
        ?student rdf:type ks:Student.
        ?studentAssessmentTest rdf:type ks:StudentAssessmentTest.
        ?problem rdf:type ks:Problem.
        ?problem ks:hasTitle ?title.

        ?assessmentTest part:hasPart ?question.
        ?question part:hasPart ?correctAnswer.
        ?correctAnswer ks:hasCorrect true.

        ?student ks:hasFullName ?fullname.
        ?student ks:hasAssessmentTest ?studentAssessmentTest.
        ?studentAssessmentTest ks:belongsToTest ?assessmentTest.
        ?studentAssessmentTest part:hasPart ?studentAnswer.

        ?problem part:hasPart ?question.

        FILTER(?studentAnswer = ?correctAnswer && regex(STR(?fullname), "{student_name}", "i"))

        }}
        """
    results = list(default_world.sparql(query))
    
    for result in results:
        print(result[0])


def find_next_problems_for_student(student_name):
    query = f"""
    PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
    PREFIX owl: <http://www.w3.org/2002/07/owl#>
    PREFIX ks: <http://www.semanticweb.org/legion/ontologies/2023/11/ks_ontology#>

    SELECT DISTINCT ?problemTitle ?nextProblemTitle
    WHERE {{
        ?assessmentTest rdf:type ks:AssessmentTest.
        ?student rdf:type ks:Student.
        ?studentAssessmentTest rdf:type ks:StudentAssessmentTest.
        ?problem rdf:type ks:Problem.

        ?assessmentTest part:hasPart ?question.
        ?question part:hasPart ?correctAnswer.
        ?correctAnswer ks:hasCorrect true.

        ?student ks:hasFullName ?fullname.
        ?student ks:hasAssessmentTest ?studentAssessmentTest.
        ?studentAssessmentTest ks:belongsToTest ?assessmentTest.
        ?studentAssessmentTest part:hasPart ?studentAnswer.

        ?problem part:hasPart ?question.

        ?problem ks:isSubProblemOf ?nextProblem.

        ?problem ks:hasTitle ?problemTitle.
        ?nextProblem ks:hasTitle ?nextProblemTitle.

        FILTER(?studentAnswer = ?correctAnswer && regex(?fullname, "{student_name}", "i"))
    }}
    """

    results = list(default_world.sparql(query))
    for result in results: print(result[0], " -> ", result[1])




    # qa = """
    #  PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
    #     PREFIX owl: <http://www.w3.org/2002/07/owl#>
    #     PREFIX ks: <http://www.semanticweb.org/legion/ontologies/2023/11/ks_ontology#>

    #     SELECT ?question ?correctAnswer
    #     WHERE {
    #     ks:Assessment_Test_1 rdf:type ks:AssessmentTest .
    #     ks:Assessment_Test_1 part:hasPart ?question .
    #     ?question part:hasPart ?correctAnswer .
    #     ?correctAnswer ks:hasCorrect "true"^^xsd:boolean .
    #     }
    # """
    # qaResults = list(default_world.sparql(qa))
    # for qaResult in  qaResults : print(qaResult[0], " : ", qaResult[1])


def find_optimum_learning_path(current_problem, path, visited):
    visited.add(current_problem)

    # Check if last
    if not current_problem.isSubProblemOf:
        return path

    optimum_path = None
    max_correct_answers = 0

    for next_problem in current_problem.isSubProblemOf:
        if next_problem not in visited:
            sub_path = find_optimum_learning_path(next_problem, path + [next_problem], visited.copy())

            total_correct_answers = count_correct_answers(next_problem.hasTitle[0])

            if total_correct_answers > max_correct_answers:
                max_correct_answers = total_correct_answers
                optimum_path = sub_path

    return optimum_path

def count_correct_answers(problem_title):
    query = f"""
    PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
    PREFIX owl: <http://www.w3.org/2002/07/owl#>
    PREFIX ks: <http://www.semanticweb.org/legion/ontologies/2023/11/ks_ontology#>

   SELECT (COUNT(?student) as ?correctAnswerCount)
    WHERE {{
        ?assessmentTest rdf:type ks:AssessmentTest.
        ?student rdf:type ks:Student.
        ?studentAssessmentTest rdf:type ks:StudentAssessmentTest.
        ?problem rdf:type ks:Problem.

        ?problem ks:hasTitle ?title

        ?problem part:hasPart ?question.
        ?assessmentTest part:hasPart ?question.
        ?question part:hasPart ?correctAnswer.
        ?correctAnswer ks:hasCorrect true.
        
        ?student ks:hasAssessmentTest ?studentAssessmentTest.
        ?studentAssessmentTest ks:belongsToTest ?assessmentTest.
        ?studentAssessmentTest part:hasPart ?studentAnswer.
        ?studentAnswer rdf:type ks:Answer.
        ?studentAnswer ks:hasCorrect true.
        FILTER(?studentAnswer = ?correctAnswer && ?title = "{problem_title}")
    }}
    """

    results = list(default_world.sparql(query))
    return results[0][0]
