from urllib.request import urlopen, URLError
from bs4 import BeautifulSoup
import os


def send_alert(old_ver, new_ver, error=False):
    SENDMAIL = "/usr/sbin/sendmail"  # sendmail location
    FROM = "alerts@iptp.net"
    TO = ["alerts@iptp.net"]
    SUBJECT = "version of the 'PAU' program - AG-Pilot"
    if error:
        TEXT = "Web-page reading error occurred"
    else:
        TEXT = "Check the version of the program as per RT #444526" + \
            "\n" + "old version: "+old_ver + "\nNew version: " + new_ver
    # Prepare actual message

    message = """\
    From: %s
    To: %s
    Content-Type: text/plain;
    Subject: %s

    %s
    """ % (FROM, ", ".join(TO), SUBJECT, TEXT)

    # Send the mail
    #completed = subprocess.run(['echo', "-e", '"{}"'.format(message), "| {} -t -f alerts@iptp.net".format(SENDMAIL)])
    #print(completed)

    p = os.popen("%s -t -i" % SENDMAIL, "w")
    p.write(message)


def main():
    try:
        with urlopen('http://www.rsit.ru/products/ama/whatsnew.php') as data:
            data1 = data.read()
    except URLError:
        send_alert(error=True)
        return
    soup = BeautifulSoup(data1.decode(), "lxml")
    new_ver = soup.find('div', {'class': 'content'}).find('h3').text
    try:
        with open('tempfile.txt', 'r') as f:
            old_ver = f.read()
            if old_ver != new_ver:
                send_alert(old_ver, new_ver)
                with open('tempfile.txt', 'w') as f:
                    f.write(new_ver)
            else:
                print("version ok")
    except FileNotFoundError:
        send_alert(old_ver="None", new_ver=new_ver)
        with open('tempfile.txt', 'w+') as f:
            f.write(new_ver)

if __name__ == "__main__":
    main()
