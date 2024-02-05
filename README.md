# Uputstvo za pokretanje


# Knowledge space theory
In electronically supported learning, students often have to take very large tests to automatically determine what students know.
The *Knowledge Space Theory* (KST) is a set concepts and structures that aims to assess and represent one’s knowledge state. Assess students' knowledge is an important task in order to check if someone is capable to perform certain tasks or offering guidance toward mastering a particular subject.\

In KST, knowledge states are depicted as a collection of **problems** that an individual is qualified to solve. A set of such problems is called a **domain**.\
Each problem represents one specific task to be performed withing a domain. A specific problem is called an **instance**.\
A student's knowledge state is the subset of domain problems that a student can answer correctly under ideal circumstances.

![image](https://github.com/branislavroljic/semantic-web-kst/assets/58853003/c290e8eb-3eba-4268-840d-a6591e6facd2)


Cvorovi u grafu predstavljaju stanja znanja, a lukovi grafa predstavljaju relaciju uključivanja, odnosno znače da je jedno stanje znanja podskup drugog stanja znanja
Intuitively we can say that before mastering item c, we need to master item b or item a. 

Da bi strutkura znanja bila prostor učenja, potrebno je da zadovolji i sledeće aksiome:
Learning Smoothness : This property estabilishes the existence of enough knowledge states such that every state can be mastered learning one concept at a time. 
Learning Consistency: This property ensures the existence of enough states to represent any feasible order of item mastery.

## Projekat

Na narednoj slici dat je prikaz KST ontologije u Protégé-u.

![image](https://github.com/branislavroljic/semantic-web-kst/assets/58853003/64e2c30d-7fa1-4ca5-90db-b333e22a2a25)


Hijerarhija klasa je reprezentovana sljedećim dijagramom:

![image](https://github.com/branislavroljic/semantic-web-kst/assets/58853003/7959ec57-ce6c-4ef7-b1c5-2062acc843ac)

Prostor znanja se sastoji iz problema, pri čemu su individuali klase Problem povezani tranzitivnim, inverznim property-jima ```hasSubProblem``` i ```isSubProblemOf```.\
Problemi se sastoje iz pripadajućih pitanja, dok svako pitanje sadrži određeni broj odgovora koji se nude studentu.\

OWL does not provide any built-in primitives for part-whole relations. The study of part-whole relations is called "mereology". Za potrebe reprezentovanja part-whole relacija korištena je ontologija: https://www.w3.org/2001/sw/BestPractices/OEP/SimplePartWhole/part.owl. Potrebno je naglasiti da je zbog semantike i načina rada OWL reasoner-a odabrana ```hasPart``` relacija.\

Data propery-jem ```hasCorrect```, Range-a `xsd:boolean` se naznačava da li je odgovor tačan ili "maska".\
Klasom ```AssessmentTest``` predstavljen je test kreiran od strane domenskog stručnjaka, a koji rade studenti. ```AssessmentTest``` se sastoji iz skupa pitanja, na koje studenti daju odgovore. Rezultati testa svakog studenta su reprezentovani klasom ```StudentAssessmentTest```.

Za rezonovanje ontologije korišten je *HermiT Reasoner*

Nakon kreiranja ontologije, izvršeno je kreiranje individuala.

### Upiti nad ontologijom
U programskom jeziku `Python` upotrebom `OwlReady2` paketa kreirana je konzolna aplikacija za vršenje upita nad ontologijom.
OwlReady2 can load, modify, save ontologies, and it supports reasoning via HermiT (included). OwlReady2 omogućava pisanje SPARQL upita u Python programskom jeziku. 
Ponuđene opcije:

1. Izlistavanje studenata
2. Pronalazak prostora znanja za određenog studenta (po imenu studenta)
3. Pronalazak studenata koji mogu da riješe određeni problem
4. Pronalazak sljedećih problema koje student može da riješi (po imenu studenta)
5. Pronalazak studenata koji se nalaze u određenom prostoru znanja
6. Pronalazak optimalne putanje učenja



