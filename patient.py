from datetime import datetime

# Patient Class #######################################################################
# csv entry mapped directly to this class
# extended with attributes for tour & location classification
# 
# params: json object to map to
# notes: handles internal logic for unique cases & tour classification
class patient(object):
	tour = -1 # -1 if isn't assigned or match any tour criteria
	location = 0

	def __init__(self, json):
		self.__dict__ = json	
		self.__dict__['procedures'] = dict()
	
	def setTour(self, t):
		self.tour = t

	def setLocation(self, l):
		self.location = l

	# Distinguish which tour we are based off of given procedure
	# returns t (or last assigned Tour) if new procedure doesn't map to any criteria above
	def acquireTour(self, p, t):
		if self.isTourOne(p):
			return 1
		elif self.isTourThree(p):
			return 3
		elif self.isTourFour(p):
			return 4
		else:
			# print(p + " not found. using: " + str(t))
			return t

	def getProcedures(self):
		return self.__dict__['procedures']

	# add a procedure to this patient on a given date
	# handles unique cases for more than one procedure
	def addProcedure(self, date, proc):
		procs = self.getProcedures()
		if (date in procs):
			procs[date].append(proc)

			# check for unique case 1
			self.checkUniqueTourCase(date)
		else:
			procs[date] = [proc]

			# set tour to the most recent procedure
			self.setMostRecentProcedureTour()

		# otherwise set tour to recent procedure set
		# self.setTour(self.acquireTour(proc, self.tour))

	# check for the unique case
	def checkUniqueTourCase(self, date):
		flag = 0
		procs = self.getProcedures()

		for p in procs[date]:
			if (self.isTourOne(p)): flag += 1
			if (self.isTourThree(p)): flag += 1

		if (flag == 2):
			# this patient has 2 procedures on the same date; one is a FLEX BRONCH WITH BAL or TRANS BRONCH BX
			# the other is THORACENTIS (must be exactly 2 procedures)

			# override tour to 1
			self.setTour(1)

	# check for a patient with > 1 procedures; set tour to whichever is the nearest procedure date
	def setMostRecentProcedureTour(self):
		procs = self.getProcedures()

		# if len(procs.keys()) < 2: return

		min_ = datetime.today()
		min_p = 0
		date_format = "%m/%d/%y"
		
		for p in procs:
			m_ = datetime.strptime(p, date_format)

			if m_ < min_:
				min_ = m_
				min_p = p

		# set tour to most recent dated procedure
		self.setTour(self.acquireTour(procs[min_p][0], self.tour)) 

	# Check for tour one criteria
	def isTourOne(self, p):
		if (type(p) == str):
			return p == 'FLEX BRONCH WITH BAL' or p == 'TRANS BRONCH BX'

		return p.Type == 'FLEX BRONCH WITH BAL' or p.Type  == 'TRANS BRONCH BX'

	# Check for tour three criteria
	def isTourThree(self, p):
		if (type(p) == str):
			return p == 'THORACENTIS'

		return p.Type  == 'THORACENTIS'

	# Check for tour four criteria
	def isTourFour(self, p):
		if (type(p) == str):
			return p == 'PLEURX'

		return self.Type  == 'PLEURX'

	# Check for language criteria
	def isLanguage(self, language):
		return self.__dict__["Pref Language"] == language

	# check if a patient is scheduled at least 'days' away
	def isScheduled(self, days):
		
		date_format = "%m/%d/%y"
		date = self.Date

		return (datetime.today() - datetime.strptime(date, date_format)).days >= days