import finder, run_comparison, writer

if __name__ == "__main__":
    finder_d = finder.Finder("D:\\")
    finder_c = finder.Finder("C:\\")
    writer_d = writer.Writer("D:\\test\\", "D")
    writer_c = writer.Writer("D:\\test\\run_2", "C")
    writer_d.start()
    writer_c.start()
    run_comparison.run_comparison(10000, finder_d, writer_d)
    run_comparison.run_comparison(10000, finder_c, writer_c)
