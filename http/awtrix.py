
import time
import requests

awtrix = "192.168.178.60"
api = "http://" + awtrix + "/api/"

def api_status():
    r = requests.get(api + "stats")
    print(r.text)
    r = requests.get(api + "loop")
    print(r.text)

def indicator_on():
    r = requests.post(api + "indicator1", data='{"color": [255,0,0]}')
    print(r)
    r = requests.post(api + "indicator2", data='{"color": [0,255,0]}')
    print(r)
    r = requests.post(api + "indicator3", data='{"color": [0,0,255]}')
    print(r)

def indicator_off():
    r = requests.post(api + "indicator1", data='{"color": "0"}')
    print(r)
    r = requests.post(api + "indicator2", data='{"color": "0"}')
    print(r)
    r = requests.post(api + "indicator3", data='{"color": "0"}')
    print(r)

indicator_on()
time.sleep(2)

ICO_MOON    = 1465
ICO_CLOUD   = 91
ICO_SUN     = 4973
ICO_HEART   = 794
ICO_BATTERY = 390

def update_app(name, text, icon, save=False):
    data = '{"icon": "' + str(icon) + '", "textCase": 2, "text": "' + text + '"'
    if save:
        data = data + ', "save": true'
    data = data + '}'
    r = requests.post(api + 'custom?name='+name, data=data)
    print(r)

update_app("pvcur", "000 W", ICO_SUN)
update_app("pvsum", "000 kWh", ICO_BATTERY)

def update_chart(name, charttype, values):
    data = '{"' + charttype + '": ' + str(values) + '}'
    r = requests.post(api + 'custom?name='+name, data=data)
    print(r)
    
update_chart("bar", "bar", [1, 2, 3, 4, 5, 6, 7, 8, 7, 6, 5, 4, 3, 2, 1])
update_chart("line", "line", [1, 2, 3, 4, 5, 6, 7, 8, 7, 6, 5, 4, 3, 2, 1])

def update_progress(name, value):
    data = '{"progress": ' + str(value) + '}'
    r = requests.post(api + 'custom?name='+name, data=data)
    print(r)

update_progress("progress", 77)

api_status()

indicator_off()
