import csv, os

class Writer:
    def __init__(self, path, name):
        self.path = path
        self.name = name

    def start(self):
        self.filename = self.name + "_test.csv"
        self.full_path = os.path.join(self.path, self.filename)
        self.file = open(self.full_path, "w+")
        self.writer = csv.writer(self.file, dialect="excel", lineterminator='\n')
        head_row = ["filename", "comparison_status", "origin_path", "backup_path", "original_size",
                   "backup_size", "difference"]
        self.writer.writerow(head_row)

    def write(self, row):
        self.writer.writerow(row)

    def end(self):
        self.file.close()
