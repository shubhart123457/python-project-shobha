# def info():
#     return "this is info function from modules file"

# def msg():
#     return "this is message from modules file"


# import random

# # 1. OTP जनरेट करने का फंक्शन
# def generate_otp():
#     return random.randint(1000, 9999)

# print("--- 📱 लॉगिन / वेरिफिकेशन सिस्टम ---")

# # यूजर से मोबाइल नंबर लेना
# mobile_number = input("अपना मोबाइल नंबर दर्ज करें: ")

# 2. सर्वर द्वारा OTP जनरेट करना
# sent_otp = generate_otp()

# # (वास्तविक जीवन में यह OTP SMS के जरिए मोबाइल पर भेजा जाता है, 
# # यहाँ टेस्टिंग के लिए हम इसे स्क्रीन पर दिखा रहे हैं)
# #print(f"[सिम्युलेशन संदेश]: आपके नंबर पर OTP भेजा गया है -> {sent_otp}")

# # 3. यूजर से OTP इनपुट लेना
# user_entered_otp = int(input("कृपया 4-अंकों का OTP दर्ज करें: "))

# # 4. OTP की जाँच (Verification using if-else)
# # if user_entered_otp == sent_otp:
# #     print("✅ लॉगिन सफल! (Verification Successful). स्वागत है!")
# # else:
# #     print("❌ गलत OTP! (Invalid OTP). कृपया पुनः प्रयास करें।")