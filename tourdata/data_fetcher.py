__author__ = 'vishal'

import json
from utils import Utils

class DataFetcher(object):

    def __init__(self, host, key):
        self.utils = Utils(host, key)

    def get_tournament_schedule(self, tour, year):
        tour_data = self.utils.get_request("/schedule/"+tour+"/"+str(year)+"/tournaments/schedule.json")
        return tour_data

    def get_player_profiles(self, tour, year):
        player_profiles = self.utils.get_request("/profiles/"+tour+"/"+str(year)+"/players/profiles.json")
        return player_profiles

    def get_seasonal_statistics(self, tour, year):
        seasonal_statistics = self.utils.get_request("/seasontd/"+tour+"/"+str(year)+"/players/statistics.json")
        return seasonal_statistics

    def get_tournament_summary(self, tour, year, tournament_id):
        summary = self.utils.get_request("/summary/"+tour+"/"+str(year)+"/tournaments/"+tournament_id+"/summary.json")
        return summary

    def get_tournament_leaderboard(self, tour, year, tournament_id):
        leaderboard = self.utils.get_request("/leaderboard/"+tour+"/"+str(year)+"/tournaments/"+tournament_id+"/leaderboard.json")
        return leaderboard

    def get_tournament_hole_statistics(self, tour, year, tournament_id):
        hole_stats = self.utils.get_request("/hole_stats/"+tour+"/"+str(year)+"/tournaments/"+tournament_id+"/hole-statistics.json")
        return hole_stats

    def get_teetimes_per_round(self, tour, year, tournament_id, round):
        teetimes = self.utils.get_request("/teetimes/"+tour+"/"+str(year)+"/tournaments/"+tournament_id+"/rounds/"+str(round)+"/teetimes.json")
        return teetimes

    def get_scorecards_per_round(self, tour, year, tournament_id, round):
        scorecard = self.utils.get_request("/scorecards/"+tour+"/"+str(year)+"/tournaments/"+tournament_id+"/rounds/"+str(round)+"/scores.json")
        return scorecard

