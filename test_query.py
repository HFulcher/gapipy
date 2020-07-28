import gapipy

ga_client = gapipy.client.authenticate(fileName="ga-key.json")
output = ga_client.get("223160034", "2020-07-21", "2020-07-27", ["sessions", "bounceRate"])

print(output)
