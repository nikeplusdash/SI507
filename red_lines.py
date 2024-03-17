import os
import random as random
import json
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.path import Path
import matplotlib
from requests import get

class DetroitDistrict:
    """
    A class representing a district in Detroit with attributes related to historical redlining.
    coordinates,holcGrade,holcColor,id,description should be load from the redLine data file
    if cache is not available

    Parameters 
    ------------------------------
    coordinates : list of lists, 2D List, not list of list of list
        Coordinates defining the district boundaries from the json file
        Note that some districts are non-contiguous, which may
        effect the structure of this attribute

    holcGrade : str
        The HOLC grade of the district.

    id : str
        The identifier for the district, the HOLC ID.

    description : str, optional
        Qualitative description of the district.

    holcColor : str, optional
        A string represent the color of the holcGrade of the district

    randomLat : float, optional
        A random latitude within the district (default is None).

    randomLong : float, optional
        A random longitude within the district (default is None).

    medIncome : int, optional
        Median household income for the district, to be filled later (default is None).
        
    censusTract : str, optional
        Census tract code for the district (default is None).


    Attributes
    ------------------------------
    self.coordinates 
    self.holcGrade 
    holcColor : str
        The color representation of the HOLC grade.
        • Districts with holc grade A should be assigned the color 'darkgreen'
        • Districts with holc grade B should be assigned the color 'cornflowerblue'
        • Districts with holc grade C should be assigned the color 'gold'
        • Districts with holc grade D should be assigned the color 'maroon'
        If there is no input for holcColor, it should be generated based on the holcGrade and the rule above.

    self.id 
    self.description 
    self.randomLat 
    self.randomLong 
    self.medIncome 
    self.censusTract 
    """

    def __init__(self, coordinates, holcGrade, id, description, holcColor = None, randomLat=None, randomLong=None, medIncome=None, censusTract=None, state=None, county=None):
        """
        Initializes a DetroitDistrict instance with the specified attributes.
        """
        self.coordinates = coordinates
        self.holcGrade = holcGrade
        self.id = id
        self.description = description
        self.randomLat = randomLat
        self.randomLong = randomLong
        self.medIncome = medIncome
        self.censusTract = censusTract
        self.state = state
        self.county = county
        if holcColor is None:
            if holcGrade == 'A':
                self.holcColor = 'darkgreen'
            elif holcGrade == 'B':
                self.holcColor = 'cornflowerblue'
            elif holcGrade == 'C':
                self.holcColor = 'gold'
            elif holcGrade == 'D':
                self.holcColor = 'maroon'
        else:
            self.holcColor = holcColor

class RedLines:
    """
    A class to manage and analyze redlining district data.

    Attributes
    ----------
    districts : list of DetroitDistrict
        A list to store instances of DetroitDistrict.

    """

    def __init__(self,cacheFile = None):
        """
        Initializes the RedLines class without any districts.
        assign districts attribute to an empty list
        """
        self.districts = []
        if cacheFile is not None:
            self.loadCache(cacheFile)

    def createDistricts(self, fileName):
        """
        Creates DetroitDistrict instances from redlining data in a specified file.
        Based on the understanding in step 1, load the file,parse the json object, 
        and create 238 districts instance.
        Finally, store districts instance in a list, 
        and assign the list to be districts attribute of RedLines.

        Parameters
        ----------
        fileName : str
            The name of the file containing redlining data in JSON format.

        Hint
        ----------
        The data for description attribute could be from  
        one of the dict key with only number.

        """
        with open(fileName, 'r') as f:
            data = json.load(f)['features']
            for i in range(data.__len__()):
                coordinates = data[i]['geometry']['coordinates'][0][0]
                holcGrade = data[i]['properties']['holc_grade']
                id = data[i]['properties']['holc_id']
                description = data[i]['properties']['area_description_data']['8']
                holcColor = None
                district = DetroitDistrict(coordinates, holcGrade, id, description, holcColor)
                self.districts.append(district)

    def plotDistricts(self):
        """
        Plots the districts using matplotlib, displaying each district's location and color.
        Name it redlines_graph.png and save it to the current directory. 
        """
        fig, ax = plt.subplots()
        for district in self.districts:
            ax.add_patch(matplotlib.patches.Polygon(district.coordinates, closed=True, fill=True, color=district.holcColor))
            ax.autoscale()
        plt.rcParams["figure.figsize"] = (15,15)
        plt.savefig('redlines_graph.png')
        plt.show()

    def generateRandPoint(self):
        """
        Generates a random point within the boundaries of each district.

        This method creates a mesh grid of points covering the geographical area of interest
        and then selects a random point within the boundary of each district.

        Attributes
        ----------
        self.districts : list of DetroitDistrict
            The list of district instances in the RedLines class.

        Note
        ----
        The random point is assigned as the randomLat and randomLong  for each district.
        This method assumes the 'self.districts' attribute has been populated with DetroitDistrict instances.

        """
        xgrid = np.arange(-83.5,-82.8,.004)
        ygrid = np.arange(42.1, 42.6, .004)
        xmesh, ymesh = np.meshgrid(xgrid,ygrid)
        mesh = np.vstack((xmesh.flatten(),ymesh.flatten())).T
        for district in self.districts:
            points = Path(district.coordinates)
            grid = points.contains_points(mesh)
            point = mesh[random.choice(list(np.where(grid)[0]))]
            district.randomLong = point[0]
            district.randomLat = point[1]
        
    def fetchCensus(self):
        """
        Fetches the census tract for each district in the list of districts using the FCC API.

        This method iterates over the all districts in `self.districts`, retrieves the census tract 
        for each district based on its random latitude and longitude, and updates the district's 
        `censusTract` attribute.

        Note
        ----
        The method fetches data from "https://geo.fcc.gov/api/census/area" and assumes that 
        `randomLat` and `randomLong` attributes of each district are already set.

        The function `fetch` is an internal helper function that performs the actual API request.

        In the api call, check if the response.status_code is 200.
        If not, it might indicate the api call made is not correct, check your api call parameters.

        If you get status_code 200 and other code alternativly, it could indicate the fcc webiste is not 
        stable. Using a while loop to make anther api request in fetch function, until you get the correct result. 

        Important
        -----------
        The order of the API call parameter has to follow the following. 
        'lat': xxx,'lon': xxx,'censusYear': xxx,'format': 'json' Or
        'lat': xxx,'lon': xxx,'censusYear': xxx

        """
        # progress = 0
        # PROGRESS_SCALE = 10
        for district in self.districts:
            # get census tract for each district using fetch function
            response = get('https://geo.fcc.gov/api/census/area', params={'lat': district.randomLat, 'lon': district.randomLong, 'format': 'json'})

            if response.status_code == 200:
                district.censusTract = response.json()['results'][0]['block_fips'][5:11]
            else:
                while response.status_code != 200:
                    response = get('https://geo.fcc.gov/api/census/area', params={'lat': district.randomLat, 'lon': district.randomLong, 'format': 'json'})
                    if response.status_code == 200:
                        district.censusTract = response.json()['results'][0]['block_fips'][5:11]
                        break
        #     progress += 1
        #     print('|',''.join(["█" for _ in range(int(progress/PROGRESS_SCALE))]),''.join(["—" for _ in range(int((len(self.districts) - progress)/PROGRESS_SCALE))]), "|       ", int(progress/len(self.districts)*100)," %", sep='', end='\r')
        # print("                                                                                ")

    def fetchIncome(self):

        """
        Retrieves the median household income for each district based on the census tract.

        This method requests income data from the ACS 5-Year Data via the U.S. Census Bureau's API 
        for the year 2018. It then maps these incomes to the corresponding census tracts and updates 
        the median income attribute of each district in `self.districts`.

        Note
        ----
        The method assumes that the `censusTract` attribute for each district is already set. It updates 
        the `medIncome` attribute of each district based on the fetched income data. If the income data 
        is not available or is negative, the median income is set to 0.
        """
        API_KEY = '2dd4d753356f540b4f1333f33ed71f5f6c94f0c5'
        response = get('https://api.census.gov/data/2018/acs/acs5?get=B19013_001E&for=tract:*&in=state:26&key='+API_KEY)
        income_data = response.json()
        tract_income = {data[-1]: data[0] for data in income_data[1:]}
        for district in self.districts:
            district.medIncome = int(tract_income.get(district.censusTract, 0))
            if district.medIncome < 0:
                district.medIncome = 0

    def calcIncomeStats(self):
        """
        Use np.median and np.mean to
        Calculates the mean and median of median household incomes for each district grade (A, B, C, D).

        This method computes the mean and median incomes for districts grouped by their HOLC grades.
        The results are stored in a list following the pattern: [AMean, AMedian, BMean, BMedian, ...].
        After your calculations, you need to round the result to the closest whole int.
        Relate reading https://www.w3schools.com/python/ref_func_round.asp


        Returns
        -------
        list
            A list containing mean and median income values for each district grade in the order A, B, C, D.
        """
        list_to_return = []
        for grade in ['A', 'B', 'C', 'D']:
            income_list = [district.medIncome for district in self.districts if district.holcGrade == grade]
            list_to_return.append(round(np.mean(income_list)))
            list_to_return.append(round(np.median(income_list)))
        print(list_to_return)
        return list_to_return

    def findCommonWords(self):
        """
        Analyzes the qualitative descriptions of each district category (A, B, C, D) and identifies the
        10 most common words unique to each category.

        This method aggregates the qualitative descriptions for each district category, splits them into
        words, and computes the frequency of each word. It then identifies and returns the 10 most 
        common words that are unique to each category, excluding common English filler words.

        Returns
        -------
        list of lists
            A list containing four lists, each list containing the 10 most common words for each 
            district category (A, B, C, D). The first list should represent grade A, and second for grade B,etc.
            The words should be in the order of their frequency.

        Notes
        -----
        - Common English filler words such as 'the', 'of', 'and', etc., are excluded from the analysis.
        - The method ensures that the common words are unique across the categories, i.e., no word 
        appears in more than one category's top 10 list.
        - Regular expressions could be used for word splitting to accurately capture words from the text.
        - Counter from collections could also be used.

        """
        # List of common filler words to exclude
        filler_words = set(['the', 'of', 'and', 'in', 'to', 'a', 'is', 'for', 'on', 'that'])
        word_freq = {'A': {}, 'B': {}, 'C': {}, 'D': {}}
        
        for district in self.districts:
            for word in district.description.split():
                if word.lower() not in filler_words:
                        word_freq[district.holcGrade][word] = word_freq[district.holcGrade].get(word, 0) + 1
        for grade in word_freq:
            word_freq[grade] = sorted(word_freq[grade].items(), key=lambda x: x[1], reverse=True)
            word_freq[grade] = [word[0] for word in word_freq[grade][:10]]
        
        print(word_freq)

        return [word_freq['A'], word_freq['B'], word_freq['C'], word_freq['D']]
    
    def calcRank(self):
        """
        Calculates and assigns a rank to each district based on median income.

        This method sorts the districts in descending order of their median income and then assigns
        a rank to each district, with 1 being the highest income district.

        Note
        ----
        The rank is assigned based on the position in the sorted list, so the district with the highest
        median income gets a rank of 1, the second-highest gets 2, and so on. Ties are not accounted for;
        each district will receive a unique rank.

        Attribute 
        ----
        rank

        """
        sorted_districts = sorted(self.districts, key=lambda x: x.medIncome, reverse=True)

        for district in sorted_districts:
            district.rank = sorted_districts.index(district) + 1

        rank = {'A': 0, 'B': 0, 'C': 0, 'D': 0}
        for grade in ['A', 'B', 'C', 'D']:
            rank[grade] = [district.rank for district in self.districts if district.holcGrade == grade]
            print(f"Average rank of District [Grade: {grade}]: {round(np.mean(rank[grade]), 2)}")
        
    def calcPopu(self):
        """
        Fetches and calculates the percentage of Black or African American residents in each district.

        This method fetch the total and Black populations for each census tract in Michigan from 
        the U.S. Census Bureau's API, like the median income data.  It then calculates the percentage of Black residents in each tract
        and assigns this value to the corresponding district percent attribute.

        Note
        ----
        The method assumes that the census tract IDs in the district data match those used by the Census Bureau.
        The percentage is rounded to two decimal places. If the Black population is zero, the percentage is set to 0. 
        Elif the total population is zero, the percentage is set to 1.


        Attribute 
        ----
        percent

        """

        API_KEY = '2dd4d753356f540b4f1333f33ed71f5f6c94f0c5'
        response = get('https://api.census.gov/data/2018/acs/acs5?get=B02001_003E,B02001_001E&for=tract:*&in=state:26&key='+API_KEY)
        population_data = response.json()
        tract_population = {data[-1]: (int(data[0]), int(data[1])) for data in population_data[1:]}

        for district in self.districts:
            population = tract_population.get(district.censusTract, (0, 0))
            if population[0] == 0:
                district.percent = 0
            elif population[1] == 0:
                district.percent = 1
            else:
                district.percent = round(population[0]/population[1]*100, 2)
            
        # aggregate and print rough percentage of black population in each district grade (A, B, C, D)
        percent = {'A': [], 'B': [], 'C': [], 'D': []}
        for grade in ['A', 'B', 'C', 'D']:
            percent[grade] = [district.percent for district in self.districts if district.holcGrade == grade]
            print(f"Rough percentage of black population in grade {grade}: {round(np.mean(percent[grade]), 2)}")
            

    def cacheData(self, fileName='redlines_cache.json'):
        """
        Saves the current state of district data to a file in JSON format.
        Using the __dict__ magic method on each district instance, and save the 
        result of it to a list.
        After creating the list, dump it to a json file with the inputted name.
        You should name the cache file as redlines_cache.json

        Parameters
        ----------
        filename : str
            The name of the file where the district data will be saved.
        """
        file_dump = [district.__dict__ for district in self.districts]
        with open(fileName, 'w') as f:
            json.dump(file_dump, fp=f)

    def loadCache(self, fileName='redlines_cache.json'):
        """
        Loads district data from a cache JSON file if it exists.

        Parameters
        ----------
        fileName : str
            The name of the file from which to load the district data.
            You should name the cache file as redlines_cache.json

        Returns
        -------
        bool
            True if the data was successfully loaded, False otherwise.
        """
        if os.path.isfile(fileName):
            with open(fileName, 'r') as f:
                data = json.load(f)
                self.districts = [DetroitDistrict(**data) for data in data]
            return True
        else:
            return False

    def comment(self):
        '''
        Look at the
        districts in each category, A, B, C and D. Are there any trends that you see? Share 1 paragraph of your
        findings. And a few sentences(more than 50 words) about how this exercise did or did not change your understanding of
        residential segregation. Print you thought in the method.
        '''
        print("The average rank per district shows that district A and B rank higher than district C and D. The average percentage of black population in each district grade also shows that district A and B have a lower percentage of black population than district C and D. This is further supplemented by the mean and median income discrepancy in the 4 zones (A, B, C, D), wherein Zone A & B have marginally higher income than those in Zone C & D, which shows that there is an income disaparity. This data correlation insinuates presence of redlining in the United States")

def main():
    # myRedLines = RedLines()
    # myRedLines.createDistricts('redlines_data.json')
    # myRedLines.plotDistricts()
    # myRedLines.findCommonWords()
    # myRedLines.generateRandPoint()
    # myRedLines.fetchCensus()
    # myRedLines.cacheData('redlines_cache.json')

    myRedLines = RedLines('redlines_cache.json')
    myRedLines.fetchIncome()
    myRedLines.calcIncomeStats()
    myRedLines.calcRank()
    myRedLines.calcPopu()
    myRedLines.comment()

if __name__ == '__main__':
    main()