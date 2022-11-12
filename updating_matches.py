from espncricinfo.match import Match
import pandas as pd
import requests
from bs4 import BeautifulSoup
import re

# imports data from all T20Is before the 2022 ICC World Cup
df = pd.read_csv("T20I_Matches_Data.csv")

# anticipated years of matches where an update is necessary
years = ['2022']
last_match_number_in_year = 369

match_ids = []

# scrapes data from each year of T20I matches and adds the Match IDs for the year to a list
for year in years:
    url = 'https://stats.espncricinfo.com/ci/engine/records/team/match_results.html?class=3;id=' + year + ';type=year'
    reqs = requests.get(url)
    soup = BeautifulSoup(reqs.text, 'html.parser')
    matches = soup.find_all(class_='data1')
    for match in matches:
        link_in_html = match.find_all('a')[-1]
        link = link_in_html.get('href')
        match_id_finder = re.search('/ci/engine/match/(.*).html', link)
        match_id = match_id_finder.group(1)
        match_ids.append(match_id)
match_ids = match_ids[last_match_number_in_year + 1:]

# Match Ids for the 2022 ICC T20I World Cup
wc_2022_match_ids = ['1298135', '1298136', '1298137', '1298138', '1298139', '1298140', '1298141', '1298142', '1298143',
                     '1298144', '1298145', '1298146', '1298147', '1298148', '1298149', '1298150', '1298151', '1298152',
                     '1298153', '1298154', '1298155', '1298156', '1298157', '1298158', '1298159', '1298160', '1298161',
                     '1298162', '1298163', '1298164', '1298165', '1298166', '1298167', '1298168', '1298169', '1298170',
                     '1298171', '1298172', '1298173', '1298174', '1298175', '1298176', '1298177', '1298178', '1298179']

# converts team abbreviation to full team name
code_to_country = {'AUS': 'Australia', 'NZ': 'New Zealand', 'ENG': 'England', 'SA': 'South Africa', 'WI': 'West Indies',
                   'SL': 'Sri Lanka', 'PAK': 'Pakistan', 'BAN': 'Bangladesh', 'ZIM': 'Zimbabwe', 'INDIA': 'India',
                   'KENYA': 'Kenya', 'SCOT': 'Scotland', 'NED': 'Netherlands', 'IRE': 'Ireland', 'CAN': 'Canada',
                   'BMUDA': 'Bermunda', 'AFG': 'Afghanistan', 'NEPAL': 'Nepal', 'UAE': 'UAE', 'PNG': 'Papua New Guinea',
                   'OMA': 'Oman', 'BHR': 'Bahrain', 'Saudi': 'Saudi Arabia', 'Mald': 'Maldives', 'KUW': 'Kuwait',
                   'QAT': 'Qatar', 'USA': 'USA', 'PHI': 'Philippines', 'VAN': 'Vanuatu', 'MLT': 'Malta', 'ESP': 'Spain',
                   'Mex': 'Mexico', 'Blz': 'Belize', 'NGA': 'Nigeria', 'Ghana': 'Ghana', 'NAM': 'Namibia',
                   'UGA': 'Uganda', 'BOT': 'Botswana', 'ITA': 'Italy', 'JER': 'Jersey', 'GUE': 'Guernsey',
                   'NOR': 'Norway', 'DEN': 'Denmark', 'THAI': 'Thailand', 'Samoa': 'Samoa', 'Fin': 'Finland',
                   'SGP': 'Singapore', 'Caym': 'Cayman Islands', 'ROM': 'Romania', 'Aut': 'Austria', 'TKY': 'Turkey',
                   'LUX': 'Luxembourg', 'CZK-R': 'Czech Republic', 'Arg': 'Argentina', 'BRA': 'Brazil',
                   'Chile': 'Chile', 'Peru': 'Peru', 'SRB': 'Serbia', 'BUL': 'Bulgaria', 'GRC': 'Greece',
                   'PORT': 'Portugal', 'GIBR': 'Gibraltar', 'MOZ': 'Mozambique', 'MWI': 'Malawi', 'BHU': 'Bhutan',
                   'Iran': 'Iran', 'IOM': 'Isle of Man', 'Fran': 'France', 'SWE': 'Sweden', 'RWN': 'Rwanda',
                   'HUN': 'Hungary', 'EST': 'Estonia', 'CYP': 'Cyprus', 'SWA': 'Swaziland', 'LES': 'Lesotho',
                   'SEY': 'Seychelles', 'SLE': 'Sierra Leone', 'SUI': 'Switzerland', 'TAN': 'Tanzania',
                   'CAM': 'Cameroon', 'Bhm': 'Bahamas', 'ISR': 'Israel', 'CRT': 'Croatia', 'SVN': 'Slovenia',
                   'SWZ': 'Eswatini', 'Fiji': 'Fiji', 'COK': 'Cook Islands', 'JAPAN': 'Japan', 'INA': 'Indonesia',
                   'SKOR': 'South Korea', 'HKG': 'Hong Kong', 'CRC': 'Costa Rica', 'PNM': 'Panama', 'GER': 'Germany',
                   'Belg': 'Belgium', 'MAL': 'Malaysia'
                   }

# finds country based on city. Many cities in Caribbean countries are instead given 'West Indies' as value instead of
# the original country. This is to be consistent with the national side 'West Indies'.
cities_to_country = {'Auckland': 'New  Zealand', 'Southampton': 'England', 'Johannesburg': 'South Africa',
                     'Brisbane': 'Australia', 'Bristol': 'England', 'Khulna': 'Bangladesh', 'Wellington': 'New Zealand',
                     'Sydney': 'Australia', 'London': 'England', 'Nairobi': 'Kenya', 'Durban': 'South Africa',
                     'Cape Town': 'South Africa', 'Mumbai': 'India', 'Perth': 'Australia', 'Gqeberha': 'South Africa',
                     'Melbourne': 'Australia', 'Christchurch': 'New Zealand', 'Karachi': 'Pakistan',
                     'Manchester': 'England', 'Bridgetown': 'West Indies', 'Belfast': 'Northern Ireland',
                     'King City': 'Canada', 'Hamilton': 'New Zealand', 'Colombo': 'Sri Lanka',
                     'Port of Spain': 'West Indies', 'Centurion': 'South Africa', 'Dubai': 'UAE',
                     'Nottingham': 'England', 'Basseterre': 'West Indies', 'Nagpur': 'India', 'Chandigarh': 'India',
                     'Abu Dhabi': 'UAE', 'Hobart': 'Australia', 'Providence': 'West Indies',
                     'Gros Islet': 'West Indies', 'North Sound': 'West Indies', 'Lauderhill': 'USA',
                     'Harare': 'Zimbabwe', 'Birmingham': 'England', 'Cardiff': 'Wales', 'Bloemfontein': 'South Africa',
                     'Kimberley': 'South Africa', 'Adelaide': 'Australia', 'Kandy': 'Sri Lanka', 'Dhaka': 'Bangladesh',
                     'Kolkata': 'India', 'Mombasa': 'Kenya', 'Hambantota': 'Sri Lanka', 'The Hague': 'Netherlands',
                     'Chester-le-Street': 'England', 'Chennai': 'India', 'Pune': 'India', 'East London': 'South Africa',
                     'Bengaluru': 'South Africa', 'Ahmedabad': 'India', 'Sharjah': 'UAE', 'Windhoek': 'Namibia',
                     'Bulawayo': 'Zimbabwe', 'Aberdeen': 'Scotland', 'Kingstown': 'West Indies', 'Rajkot': 'India',
                     'Chattogram': 'Bangladesh', 'Kingston': 'West Indies', 'Sylhet': 'Bangladesh',
                     'Roseau': 'West Indies', 'Lahore': 'Pakistan', 'Bready': 'Northern Ireland',
                     'Amstelveen': 'Netherlands', 'Rotterdam': 'Netherlands', 'Edinburgh': 'Scotland',
                     'Dublin': 'Ireland', 'Dharamsala': 'India', 'Cuttack': 'India', 'Mount Maunganui': 'New Zealand',
                     'Mong Kok': 'Hong Kong', 'Townsville': 'Australia', 'Ranchi': 'India', 'Visakhapatnam': 'India',
                     'Fatullah': 'Bangladesh', 'Delhi': 'India', 'Napier': 'New Zealand', 'Kanpur': 'India',
                     'Geelong': 'Australia', 'Greater Noida': 'India', 'Taunton': 'England', 'Guwahati': 'India',
                     'Potchefstroom': 'South Africa', 'Thiruvananthapuram': 'India', 'Indore': 'India',
                     'Nelson': 'New Zealand', 'Dehra Dun': 'India', 'Deventer': 'Netherlands', 'Lucknow': 'India',
                     'Carrara': 'Australia', 'Al Amarat': 'Oman', 'Port Moresby': 'Papua New Guinea', 'Murcia': 'Spain',
                     'Naucalpan': 'Mexico', 'Waterloo': 'Belgium', 'Kampala': 'Uganda', 'Utrecht': 'Netherlands',
                     'St Peter Port': 'Guernsey', 'Castel': 'Guernsey', 'Kuala Lumpur': 'Malaysia', 'Doha': 'Qatar',
                     'Apia': 'Samoa', 'Brondby': 'Denmark', 'Singapore': 'Singapore', 'Kerava': 'Finland',
                     'Ilfov County': 'Romania', 'Lima': 'Peru', 'Corfu': 'Greece', 'Marsa': 'Malta',
                     'Canberra': 'Australia', 'Lilongwe': 'Malawi', 'Blantyre': 'Malawi', 'Kirtipur': 'Nepal',
                     'Hyderabad': 'India', "St George's": 'West Indies', 'Bangkok': 'Thailand', 'Almeria': 'Spain',
                     'Walferdange': 'Luxembourg', 'Sofia': 'Bulgaria', 'Rawalpindi': 'Pakistan',
                     'Paarl': 'South Africa', 'Dunedin': 'New Zealand', 'Coolidge': 'West Indies',
                     'Prague': 'Czech Republic', 'Leeds': 'England', 'Krefeld': 'Germany', 'Kigali City': 'Rwanda',
                     'Albergaria': 'Portugal', 'Entebbe': 'Uganda', 'Episkopi': 'Cyprus', 'Lagos': 'Nigeria',
                     'Jaipur': 'India', 'George Town': 'Cayman Islands', 'Lower Austria': 'Austria', 'Ghent': 'Belgium',
                     'Bangi': 'Malaysia', 'Belgrade': 'Serbia', 'Vantaa': 'Finland', 'Malkerns': 'Swaziland',
                     'Tarouba': 'West Indies', 'Port Vila': 'Vanuatu', 'Benoni': 'South Africa', 'Sano': 'Japan',
                     'Dar-es-Salaam': 'Tanzania'
                     }

# analyzes each match and extracts key data
match_nums = []
is_world_cup_match = []
dates = []
grounds = []
cities = []
countries = []
winners = []
bf = []
bf_runs = []
bf_wickets = []
bf_overs = []
bf_adjusted_run_rate = []
bs = []
bs_runs = []
bs_wickets = []
bs_overs = []
bs_adjusted_run_rate = []
num_of_matches = len(match_ids)
for match_num, match_id in enumerate(match_ids):
    match = Match(match_id)
    match_nums.append(match_num + 1827)
    dates.append(match.date)
    if match_id in wc_2022_match_ids:
        is_world_cup_match.append(True)
    else:
        is_world_cup_match.append(False)
    full_ground_name = match.ground_name
    if "," in full_ground_name:
        grounds.append(full_ground_name.split(',')[0])
    else:
        grounds.append(full_ground_name)
    cities.append(match.town_name)
    country_of_match = cities_to_country[cities[-1]]
    countries.append(country_of_match)
    if match.result[0:9] == 'No result':
        winners.append('No Result')
    elif match.result[0:10] == 'Match tied':
        winners.append('Tie')
    elif match.result == 'Match abandoned without a ball bowled':
        winners.append('No Result')
    else:
        winners.append(code_to_country[match.match_winner])
    team_1 = code_to_country[match.team_1_abbreviation]
    team_2 = code_to_country[match.team_2_abbreviation]
    batting_first = code_to_country[match.batting_first]
    innings = match.innings
    if len(innings) > 0:
        for inning_number, inning in enumerate(innings):
            if inning_number == 0:
                bf.append(batting_first)
                bf_runs.append(int(inning['runs']))
                bf_wickets.append(int(inning['wickets']))
                overs_completed = int(inning['balls']) // 6
                balls_in_last_over = int(inning['balls']) % 6
                overs = str(overs_completed)
                if balls_in_last_over != 0:
                    overs += '.' + str(balls_in_last_over)
                bf_overs.append(overs)
                if bf_wickets[-1] != 10:
                    balls_for_rr = overs_completed * 6 + balls_in_last_over
                else:
                    balls_for_rr = int(inning['ball_limit'])
                if balls_for_rr == 0:
                    bf_adjusted_run_rate.append('NA')
                else:
                    bf_adjusted_run_rate.append(bf_runs[-1] / balls_for_rr * 6)
            else:
                if team_1 == batting_first:
                    bs.append(team_2)
                else:
                    bs.append(team_1)
                bs_runs.append(int(inning['runs']))
                bs_wickets.append(int(inning['wickets']))
                overs_completed = int(inning['balls']) // 6
                balls_in_last_over = int(inning['balls']) % 6
                overs = str(overs_completed)
                if balls_in_last_over != 0:
                    overs += '.' + str(balls_in_last_over)
                bs_overs.append(overs)
                if bf_wickets[-1] != 10:
                    balls_for_rr = int(inning['balls'])
                else:
                    balls_for_rr = int(inning['ball_limit'])
                if balls_for_rr == 0:
                    bs_adjusted_run_rate.append('NA')
                else:
                    bs_adjusted_run_rate.append(bs_runs[-1] / balls_for_rr * 6)
    else:
        bf.append(batting_first)
        bf_runs.append(0)
        bf_wickets.append(0)
        bf_overs.append(0)
        bf_adjusted_run_rate.append('NA')
        if team_1 == batting_first:
            bs.append(team_2)
        else:
            bs.append(team_1)
        bs_runs.append(0)
        bs_wickets.append(0)
        bs_overs.append(0)
        bs_adjusted_run_rate.append('NA')
    print(str((match_num + 1) * 100 / num_of_matches) + '% complete')

new_data = {'T20I #': match_nums, 'World Cup Match?': is_world_cup_match, 'Winner': winners, 'Date': dates, 'Batting First': bf,
        'Team 1 Runs': bf_runs, 'Team 1 Wickets': bf_wickets, 'Team 1 Overs': bf_overs,
        'Team 1 Adjusted Run Rate': bf_adjusted_run_rate, 'Batting Second': bs, 'Team 2 Runs': bs_runs,
        'Team 2 Wickets': bs_wickets, 'Team 2 Overs': bs_overs,
        'Team 2 Adjusted Run Rate': bs_adjusted_run_rate, 'Ground': grounds, 'City': cities, 'Country': countries}
new_df = pd.DataFrame(new_data)

# Combines pre-WC data with 2022 T20 World Cup Data
df = pd.concat([df, new_df])

# updates data frame to original CSV file
df.to_csv("T20I_Matches_Data.csv", index=False, header=True)
