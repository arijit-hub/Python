import http.client

conn=http.client.HTTPSConnection("www.uci.edu")

conn.request("GET","/")

data=conn.getresponse()

page=str(data.read(1000))

print(page)


