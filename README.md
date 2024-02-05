# Usage

### Prerequisites
- Python 3.x

### Setup

1. Clone the repository:

    ```bash
    git clone https://github.com/branislavroljic/semantic-web-kst.git
    cd semantic-web-kst
    ```

2. Create and activate a virtual environment (optional but recommended):

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

### Running the Project

Make sure your virtual environment is activated.

Run the main script:

```bash
python ./src/app.py
```

# Knowledge space theory
In electronically supported learning, students often have to take very large tests to automatically determine what students know.
The *Knowledge Space Theory* (KST) is a set concepts and structures that aims to assess and represent one’s knowledge state. Assess students' knowledge is an important task in order to check if someone is capable to perform certain tasks or offering guidance toward mastering a particular subject.

In KST, knowledge states are depicted as a collection of **problems** that an individual is qualified to solve. A set of such problems is called a **domain**.\
Each problem represents one specific task to be performed withing a domain. A specific problem is called an **instance**.\
A student's knowledge state is the subset of domain problems that a student can answer correctly under ideal circumstances.

![image](https://github.com/branislavroljic/semantic-web-kst/assets/58853003/c290e8eb-3eba-4268-840d-a6591e6facd2)

The nodes in the graph represent states of knowledge, and the edges of the graph represent the inclusion relation, meaning that one state of knowledge is a subset of another state of knowledge. Intuitively, we can say that before mastering item c, we need to master item b or item a.

For the knowledge structure to be a learning space, it is necessary to satisfy the following axioms:

**Learning Smoothness**: This property establishes the existence of enough knowledge states such that every state can be mastered by learning one concept at a time.\
**Learning Consistency**: This property ensures the existence of enough states to represent any feasible order of item mastery.

## Project

The next image provides a representation of the KST ontology in Protégé.

![image](https://github.com/branislavroljic/semantic-web-kst/assets/58853003/64e2c30d-7fa1-4ca5-90db-b333e22a2a25)


The class hierarchy is represented by the following diagram:

![image](https://github.com/branislavroljic/semantic-web-kst/assets/58853003/7959ec57-ce6c-4ef7-b1c5-2062acc843ac)

The knowledge space consists of problems, where individuals of the Problem class are connected by transitive, inverse properties `hasSubProblem` and `isSubProblemOf`.\
Problems consist of corresponding questions, and each question contains a certain number of answers offered to the student.

OWL does not provide any built-in primitives for part-whole relations. The study of part-whole relations is called "mereology". For representing part-whole relations, the ontology at https://www.w3.org/2001/sw/BestPractices/OEP/SimplePartWhole/part.owl was used. It is essential to emphasize that, due to the semantics and the way OWL reasoners operate, the `hasPart` relation was chosen.

The data property `hasCorrect`, with a range of `xsd:boolean`, indicates whether the answer is correct or a "mask."\
The class `AssessmentTest` represents a test created by a domain expert and taken by students. `AssessmentTest` consists of a set of questions to which students provide answers. The results of each student's test are represented by the class `StudentAssessmentTest`.

The *HermiT Reasoner* was used for ontology reasoning.

After creating the ontology, individuals were instantiated.

### Queries on the Ontology
Using the `OwlReady2` package in the `Python` programming language, a console application has been created for querying the ontology. OwlReady2 enables loading, modifying, and saving ontologies, and it supports reasoning via *HermiT*. Additionally, OwlReady2 allows writing *SPARQL* queries in the Python programming language.

The provided options are:

1. List students
2. Find the knowledge space for a specific student (by student's name)
3. Find students who can solve a particular problem
4. Find the next problems a student can solve (by student's name)
5. Find students located in a specific knowledge space
6. Find the optimal learning paths




