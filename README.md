# Medumo Project
Henry Wrightman 


## Information
- Python (pandas)

## Medumo Programming Assignment
### Assumptions
- Patients with > 1 procedure are listed as separate entries (rows)
- Types: 'FLEX BRONCH WITH BAL or TRANS BRONCH BX' are two distinct type entries
- As per unique case, we'll always ensure that they're listed in Tour_One; they may however be in Tour_Three as well, given ordering
- Greater than 1 procedures on the same day NOT equaling the above criteria -> 'multiple_enroll' list
- Each patient has at least one procedure scheduled on a given date (per entry)

For the logic, please refer to pulmonary_feed.py

Essentially, the main criteria is handled using straight forward predicates. The tour predicates, (distinguish tour based off of procedure) as well as the more complex, unique cases for more than one procedure per patient, are handled internally within the patient class when adding a new procedure (given that this patient has already been scheduled for another procedure prior). 

## Medumo Deployment Engineer - Data Analysis
### Assumptions
- 'Module views' are when an Event has an Event_Name = 'Node_Viewed'
- ‘Module completion’ is dictated as Event marked with Event_Name = ‘User_completed_module’

### Answers; deployment_engineer.py
1) Enrolled: 1725
2) Enrolled as of 3/28 & completed at least one module: 102
3) Highest viewed module: 800.0
4) Highest completion rate module: 798.0
5) Those satisfied with their care: 514

