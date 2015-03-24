import requests,winsound

def help():
    print'Press number corresponding to option.\n'+'+'*50

def menu_screen():
    print '+'*50
    print'1. Train Codes and Names'
    print'2. Train arrivals at Stations'
    print'3. Live Train Status'
    print'4. Train between Stations'
    print'5. Train Route Information'
    print'6. PNR Status'
    print'7. Train Fare Enquiry'
    print'8. Station Codes and names'
    print'Press h for help.'
    print'+'*50

def menu():
    done1 = False
    while not done1:
        menu_screen()
        uinput = raw_input()
        if uinput == 'h':
            help()
        elif uinput == '1':
            train_code()
        elif uinput == '2':
            train_arrivals_at_station()
        elif uinput == '3':
            live_train_status()
        elif uinput == '4':
            train_bw_station()
        elif uinput == '5':
            train_route_information()
        elif uinput == '6':
            pnr_status()
        elif uinput == '7':
            train_fare_enquery()
        elif uinput == '8':
            station = raw_input('Enter name of station :')
            station_code(station)

def pnr_status():
    done = False
    while not done:
        pnr_no = raw_input('Enter your PNR number : ')
        if pnr_no.isdigit() and len(pnr_no)==10:
            try:
                pnr = requests.get('http://api.railwayapi.com/pnr_status/pnr/'+pnr_no+'/apikey/57252/')
                if pnr.status_code == requests.codes.ok:
                    beep()
                    pnr_response = pnr.json()
                    if pnr_response[error]:
                        entry = raw_input('Want to retry or quit(r/q)???\n')
                        print '-'*50
                        if entry == 'r':
                            done = False
                        if entry == 'q':
                            done = True
                    else:
                        for item in pnr_response:
                            print item,':',pnr_response[item]
                        print('Press any key for exit.')
                        entry = raw_input('')
                        print '-'*50
                        if len(entry)!=0:
                            done = True
                        else:
                            done = False
            except requests.exceptions.RequestException as e:
                print 'Can\'t fetch  PNR Status.'
                print 'The server couldn\'t fulfill the request.'
                for items in e:
                    print items
                    print '-'*50
        else:
            print'Enter a valid PNR.'
            entry = raw_input('Want to retry or quit(r/q)???\n')
            print '-'*50
            if entry == 'r':
                done = False
            if entry == 'q':
                done = True

def train_arrivals_at_station():
    done = False
    while not done:
        location_input = raw_input('Use your current location code (y/n)\n')
        if location_input.lower() == 'y':
            city = str(city)
            city_ = city.lower()
            station = station_code(city_)
        if location_input.lower() == 'n':
            print('(If you dont\'t know station code,refer option 1 in option menu.)')
            station = raw_input('Enter Station CODE : ')
        hour = raw_input('Enter Window time in hours in which to search for train arrivals(only integer) : ')
        try:
            train_at_station = requests.get('http://api.railwayapi.com/arrivals/station/'+station+'/hours/'+hour+'/apikey/57252/')
            if train_at_station.status_code == requests.codes.ok:
                beep()
                train_at_station_response = train_at_station.json()
                print train_at_station_response['station']
                print 'Number of trains available are',str(train_at_station_response['total'])
                for item in train_at_station_response['train']:
                    for items in item:
                        print items,':',item[items]
                    print '+'*50
                print('Press any key for exit.')
                entry = raw_input('')
                print '-'*50
                if len(entry)!=0:
                    done = True
                else:
                    done = False
        except requests.exceptions.RequestException as e:
            print 'Can\'t fetch Train arrival data fom server.'
            print 'The server couldn\'t fulfill the request.'
            for items in e:
                print items
                print '-'*50
            entry = raw_input('Want to retry or quit(r/q)???\n')
            print '-'*50
            if entry.lower() == 'r':
                done = False
            if entry.lower() == 'q':
                done = True

def station_code(station):
    done = False
    while not done:
        try:
            station_req = requests.get('http://name_to_code/station/'+station+'/apikey/57252/')
            if station_req.status_code == requests.codes.ok:
                beep()
                station_response = station_req.json()
                for items in station_response['stations']:
                    print items,':',station_response['stations'][items]
                    print '+'*50
                print('Press any key for exit.')
                entry = raw_input('')
                print '-'*50
                if len(entry)!=0:
                    done = True
                else:
                    done = False

        except requests.exceptions.RequestException as e:
            print 'Can\'t fetch Train arrival data fom server.'
            print 'The server couldn\'t fulfill the request.'
            for items in e:
                print items
                print '-'*50
            entry = raw_input('Want to retry or quit(r/q)???\n')
            print '-'*50
            if entry.lower() == 'r':
                done = False
            if entry.lower() == 'q':
                done = True

def live_train_status():
    done =False
    while not done:
        station = raw_input('Enter station name: ')
        date= raw_input('Enter date of journey(yyyymmdd): ')
        if date.isdigit() and len(date)== 8:
            done =True
        else:
            print '-'*50+'Enter Data In Valid Format'+'-'*50

    done = False
    while not done:
        try:
            live_train = requests.get('http://api.railwayapi.com/live/train/'+train+'/doj/'+date+'/apikey/57252/')
            if live_train.status_code == requests.codes.ok:
                beep()
                l_train_response = live_train.json()
                for items in l_train_response:
                    print items
                for item in l_train_response['route']:
                    print item
                print('Press any key for exit.')
                entry = raw_input('')
                print '-'*50
                if len(entry)!=0:
                    done = True
                else:
                    done = False
        except requests.exceptions.RequestException as e:
            print 'Can\'t fetch Train data fom server.'
            print 'The server couldn\'t fulfill the request.'
            for items in e:
                print items
                print '-'*50
            entry = raw_input('Want to retry or quit(r/q)???\n')
            print '-'*50
            if entry.lower() == 'r':
                done = False
            if entry.lower() == 'q':
                done = True

def train_route_information():
    train = raw_input('Enter train number: ')
    done = True
    while not done:
        try:
            train_route  = requests.get('http://api.railwayapi.com/route/train/'+train+'/apikey/57252/')
            if train_route.station_code == requests.codes.ok:
                beep()
                train_route_response = train_route.json()
                for item in items in train_route_response:
                    print item
                print('Press any key for exit.')
                entry = raw_input('')
                print '-'*50
                if len(entry)!=0:
                    done = True
                else:
                    done = False 
        except requests.exceptions.RequestException as e:
            print 'Can\'t fetch Train data fom server.'
            print 'The server couldn\'t fulfill the request.'
            for items in e:
                print items
                print '-'*50
            entry = raw_input('Want to retry or quit(r/q)???\n')
            print '-'*50
            if entry.lower() == 'r':
                done = False
            if entry.lower() == 'q':
                done = True

def train_bw_station():
    source_station = raw_input('Enter source station: ')
    destination = raw_input('Enter Destination: ')
    done = True
    while not done:
        try:
            train_bw = requests.get('http://api.railwayapi.com/between/source/'+source_station+'/dest/'+destination+'/apikey/57252/')
            if train_bw.status_code == requests.codes.ok:
                beep()
                train_bw_response = train_bw.json()
                

def beep():
    winsound.Beep(10000,500)

print '*'*75+'\n'+'-'*75
try:
    connectivity = requests.get('https://www.google.co.in/')
    if connectivity.status_code == requests.codes.ok:
        beep()
        del connectivity
        print('Google connectivity available.\n'+'-'*50)
        try:
            ip_get = requests.get('http://ip-api.com/json')
            if ip_get.status_code == requests.codes.ok:
                beep()
                ip_response = ip_get.json()
                ip_add = ip_response['query']
                lon_coor = ip_response['lon']
                lat_coor = ip_response['lat']
                regionName = ip_response['regionName']
                city = ip_response['city']
                print'Your public ip address is '+ ip_add+'.'
                print 'Current location : '+str(city)+ ', '+ str(regionName)
                print 'lattitude : '+str(lat_coor) +'   longitude : '+ str(lon_coor)
                print '-'*50
                try:
                    weather = requests.get("https://george-vustrey-weather.p.mashape.com/api.php?location="+str(city),
                                           headers={"X-Mashape-Key": "fzI1hxtp1wmsh8ncFSwYwGxBTqrep1wUxtwjsnhNvihGxaFz6e",
                                           "Accept": "application/json"})
                    if weather.status_code == requests.codes.ok:
                        beep()
                        weather_respnse = weather.json()
                        day = weather_respnse[0]['day_of_week']
                        high = weather_respnse[0]['high_celsius']
                        low = weather_respnse[0]['low_celsius']
                        condition = weather_respnse[0]['condition']
                        print('Weather Forecast\n+++++++++++++++++')
                        print('Day : '+str(day)+'\nHigh : '+str(high)+'   Low : '+str(low)+'\n'+str(condition)+'\n'+'-'*50)

                        if raw_input('Want to see more weather forecast (y/n)??') == 'y':
                            for i in range(len(weather_respnse)-1):
                                print '('+str(i+1)+')'
                                for items in weather_respnse[i]:
                                    print items,':',weather_respnse[i][items]
                                print '+'*50

                        menu()
                except requests.exceptions.RequestException as e:
                    print 'Can\'t fetch weather data'
                    print 'The server couldn\'t fulfill the request.'
                    for items in e:
                        print items
                        print '-'*50
        except requests.exceptions.RequestException as e:
            print 'Can\'t connect to ip-address server'
            print 'The server couldn\'t fulfill the request.'
            for items in e:
                print items
                print('-'*50)
except requests.exceptions.RequestException as e:
    print('Google connectivity unavailable.')
    print('-'*50)
    print 'The server couldn\'t fulfill the request.'
    for items in e:
        print items
print '*'*75
