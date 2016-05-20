from collections import OrderedDict
import netCDF4
import sys

class GroupByException(Exception):

	def __init__(self, details):
		self.details = details

	def __repr__(self):
		return repr(self.details)


def yearmonth(timevar):
	"""
	Group coordinate variable (assumed to be time and one dimensional) by unique year/month combinations.  This
	is used to produce timeseries of monthly statistics
	"""

	result = OrderedDict()

	# We have to assume the variable is a CF time index
	try:
		datetimes = netCDF4.num2date(timevar[:], timevar.units, calendar=timevar.calendar)
	except:
		print sys.exc_info()
		raise GroupByError("Cannot convert coordinate to datetime(s).  yearmonth grouping requires a CF time coordinate variable")

	# Step through all times
	for index in range(0, len(datetimes)):

		# Generate key
		yearmonth = datetimes[index].year, datetimes[index].month

		# Add to results dictionary
		if yearmonth not in result.keys():
			result[yearmonth] = [index]
		else:
			result[yearmonth].append(index)

	return result

def year(timevar):
	"""
	Group coordinate variable (assumed to be time and one dimensional) by unique years.  This
	is used to produce timeseries of monthly statistics
	"""

	result = OrderedDict()

	# We have to assume the variable is a CF time index
	try:
		datetimes = netCDF4.num2date(timevar[:], timevar.units, calendar=timevar.calendar)
	except:
		raise GroupByError("Cannot convert coordinate to datetime(s).  yearmonth grouping requires a CF time coordinate variable")

	# Step through all times
	for index in range(0, len(datetimes)):

		# Generate key
		year = datetimes[index].year

		# Add to results dictionary
		if year not in result.keys():
			result[year] = [index]
		else:
			result[year].append(index)

	return result

def month(timevar):
	"""
	Group coordinate variable (assumed to be time and one dimensional) by months.  This
	is used to produce timeseries of monthly statistics
	"""

	result = OrderedDict()

	# We have to assume the variable is a CF time index
	try:
		datetimes = netCDF4.num2date(timevar[:], timevar.units, calendar=timevar.calendar)
	except:
		raise GroupByError("Cannot convert coordinate to datetime(s).  yearmonth grouping requires a CF time coordinate variable")

	# Step through all times
	for index in range(0, len(datetimes)):

		# Generate key
		month = datetimes[index].month

		# Add to results dictionary
		if month not in result.keys():
			result[month] = [index]
		else:
			result[month].append(index)

	return result

def yearseason(timevar):
	"""
	Group coordinate variable (assumed to be time and one dimensional) by unique seasons.  This
	is used to produce timeseries of monthly statistics
	"""

	seasons = {'DJF':[11,0,1], 'MAM':[2,3,4], 'JJA':[5,6,7], 'SON':[8,9,10]}

	result = OrderedDict()

	# We have to assume the variable is a CF time index
	try:
		datetimes = netCDF4.num2date(timevar[:], timevar.units, calendar=timevar.calendar)
	except:
		raise GroupByError("Cannot convert coordinate to datetime(s).  yearmonth grouping requires a CF time coordinate variable")

	# Step through all times
	for index in range(0, len(datetimes)):

		# Generate key
		for name, months in seasons.items():
			if datetimes[index].month in months:
				key = name
				break

		# Add to results dictionary
		if key not in result.keys():
			result[key] = [index]
		else:
			result[key].append(index)

	return result

def yearseason(timevar):
	"""
	Group coordinate variable (assumed to be time and one dimensional) by unique seasons.  This
	is used to produce timeseries of monthly statistics
	"""

	seasons = {'DJF':[12,1,2], 'MAM':[3,4,5], 'JJA':[6,7,8], 'SON':[9,10,11]}

	result = OrderedDict()

	# We have to assume the variable is a CF time index
	try:
		datetimes = netCDF4.num2date(timevar[:], timevar.units, calendar=timevar.calendar)
	except:
		raise GroupByError("Cannot convert coordinate to datetime(s).  yearmonth grouping requires a CF time coordinate variable")

	# Step through all times
	for index in range(0, len(datetimes)):

		# Generate key
		for name, months in seasons.items():
			if datetimes[index].month in months:
				year = datetimes[index].year

				if datetimes[index].month < months[0]:
					year -= 1
					
				key = year, name
				break

		# Add to results dictionary
		if key not in result.keys():
			result[key] = [index]
		else:
			result[key].append(index)

	return result
