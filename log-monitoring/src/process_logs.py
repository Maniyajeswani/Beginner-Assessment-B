import pandas as pd
import json


# Load JSON logs
def load_logs(file_path):
    try:
        df = pd.read_json(file_path)
        return df
    except Exception as e:
        print("Error loading logs:", e)
        return None


# Preprocess logs
def preprocess_logs(df):
    try:
        df["timestamp"] = pd.to_datetime(df["timestamp"])
        df["hour"] = df["timestamp"].dt.hour
        return df
    except Exception as e:
        print("Error preprocessing logs:", e)
        return df


# Calculate metrics
def calculate_metrics(df):

    # Identify errors
    df["is_error"] = df["status_code"] >= 400

    # Error rate per hour
    error_rate = (
        df.groupby("hour")["is_error"]
        .mean()
        .reset_index(name="error_rate")
    )

    # Average response time per hour
    avg_response = (
        df.groupby("hour")["response_time_ms"]
        .mean()
        .reset_index(name="avg_response_time")
    )

    # Merge both
    summary = pd.merge(error_rate, avg_response, on="hour")

    # Top failing services
    failing = (
        df[df["status_code"] >= 400]
        .groupby("service")
        .size()
        .sort_values(ascending=False)
    )

    return summary, failing


# Generate reports
def generate_reports(summary, failing):

    summary.to_csv("summary_report.csv", index=False)

    error_summary = {
        "top_failing_services": failing.to_dict()
    }

    with open("error_summary.json", "w") as f:
        json.dump(error_summary, f, indent=4)

# Main function
def main():

    file_path = "data/app_logs.json"

    df = load_logs(file_path)
    print(df.columns)

    if df is None:
        return

    df = preprocess_logs(df)

    summary, failing = calculate_metrics(df)

    generate_reports(summary, failing)

    print("Reports generated successfully!")


if __name__ == "__main__":
    main()