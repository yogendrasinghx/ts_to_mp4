import glob
import subprocess
ts_files = []
#Getting .ts files 
ts_files = glob.glob('*.ts')

for file in ts_files:
    #Creating command 
    command = 'ffmpeg -i "'+file+'" -c copy "'+file[:-3]+'.mp4"'
    #print(command)

    #Run conversion command and get return code
    return_code = subprocess.run(command, shell=True).returncode
    

    if return_code == 0:
        print(file,"is converted to mp4 successfully")
    else:
        print(file,"Conversion Failed!")


    
