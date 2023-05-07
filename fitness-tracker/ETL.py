import pandas as pd
from lib.utils import config
import psycopg2
from lib.utils import get_consumer
from sqlalchemy import create_engine

if __name__ == "__main__":
    consumer = get_consumer('health_data')

    #conn = psycopg2.connect(**config('database.conf'))
    engine = create_engine('postgresql://postgres:arnav123@database-2.cvhwbyvvdws2.ap-south-1.rds.amazonaws.com:5432/db1')

    for message in consumer:
        df = pd.DataFrame(message.value)
        print(df.head())
        df.to_sql('sunita_sharma_data', con=engine, if_exists='append', index=False)