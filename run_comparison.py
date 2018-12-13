import comparer


def run_comparison(range, finder, writer):
    counter = 1
    while counter <= range:
        print("Round: ", counter)
        found_drive = finder.file_to_compare()
        already_checked = []
        if found_drive:
            for found in found_drive:
                if found in already_checked:
                    print(found, " - Already Tested")
                else:
                    print(found)
                    comparer_d = comparer.Comparer(found, found_drive[found])
                    result = comparer_d.compare()
                    writer.write(result)
                    print("{ File:", result[0], "|||", "Result:", result[1], "}")
                    already_checked.append(found)
        counter += 1
    writer.end()
