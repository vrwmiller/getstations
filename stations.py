#! /usr/local/bin/python3.7

import sys, json, requests, argparse
from pyld import jsonld

parser = argparse.ArgumentParser(description="Get NWS Office Approved Stations")
parser.add_argument('-o', help='NWS Office Code', required=True)
args=vars(parser.parse_args())

office = args["o"]
url = 'https://api.weather.gov/offices/%s/' % office

if __name__ == "__main__":
    r = requests.get(url)
    parsed = json.loads(r.content)
    for i in parsed:
        if i == 'approvedObservationStations':
            for e in parsed[i]:
                rr = requests.get(e)
                rrparsed = json.loads(rr.content)
                props = rrparsed.get("properties")
                stationid = props.get("stationIdentifier")
                stationname = props.get("name")
                print(f"{stationid}: {stationname}".format( stationid, stationname))
