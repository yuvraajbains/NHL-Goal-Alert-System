import requests
from config import WATCH_TEAMS
from sms import send_sms
import logging

seen_goals = set()

def check_for_goals():
    try:
        response = requests.get("https://api-web.nhle.com/v1/score/now", timeout=10)
        games = response.json().get("games", [])

        for game in games:
            state = game.get("gameState")
            if state not in ["LIVE", "FINAL"]:
                continue

            home = game["homeTeam"]["name"].get("default", "")
            away = game["awayTeam"]["name"].get("default", "")

            if home not in WATCH_TEAMS and away not in WATCH_TEAMS:
                continue

            for goal in game.get("goals", []):
                scorer = goal.get("lastName", {}).get("default", "Unknown")
                team = goal.get("teamAbbrev", "UNK")
                period = goal.get("period", "?")
                time_in_period = goal.get("timeInPeriod", "??:??")
                home_score = goal.get("homeScore", "?")
                away_score = goal.get("awayScore", "?")

                goal_key = f"{team}-{period}-{time_in_period}-{scorer}"
                if goal_key in seen_goals:
                    continue
                seen_goals.add(goal_key)

                message = (
                    f"🚨 GOAL! {scorer} scored for {team}.\n"
                    f"Score: {away} {away_score} - {home} {home_score}\n"
                    f"Period {period}, Time: {time_in_period}"
                )
                send_sms(message)

    except Exception as e:
        logging.error(f"❌ Error checking goals: {e}", exc_info=True)
