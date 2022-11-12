import pandas as pd

# imports data from all T20Is
df = pd.read_csv("T20I_Matches_Data.csv")

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

# these are all the teams that qualified for each World Cup
wc_years = {'2007': ['South Africa', 'Bangladesh', 'West Indies', 'Australia', 'England', 'Zimbabwe', 'Sri Lanka',
                     'New Zealand', 'Kenya', 'India', 'Pakistan', 'Scotland'],
            '2009': ['India', 'Bangladesh', 'Ireland', 'Pakistan', 'England', 'Netherlands', 'Australia', 'Sri Lanka',
                     'West Indies', 'New Zealand', 'South Africa', 'Scotland'],
            '2010': ['Pakistan', 'Bangladesh', 'Australia', 'Sri Lanka', 'New Zealand', 'Zimbabwe', 'South Africa',
                     'India', 'Afghanistan', 'West Indies', 'England', 'Ireland'],
            '2012': ['England', 'India', 'Afghanistan', 'Australia', 'West Indies', 'Ireland', 'Sri Lanka',
                     'South Africa', 'Zimbabwe', 'Pakistan', 'New Zealand', 'Bangladesh'],
            '2014': ['Afghanistan', 'Bangladesh', 'Hong Kong', 'Ireland', 'Nepal', 'Netherlands', 'UAE', 'Zimbabwe',
                     'Australia', 'England', 'India', 'New Zealand', 'Pakistan', 'South Africa', 'Sri Lanka',
                     'West Indies'],
            '2016': ['Afghanistan', 'Bangladesh', 'Hong Kong', 'Ireland', 'Netherlands', 'Oman', 'Scotland', 'Zimbabwe',
                     'India', 'Australia', 'England', 'New Zealand', 'Pakistan', 'South Africa', 'Sri Lanka',
                     'West Indies'],
            '2021': ['Bangladesh', 'Ireland', 'Namibia', 'Netherlands', 'Oman', 'Papua New Guinea', 'Scotland',
                     'Sri Lanka', 'India', 'Afghanistan', 'Australia', 'England', 'New Zealand', 'Pakistan',
                     'South Africa', 'West Indies'],
            '2022': ['Namibia', 'Sri Lanka', 'Scotland', 'West Indies', 'Netherlands', 'UAE', 'Ireland', 'Zimbabwe',
                     'Afghanistan', 'Australia', 'England', 'New Zealand', 'Bangladesh', 'India', 'Pakistan',
                     'South Africa']
            }
# creates an elo dictionary for all T20I teams
# These initial elo ratings are only for countries in the ODI ranking table in February 2005
elo_dict = {'Australia': 1926, 'New Zealand': 1904, 'Sri Lanka': 1910, 'Pakistan': 1899, 'England': 1899,
            'West Indies': 1891, 'South Africa': 1883, 'India': 1879, 'Zimbabwe': 1766, 'Kenya': 1649,
            'Bangladesh': 1550}

# every country is given a starting rating of 1500 except countries where ratings are provided above. Bangladesh,
# Zimbabwe, and Kenya have won about 57% of T20I matches, so Bangladesh, the lowest-ranked ODI side in February 2005
# gets a 50 rating bump
for country_code, country in code_to_country.items():
    if country not in elo_dict:
        elo_dict.update({country: 1500})
wc_initiated = False
# goes through match data for all T20Is and determines elo ratings
for match, match_facts in df.iterrows():
    bf = match_facts["Batting First"]
    bs = match_facts["Batting Second"]
    winner = match_facts["Winner"]
    if winner == 'No Result':
        continue
    bf_pre_match_elo = elo_dict[bf]
    bs_pre_match_elo = elo_dict[bs]
    if not wc_initiated:
        if match_facts["Date"][0:4] in wc_years:
            if match_facts['World Cup Match?']:
                wc_initiated = True
                for country in wc_years[match_facts["Date"][0:4]]:
                    # countries get a boost of 75 to indicate they have qualified for the World Cup
                    # This ensures nations who suffer heavy defeats at the World Cup are only penalized in relation to
                    # other World Cup teams and not teams who did not qualify for the World Cup
                    elo_dict.update({country: elo_dict[country] + 75})
        else:
            wc_initiated = False
    else:
        if match_facts["Date"][0:4] not in wc_years:
            wc_initiated = False
    k_factor = 20
    if match_facts['World Cup Match?']:
        k_factor *= 2
    # calculates the odds of the team batting first winning the match
    bf_win_expectancy = 1 / (10 ** ((bs_pre_match_elo - bf_pre_match_elo) / 400) + 1)
    bf_adjusted_run_rate = match_facts["Team 1 Adjusted Run Rate"]
    bs_adjusted_run_rate = match_facts["Team 2 Adjusted Run Rate"]
    if winner == bf:
        bf_change_in_rating = k_factor * bf_adjusted_run_rate / bs_adjusted_run_rate * (1 - bf_win_expectancy)
    elif winner == 'Tie':
        bf_change_in_rating = k_factor * (0.5 - bf_win_expectancy)
    else:
        bf_change_in_rating = k_factor * -1 * bs_adjusted_run_rate / bf_adjusted_run_rate * (
                    1 - (1 - bf_win_expectancy))
    bs_change_in_rating = 0 - bf_change_in_rating
    elo_dict.update({bf: bf_pre_match_elo + bf_change_in_rating})
    elo_dict.update({bs: bs_pre_match_elo + bs_change_in_rating})

elo_country_data = []
for country, rating in elo_dict.items():
    elo_country_data.append([country, rating])

elo_df = pd.DataFrame(elo_country_data, columns=['Country', 'Rating'])

elo_df['Rank'] = elo_df['Rating'].rank(ascending=0)
elo_df = elo_df.round()
elo_df = elo_df.astype({"Rank": 'int', "Rating": 'int'})
elo_df = elo_df.set_index('Rank')
elo_df = elo_df.sort_index()

# exports T20I Ratings to a CSV file
elo_df.to_csv("T20I_Team_Ratings.csv", index=True, header=True)