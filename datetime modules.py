# from datetime import datetime, date, time, timedelta

# print("--- 1. Getting Current Dates & Times ---")
# # Current local date and time
# now_dt = datetime.now()
# print(f"Current Datetime (.now()): {now_dt}")

# # Current calendar date
# today_date = date.today()
# print(f"Today's Date (.today()): {today_date}\n")


# print("--- 2. Parsing and Formatting Strings ---")

# Convert a datetime object into a readable string
# formatted_str = parsed_dt.strftime("%A, %B %d, %Y at %I:%M %p")
# print("hello")
# print(f"Formatted String (.strftime()): {formatted_str}\n")


# print("--- 3. Time Math & Durations (timedelta) ---")
# # Find a future date by adding 7 days
# future_date = today_date + timedelta(days=7)
# print(f"Date in 7 Days (+ timedelta): {future_date}")

# # Calculate the precise difference between two datetimes
# past_dt = datetime(2026, 10, 1)
# time_diff = now_dt - past_dt
# print(f"Time Elapsed Since Oct 1: {time_diff}")
# print(f"Total Elapsed Seconds (.total_seconds()): {time_diff.total_seconds()} seconds\n")


# print("--- 4. Extracting & Combining Components ---")
# # Extract only the date component from a datetime object
# extracted_date = now_dt.date()
# print(f"Extracted Date (.date()): {extracted_date}")

# # Create a separate time object
# custom_time = time(16, 45, 0) # 4:45 PM

# # Combine an independent date and time into one datetime object
# combined_dt = datetime.combine(extracted_date, custom_time)
# print(f"Combined Datetime (.combine()): {combined_dt}\n")


# print("--- 5. Timestamps and Calendar Metadata ---")
# # Convert a Unix epoch timestamp into a datetime object
# unix_timestamp = 1792062000  # Represents Oct 15, 2026
# ts_datetime = datetime.fromtimestamp(unix_timestamp)
# print(f"From Timestamp (.fromtimestamp()): {ts_datetime}")

# # Find the day of the week (where Monday is 0, Sunday is 6)
# weekday_idx = today_date.weekday()
# print(f"Weekday Index (.weekday()): {weekday_idx} (Thursday)")