# Project Benson
## Exploring NYC MTA Turnsile Data

### Background Info
Project Benson consists of playing the part of a data science consultant to the WomenTechWomenYes (WTWY), whose charter is to increase support and awareness for women in technology.  After your initial contact at a recent event, you received a proposal to assist the organization with the placement of their street teams leading up to their annual summer gala.

### Approach
After receiving the proposal, my partner and I broke the project down into 3 parts:
1. Definition of objectives and assumptions. 
2. Data identification.
3. Data acquisition and analysis.

#### Part 1:
After reviewing the proposal, we determined the multifaceted problem of optimal street team placement was driven by two main objectives, increase attendance and attract monetary support.  From these objectives we derived a target demographic for the WTWY gala.  We made additional assumptions regarding the date of the event as well as the timeline for street team canvassing as well as defined our assumptions regarding the event date and canvassing timeframe.

##### Objectives
Optimize Placement of WTWY street teams to:
* Increase attendance at their annual summer gala.
* Attract potential donors to the organization.

##### Assumptions
* WYWT annual gala will be held mid-June 2018.
* Street team canvassing will target March through June 2018 timeframe.
* Target Demographic:
    * Highly Educated (bachelors degree or higher)
    * Techology Workers (engineers, scientists, researchers, etc.)
    * Wealthy Donors (yearly income greater than $200K)

#### Part 2:
The WTWY client identified NYC MTA turnsile data as their primary data source of interest.  Because the insights available within the MTA turnsile data are limited mainly to foot traffic counts, we spent some time brainstorming and searching the web for potential data sources that would we could link to the MTA data to identify those stations most closely associated with the target demographic.  Our search led to several additional data sets of interest: American Community Survey (ACS) data from the US Census Bureau, ACS data from the NYC Department of City Planning, startup location data from Digital NYC and Built in NYC, and NYC technology Meetup locations.

##### Data
* NYC MTA Turnsile Data: Entry and exit counts for the years 2015 to 2017 during the months of March through June.
* 5-Year ACS data: Age, sex, income, education level data for the years 2011 to 2016.
* Current NYC startup locations as of January 2018.
* Current technology meetup locations as of January 2018.   
    
#### Part 3: 
Finally, we got to the fun stuff, actually getting the data and performing exploratory analysis.  Acquiring the MTA turnstile data was fairly straightforward.  It entailed scraping the HTML anchor tags from the MTA website to compile a list of links to each data file, then looping through the list to download each file that fell within the time period of interest.  Obtaining the ACS data was somewhat more painful as this required a deeper understanding of the different aggregation levels of the data as well as a tradeoff in time to acquire the data at a particular resolution.   , following a similar methodology to identify the paths to the data files

### Challenges
 
