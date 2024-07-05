# parse a txt file and accept multiple arguments in array form
def parse_tsv_file(file_path, params):
    retrieved_data = {
        i: [] for i in params
    }  # create a dictionary with keys as the parameters and empty arrays to store the data

    with open(file_path, "r") as file:
        # read the header to identify places
        header = [i.strip() for i in file.readline().split("\t")]

        # read the records
        data = file.readlines()

    # processing the data and creating disitnct arrays for each parameter
    ref_hash = [
        header.index(i) for i in params
    ]  # reference hash to store the parameters for extracting from line

    # iterate through the data and extract the parameters, storing in the respective arrays
    for line in data:
        line = line.split("\t")
        for i in range(len(ref_hash)):
            retrieved_data[params[i]].append(line[ref_hash[i]])

    return retrieved_data
