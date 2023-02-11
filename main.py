import csv

from censys.search import CensysCertificates

# Put your credentials here if you didn't set them up through censys config
api_id = ""
api_secret = ""


def get_certificate_data(query, fields):
    """
    Fetch certificates data from Censys API.

    Args:
        query (str): The query to be executed.
        fields (Fields): Optional; Fields to be returned in the result set.

    Returns:
        results (Iterator[dict]): Results from the API request.
    """
    c = CensysCertificates(api_id=api_id, api_secret=api_secret)
    results = c.search(query, fields)
    return results


def write_to_csv(data, filename="results.csv", header=None):
    """
    Write the results from the API request to a CSV file.

    Args:
        data (Iterator[dict]): Use the result returned from get_certificate_data().
        filename (str): Optional; Set the name of the output file.
        header (List[str]): Optional; Set the header row in the output file.
    """
    with open(filename, 'w', newline='') as f:
        writer = csv.writer(f)
        if header:
            writer.writerow(header)
        for entry in data:
            writer.writerow(
                [entry["parsed.fingerprint_sha256"], entry["parsed.validity.start"], entry["parsed.validity.end"]])


if __name__ == '__main__':
    # modify the arguments as you need
    query = "parsed.names: censys.io and tags: trusted"
    fields = ["parsed.fingerprint_sha256", "parsed.validity.start", "parsed.validity.end"]
    filename = "results.csv"
    header = ["SHA-256 Fingerprint", "Validity Start", "Validity End"]

    query_result = get_certificate_data(query, fields)
    write_to_csv(query_result, filename, header)
