import requests
import json
from fake_useragent import UserAgent


def register(fname, lname, umail):
    cookies = dict(requests.get(
        'https://internshala.com/1-day-in-your-dream-company?utm_source=bb_wa&utm_medium=bb989790').cookies)

    # cookies = {
    #     'csrf_cookie_name': '23c2de00d3d95164adfc94e9efd16ea8',
    #     'u': '1',
    #     'isc': 'fd7143b94bbbbc54745c8055dde95b9ed2ee2e40',
    #     'ists': '0',
    #     'spui': '0',
    #     'PHPSESSID': '6c680ac3cc4ed1b3e909b444b190725522a4ae50',
    #     'toUpdatePersistentSession': '2',
    #     'pdc_new': '7DE1AA4267CEC9ED2D7F710A9BD1177E%2F6c680ac3cc4ed1b3e909b444b190725522a4ae50%2F1565288153',
    #     'pdcVersion': '1',
    #     'persistentSession': '6c680ac3cc4ed1b3e909b444b190725522a4ae50%2F1565288153',
    #     'persistentSessionDateTimeStamp': '1565202600',
    #     'sessionToken': '6c680ac3cc4ed1b3e909b444b190725522a4ae50%2F1565288153',
    #     'AWSELB': '11A3412B08B1863C3F8327801F7CCFCEAF70CAB4C04AF93E9DAC2C76CE5A413BF5928D9B2862E3A170D4434FB5E1EE595DAD5E9F02B66BCDA7FB17D864C3BFACACBFB3369B',
    #     '_ga': 'GA1.2.1873076598.1565288155',
    #     '_gid': 'GA1.2.673997629.1565288155',
    # }

    headers = {
        'User-Agent': UserAgent().random,
        'Referer': 'https://internshala.com/1-day-in-your-dream-company',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'X-Requested-With': 'XMLHttpRequest',
    }

    data = 'csrf_test_name='+cookies["csrf_cookie_name"]+'&campaign=big_brand_aug19&campaign_type=tier_2_campaign&campaign_param=&utm_source=bb_wa&utm_medium=bb989790&utm_campaign=&email='+umail.replace('%40', '@')+'&password='+umail.replace('%40', '@')+'&first_name='+fname+'&last_name='+lname + \
        '&college=RGPV+Collage&city_sublocality_level_2=&city_sublocality_level_1=&city_locality=Indore&city_administrative_area_level_2=Indore&city_administrative_area_level_1=Madhya+Pradesh&city_country=India&city_lat=22.7195687&city_lng=75.85772580000003&city=Indore%2C+Madhya+Pradesh%2C+India&currently_pursuing=ug&degree=Bachelor+of+Computer+Applications+(BCA)&start_year=2016&end_year=2019'

    response = requests.post('https://internshala.com/registration/student_submit',
                             headers=headers, cookies=cookies, data=data, verify=False)

    print(response.text)
    return json.loads(response.text)["success"] == True


# register('pa', 'papa', 'papapa@vmailcloud.com')
