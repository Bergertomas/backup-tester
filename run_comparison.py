import comparer
import os


def run_comparison(range, finder, writer):
    counter = 1
    true_count = 0
    false_count = 0
    already_checked = []
    while counter <= range:
        print("Round: ", counter)
        found_drive = finder.file_to_compare()
        if found_drive:
            for found in found_drive:
                checked = (os.path.split(found)[0], os.path.split(found)[1])
                if checked in already_checked:
                    print(found, " - Already Tested", "\n")
                else:
                    print(found)
                    comparer_d = comparer.Comparer(found, found_drive[found])
                    result = comparer_d.compare()
                    writer.write(result)
                    if result[1] == True:
                        true_count += 1
                    else:
                        false_count += 1
                    print("{ File:", result[0], "|||", "Result:", result[1], "}", "\n")
                    already_checked.append(checked)
        counter += 1
    print("Done. ")
    print("True count: ", true_count, "|", "False count: ", false_count)
    writer.end()
