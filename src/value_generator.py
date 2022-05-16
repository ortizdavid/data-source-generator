import random
import secrets


class ValueGenerator:


	@classmethod  
	def generate_int(cls, min_value, max_value):
		min_value = int(min_value)
		max_value = int(max_value)
		return random.randint(min_value, max_value)


	@classmethod
	def generate_float(cls, min_value, max_value):
		min_value = float(min_value)
		max_value = float(max_value)
		return round(random.uniform(min_value, max_value), 2)


	@classmethod
	def generate_str(cls, prefix, max_value):
		max_value = int(max_value)
		pos = random.randint(1, max_value)
		str_result = secrets.token_hex(pos)
		#str_result[1:pos]
		return f'{prefix.upper()}_{str_result}'


	@classmethod
	def generate_date(cls, min_year, max_year):
		years = cls.generate_list(min_year, max_year)
		months = cls.generate_list(1, 12)
		days = cls.generate_list(1, 30)
		rand_year = random.randint(0, len(years)-1) 
		rand_month = random.randint(0, len(months)-1) 
		rand_day = random.randint(0, len(days)-1) 
		month = cls.format_digit(rand_month)
		day = cls.format_digit(rand_day)
		return f'{years[rand_year]}-{month}-{day}'


	@classmethod
	def generate_time(cls, min_hour, max_hour):
		hours = cls.generate_list(min_hour, max_hour)
		minutes = cls.generate_list(0, 59)
		seconds = cls.generate_list(0, 59)
		rand_hour = random.randint(0, len(hours)-1)
		rand_min = random.randint(0, len(minutes)-1)
		rand_sec = random.randint(0, len(seconds)-1)
		hour = cls.format_digit(rand_hour)
		minute = cls.format_digit(rand_min)
		second = cls.format_digit(rand_sec)
		return f'{hour}:{minute}:{second}'

	
	@classmethod
	def generate_date_time(cls, min_year, max_year):
		return f'{cls.generate_date(min_year, max_year)} {cls.generate_time(min_year, max_year)}'


	@classmethod
	def generate_list(cls, min_value, max_value):
		min_value = int(min_value)
		max_value = int(max_value)
		new_list = []
		for i in range(min_value, max_value+1):
			new_list.append(i)
		return new_list


	@classmethod
	def format_digit(cls, num):
		return f'0{num}' if num < 10 else f'{num}'

