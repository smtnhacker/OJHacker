"""Database Functions

The functions that interacts with replit's builtin database named "db".
"""

from replit import db

def insert_testcase(uid, typ, idx, name, tc_in, tc_out):
  """Inserts the test case into the database.

  Parameters
  uid : int
    The unique identification number of the test case
  typ : str
    Can either be "LE", "PA", or "MP" and tells the type of problem
  idx : int
    The problem number. It should be typecasted to str (for some reason related sa db)
  name : str
    The label / description for the inserted test case
  tc_in, tc_out : str
    Contains information on the test cases
  """
  idx = str(idx)

  if typ not in db.keys():
    print(f"ADDING {typ} TO DB")
    db[typ] = dict()
  temp_db = db[typ]

  if idx not in temp_db.keys():
    print(f"ADDING {idx} to {typ}")
    temp_db[idx] = [[name, tc_in, tc_out, uid]]
    db[uid] = (typ, idx)
    db[typ] = temp_db
    temp_db = db[typ]
    if idx not in temp_db.keys():
      print(f"SHIIIIIIIIT. Database cannot insert {uid} {typ} {idx} {name}.")  
    else:
      print("NICEEEEEEEEEEE. Testcase successfully inserted!")
  else:
    temp_db = db[typ]
    temp_db[idx].append([name, tc_in, tc_out, uid])
    db[uid] = (typ, idx)
    db[typ] = temp_db

def erase_db():
  keys = [*db.keys()]
  for x in keys:
    del db[x]

def get_all(typ, idx):
  idx = str(idx)
  if typ not in db.keys():
    print(f"NO TYP {typ} in DB")
    return []
  
  temp_db = db[typ]
  if idx not in temp_db.keys():
    print(f"NO IDX {idx} in {typ}")
    return []
  
  return temp_db[idx]

def get_id():
  if "id" not in db.keys():
    db["id"] = 0
  res = db["id"]
  db["id"] += 1
  return res

def delete_entry(uid):
  print(*db.keys())
  try:
    typ, idx = db[uid]
    print(f"AT {typ}{idx}")
    for i in range(len(db[typ][idx])):
      if db[typ][idx][i][3] == uid:
        temp_db = db[typ]
        del temp_db[idx][i]
        db[typ] = temp_db
        del db[uid]
        return True 
  except Exception:
    print(f"Can't find {uid} in UID Database")
    found = False
    for typ in ['LE','PA']:
      for idx in range(9):
        if typ not in db.keys():
          continue
        temp_db = db[typ]
        if str(idx) not in temp_db:
          continue
        print(typ,idx,temp_db[str(idx)])
        print(type(uid))
        for i in range(len(temp_db[str(idx)])):
          x = temp_db[str(idx)][i]
          if x[3] == uid:
            del temp_db[str(idx)][i]
            found = True
          if found:
            db[typ] = temp_db
            return True
    return False
  return False

def get_entry(uid):
  try:
    typ, idx = db[uid]
  except Exception:
    print(f"Test case with UID {uid} has no typ or idx.")
    return
  try:
    temp_db = db[typ]
    for x in temp_db[idx]:
      if x[3] == uid:
        io = x
        break
    return typ, idx, io
  except Exception:
    print(f"Cannot access problem {uid} but it exists.")
    return

def delete_row(typ, idx):
  try:
    temp_db = db[typ]
    for x in temp_db[idx]:
      del db[x[3]]
    del temp_db[idx]
    db[db] = temp_db
  except:
    raise IndexError
