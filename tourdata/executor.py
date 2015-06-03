__author__ = 'vishal'

import argparse
from handicap import Handicap
from data_fetcher import DataFetcher
import json

ap = argparse.ArgumentParser()
ap.add_argument("--host", required = True,
help = "host")
ap.add_argument("--key", required = True,
help = "key")
ap.add_argument("--tour", required = True,
help = "tour")
ap.add_argument("--year", required = True,
help = "year")
ap.add_argument("--tournament", required = True,
help = "tournament")
ap.add_argument("--player", required = True,
help = "player")
ap.add_argument("--slope", required = True,
help = "slope")
args = vars(ap.parse_args())

handicap = Handicap(args['host'], args['key'])
handicap = handicap.calculate(args['player'], args['tour'], args['year'], args['tournament'], args['slope'])
#df = DataFetcher(args['host'], args['key'])
#print df.get_tournament_schedule(args['tour'], args['year'])

#########
# commandline
#########
# python executor.py --host=http://api.sportradar.us/golf-t1 --key=auybdxsjvbdducmvj3et2v9a --tour=pga --year=2015 --tournament=b95ab96b-9a0b-4309-880a-ad063cb163ea --player="Jordan Spieth"
########


print handicap