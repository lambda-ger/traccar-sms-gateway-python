import requests
# config area
api = 'xxxxxxxx-xxxx-xxxxxxxx'
url = 'http://192.168.160.54:8082'  


def send(number, message):
    try:
        x = requests.post(url, json={'to': number, 'message': message}, headers={"Authorization": api})
        if x.status_code == 202:
            return True
        else:
            return False

    except Exception as error:
        print("An exception occurred:", error)
        return False


# example
if send("+49176xxxxxxxx", "I am a Message!"):
    print("Message send")
