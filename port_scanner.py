# from datetime import datetime
# import socket

# # Target host define karna (Hum yahan apne hi computer / localhost ko scan karenge)
# target_host = "127.0.0.1"            # "192.168.29.121"

# print("-" * 60)
# print(f"🔍 Scanning Target: {target_host}")
# print(f"⏰ Scan Started at: {str(datetime.now())}")
# print("-" * 60)

# try:
#   # Kuch common ports ki list jinhe hum scan karenge
#   # (Jaise: 21=FTP, 22=SSH, 80=HTTP, 443=HTTPS, 3306=MySQL)
#   ports_to_scan = [21, 22, 23, 80, 443, 3306, 8080, 5000]

#   for port in ports_to_scan:
#     # Socket object banana (AF_INET = IPv4, SOCK_STREAM = TCP)
#     s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#     s.settimeout(1.0)  # 1 second ka timeout taaki script zyada der ruke na

    # connect_ex() check karta hai ki connection successful hua ya nahi
    # Agar connection ban gaya toh 0 return karega, warna error code
#     result = s.connect_ex((target_host, port))

#     if result == 0:
#       print(f"🟢 Port {port:<5} -> OPEN (Service chal rahi hai)")
#     else:
#       print(f"🔴 Port {port:<5} -> CLOSED (Band hai)")

#     # Socket ko close karna zaroori hai
#     s.close()

# except KeyboardInterrupt:
#   print("\n⚠️ User ne script beech mein rok di (Ctrl + C).")
# except socket.gaierror:
#   print("\n❌ Error: Hostname resolve nahi ho paya.")
# except socket.error:
#   print("\n❌ Error: Server se connection establish nahi ho saka.")

# print("-" * 60)
# print("🏁 Scan poora ho gaya!")