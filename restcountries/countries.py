import logging
import requests
import pandas as pd
import restcountries.utils as countries_utils


class Countries:
    """
    General class for fetching and parsing json data from restcountries API
    """
    API_URL = "https://restcountries.eu/rest/v2/all"
    countries = pd.DataFrame()

    def __init__(self):
        self.logger = logging.getLogger(self.__class__.__name__)

    def fetch(self):
        """
        Fetch restcountries
        :return: pandas df of restcountries or None if not 200 response
        """
        try:
            logging.debug("Sending request for " + self.API_URL)
            resp = requests.get(self.API_URL)
            self.logger.debug("Received response from " + self.API_URL)

            if resp.status_code != 200:
                self.logger.error('Received ' + str(resp.status_code) + ' response for: ' + self.API_URL)
                return

            self.countries = pd.DataFrame(resp.json())
            self.logger.debug("Fetched total countries:" + str(len(self.countries)))
            return self.countries

        except requests.exceptions.RequestException as e:
            self.logger.error("Error while fetching countries data:", e)
            raise SystemExit(e)

    @staticmethod
    def parse(df):
        """
        Basic data cleaning and preprocessing
        :param df: countries df
        :return: tuple (cleaned_countries, languages)
        """
        # Format the area in square miles, without decimals (example, for Norway “125020”)
        df['area'] = df['area'].fillna(0.0).apply(countries_utils.km2_to_miles2).astype(int)

        # Format the population in millions with one decimal (example, for Norway “5.2”)
        df['population'] = df['population'].fillna(0.0).apply(lambda x: x / 1000000).round(1)

        return df
