import random
import secrets

from scipy import rand

class ValueGenerator:
        
	def generate_int(min, max):
		min = int(min)
		max = int(max)
		return random.randint(min, max)

	def generate_float(min, max):
		min = float(min)
		max = float(max)
		return round(random.uniform(min, max), 2)

	def generate_str(prefix, max):
		max = int(max)
		pos = random.randint(1, max)
		str_result = secrets.token_hex(pos)
		#str_result[1:pos]
		return f'{prefix.upper()}_{str_result}'


	def generate_date(years_list = ['2021', '2022']):

		years = years_list
		months = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12']
		days = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', 
				'11', '12', '13', '14', '15', '16', '17', '18', '19', '20',
				'21', '22', '23', '24', '25', '26', '27', '28', '29', '30']
		
		rand_year = random.randint(0, len(years)-1) 
		rand_month = random.randint(0, 11) 
		rand_day = random.randint(0, 29) 
		result_date = f'{years[rand_year]}-{months[rand_month]}-{days[rand_day]}'
		return f'{result_date}'


	def generate_date_time():
		pass


	def generate_time():
		pass

