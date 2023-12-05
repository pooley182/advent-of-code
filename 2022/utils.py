import datetime
import urllib.request

TODAY = datetime.datetime.today().day


def fetch(day: int = TODAY):
    request = urllib.request.Request('https://adventofcode.com/2022/day/' + str(day) + '/input')
    request.add_header("Cookie",
                       "")

    return urllib.request.urlopen(request)
