# Medumo Project
Henry Wrightman 


## Information
- Python (pandas)

## Medumo Programming Assignment
### Assumptions
- Patients with > 1 procedure are listed as separate entries (rows)
- Types: 'FLEX BRONCH WITH BAL or TRANS BRONCH BX' are two distinct type entries
- Each patient has at least one procedure scheduled on a given date (per entry)

For the core logic - sorting into tour, unique cases, etc please refer to patient.py. pulmonary_feed.py handles initial criteria; in this case language=English & >= 2 days until scheduled procedure.

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

