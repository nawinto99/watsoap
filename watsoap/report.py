from datetime import datetime

import pandas as pd

now = datetime.now()


def csv(df, output_file):
    try:
        df.to_csv(output_file, index=False)
    except:
        raise


def json(df, output_file):
    try:
        df.to_json(output_file, orient="records")
    except:
        raise


def create_report(response, file_location, file_type):
    df = pd.DataFrame.from_dict(response)
    output_file = (
        file_location + "endpoints_health_report_" + now.strftime("%Y%m%d%H%M%S")
    )
    if file_type == "CSV":
        output_file = output_file + ".csv"
        csv(df, output_file)
    elif file_type == "JSON":
        output_file = output_file + ".json"
        json(df, output_file)
