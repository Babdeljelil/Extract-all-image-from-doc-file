import zipfile
import pathlib

fname=input("enter the file name exmple filname.docx :")



if(zipfile.is_zipfile(fname)):
  p = pathlib.Path('Extracted Images')
  try:
        p.mkdir()
  except Exception:
                   print()
  print("please wait:")
  with zipfile.ZipFile(fname, 'r') as zf:
    k=zf.namelist()



    for i in range(0,len(k)):
                             if "media" in k[i]:
                                                   data=zf.read(k[i])

                                                   p=str(k[i]).split("/")

                                                   with open('Extracted Images\\'+p[2],"bw") as pk:
                                                                                pk.write(data)
  print("done")

else:
       print(fname+" is not valid")



