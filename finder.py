import os, random

# DEFINES
DATA_DRIVE = "D:"
WIN_DRIVE = "C:"
BACKUP_DRIVE = "F:\\comp_backup"
DATA_BACKUP = "Data"
WIN_BACKUP = "C"
DATA_BACKUP_PATH = os.path.join(BACKUP_DRIVE, DATA_BACKUP)
WIN_BACKUP_PATH = os.path.join(BACKUP_DRIVE, WIN_BACKUP)


class Finder:
    def __init__(self, drive):
        self.drive = drive
        self.folders = os.listdir(self.drive)

    def file_to_compare(self):
        chosen = random.choice(self.folders)
        self.chosen_path = os.path.join(self.drive, chosen)
        try:
            os.listdir(self.chosen_path)
            return self.compare()
        except PermissionError:
            return self.file_to_compare()
        except NotADirectoryError:
            return self.file_to_compare()
    
    def compare(self):
        to_compare = {}
        if os.path.isfile(self.chosen_path):
            to_compare[self.chosen_path] = self.find_file(self.chosen_path)
        else:
            self.sub_to_folder = os.listdir(self.chosen_path)
            for sub in self.sub_to_folder:
                sub_path = os.path.join(self.chosen_path, sub)
                if os.path.isfile(sub_path):
                    to_compare[sub_path] = self.find_file(sub_path)
                else:
                    to_compare[sub_path] = self.find_folder(sub_path)
        return to_compare

    def find_folder(self, path):
        # foldersize = sum([os.path.getsize(f) for f in os.listdir(path) if os.path.isfile(f)])
        total_size = 0
        for dirpath, dirnames, filenames in os.walk(path):
            for f in filenames:
                fp = os.path.join(dirpath, f)
                if os.path.exists(fp):
                    total_size += os.path.getsize(fp)
        return total_size

    def find_file(self, path):
        filesize = os.path.getsize(path)
        return filesize

    def dig_deeper(self):
        pass
