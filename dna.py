import csv
import sys


def main():

    # TODO: Check for command-line usage
    if len(sys.argv) != 3:
        print("Usage: python dna.py databases/ sequences/")
        return 1
    # TODO: Read database file into a variable
    lists = []
    with open(sys.argv[1]) as file:
        reader = csv.DictReader(file)
        for row in reader:
            lists.append(row)
    # TODO: Read DNA sequence file into a variable
    with open(sys.argv[2], "r") as file:
        seq_reader = file.read()
    # TODO: Find longest match of each STR in DNA sequence
    longest = []
    with open(sys.argv[1]) as file:
        reader = csv.reader(file)
        header = next(reader)
    for i in range(len(header) - 1):
        i += 1
        x = longest_match(seq_reader, header[i])
        longest.append(x)

    # TODO: Check database for matching profiles
    c = 0
    with open(sys.argv[1]) as file:
        reader = csv.reader(file)
        header = next(reader)
        for j in range(len(lists)):
            header = next(reader)
            for i in range(len(longest)):
                k = i + 1
                if int(longest[i]) == int(header[k]):
                    c += 1
            if c == len(longest):
                print(header[0])
                break
            else:
                c = 0
    if c < len(longest):
        print("No match")
    return


def longest_match(sequence, subsequence):
    """Returns length of longest run of subsequence in sequence."""

    # Initialize variables
    longest_run = 0
    subsequence_length = len(subsequence)
    sequence_length = len(sequence)

    # Check each character in sequence for most consecutive runs of subsequence
    for i in range(sequence_length):

        # Initialize count of consecutive runs
        count = 0

        # Check for a subsequence match in a "substring" (a subset of characters) within sequence
        # If a match, move substring to next potential match in sequence
        # Continue moving substring and checking for matches until out of consecutive matches
        while True:

            # Adjust substring start and end
            start = i + count * subsequence_length
            end = start + subsequence_length

            # If there is a match in the substring
            if sequence[start:end] == subsequence:
                count += 1

            # If there is no match in the substring
            else:
                break

        # Update most consecutive matches found
        longest_run = max(longest_run, count)

    # After checking for runs at each character in seqeuence, return longest run found
    return longest_run


main()
