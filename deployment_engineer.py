from datetime import datetime
import xlrd
import sys
import pandas as pd
 
def scan_input():

	#workbook = xlrd.open_workbook('Deployment Engineer - Data Analysis Questions v3.xlsx')

	#worksheet = workbook.sheet_by_name('Enrollment Data')

	df = pd.ExcelFile("Deployment Engineer - Data Analysis Questions v3.xlsx", sheetname=None, ignore_index=True)
	df_enrollment = df.parse("Enrollment Data")
	df_event_data = df.parse("Event Data")
	df_survey_data = df.parse("Survey Response Data")
<<<<<<< HEAD
	# df_module_date = df.parse("Message Reference Sheet")
	# df_survey_ref = df.parse("Survey Reference Sheet")
=======
	df_module_date = df.parse("Message Reference Sheet")
	df_survey_ref = df.parse("Survey Reference Sheet")
>>>>>>> 131d71f292069b4d9e7ba62ba549aaa1b5765a18


	# questions 1-2
	question_one_sum = 0
	question_one_individual_sums = [0, 0, 0]
	completed_modules = set() # to exclude duplicates.

	for index, row in df_enrollment.iterrows():
		# calculate individual sums per criteria
		if (isCompleted(row)): question_one_individual_sums[0] += 1
		if (isCancelled(row)): question_one_individual_sums[1] += 1
		if (isScheduled(row)): question_one_individual_sums[2] += 1

		# calculate sums aggregated
		if isCompleted(row) or isCancelled(row) or isScheduled(row):
			question_one_sum += 1

		# pd.to_datetime()
		if asFrom('3/28/2018', row) and completedModule(row, df_event_data):
			completed_modules.add(row['Patient Id'])


	print("Enrolled: " + str(question_one_sum) + " individual sums: " + str(question_one_individual_sums))
	print("Enrolled as of 3/28 & completed at least one module: " + str(len(completed_modules)))


	# question 3-4
	# * Completion rate is defined as # times completed over # of times Viewed
	question_three, question_four, question_five = 0,0,0
	mod_views = moduleViews(df_event_data)
	mod_completed = moduleCompleted(df_event_data)

	# calculate completion rates with both views & completed dictionarys
	completion_rates = dict((k, float(mod_completed[k])/mod_views[k]) for k in mod_completed)
	# sort; by value descending
	completion_rates_sorted = sorted(completion_rates.items(), key=lambda x: x[1], reverse=True)
	
	if (len(mod_views) > 0):
		question_three = list(mod_views.keys())[0]
	if (len(completion_rates) > 0):
		question_four = completion_rates_sorted[0] # highest completion rate module

	question_five = surveyResponseCount(df_survey_data, 'Are you satisfied with your care? ', 'Yes')
	

	print("Higest viewed module: " + str(question_three) + " " + str(mod_views))
	print("Highest completion rate module: " + str(question_four) + " " + str(completion_rates))
	print("Those satisfied with their care: " + str(question_five))



# criteria methods

# check if Status is completed
def isCompleted(x):
	return x['Status'] == 'Completed'

# check if Status is scheduled
def isScheduled(x):
	return x['Status'] == 'Scheduled'

# check if Status is cancelled
def isCancelled(x):
	return x['Status'] == 'Cancelled'

# check if patient is enrolled as of a date
def asFrom(asFrom, y):
	return (pd.to_datetime(y['Procedure Date']) - datetime.strptime(asFrom, "%m/%d/%Y")).days >= 0

# check if said patient has completed modules (> 0); queries said module by 'Patient Id' where they've marked a module as 'User_completed_module'
def completedModule(row, module):
	return len(module[(module['Patient Id'] == row['Patient Id']) & (module['Event_Name'] == 'User_completed_module')]) > 0

# return the counts of events marked 'Node_viewed' with their respective module id & count mapped to dictionary
def moduleViews(module):
	return dict(module[(module['Event_Name'] == 'Node_Viewed')]['Module Id'].value_counts())

# return the counts of events marked 'User_completed_module' with their respective module id & count mapped to dictionary
def moduleCompleted(module):
	return dict(module[(module['Event_Name'] == 'User_completed_module')]['Module Id'].value_counts())

# return the count of survey responses with given question & answer
def surveyResponseCount(module, question, answer):
	return len(module[(module['Question Text'] == question) & (module['Response'] == answer)])


scan_input()
