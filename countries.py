import argparse
import logging
import time
from restcountries.countries import Countries
from google.cloud import bigquery

URL = "https://restcountries.eu/rest/v2/all"


def run(args):

    # Fetch countries dataset
    start_time = time.time()
    countries = Countries()
    countries_df = countries.fetch()
    query_time = round((time.time()-start_time), 2)
    logging.info("Countries fetched in (sec): " + str(query_time))

    countries_df = Countries.parse(countries_df)

    # Return or upload to BQ
    if args.bq_upload:
        bq_dest_table = args.bq_dest
        logging.info("Uploading dataset to BQ table " + bq_dest_table)
        upload_gcp(countries_df, bq_dest_table)
        logging.info("BQ upload done")
    else:
        logging.info("Saving dataset to " + args.out_file)
        countries_df.reset_index().to_json(args.out_file, orient='records')
        logging.info("File save done")


def upload_gcp(df, table):
    client = bigquery.Client()

    job_config = bigquery.LoadJobConfig(
        write_disposition="WRITE_TRUNCATE",
    )

    job = client.load_table_from_dataframe(
        df, table, job_config=job_config
    )
    job.result()


if __name__ == '__main__':
    logging.getLogger().setLevel(logging.DEBUG)

    # Handle arguments
    parser = argparse.ArgumentParser(description='Simple job for fetching countries from restcountries.eu API and uploading it to GCP - BQ')
    parser.add_argument('--bq_upload', help='Upload dataframe to GCP BigQuery (Default False)', action='store_true')
    parser.add_argument('--bq_dest', type=str, help='GCP destination table ', required=True)
    parser.add_argument('--out_file', type=str, help='Output json file name (Default countries_dump.json)', default="countries_dump.json")
    args, _ = parser.parse_known_args()

    # TODO: Add arguments check

    run(args)
    logging.info("Done")