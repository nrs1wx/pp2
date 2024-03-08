import json

with open('2.json') as f:
    data = json.load(f)

header = "Interface Status\n" + "=" * 80 + "\n"
table_format = "{:<50} {:<20} {:<8} {:<6}\n"

print(header)
print(table_format.format("DN", "Description", "Speed", "MTU"))
print("-" * 80)

for item in data:
    dn = item.get('DN', '')
    description = item.get('Description', '')
    speed = item.get('Speed', 'inherit')
    mtu = item.get('MTU', '')
    print(table_format.format(dn, description, speed, mtu))