
def are_valid_groups(studentNum: String, groups):
  flag = True

  for num in studentNum:
    flag = False
    
    for group in groups:
      if num in group:
        flag = True
      
    if not flag:
      return False

  return True

