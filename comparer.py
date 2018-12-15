import os

# DEFINES
DATA_DRIVE = "D:"
WIN_DRIVE = "C:"
BACKUP_DRIVE = "F:\\comp_backup"
DATA_BACKUP = "Data"
WIN_BACKUP = "C"
DATA_BACKUP_PATH = os.path.join(BACKUP_DRIVE, DATA_BACKUP)
WIN_BACKUP_PATH = os.path.join(BACKUP_DRIVE, WIN_BACKUP)


class Comparer:
    def __init__(self, original_path, original_size):
        self.original_path = original_path
        self.original_size = original_size

    def get_local_path(self):
        drive, relative_path = os.path.splitdrive(self.original_path)
        self.filename = os.path.split(relative_path)[1]
        if drive == DATA_DRIVE:
            self.backup_path = DATA_BACKUP_PATH + relative_path
        elif drive == WIN_DRIVE:
            self.backup_path = WIN_BACKUP_PATH + relative_path

    def is_folder(self):
        folder_size = 0
        for dirpath, dirnames, filenames in os.walk(self.backup_path):
            for f in filenames:
                fp = os.path.join(dirpath, f)
                try:
                    folder_size += os.path.getsize(fp)
                except:
                    #GET DEEPER
                    folder_size += 0
        return folder_size

    def is_file(self):
        return os.path.getsize(self.backup_path)

    def compare(self):
        self.get_local_path()
        try:
            os.path.exists(self.backup_path)
        except FileNotFoundError:
            return self.filename, False, self.original_path, "NOT FOUND", self.original_size, 0, self.original_size
        if os.path.isfile(self.backup_path):
            size = self.is_file()
        else:
            size = self.is_folder()
        if self.original_size == size:
            comparison_status = True
        else:
            return self.compare_specific_folder()
        difference = self.original_size - size
        return(self.filename, comparison_status, self.original_path, self.backup_path,
               self.original_size, size, difference)

    def compare_specific_folder(self):
        original_folder_path = self.original_path
        backup_folder_path = self.backup_path
        if os.path.exists(self.backup_path) and not os.path.isfile(self.backup_path):
            for dirpath, dirnames, filenames in os.walk(self.original_path):
                for filename in filenames:
                    original_filepath = os.path.join(dirpath, filename)
                    original_filesize = os.path.getsize(original_filepath)
                    try:
                        backup_filepath = os.path.join(self.backup_path, filename)
                        backup_filesize = os.path.getsize(backup_filepath)
                        if original_filesize == backup_filesize:
                            comparison_status = True
                        else:
                            comparison_status = False
                        difference = original_filesize - backup_filesize
                        return (filename, comparison_status, original_filepath, backup_filepath,
                                original_filesize, backup_filesize, difference)
                    except FileNotFoundError:
                        return (filename, False, original_filepath, "N/A", original_filesize,
                                "0", (original_filesize*-1))
        elif os.path.exists(self.backup_path):
            backup_filesize = os.path.getsize(self.backup_path)
            difference = self.original_size - backup_filesize
            return (self.filename, False, self.original_path, self.backup_path,
                    self.original_size, backup_filesize, difference)
        return self.filename, False, self.original_path, "Not in backup", "irrelevant", "N/A", "N/A"

w = Comparer("D:\\11111", 193994)
w.backup_path = "F:\comp_backup\Data\\11111"
w.compare_specific_folder()
