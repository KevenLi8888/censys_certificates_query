import csv
from censys.search import CensysCertificates

api_id = ""
api_secret = ""


def get_certificate_data():
    fields = ["parsed.fingerprint_sha256", "parsed.validity.start", "parsed.validity.end"]
    query = "parsed.names: censys.io and tags: trusted"
    c = CensysCertificates(api_id=api_id, api_secret=api_secret)
    results = c.search(query, fields)
    return results


def write_to_csv(data):
    with open('results.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        header = ["SHA-256 Fingerprint", "Validity Start", "Validity End"]
        writer.writerow(header)
        for entry in data:
            writer.writerow(
                [entry["parsed.fingerprint_sha256"], entry["parsed.validity.start"], entry["parsed.validity.end"]])


if __name__ == '__main__':
    query_result = get_certificate_data()
    write_to_csv(query_result)
