**Experiment 1: Agile and Scrum Demo**

**Aim**

**To perform and understand the Agile methodology and Scrum framework by simulating an MLOps project lifecycle, including Scrum roles, Product Backlog, Sprint Planning, Daily Scrum, Sprint Review, Sprint Retrospective, and the development of a simple Machine Learning model.**

**Learning Objectives**

After completing this experiment, students will be able to:

* Understand Agile principles and the Scrum framework.
* Identify Scrum roles and responsibilities.
* Create a Product Backlog and Sprint Backlog.
* Conduct Scrum ceremonies such as Sprint Planning, Daily Scrum, Sprint Review, and Sprint Retrospective.
* Develop a simple Machine Learning model using Agile practices.
* Understand how Agile is applied in MLOps projects.

**Real-Time Scenario**

Suppose a company wants to develop an AI system that classifies Iris flowers.

Instead of developing the entire system at once, the company follows the **Agile Scrum methodology**.

The development team works in **small iterations (Sprints)**.

During each Sprint, the team:

* plans the work,
* develops a part of the project,
* tests it,
* reviews progress,
* improves the next Sprint.

Today, students will simulate this entire process.

**Step 1: Create the MLOps Project**

**Objective**

Create the project workspace.

**Procedure**

Open **VS Code**.

Open the folder

D:\MLOps\_Agile\_Demo

Create the following folders.

MLOps\_Agile\_Demo

│

├── data

├── src

├── models

├── docs

└── README.md

**Activity**

Students create the project structure.

**Outcome**

Project workspace is ready.

**Step 2: Scrum Team Formation**

**Objective**

Understand Scrum roles.

**Procedure**

Assume the following team.

| **Student** | **Scrum Role** |
| --- | --- |
| Student 1 | Product Owner |
| Student 2 | Scrum Master |
| Student 3 | ML Engineer |
| Student 4 | Data Engineer |
| Student 5 | Tester |

If only one student is performing the experiment, assume all five roles.

**Responsibilities**

**Product Owner**

The Product Owner interacts with the customer.

Responsibilities

* Defines project requirements
* Prioritizes work
* Maintains Product Backlog
* Accepts completed work

Example

"Develop an Iris Flower Classification model with at least 95% accuracy."

**Scrum Master**

The Scrum Master manages the Sprint.

Responsibilities

* Conduct Sprint Planning
* Conduct Daily Scrum
* Remove blockers
* Ensure Scrum rules are followed

Example

"Today's Sprint Goal is to prepare the dataset and train the model."

**ML Engineer**

Responsibilities

* Select ML algorithm
* Train the model
* Improve model performance
* Save trained model

**Data Engineer**

Responsibilities

* Collect dataset
* Clean data
* Split dataset
* Prepare features

**Tester**

Responsibilities

* Test the ML model
* Verify prediction accuracy
* Report bugs
* Validate output

**Step 3: Create Product Backlog**

**Objective**

Prepare all project requirements.

Create a file named

Product\_Backlog.xlsx

or

Product\_Backlog.md

Add the following user stories.

| **ID** | **User Story** | **Priority** |
| --- | --- | --- |
| US1 | Download Iris Dataset | High |
| US2 | Clean Dataset | High |
| US3 | Train Decision Tree Model | High |
| US4 | Evaluate Accuracy | Medium |
| US5 | Save Model | Medium |
| US6 | Prepare Documentation | Low |

Discuss why High Priority tasks are selected first.

**Step 4: Sprint Planning**

**Objective**

Select tasks for Sprint 1.

Assume

Sprint Duration

1 Week

Sprint Goal

Build the first working ML model.

Sprint Backlog

| **Task** |
| --- |
| Download Dataset |
| Data Cleaning |
| Train Model |
| Evaluate Accuracy |

Students estimate time required.

Example

| **Task** | **Time** |
| --- | --- |
| Download Dataset | 20 min |
| Data Cleaning | 30 min |
| Train Model | 30 min |
| Testing | 20 min |

**Step 5: Daily Scrum Meeting**

Each student answers three questions.

**Product Owner**

Yesterday

Requirements finalized.

Today

Review Sprint progress.

Blockers

None.

**Scrum Master**

Yesterday

Sprint planned.

Today

Conduct Daily Scrum.

Blockers

Git installation issue.

**ML Engineer**

Yesterday

Selected Decision Tree.

Today

Train model.

Blockers

Dataset unavailable.

**Data Engineer**

Yesterday

Downloaded Iris dataset.

Today

Split dataset.

Blockers

Missing library.

**Tester**

Yesterday

Prepared test cases.

Today

Evaluate accuracy.

Blockers

None.

**Step 6: Build the ML Model**

Create

src/iris\_demo.py

Students execute the provided Python code.

Run

python iris\_demo.py

Expected output

Accuracy = 0.96

(or similar)

from sklearn.datasets import load\_iris

from sklearn.model\_selection import train\_test\_split

from sklearn.tree import DecisionTreeClassifier

from sklearn.metrics import accuracy\_score

iris = load\_iris()

X = iris.data

y = iris.target

X\_train, X\_test, y\_train, y\_test = train\_test\_split(

X,

y,

test\_size=0.2,

random\_state=42

)

model = DecisionTreeClassifier()

model.fit(X\_train, y\_train)

prediction = model.predict(X\_test)

accuracy = accuracy\_score(y\_test, prediction)

print("Accuracy:", accuracy)

**Step 7: Sprint Review**

The team demonstrates the completed work.

Checklist

✅ Dataset downloaded

✅ Data cleaned

✅ Model trained

✅ Accuracy generated

Discuss

* Was Sprint Goal achieved?
* What was delivered?

**Step 8: Sprint Retrospective**

Discuss

**What went well?**

Example

Good communication

**What problems occurred?**

Example

Python packages were missing.

**Improvements**

Example

Install required libraries before Sprint starts.

**Step 9: Sprint Increment**

Deliverables

* Working ML Model
* Python Source Code
* Documentation
* Accuracy Report

**Expected Output**

Students should successfully:

* Create the project workspace.
* Assign Scrum roles.
* Prepare Product Backlog.
* Plan Sprint.
* Conduct Daily Scrum.
* Train the ML model.
* Review Sprint.
* Conduct Sprint Retrospective.
* Understand the Agile workflow in an MLOps project.

**Result**

**The Agile and Scrum methodology was successfully demonstrated by simulating an MLOps project. Scrum roles, Product Backlog, Sprint Planning, Daily Scrum, Sprint Review, Sprint Retrospective, and the development of a simple Machine Learning model were successfully performed.**