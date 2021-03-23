from pydrive.drive import GoogleDrive

def file(drive:GoogleDrive, id:str, name:str):
  stream = drive.CreateFile({'id':id})
  stream.GetContentFile(name)
  print(stream)

file(drive, '146lQLVPkzuJ0IxvWhvWMlZC3QGMVS7tu', 'kode2.csv')