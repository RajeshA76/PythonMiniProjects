import speedtest


test = speedtest.Speedtest()
print("loading server list...")
test.get_servers() # get list of servers available for spped test
print("choosing best server...")
best = test.get_best_server() # getting best server

print(f"Found: {best['host']} located in {best['country']}")

print("performing download test ...")
download_result = test.download()
print("performing upload test ...")
upload_result = test.upload()
ping_result = test.results.ping



def mbit():
	print(f"Download Speed: {download_result / 1024 / 1024:.2f} Mbit/s")
	print(f"Upload Speed: {upload_result / 1024 / 1024:.2f} Mbit/s")
def kbit():
	print(f"Download Speed: {download_result / 1024:.2f} Kbit/s")
	print(f"Upload Speed: {upload_result / 1024:.2f} Kbit/s")
while True:	
	s = input("Enter (M) Display data in Mbit/s or Enter (K) to Display data in Kbit/s:  ")
	if s.lower() == 'm':
		mbit()
		break
	elif s.lower() == 'k':
		kbit()
		break
	else:
		print("Invalid input!! Try Again")



print(f"Ping: {ping_result:.2f} ms")