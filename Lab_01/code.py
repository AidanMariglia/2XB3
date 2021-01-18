
def are_valid_groups(studentNum, groups):
  
  if not type(studentNum[0]) == str:
    print("invalid student number type")
    return False

  for g in groups:
    if not 2 <= len(g) <= 3:
      return False



  for num in studentNum:
    seen = False
    
    for group in groups:
      if num in group and seen:
        return False
      elif num in group:
        seen = True
      
    if not seen:
      return False

  return True

