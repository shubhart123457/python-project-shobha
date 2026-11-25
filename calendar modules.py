# import calendar

# def show_month_details(year, month):
#     print(f"--- {calendar.month_name[month]} {year} की जानकारी ---")
    
#     # 1. लीप ईयर चेक
#     if calendar.isleap(year):
#         print(f"👉 {year} एक लीप वर्ष (Leap Year) है।")
#     else:
#         print(f"👉 {year} एक साधारण वर्ष है।")
        
#     # 2. महीने का पहला दिन और कुल दिन
#     start_day_idx, total_days = calendar.monthrange(year, month)
#     print(f"👉 महीने की शुरुआत: {list(calendar.day_name)[start_day_idx]} से हुई")
#     print(f"👉 कुल दिन: {total_days}")
    
#     print("\nकैलेंडर व्यू:")
#     # 3. महीने का टेक्स्ट कैलेंडर प्रिंट करें
#     print(calendar.month(year, month))

# # फ़ंक्शन को कॉल करें (अक्टूबर 2026 के लिए)
# show_month_details(2026, 10)