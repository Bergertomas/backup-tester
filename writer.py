import csv, os

class Writer:
    def __init__(self, path, name):
        self.path = path
        self.name = name

    def start(self):
        self.filename = self.name + "_test.csv"
        self.full_path = os.path.join(self.path, self.filename)
        if not os.path.exists(self.path):
            os.mkdir(self.path)
        self.file = open(self.full_path, "w+")
        self.writer = csv.writer(self.file, dialect="excel", lineterminator='\n')
        head_row = ["filename", "comparison_status", "origin_path", "backup_path", "original_size",
                   "backup_size", "difference"]
        self.writer.writerow(head_row)

    def write(self, row):
        try:
            self.writer.writerow(row)
        except UnicodeEncodeError:
            new_row = []
            for i in row:
                if type(i) == str:
                    new_i = i.encode("utf-8")
                    new_row.append(new_i)
                else:
                    new_row.append(i)
            self.writer.writerow(new_row)

    def end(self):
        self.file.close()
