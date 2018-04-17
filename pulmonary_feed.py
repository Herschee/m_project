import csv
from patient import patient

# scan_input  ######################################################################
# scans csv 
# 
# params: none
# notes: handles initial sorting logic for preconditions 1) language = English 2) Sceduled at least 2 days away
def scan_input(feed):

		# enrollment dictionary to store patient objects
		enrollment = dict()

		#### example full traversal filtrage with preconditions #######################
		# we'll iterate through each procedure scheduled 
		# english only, at least 2 days until procedure date, location one for every entry, etc
		# the patient class handles tour classification via procedures
		for row in feed:

			p = patient(dict(row))

			# general enrollment for location 1
			p.setLocation(1)

			# initial tour qualifications; english language & 2 day schedule buffer
			if (p.isLanguage('English') and p.isScheduled(2)):

				# add the patient to the enrollment list; else if they already exist, update their new procedure
				if (p.Patient not in enrollment):
					p.addProcedure(p.Date, p.Type)
					enrollment[p.Patient] = p
				else:
					enrollment[p.Patient].addProcedure(p.Date, p.Type)
			else:
				enrollment[p.Patient] = p
				enrollment[p.Patient].tour = -1

		return enrollment


######################################################################################
# To test using a sample csv #########################################################
"""
with open('Sample Pulmonary Enrollment Data .csv', 'r') as csvfile:

	# initial read
	raw_reader = csv.DictReader(csvfile, delimiter=',')

	scan_input(raw_reader)
"""



