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
- 'Satisfied with their care' is dictated as answering 'Yes' to the question 'Are you satisfied with your care? '. 

### Answers; deployment_engineer.py for my interim calculations. You can run this as well to output the respective results.
1) Enrolled: 1725; individual sums: [845, 312, 568] for completed, cancelled, and scheduled respectively.
2) Enrolled as of 3/28 & completed at least one module: 102
3) Highest viewed module: 800.0 (2319); {800.0: 2319, 799.0: 1960, 795.0: 1948, 798.0: 1786, 796.0: 1299, 797.0: 1194, 801.0: 1082, 806.0: 433, 807.0: 416, 802.0: 367, 805.0: 299, 808.0: 249, 804.0: 248, 803.0: 241}
4) Highest completion rate module: 803.0 (43%); {798.0: 0.405, 799.0: 0.345, 800.0: 0.257, 796.0: 0.390, 795.0: 0.244, 806.0: 0.402, 807.0: 0.351, 802.0: 0.354, 805.0: 0.425, 803.0: 0.432} 
5) Those satisfied with their care: 514

