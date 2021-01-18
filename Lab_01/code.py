<<<<<<< HEAD
def are_valid_groups(studentNum, groups):
  flag = True

  for num in studentNum:
    flag = False
    
    for group in groups:
      if num in group:
        flag = True
      
    if not flag:
      return False

  return True
>>>>>>> 9f52672de22a7d1f1d4b99e8b1862124762affea
