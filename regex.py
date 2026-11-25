#import re

# text = "Contact us at hello@example.com or support@gmail.com +910987654321"

# emails = re.findall(r'[\w.-]+@[\w.-]+\.\w+', text)
# numbers = re.search(r'\d{12}', text)


# print(emails,"-", numbers)



# import re
# text = "Today's date is 22-10-2026"
# match = re.search(r'(\d{2})-(\d{2})-(\d{4})', text)

# if match:
#     print(match.group(0))  # 22-10-2026
#     print(match.group(1))  # 22
#     print(match.group(2))  # 10
#     print(match.group(3))  # 2026


import re
pattern = r'(?P<day>\d{2})-(?P<month>\d{2})-(?P<year>\d{4})'

match = re.search(pattern, '22-10-2026')

if match:
    print(match.group('day'))
    print(match.group('month'))
    print(match.group('year'))