__author__ = 'vishal'

from data_fetcher import DataFetcher
import json

class Handicap(object):

    def __init__(self, host, key):
        self.data_fetcher = DataFetcher(host, key)

    def calculate(self, player_name, tour, year, tournament_id, slope):
        differentials = []
        for round in range(1, 6):
            scorecard = json.load(self.data_fetcher.get_scorecards_per_round(tour, year, tournament_id, round))
            print scorecard
            if 'round' in scorecard:
                for player in scorecard['round']['players']:
                    if player['first_name']+' '+player['last_name'] == player_name:
                        gross_score = 0
                        par = player['course']['par']
                        for score in player['scores']:
                            gross_score += score['strokes']
                        differential = self.handicap_differential(gross_score, int(slope))
                        differentials.append(differential)
        handicap = self.handicap_index(differentials)
        course_handicap = self.course_handicap(handicap, int(slope))
        return handicap, course_handicap

    def handicap_index(self, differentials):
        count = 0
        total = 0
        for differential in differentials:
            count += 1
            total += differential
        return (total/count)*0.96

    def handicap_differential(self, gross_score, slope_rating):
        differential = (85 - gross_score) * 113 / slope_rating
        return differential

    def course_handicap(self, index, slope):
        course_handicap = ( index * slope )/113
        return course_handicap

