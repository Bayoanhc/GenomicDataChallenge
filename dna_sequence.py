import collections
import csv
import io


def main():
    all_nums = collections.Counter()
    with io.open("reads.csv", mode="r", encoding="utf-8") as freads:
        reads_reader = csv.reader(freads)
        next(reads_reader)

        for start, range_ in reads_reader:
            start = int(start)
            range_ = int(range_)
            end = start + range_

            all_nums.update(range(start, end))

    output = io.StringIO()
    output.write("position,coverage\n")
    fmt = "{},{}\n"

    with io.open("loci.csv", mode="r", encoding="utf-8") as floci:
        loci_reader = csv.reader(floci)
        next(loci_reader)  # Skip headers

        for loci, _ in loci_reader:
            loci = int(loci)
            output.write(fmt.format(loci, all_nums[loci]))

    with io.open("loci.csv", mode="w", encoding="utf-8") as write_floci:
        write_floci.write(output.getvalue())


if __name__ == '__main__':
    main()
