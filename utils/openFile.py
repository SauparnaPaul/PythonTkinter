from tkinter.filedialog import askopenfile 

def open_file():
    
    try:
         file = askopenfile()
         if file is not None: 
             return file.name
         else:
             return None
    except:
         raise Exception("File Not Found")
       
