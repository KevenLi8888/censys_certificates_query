# censys_certificates_query
This script queries all trusted (unexpired) X.509 certificates associated with the [censys.io](http://censys.io/) domain. It produces a CSV file containing the SHA256 fingerprints, validity start and end dates of the certificates.

## Installation

Run the following command to install the Python library for the Censys API:

```
pip install -r requirements.txt
```

## Set Up Credentials

To configure your search credentials, run `censys config`, or manually enter your credentials in the `api_id` and `api_secret` fields at the start of `main.py`.

```
$ censys config

Censys API ID: XXX
Censys API Secret: XXX
Do you want color output? [y/n]: y

Successfully authenticated for your@email.com
```

The credentials entered into `main.py` will be given priority. If you want to use credentials stored in the cycsys config, leave the `api_id` and `api_secret` fields blank in `main.py`.

## Run

```
python main.py
```

The output will be saved to `results.csv`.