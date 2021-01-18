def are_valid_groups(Studs, Groups):
	result = True
	for Student in Studs:
		for Group in Groups:
			if(Student  in Group):
				result = True

			else:
				return False

