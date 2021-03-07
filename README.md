# countries

Simple countries json data fetch and data-visualization.

![Countries Dashboard](dashboard.png?raw=true "Countries Dashboard")

[Dashboard Link](https://datastudio.google.com/reporting/1d0aa20a-c7aa-45ad-ae70-8d6bb1eacfd6)


## About
Simple program for:
 1. Fetching countries json from public [https://restcountries.eu](https://restcountries.eu)
 2. Applied minor preprocessing
 3. Extra/optional: Upload to GCP - BQ for visualization in Data-Studio


## Requirements
Built and tested with python 3.8. If you want to upload data to GCP you need to provide big-query credentials [gcp auth info](https://googleapis.dev/python/google-api-core/latest/auth.html)

Python modules install (ideally in separate environment)
```
pip install -r requirements.txt
```


## Usage

```
usage: countries.py [-h] [--bq_upload] --bq_dest BQ_DEST [--out_file OUT_FILE]

Simple job for fetching countries from restcountries.eu API and uploading it to GCP - BQ

optional arguments:
  -h, --help           show this help message and exit
  --bq_upload          Upload dataframe to GCP BigQuery (Default False)
  --bq_dest BQ_DEST    GCP destination table
  --out_file OUT_FILE  Output json file name (Default countries_dump.json)

```

Example run with uploading data to BigQuery
```
python countries.py --bq_dest genemoos-playground.sandbox.countries --bq_upload
```

