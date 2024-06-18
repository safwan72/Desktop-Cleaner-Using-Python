import os
import extensions
import shutil
Base_dir='C:\\Users\\safwa\\Downloads\\0. Sorter' 
# Target_dir='C:\\Users\\safwa\\Downloads' 
Target_dir='C:\\Users\\safwa\\Downloads' 
for key in extensions.extensions:   #create new folders using 
        newDIR=os.path.join(Base_dir,key)
        if not os.path.isdir(newDIR):
            os.makedirs(newDIR)
            print("Directory Created  ",newDIR)
      
          
for files in os.listdir(Target_dir):
    file_splits=os.path.splitext(files)
    file_extension=file_splits[1]
    file_name=file_splits[0]
    i=1
    for key in extensions.extensions:
        for exts in extensions.extensions[key]:
            if exts==file_extension:
                checkfile=os.path.isfile(Base_dir+"\\"+key+"/"+files)
                dest=os.path.join(Base_dir+"\\"+key)
                targ=os.path.join(Target_dir,files)
                if checkfile:
                    print(checkfile)
                    i+=1
                    newtarg=os.path.join(Base_dir+"\\"+key,file_name+"("+str(i)+")"+str(file_extension))
                    os.rename(targ,newtarg)
                    print("File Copied. ",file_name)
                    shutil.copy(targ,dest)
                else:
                    print("File Copied. ",file_name)
                    shutil.copy(targ,dest)
                    

