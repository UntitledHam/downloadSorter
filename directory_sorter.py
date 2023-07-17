import os
import shutil

#This is the directory that will be sorted:
directory = "/home/ham/Downloads/"

#These are the directories that the files will be sorted into:
archives = "/home/ham/Archives"
documents = "/home/ham/Documents"
pictures = "/home/ham/Pictures/"
videos = "/home/ham/Videos/"
music = "/home/ham/Music/"

#File extensions for each type:
file_extensions_for_archives = (".zip", ".7z", ".rar", ".pea", ".arc", ".tar.gz", ".tar.bz", ".tar.bz2", ".tar.xz", ".tar.zst", ".tgz", ".tbz", ".txz", ".tzst")
file_extensions_for_documents = (".docx", ".pdf", ".txt", ".xml", ".html", ".latte", ".colorscheme", ".md", ".json")
file_extensions_for_pictures = (".png", ".jpg", ".gif", ".webp", ".avif")
file_extensions_for_videos = (".mp4", ".mkv", ".webm", ".avi", ".amv", ".mov")
file_extensions_for_music = (".mp3", ".flac", ".wav")

#Moves the files and prints it out: 
def moveFile(filename, new_directory):
    print("\033[94m" + filename + " was moved to: " + new_directory + "\033[0m")
    directory_of_file = directory + "/" + filename 
    shutil.move(directory_of_file, new_directory)
    
#Loops through every file in the directory and sorts it.
for file in os.listdir(os.fsencode(directory)):
    filename = os.fsdecode(file) 
    if filename.endswith(file_extensions_for_archives):
        moveFile(filename, archives)

    elif filename.endswith(file_extensions_for_documents):
        moveFile(filename, documents)

    elif filename.endswith(file_extensions_for_pictures): 
        moveFile(filename, pictures)

    elif filename.endswith(file_extensions_for_videos):
        moveFile(filename, videos)

    elif filename.endswith(file_extensions_for_music): 
        moveFile(filename, music)

    else: 
        print(filename + " file extension not recognized, skipping...")
  
    
