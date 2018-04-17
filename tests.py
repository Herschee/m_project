import unittest
from pulmonary_feed import scan_input

# Some test cases to keep me sane while maintaining 

class SolutionsTests(unittest.TestCase):

	def test_tour_one_a(self):
		feed = [{'Appt Status': 'Sch', 'Patient Class': 'Outpatient', 'Type': 'FLEX BRONCH WITH BAL', 'Department': 'PULM GRYBIG9', 'VT ID': '100188', 'Status': 'Alive', 'Date': '4/14/18', 'Provider/Resource': 'Doctor 1 ', 'Appt Time': ' 9:00 AM', 'Canc Date': '', 'Pref Language': 'English', 'Patient': 'Paudell, Max J', 'CSN': '1445578838', 'Mobile #': '333-333-3333', 'Pt. E-mail Address': 'test1@gmail.com', 'Birth Date': '4/10/64', 'Gender': 'Female', 'MRN': '1445578838'}]
		self.assertTrue(scan_input(feed)["Paudell, Max J"].tour == 1)

	def test_tour_one_b(self):
		feed = [{'Appt Status': 'Sch', 'Patient Class': 'Outpatient', 'Type': 'TRANS BRONCH BX', 'Department': 'PULM GRYBIG9', 'VT ID': '100188', 'Status': 'Alive', 'Date': '4/14/18', 'Provider/Resource': 'Doctor 1 ', 'Appt Time': ' 9:00 AM', 'Canc Date': '', 'Pref Language': 'English', 'Patient': 'Paudell, Max J', 'CSN': '1445578838', 'Mobile #': '333-333-3333', 'Pt. E-mail Address': 'test1@gmail.com', 'Birth Date': '4/10/64', 'Gender': 'Female', 'MRN': '1445578838'}]
		self.assertTrue(scan_input(feed)["Paudell, Max J"].tour == 1)

	def test_tour_three(self):
		feed = [{'Appt Status': 'Sch', 'Patient Class': 'Outpatient', 'Type': 'THORACENTIS', 'Department': 'PULM GRYBIG9', 'VT ID': '100188', 'Status': 'Alive', 'Date': '4/14/18', 'Provider/Resource': 'Doctor 1 ', 'Appt Time': ' 9:00 AM', 'Canc Date': '', 'Pref Language': 'English', 'Patient': 'Paudell, Max J', 'CSN': '1445578838', 'Mobile #': '333-333-3333', 'Pt. E-mail Address': 'test1@gmail.com', 'Birth Date': '4/10/64', 'Gender': 'Female', 'MRN': '1445578838'}]
		self.assertTrue(scan_input(feed)["Paudell, Max J"].tour == 3)

	def test_tour_four(self):
		feed = [{'Appt Status': 'Sch', 'Patient Class': 'Outpatient', 'Type': 'PLEURX', 'Department': 'PULM GRYBIG9', 'VT ID': '100188', 'Status': 'Alive', 'Date': '4/14/18', 'Provider/Resource': 'Doctor 1 ', 'Appt Time': ' 9:00 AM', 'Canc Date': '', 'Pref Language': 'English', 'Patient': 'Paudell, Max J', 'CSN': '1445578838', 'Mobile #': '333-333-3333', 'Pt. E-mail Address': 'test1@gmail.com', 'Birth Date': '4/10/64', 'Gender': 'Female', 'MRN': '1445578838'}]
		self.assertTrue(scan_input(feed)["Paudell, Max J"].tour == 4)

	def test_tour_uniquecase_tour_one_a(self):
		feed = [{'Appt Status': 'Sch', 'Patient Class': 'Outpatient', 'Type': 'FLEX BRONCH WITH BAL', 'Department': 'PULM GRYBIG9', 'VT ID': '100188', 'Status': 'Alive', 'Date': '4/14/18', 'Provider/Resource': 'Doctor 1 ', 'Appt Time': ' 9:00 AM', 'Canc Date': '', 'Pref Language': 'English', 'Patient': 'Paudell, Max J', 'CSN': '1445578838', 'Mobile #': '333-333-3333', 'Pt. E-mail Address': 'test1@gmail.com', 'Birth Date': '4/10/64', 'Gender': 'Female', 'MRN': '1445578838'},
				{'Appt Status': 'Sch', 'Patient Class': 'Outpatient', 'Type': 'THORACENTIS', 'Department': 'PULM GRYBIG9', 'VT ID': '100188', 'Status': 'Alive', 'Date': '4/14/18', 'Provider/Resource': 'Doctor 1 ', 'Appt Time': ' 9:00 AM', 'Canc Date': '', 'Pref Language': 'English', 'Patient': 'Paudell, Max J', 'CSN': '1445578838', 'Mobile #': '333-333-3333', 'Pt. E-mail Address': 'test1@gmail.com', 'Birth Date': '4/10/64', 'Gender': 'Female', 'MRN': '1445578838'}]
		self.assertTrue(scan_input(feed)["Paudell, Max J"].tour == 1)

	def test_tour_uniquecase_tour_one_b(self):
		feed = [{'Appt Status': 'Sch', 'Patient Class': 'Outpatient', 'Type': 'TRANS BRONCH BX', 'Department': 'PULM GRYBIG9', 'VT ID': '100188', 'Status': 'Alive', 'Date': '4/14/18', 'Provider/Resource': 'Doctor 1 ', 'Appt Time': ' 9:00 AM', 'Canc Date': '', 'Pref Language': 'English', 'Patient': 'Paudell, Max J', 'CSN': '1445578838', 'Mobile #': '333-333-3333', 'Pt. E-mail Address': 'test1@gmail.com', 'Birth Date': '4/10/64', 'Gender': 'Female', 'MRN': '1445578838'},
				{'Appt Status': 'Sch', 'Patient Class': 'Outpatient', 'Type': 'THORACENTIS', 'Department': 'PULM GRYBIG9', 'VT ID': '100188', 'Status': 'Alive', 'Date': '4/14/18', 'Provider/Resource': 'Doctor 1 ', 'Appt Time': ' 9:00 AM', 'Canc Date': '', 'Pref Language': 'English', 'Patient': 'Paudell, Max J', 'CSN': '1445578838', 'Mobile #': '333-333-3333', 'Pt. E-mail Address': 'test1@gmail.com', 'Birth Date': '4/10/64', 'Gender': 'Female', 'MRN': '1445578838'}]
		self.assertTrue(scan_input(feed)["Paudell, Max J"].tour == 1)

	def test_tour_uniquecase_tour_one_c(self):
		feed = [{'Appt Status': 'Sch', 'Patient Class': 'Outpatient', 'Type': 'THORACENTIS', 'Department': 'PULM GRYBIG9', 'VT ID': '100188', 'Status': 'Alive', 'Date': '4/14/18', 'Provider/Resource': 'Doctor 1 ', 'Appt Time': ' 9:00 AM', 'Canc Date': '', 'Pref Language': 'English', 'Patient': 'Paudell, Max J', 'CSN': '1445578838', 'Mobile #': '333-333-3333', 'Pt. E-mail Address': 'test1@gmail.com', 'Birth Date': '4/10/64', 'Gender': 'Female', 'MRN': '1445578838'},
				{'Appt Status': 'Sch', 'Patient Class': 'Outpatient', 'Type': 'TRANS BRONCH BX', 'Department': 'PULM GRYBIG9', 'VT ID': '100188', 'Status': 'Alive', 'Date': '4/14/18', 'Provider/Resource': 'Doctor 1 ', 'Appt Time': ' 9:00 AM', 'Canc Date': '', 'Pref Language': 'English', 'Patient': 'Paudell, Max J', 'CSN': '1445578838', 'Mobile #': '333-333-3333', 'Pt. E-mail Address': 'test1@gmail.com', 'Birth Date': '4/10/64', 'Gender': 'Female', 'MRN': '1445578838'}]
		self.assertTrue(scan_input(feed)["Paudell, Max J"].tour == 1) # let's mess with ordering

	def test_tour_uniquecase_mult_proc_a(self):
		feed = [{'Appt Status': 'Sch', 'Patient Class': 'Outpatient', 'Type': 'PLEURX', 'Department': 'PULM GRYBIG9', 'VT ID': '100188', 'Status': 'Alive', 'Date': '4/11/18', 'Provider/Resource': 'Doctor 1 ', 'Appt Time': ' 9:00 AM', 'Canc Date': '', 'Pref Language': 'English', 'Patient': 'Paudell, Max J', 'CSN': '1445578838', 'Mobile #': '333-333-3333', 'Pt. E-mail Address': 'test1@gmail.com', 'Birth Date': '4/10/64', 'Gender': 'Female', 'MRN': '1445578838'},
				{'Appt Status': 'Sch', 'Patient Class': 'Outpatient', 'Type': 'THORACENTIS', 'Department': 'PULM GRYBIG9', 'VT ID': '100188', 'Status': 'Alive', 'Date': '4/14/18', 'Provider/Resource': 'Doctor 1 ', 'Appt Time': ' 9:00 AM', 'Canc Date': '', 'Pref Language': 'English', 'Patient': 'Paudell, Max J', 'CSN': '1445578838', 'Mobile #': '333-333-3333', 'Pt. E-mail Address': 'test1@gmail.com', 'Birth Date': '4/10/64', 'Gender': 'Female', 'MRN': '1445578838'}]
		self.assertTrue(scan_input(feed)["Paudell, Max J"].tour == 4) # most recent is PLEURX (4)

	def test_tour_uniquecase_mult_proc_b(self):
		feed = [{'Appt Status': 'Sch', 'Patient Class': 'Outpatient', 'Type': 'PLEURX', 'Department': 'PULM GRYBIG9', 'VT ID': '100188', 'Status': 'Alive', 'Date': '4/11/18', 'Provider/Resource': 'Doctor 1 ', 'Appt Time': ' 9:00 AM', 'Canc Date': '', 'Pref Language': 'English', 'Patient': 'Paudell, Max J', 'CSN': '1445578838', 'Mobile #': '333-333-3333', 'Pt. E-mail Address': 'test1@gmail.com', 'Birth Date': '4/10/64', 'Gender': 'Female', 'MRN': '1445578838'},
				{'Appt Status': 'Sch', 'Patient Class': 'Outpatient', 'Type': 'FLEX BRONCH WITH BAL', 'Department': 'PULM GRYBIG9', 'VT ID': '100188', 'Status': 'Alive', 'Date': '3/14/18', 'Provider/Resource': 'Doctor 1 ', 'Appt Time': ' 9:00 AM', 'Canc Date': '', 'Pref Language': 'English', 'Patient': 'Paudell, Max J', 'CSN': '1445578838', 'Mobile #': '333-333-3333', 'Pt. E-mail Address': 'test1@gmail.com', 'Birth Date': '4/10/64', 'Gender': 'Female', 'MRN': '1445578838'},
				{'Appt Status': 'Sch', 'Patient Class': 'Outpatient', 'Type': 'LIPO', 'Department': 'PULM GRYBIG9', 'VT ID': '100188', 'Status': 'Alive', 'Date': '3/10/18', 'Provider/Resource': 'Doctor 1 ', 'Appt Time': ' 9:00 AM', 'Canc Date': '', 'Pref Language': 'English', 'Patient': 'Paudell, Max J', 'CSN': '1445578838', 'Mobile #': '333-333-3333', 'Pt. E-mail Address': 'test1@gmail.com', 'Birth Date': '4/10/64', 'Gender': 'Female', 'MRN': '1445578838'}]
		self.assertTrue(scan_input(feed)["Paudell, Max J"].tour == 1) # most recent is LIPO (though invalid), so next most recent is FLEX BRONCH WITH BAL (1)

	def test_invalid_language_enrollment(self):
		feed = [{'Appt Status': 'Sch', 'Patient Class': 'Outpatient', 'Type': 'THORACENTIS', 'Department': 'PULM GRYBIG9', 'VT ID': '100188', 'Status': 'Alive', 'Date': '4/14/18', 'Provider/Resource': 'Doctor 1 ', 'Appt Time': ' 9:00 AM', 'Canc Date': '', 'Pref Language': 'Spanish', 'Patient': 'Paudell, Max J', 'CSN': '1445578838', 'Mobile #': '333-333-3333', 'Pt. E-mail Address': 'test1@gmail.com', 'Birth Date': '4/10/64', 'Gender': 'Female', 'MRN': '1445578838'}]
		self.assertTrue(scan_input(feed)["Paudell, Max J"].tour == -1)		

	def test_invalid_scheduled_date_enrollment(self):
		feed = [{'Appt Status': 'Sch', 'Patient Class': 'Outpatient', 'Type': 'THORACENTIS', 'Department': 'PULM GRYBIG9', 'VT ID': '100188', 'Status': 'Alive', 'Date': '4/16/18', 'Provider/Resource': 'Doctor 1 ', 'Appt Time': ' 9:00 AM', 'Canc Date': '', 'Pref Language': 'Spanish', 'Patient': 'Paudell, Max J', 'CSN': '1445578838', 'Mobile #': '333-333-3333', 'Pt. E-mail Address': 'test1@gmail.com', 'Birth Date': '4/10/64', 'Gender': 'Female', 'MRN': '1445578838'}]
		self.assertTrue(scan_input(feed)["Paudell, Max J"].tour == -1)	

	def test_invalid_tour_procedure(self):
		feed = [{'Appt Status': 'Sch', 'Patient Class': 'Outpatient', 'Type': 'LIPO', 'Department': 'PULM GRYBIG9', 'VT ID': '100188', 'Status': 'Alive', 'Date': '2/16/18', 'Provider/Resource': 'Doctor 1 ', 'Appt Time': ' 9:00 AM', 'Canc Date': '', 'Pref Language': 'English', 'Patient': 'Paudell, Max J', 'CSN': '1445578838', 'Mobile #': '333-333-3333', 'Pt. E-mail Address': 'test1@gmail.com', 'Birth Date': '4/10/64', 'Gender': 'Female', 'MRN': '1445578838'}]
		self.assertTrue(scan_input(feed)["Paudell, Max J"].tour == -1)	
 
if __name__ == '__main__':
	unittest.main()
