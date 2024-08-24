import requests
import selectorlib
import smtplib as smtp
import ssl

URL = 'https://programmer100.pythonanywhere.com/tours/'

def get_data_url(url):

    try:
        response = requests.get(url)
        if response.status_code == 200 :
            url_data = response.text
            return url_data
        else:
            return f'Failed to retrieve data. Status code: {response.status_code}'
        
    except requests.exceptions.RequestException as e:
        return f"Error: {e}"

def data_scrap(url_data):

    try :
        if url_data and not url_data.startswith("Failed") :
            extractor = selectorlib.Extractor.from_yaml_file('scrap.yaml')
            data = extractor.extract(url_data)['tours']
            return data
   
    except Exception as e:
        return f"Error during scraping: {e}"  

def store_to_inventory(scrap_data):

    with open('events_data.txt','a') as event_data:
        event_data.write(scrap_data + "\n")

def get_from_inventory(scrap_data):

    with open('events_data.txt','r') as event_data:
        data = event_data.read()
        return data

def send_email(message):
    username = 'rpraveenkumar1203@gmail.com'
    receiver = 'rpraveenkumar1203@gmail.com'
    password = "qflhtaqvayqwwkqs"

    host = 'smtp.gmail.com'
    port = '465'
    context = ssl.create_default_context()
    with  smtp.SMTP_SSL(host,port,context=context) as server:
        server.login(username,password)
        server.sendmail(username,receiver,message)
    print('mail sent successfully')

    
if __name__ == "__main__":
        url_data = get_data_url(URL)
        scraped_data = data_scrap(url_data)
        content = get_from_inventory(scraped_data)

        if scraped_data != 'No upcoming tours':
            if scraped_data not in content:
                        store_to_inventory(scraped_data)
                        send_email(message = scraped_data)

        


