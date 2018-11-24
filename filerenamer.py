import os



def remove_text_filename_at_beginning(text,dir):
    os.chdir(dir)
    files = os.listdir(dir)
    for file in files:
        new_file_name = file.split(text)[1]
        print(file, " = > ", new_file_name)
        os.rename(file,new_file_name)

def fix_filenames_to_get_metadata(dir):
    os.chdir(dir)
    files = os.listdir(dir)
    for file in files:
        s = ""
        a = file.split("-")
        for i in range(len(a)-1):
            if i == len(a)-2:
                s += a[i].strip(" ")
            else:
                s += a[i].strip(" ") + " - "

        yt_link = " [" + a[len(a) - 1].split(".")[0] + "].mp4"
        if len(yt_link) != 18:
            yt_link = " [" + a[len(a) - 2] + "-" + a[len(a) - 1].split(".")[0] + "].mp4"

        print(s + yt_link)
        os.rename(file, s + yt_link)


remove_text_filename_at_beginning("Machine Learning","/mnt/usb/Tutorials/sentdex/Machine Learning with Python/3. Training a Neural network")
#fix_filenames_to_get_metadata("/mnt/usb/sentdex/Machine Learning with Python/2. Deep Machine Learning")


# for file in a:
#     s =""
#     a = file.split("-")



    # #os.rename(file,k.strip(" ")+yt_link)

    #lol = file.split("p.")[1].split("-")[0]
    #os.rename(file, str(lol) + ". " + file)
    # for file in a:
    #     if int(i) == int(file.split("p.")[1].split("-")[0]):
    #         #os.rename(file, str(i)+". "+file)
    #         print(file," = > ", str(i)+". "+file)
#print(a)