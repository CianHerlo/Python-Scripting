"""
Cian Herlihy - R00205604 - Task 3

I started with having a constant of the parent directory that can be changed to a location of your choosing and having
it as a constant makes it easier to manage. I then created some strings to insert into text files just to provide
content rather than blank files.

I get the input off the user of the folder name and then use os.path.join() to make it 1 complete path to use.
I create the folder and then create 2 new folders using the os.mkdir() command. I did this in a separate function
to improve readability of the code. I also check if the folder exists first by using shutil.rmtree().
If it exists I delete the directory with all its contents and then remake the directories. I make folders in folders
as requested and then finally enter the directory 'docs' and create my files there. I use another function to create
these files by using a file writing connection. I use 'w' to indicate that it will be overwritten (Not that it matters).
I input the content I stated above into each file and then close each connection respectively. I create 2 more Directories
in docs and then return to my original function create_folder(). This function then returns to main to keep the
hierarchy of the functions.

My next step was to change the files names from uppercase to lower case. The .lower() function replaces the original
text therefore I used os.replace() to replace the old file name with the new name. This does not affect the content in
the file. Before I do all this though I created time.sleep() so you can visually see in the folder the file names
changing if you like. This is not needed, but I find it useful for testing purposes.
"""
import os
import shutil
import time

PARENT_DIR = "C:/Users/Cian/OneDrive - mycit.ie/Sys_Scripting/Python Assignment/"
coronaText = "This is CORONAVIRUS.txt"
dangerText = "This is DANGEROUS.txt"
keepsText = "This is KEEPSAFE.txt"
stayhomeText = "This is STAYHOME.txt"
hygieneText = "This is HYGIENE.txt"


def create_folder(folder_path):
    backup = os.path.join(folder_path, "backup")
    working = os.path.join(folder_path, "working")
    if os.path.exists(folder_path):
        shutil.rmtree(folder_path)
        os.mkdir(folder_path)
        print("Folder Deleted and then Re-Created")
    else:
        os.mkdir(folder_path)
        print("Created Folder")

    os.mkdir(backup)
    os.mkdir(working)

    # Working Directory
    workingSubDirs = ["pics", "docs", "movie"]
    for folders in workingSubDirs:
        os.makedirs(os.path.join(working, folders))

    docs_folder = os.path.join(working, "docs")
    write_files_to_docs(docs_folder)
    return docs_folder


def write_files_to_docs(docs_folder):
    # Write to Coronavirus.txt
    c = open(os.path.join(docs_folder, "CORONAVIRUS.txt"), mode="w")
    c.write(coronaText)
    c.close
    # Write to Dangerous.txt
    d = open(os.path.join(docs_folder, "DANGEROUS.txt"), mode="w")
    d.write(dangerText)
    d.close
    # Write to KeepSafe.txt
    k = open(os.path.join(docs_folder, "KEEPSAFE.txt"), mode="w")
    k.write(keepsText)
    k.close
    # Write to StayHome.txt
    s = open(os.path.join(docs_folder, "STAYHOME.txt"), mode="w")
    s.write(stayhomeText)
    s.close
    # Write to Hygiene.txt
    h = open(os.path.join(docs_folder, "HYGIENE.txt"), mode="w")
    h.write(hygieneText)
    h.close

    # docs Directory
    docsSubDirs = ["school", "party"]
    for folders in docsSubDirs:
        os.makedirs(os.path.join(docs_folder, folders))
    return


# This function is to change text files to lowercase
def adjust_capitalisation(docs_folder):
    for file in os.listdir(docs_folder):
        print(file)
        os.rename(docs_folder + "/" + file, docs_folder + "/" + file.lower())


def main():
    print("Task 4")
    folder_name = input("Enter the folder name \n>>> ")
    print("")
    path = os.path.join(PARENT_DIR, folder_name)
    docs_dir = create_folder(path)
    time.sleep(5)  # Delay second function to see effect in folders
    adjust_capitalisation(docs_dir)


if __name__ == "__main__":
    main()
