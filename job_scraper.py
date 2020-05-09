import pandas as pd
import requests

pd.set_option('display.max_columns', None)


class JobScraper:

    def __init__(self):
        """
        Constructor to fetch data from url.
        """
        url = 'https://techolution.app.param.ai/api/career/get_job/'
        self.JSONContent = requests.get(url).json()
        # print(JSONContent)

    def create_pandas_dataframe(self):
        """
        Method to create dataframe from json content received from the url.
        """
        my_list = []
        for i in self.JSONContent['data']:
            for k in self.JSONContent['data'][i]['jobs']:
                job_dictionary = {'category': k['category'], 'job_title': k['title'], 'created_at': k['created_at'],
                                  'job_type': k['job_type'], 'min_exp_years': int(k['min_exp'] / 12)}

                my_list.append(job_dictionary)

        self.jobs_df = pd.DataFrame(my_list)

    def update_dataframe(self):
        """
        Method to update dataframe date column as per requirement.
        """
        self.jobs_df['created_at'] = pd.to_datetime(self.jobs_df['created_at'])
        self.jobs_df = self.jobs_df.sort_values(by=['created_at']).reset_index(drop=True)

    def write_to_csv(self):
        """
        Method to write dataframe to a csv file.
        """
        self.jobs_df.to_csv("jobs_result.csv")


job_scraper = JobScraper()
job_scraper.create_pandas_dataframe()
job_scraper.update_dataframe()
job_scraper.write_to_csv()
