# california-coronavirus-data

The Los Angeles Times' independent tally of coronavirus cases in California.

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/datadesk/california-coronavirus-data/master?urlpath=lab/tree/notebooks/examples.ipynb)
![Jupyer Notebook tests](https://github.com/datadesk/california-coronavirus-data/workflows/Jupyer%20Notebook%20tests/badge.svg)

## Table of contents

### Agency survey

- [latimes-agency-totals.csv](#latimes-agency-totalscsv)
- [latimes-county-totals.csv](#latimes-county-totalscsv)
- [latimes-state-totals.csv](#latimes-state-totalscsv)
- [latimes-place-polygons.geojson](#latimes-place-polygonsgeojson)
- [latimes-place-totals.csv](#latimes-place-totalscsv)
- [latimes-agency-websites.csv](#latimes-agency-websitescsv)

### CDPH press releases

- [cdph-age.csv](#cdph-agecsv)
- [cdph-hospital-patient-county-totals.csv](#cdph-hospital-patient-county-totalscsv)
- [cdph-hpi-zipcodes.csv](#cdph-hpi-zipcodescsv)
- [cdph-state-totals.csv](#cdph-state-totalscsv)
- [cdph-population-race-ethnicity.csv](#cdph-population-race-ethnicitycsv)
- [cdph-positive-test-rate.csv](#cdph-positive-test-ratecsv)
- [cdph-race-ethnicity.csv](#cdph-race-ethnicitycsv)
- [cdph-regional-stay-home-metrics.csv](#cdph-regional-stay-home-metricscsv)
- [cdph-reopening-metrics.csv](#cdph-reopening-metricscsv)
- [cdph-reopening-tiers.csv](#cdph-reopening-tierscsv)
- [cdph-vaccination-county-totals.csv](#cdph-vaccination-county-totalscsv)
- [cdph-vaccination-state-totals.csv](#cdph-vaccination-state-totalscsv)
- [cdph-vaccination-zipcode-totals.csv](#cdph-vaccination-zipcode-totalscsv)

### Nursing homes

- [cdph-adult-and-senior-care-facilities.csv](#cdph-adult-and-senior-care-facilitiescsv)
- [cdph-adult-and-senior-care-totals.csv](#cdph-skilled-nursing-totalscsv)
- [cdph-skilled-nursing-facilities.csv](#cdph-skilled-nursing-facilitiescsv)
- [cdph-skilled-nursing-totals.csv](#cdph-skilled-nursing-totalscsv)
- [cdph-nursing-home-county-totals.csv](#cdph-nursing-home-county-totalscsv)

### Prisons and jails

- [cdcr-prison-totals.csv](#cdcr-prison-totalscsv)
- [cdcr-state-totals.csv](#cdcr-state-totalscsv)

### Schools

- [school-districts-reopening.csv](#school-districts-reopeningcsv)
- [charter-schools-reopening.csv](#charters-schools-reopeningcsv)

### Other

- [cdc-vaccination-state-totals.csv](#cdc-vaccination-state-totalscsv)
- [latimes-beach-closures-area-list.csv](#latimes-beach-closures-area-listcsv)
- [latimes-beach-closures-county-list.csv](#latimes-beach-closures-county-listcsv)
- [los-angeles-countywide-statistical-areas.json](#los-angeles-countywide-statistical-areasjson)
- [latimes-project-roomkey-totals.csv](#latimes-project-roomkey-totalscsv)
- [latimes-zipcode-polygons.geojson](#latimes-zipcode-polygonsgeojson)

## About the data

These files come from a continual Times survey of California's 58 county health agencies and three city agencies. Updated numbers are published throughout the day at [latimes.com/coronavirustracker](https://www.latimes.com/projects/california-coronavirus-cases-tracking-outbreak/). This repository will periodically update with an extract of that data.

The figures are typically ahead of the totals compiled by California's Department of Public Health. By polling local agencies, The Times database also gathers some information not provided by the state. The system has [won praise](https://twitter.com/palewire/status/1243329930877788160) from public health officials, who do not dispute its method of data collection.

The tallies here are mostly limited to residents of California, the standard method used to count patients by the state’s health authorities. Those totals do not include people from other states who are quarantined in California, such as the passengers and crew of the Grand Princess cruise ship that docked in Oakland.

## Reusing the data

The Los Angeles Times is making coronavirus infections data available for use by researchers and scientists to aid in the fight against COVID-19.

The company's Terms of Service apply. By using the data, you accept and agree to follow the [Terms of Services](https://www.latimes.com/terms-of-service).

It states that "you may use the content online only, and solely for your personal, non-commercial use, provided you do not remove any trademark, copyright or other notice from such Content," and that, "no other use is permitted without prior written permission of Los Angeles Times."

Reselling the data is forbidden. Any use of these data in published works requires attribution to the Los Angeles Times.

To inquire about reuse, please contact Data and Graphics Editor Ben Welsh at [ben.welsh@latimes.com](mailto:ben.welsh@latimes.com).

## Examples of reuse

- [UC San Francisco: "UCSF Health Atlas"](http://healthatlas.ucsf.edu/welcome)
- [UCLA: "COVID-19 Sandbox Maproom"](https://sandbox.idre.ucla.edu/covid19/?geo=la)
- [Capradio: "Track COVID-19 Cases In California By County"](https://www.capradio.org/articles/2020/03/31/track-covid-19-cases-in-california-by-county/)
- [Race Counts: "How race, class and place fuel a pandemic"](https://www.racecounts.org/covid/)
- [covid-19-datasette](https://covid-19.datasettes.com/covid)
- [KQED: "How Many Coronavirus Cases Are in California? See Latest Numbers by County"](https://www.kqed.org/news/11809760/how-many-california-coronavirus-cases-see-latest-numbers-by-county)
- [KQED: "Here Are the Trendlines for COVID-19 Deaths and Hospitalizations in Each Bay Area County"](https://www.kqed.org/science/1964968/charts-the-bay-area-is-opening-up-again-heres-tracking-data-for-each-county-to-see-how-its-going)
- [Geography Planet: Southern California COVID trend map](https://geographyplanet.org/map-gallery/southern-california-covid-19-trend-map/)
- [weylunlee.github.io/covidtrack](https://weylunlee.github.io/covidtrack/)

## Data dictionary

### [latimes-agency-totals.csv](./latimes-agency-totals.csv)

The total cases and deaths logged by local public health agencies each day. Each row contains the cumulative totals reported by a single agency as of that date.

Most counties have only one agency except for Alameda and Los Angeles counties, where some cities run independent health departments. In Alameda County, the city of Berkeley is managed independently. In Los Angeles County, Pasadena and Long Beach are managed independently. These cities' totals are broken out into separate rows. In order to calculate county-level totals, you must aggregate them together using the `county` field.

| field             | type    | description                                                                                                                                                                                                                         |
| :---------------- | :------ | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `agency`          | string  | The name of the county or city public health agency that provided the data. Guaranteed to be unique when combined with the `date` field.                                                                                            |
| `county`          | string  | The name of the county where the agency is based.                                                                                                                                                                                   |
| `fips`            | string  | The [FIPS code](https://en.wikipedia.org/wiki/Federal_Information_Processing_Standards) given to the `county` by the federal government. Can be used to merge with other data sources.                                              |
| `date`            | date    | The date when the data were retrieved in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format.                                                                                                                                 |
| `confirmed_cases` | integer | The cumulative number of confirmed coronavirus cases as of this `date`.                                                                                                                                                             |
| `deaths`          | integer | The cumulative number of deaths attributed to coronavirus as of this `date`.                                                                                                                                                        |
| `did_not_update`  | boolean | Indicates if the agency did not provide an update on this date. If this is `true` and the case and death totals are unchanged from the previous day, this means they were holdovers. Use this flag omit these records when desired. |

### [latimes-county-totals.csv](./latimes-county-totals.csv)

The county-level totals of cases and deaths logged by local public health agencies each day. This is a derived table. Each row contains the aggregation of all local agency reports in that county logged by Los Angeles Times reporters and editors in `latimes-agency-totals.csv`.

It comes with all of the same caveats as its source. It is included here as a convenience.

| field                 | type    | description                                                                                                                                                                            |
| --------------------- | ------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `county`              | string  | The name of the county where the agency is based.                                                                                                                                      |
| `fips`                | string  | The [FIPS code](https://en.wikipedia.org/wiki/Federal_Information_Processing_Standards) given to the `county` by the federal government. Can be used to merge with other data sources. |
| `date`                | date    | The date when the data were retrieved in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format.                                                                                    |
| `confirmed_cases`     | integer | The cumulative number of confirmed coronavirus case at that time.                                                                                                                      |
| `deaths`              | integer | The cumulative number of deaths at that time.                                                                                                                                          |
| `new_confirmed_cases` | integer | The net change in confirmed cases over the previous `date`.                                                                                                                            |
| `new_deaths`          | integer | The net change in deaths over the previous `date`.                                                                                                                                     |

### [latimes-state-totals.csv](./latimes-state-totals.csv)

The statewide total of cases and deaths logged by local public health agencies each day. This is a derived table. Each row contains the aggregation of all local agency reports logged by Los Angeles Times reporters and editors in `latimes-agency-totals.csv`.

It comes with all of the same caveats as its source. It is included here as a convenience.

| field                 | type    | description                                                                                         |
| --------------------- | ------- | --------------------------------------------------------------------------------------------------- |
| `date`                | date    | The date when the data were retrieved in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format. |
| `confirmed_cases`     | integer | The cumulative number of confirmed coronavirus case at that time.                                   |
| `deaths`              | integer | The cumulative number of deaths at that time.                                                       |
| `new_confirmed_cases` | integer | The net change in confirmed cases over the previous `date`.                                         |
| `new_deaths`          | integer | The net change in deaths over the previous `date`.                                                  |

### [latimes-place-totals.csv](./latimes-place-totals.csv)

Most counties break out the location of cases within their service area. The Times is gathering and consolidating these lists. Each row contains cumulative case totals reported in that area as of that date.

The following counties currently do not report cases by locality: Alpine, Colusa, Fresno, Glenn, Lassen, Mariposa, Modoc, San Benito, Tehama and Tuolumne.

Different counties provide different geography types. Some provide data by region, some by Census designation, some by ZIP Code. The locations provided by Los Angeles County correspond to the public health department's official "Countywide Statistical Areas". Locations can be mapped after being joined to the shapes in `latimes-places-polygons.geojson` using the `id` column.

Be aware that some counties have shifted the place names used over time.

In some circumstances the true total of cases is obscured. Los Angeles and Orange counties decline to provide the precise number of cases in areas with low populations and instead provide a potential range. The lowest number in the range is entered into the record in the `confirmed_cases` field and an accompanying `note` includes the set of possible values.

| field             | type    | description                                                                                                                                                                          |
| ----------------- | ------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `id`              | string  | The unique identifier of the city, neighborhood or other area.                                                                                                                       |
| `name`            | string  | The name of the city, neighborhood or other area.                                                                                                                                    |
| `date`            | date    | The date when the data were retrieved in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format.                                                                                  |
| `county`          | string  | The name of the county where the city is located.                                                                                                                                    |
| `fips`            | string  | The [FIPS code](https://en.wikipedia.org/wiki/Federal_Information_Processing_Standards) given to the county by the federal government. Can be used to merge with other data sources. |
| `confirmed_cases` | integer | The cumulative number of confirmed coronavirus case at that time.                                                                                                                    |
| `note`            | string  | In cases where the `confirmed_cases` are obscured, this explains the range of possible values.                                                                                       |
| `population`      | integer | The number of residents in the area. Not available for all places.                                                                                                                   |

### [latimes-place-polygons.geojson](./latimes-place-polygons.geojson)

A map of sub-county areas where cases are tracked.

Different counties provide different geography types. Some provide data by region, some by Census designation, some by ZIP Code. The locations provided by Los Angeles County correspond to the public health department's official "Countywide Statistical Areas". Locations can be analyzed after being joined to the case counts in the `latimes-places-totals.csv` using the `id` column.

This file is a combination of dozens of different data files collected by Times reporters. Some shapes from county officials who maintain their own maps, others were scraped from county dashboards. In some cases, Census maps are used.

In some cases, the precise area being tracked by local officials is unclear. What you will find here is the best effort of Times reporters to represent what's been released. If you see any errors, please contact [ben.welsh@latimes.com](mailto:ben.welsh@latimes.com).

| field             | type    | description                                                                                                                                                                          |
| ----------------- | ------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `id`              | string  | The unique identifier of the city, neighborhood or other area.                                                                                                                       |
| `name`            | string  | The name of the city, neighborhood or other area.                                                                                                                                    |
| `county`          | string  | The name of the county where the city is located.                                                                                                                                    |
| `fips`            | string  | The [FIPS code](https://en.wikipedia.org/wiki/Federal_Information_Processing_Standards) given to the county by the federal government. Can be used to merge with other data sources. |
| `centroid_x`      | float   | The longitude of the `place`.                                                                                                                                                        |
| `centroid_y`      | float   | The latitude of the `place`.                                                                                                                                                         |
| `population`      | integer | The number of residents in the area. Not available for all places.                                                                                                                   |

### [latimes-agency-websites.csv](./latimes-agency-websites.csv)

The 61 local-health agency websites that the Los Angeles Times consults to conduct its survey.

| field    | type   | description                                                                                                                                                                                    |
| -------- | ------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `county` | string | The name of the county where the city is located.                                                                                                                                              |
| `fips`   | string | The [FIPS code](https://en.wikipedia.org/wiki/Federal_Information_Processing_Standards) given to the county by the federal government. Can be used to merge with other data sources.           |
| `agency` | string | The name of the county or city public health agency.                                                                                                                                           |
| `url`    | string | The location of the agency's website on the World Wide Web.                                                                                                                                    |

### [cdph-age.csv](./cdph-age.csv)

Statewide demographic data tallying totals by age for both cases and deaths. Provided by the [California Department of Public Health](https://www.cdph.ca.gov/Programs/CID/DCDC/Pages/COVID-19/COVID-19-Cases-by-Age-Group.aspx).

| field                     | type    | description                                                                                         |
| ------------------------- | ------- | --------------------------------------------------------------------------------------------------- |
| `date`                    | date    | The date when the data were retrieved in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format. |
| `age`                     | string  | The age bracket being tallied                                                                       |
| `confirmed_cases_total`   | integer | The cumulative number of confirmed coronavirus case amoung this age bracket at that time.           |
| `confirmed_cases_percent` | float   | The case totals percentage of the total in this age bracket                                         |
| `deaths_total`            | integer | The cumulative number of deaths case amoung this age bracket at that time.                          |
| `deaths_percent`          | float   | The death totals percentage of the total in this age bracket.                                       |

### [cdph-hospital-patient-county-totals.csv](./cdph-hospital-patient-county-totals.csv)

California's Department of Public Health is releasing [county-level hospitalization totals](https://data.chhs.ca.gov/dataset/california-covid-19-hospital-data-and-case-statistics).

| field                    | type    | description                                                                                                                                                                          |
| ------------------------ | ------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `date`                   | date    | The date for which hospital data were reported in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format.                                                                         |
| `county`                 | string  | The name of the county.                                                                                                                                                              |
| `fips`                   | string  | The [FIPS code](https://en.wikipedia.org/wiki/Federal_Information_Processing_Standards) given to the county by the federal government. Can be used to merge with other data sources. |
| `positive_patients`      | integer | The current number confirmed coronavirus cases in hospitals on this `date`.                                                                                                          |
| `suspected_patients`     | integer | The current number suspected coronavirus cases in hospitals on this `date`.                                                                                                          |
| `icu_positive_patients`  | integer | The current number confirmed coronavirus cases in intensive-care units on this `date`.                                                                                               |
| `icu_suspected_patients` | integer | The current number suspected coronavirus cases in intensive-care units on this `date`.                                                                                               |
| `icu_available_beds`     | integer | The current number open and avilable intensive-care beds on this `date`.                                                                                                             |

### [cdph-hpi-zipcodes.csv](./cdph-hpi-zipcodes.csv)

California's Department of Public Health has assigned each California ZIP Code a community health score by combining a variety of economic and social indicators. It is known as the Healthy Places Index. The quartile that each ZIP Code falls within was released in response to a request by The Times.

| field                    | type    | description                                                                                                                                                                          |
| ------------------------ | ------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `id`                     | string  | The unique identifer of the ZIP Code.                                                                                                                                                |
| `hpi_quartile`           | integer | The ranked quartile that contains the ZIP Code’s Healthy Places Index score. One is the lowest. Four is the highest.                                                                  |
| `county`                 | string  | The name of the county.                                                                                                                                                              |
| `fips`                   | string  | The [FIPS code](https://en.wikipedia.org/wiki/Federal_Information_Processing_Standards) given to the county by the federal government. Can be used to merge with other data sources. |
| `city`                   | string  | The city the ZIP Code falls within                                                                                                                                                   |

### [cdph-state-totals.csv](./cdph-state-totals.csv)

Totals published by the California Department of Public Health in [its daily press releases](https://www.cdph.ca.gov/Programs/OPA/Pages/New-Release-2020.aspx). Each row contains all numbers included in that day's release.

This file includes cases and deaths, the age of victims, transmission types, tests and hospitalizations. The state has stopped supplying some fields and began supplying some others over time. Deprecated fields have been maintained in this file and are noted below.

Due to bureaucratic lags, the state's totals for cases and deaths arrive slower than The Times numbers, which are generated by surveying local agencies. The state's methods for collecting testing data have struggled with [errors](https://www.latimes.com/california/story/2020-04-04/gavin-newsom-california-coronavirus-testing-task-force) and [delays](https://www.latimes.com/business/story/2020-03-30/its-taking-up-to-eight-days-to-get-coronavirus-tests-results-heres-why).

Some dates are missing because the state did not publish a press release for that day.

| field                          | type    | description                                                                                                                                                                                                  |
| :----------------------------- | :------ | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `date`                         | date    | The date when the data were retrieved in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format.                                                                                                          |
| `confirmed_cases`              | integer | The cumulative number of confirmed coronavirus case at that time.                                                                                                                                            |
| `deaths`                       | integer | The cumulative number of deaths at that time.                                                                                                                                                                |
| `travel`                       | integer | The number of cases acquired while traveling. The state stopped publishing it on March 24.                                                                                                                   |
| `person_to_person`             | integer | The number of cases acquired from close contacts and family members. The state stopped publishing it on March 24.                                                                                            |
| `community_spread`             | integer | The number of cases acquired from community spread. The state stopped publishing it on March 29.                                                                                                             |
| `under_investigation`          | integer | The number of cases acquired from an unknown source. The state stopped publishing it on March 24.                                                                                                            |
| `other_causes`                 | integer | The number of cases acquired from other sources. On March 24 the state began combining this figure with travel, person-to-person and under investigation cases. On March 29 the state stopped publishing it. |
| `self_monitoring`              | integer | The number of people in a form of isolation monitored by the state. The state stopped publishing it on March 19.                                                                                             |
| `age_0_to_17`                  | integer | The number of confirmed cases involving a person between 0 and 18 years old.                                                                                                                                 |
| `age_18_to_49`                 | integer | The number of confirmed cases involving a person between 18 and 49 years old.                                                                                                                                |
| `age_50_to_64`                 | integer | The number of confirmed cases involving a person between 50 and 64 years old.                                                                                                                                |
| `age_65_and_up`                | integer | The number of confirmed cases involving a person 65 of older.                                                                                                                                                |
| `age_18_to_64`                 | integer | The number of confirmed cases involving a person between 18 and 64 years old. The state stopped publishing it on March 23.                                                                                   |
| `age_unknown`                  | integer | The number of confirmed cases involving a person of unknown age.                                                                                                                                             |
| `gender_male`                  | integer | The number of confirmed cases involving a male.                                                                                                                                                              |
| `gender_female`                | integer | The number of confirmed cases involving a female.                                                                                                                                                            |
| `gender_unknown`               | integer | The number of confirmed cases involving a a person of unknown gender.                                                                                                                                        |
| `total_tests`                  | integer | The total number of tests conducted.                                                                                                                                                                         |
| `received_tests`               | integer | The number of tests results received. The state stopped publishing this field in April 24.                                                                                                                   |
| `pending_tests`                | integer | The number of tests resuts that are still pending. The state stopped publishing this field in April 24.                                                                                                      |
| `confirmed_hospitalizations`   | integer | The total number of hospitalizations with a confirmed case of COVID-19.                                                                                                                                      |
| `confirmed_icu`                | integer | The number of ICU hospitalizations with a confirmed case of COVID-19.                                                                                                                                        |
| `suspected_hospitalizations`   | integer | The total number of hospitalizations with a suspected case of COVID-19.                                                                                                                                      |
| `suspected_icu`                | integer | The number of ICU hospitalizations with a suspected case of COVID-19.                                                                                                                                        |
| `healthcare_worker_infections` | integer | The total number of healthcare workers who have tested positive for COVID-19.                                                                                                                                |
| `healthcare_worker_deaths`     | integer | The total number of healthcare workers who have died from COVID-19.                                                                                                                                          |
| `vaccine_doses_administered`   | integer | The total number of vaccine doses given out.                                                                                                                                                                 |
| `vaccine_doses_distributed`    | integer | The total number of vaccine doses available in the state.                                                                                                                                                    |
| `source_url`                   | string  | The URL to the state press release.                                                                                                                                                                          |

### [cdph-population-race-ethnicity.csv](./cdph-population-race-ethnicity.csv)

The breakdown of the population by race and ethnicity statewide and in each of the 58 counties, as provided by the California Department of Public Health.

| field                    | type    | description                                                                                                                                                                          |
| ------------------------ | ------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `county`                 | string  | The name of the county. The state of California also included as a row.                                                                                                              |
| `fips`                   | string  | The [FIPS code](https://en.wikipedia.org/wiki/Federal_Information_Processing_Standards) given to the county by the federal government. Can be used to merge with other data sources. |
| `aian`                   | float   | The percentage of people in the area who are American Indian or Alaska Native                                                                                                        |
| `asian`                  | float   | The percentage of people in the area who are Asian                                                                                                                                   |
| `black`                  | float   | The percentage of people in the area who are Black                                                                                                                                   |
| `latino`                 | float   | The percentage of people in the area who are Latino                                                                                                                                  |
| `multirace`              | float   | The percentage of people in the area who are multirace                                                                                                                               |
| `nhpi`                   | float   | The percentage of people in the area who are Native Hawaiian or Pacific Islander                                                                                                     |
| `other`                  | float   | The percentage of people in the area who are of another race                                                                                                                         |
| `unknown`                | float   | The percentage of people in the area who are of unknown race                                                                                                                         |
| `white`                  | float   | The percentage of people in the area who are white                                                                                                                                   |

### [cdph-positive-test-rate.csv](./cdph-positive-test-rate.csv)

All of the data used by The Times to estimate how many recent tests have come back positive. The daily tallies of new cases and tests are drawn from [cdph-state-totals.csv](./cdph-state-totals.csv).

| field                                  | type    | description                                                                                                                                            |
| -------------------------------------- | ------- | ------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `date`                                 | date    | The date when the data were retrieved in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format.                                                    |
| `confirmed_cases`                      | integer | The cumulative number of confirmed coronavirus case at that time.                                                                                      |
| `total_tests`                          | integer | The total number of tests conducted.                                                                                                                   |
| `new_confirmed_cases`                  | integer | The number of new confirmed cases compared to the previous date.                                                                                       |
| `new_tests`                            | integer | The number of new tests compared to the previous date.                                                                                                 |
| `new_confirmed_cases_seven_day_total`  | integer | The total number of new confirmed cases in the previous seven days.                                                                                    |
| `new_tests_seven_day_total`            | integer | The total number of new tests in the previous seven days.                                                                                              |
| `positive_test_rate_seven_day_percent` | float   | The positive test rate over the past seven days, calculated by dividing the number of new confirmed cases over that time into the number of new tests. |

### [cdph-race-ethnicity.csv](./cdph-race-ethnicity.csv)

Statewide demographic data tallying race totals by age for both cases and deaths. Provided by the [California Department of Public Health](https://www.cdph.ca.gov/Programs/CID/DCDC/Pages/COVID-19/Race-Ethnicity.aspx).

The original race categories published by the state have been grouped and aggregated to match the five race categories traditionally published by the Los Angeles Times.

| field                     | type    | description                                                                                         |
| ------------------------- | ------- | --------------------------------------------------------------------------------------------------- |
| `date`                    | date    | The date when the data were retrieved in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format. |
| `race`                    | string  | The race being tallied.                                                                             |
| `age`                     | string  | The age bracket being tallied                                                                       |
| `confirmed_cases_total`   | integer | The cumulative number of confirmed coronavirus case amoung this race and age at that time.          |
| `confirmed_cases_percent` | float   | The case totals percentage of the total in this age bracket                                         |
| `deaths_total`            | integer | The cumulative number of deaths case amoung this race and age at that time.                         |
| `deaths_percent`          | float   | The death totals percentage of the total in this age bracket.                                       |
| `population_percent`      | float   | The race's percentage of the overall state population in this age bracket.                          |

### [cdph-regional-stay-home-metrics.csv](./cdph-regional-stay-home-metrics.csv)

In December 2020, the state [introduced a new system](https://covid19.ca.gov/stay-home-except-for-essential-needs/) for issuing stay home orders. The state's 58 counties were grouped into six regions and judged based on the percentage of available ICU beds. When the percentage available beds dropped below 15%, a stay home order restricting businesses and movement would be issued. 

This file records the metrics released for each region by day.

| field                  | type    | description                                                                                                                                     |
| ---------------------- | ------- | ----------------------------------------------------------------------------------------------------------------------------------------------- |
| `date`                 | date    | The date when the data were collected in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format.                                             |
| `region`               | string  | The name of the region.                                                                                                                         |
| `icu_capacity_percent` | float   | The percentage of ICU beds in the region that were available on that `date`                                                                     |
| `stay_home_order`      | string  | An indicator of whether or not a stay home order was in effect for the region on that `date`. The range of values is `pending`, `yes` and `no`. |

### [cdph-reopening-metrics.csv](./cdph-reopening-metrics.csv)

In August 2020, the state introduced a new framework for deciding when and how counties can reopen. Under the regime, each county is assigned to one of four tiers based on a set of metrics developed by state officials.

This file records the metrics released for each county by day. Definition of the benchmarks can be found on the [state's website](https://www.cdph.ca.gov/Programs/CID/DCDC/Pages/COVID-19/COVID19CountyMonitoringOverview.aspx).

| field                 | type    | description                                                                                                                                                                          |
| --------------------- | ------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `date`                | date    | The date when the data were collected in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format.                                                                                  |
| `county`              | string  | The name of the county.                                                                                                                                                              |
| `fips`                | string  | The [FIPS code](https://en.wikipedia.org/wiki/Federal_Information_Processing_Standards) given to the county by the federal government. Can be used to merge with other data sources. |
| `percapita_case_rate` | float   | The number of new cases in a recent seven-day period — excluding cases at prisons and jails — adjusted for population and multiplied by 100,000.                                     |
| `adjusted_case_rate`  | float   | The `percapita_case_rate` adjusted to account for the volume of testing in the area. Not done for all counties.                                                                      |
| `positivity_rate`     | float   | The percentage of tests for the virus that come back positive in a recent seven-day period.                                                                                          |
| `equity_metric`       | float   | An index measuring disparities in disadvantaged neighborhoods compared to the county overall. Many small counties are exempted. Added Oct. 6, 2020                                   |

### [cdph-reopening-tiers.csv](./cdph-reopening-tiers.csv)

In August 2020, the state introduced a new framework for deciding when and how counties can reopen. Under the regime, each county is assigned to one of four tiers based on a set of metrics developed by state officials.

This file records the current tier of each county by day. The definition for each group can be found on the [state's website](https://web.archive.org/web/20200829140027/https://covid19.ca.gov/safer-economy/).

| field    | type    | description                                                                                                                                                                          |
| -------- | ------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `date`   | date    | The date when the data were collected in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format.                                                                                  |
| `county` | string  | The name of the county.                                                                                                                                                              |
| `fips`   | string  | The [FIPS code](https://en.wikipedia.org/wiki/Federal_Information_Processing_Standards) given to the county by the federal government. Can be used to merge with other data sources. |
| `tier`   | integer | The tier the county was classified in on this `date`. There are four possible values on an ordinal scale with one being the most restrictive and four the least restrictive.         |

### [cdph-vaccination-county-totals.csv](./cdph-vaccination-county-totals.csv)

California's Department of Public Health releases [county-level vaccination totals](https://public.tableau.com/profile/ca.open.data#!/vizhome/COVID-19VaccineDashboardPublic/Vaccine) via a Tableau dashboard. Our team extracts and logs the data each day.

| field                         | type    | description                                                                                                                                                                          |
| ----------------------------- | ------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `date`                        | date    | The date for which data were reported in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format.                                                                                  |
| `county`                      | string  | The name of the county.                                                                                                                                                              |
| `fips`                        | string  | The [FIPS code](https://en.wikipedia.org/wiki/Federal_Information_Processing_Standards) given to the county by the federal government. Can be used to merge with other data sources. |
| `population`                  | integer | The number of people who live in the county.                                                                                                                                         |
| `doses_administered`          | integer | The total number of doses given as of this `date`.                                                                                                                                   |
| `new_doses_administered`      | integer | The number of new doses compared to the previous `date`.                                                                                                                             |
| `pfizer_doses`                | integer | The total number of Pfizer doses given as of this `date`.                                                                                                                            |
| `new_pfizer_doses`            | integer | The number of new Pfizer doses compared to the previous `date`.                                                                                                                      |
| `moderna_doses`               | integer | The total number of Moderna doses given as of this `date`.                                                                                                                           |
| `new_moderna_doses`           | integer | The number of new Moderna doses compared to the previous `date`.                                                                                                                     |
| `jj_doses`                    | integer | The total number of Johnson & Johnson doses given as of this `date`.                                                                                                                 |
| `new_jj_doses`                | integer | The number of new Johnson & Johnson doses compared to the previous `date`.                                                                                                           |
| `partially_vaccinated`        | integer | The total number of partially vaccinated people as of this `date`.                                                                                                                   |
| `new_partially_vaccinated`    | integer | The number of new partially vaccinated people compared to the previous `date`.                                                                                                       |
| `at_least_one_dose`           | integer | The total number of people who have received at least one dose any vaccine given as of this `date`.                                                                                  |
| `new_at_least_one_dose`       | integer | The number of new people who have received at least one dose any vaccine compared to the previous `date`.                                                                            |
| `fully_vaccinated`            | integer | The total number of fully vaccinated people as of this `date`.                                                                                                                       |
| `new_fully_vaccinated`        | integer | The number of new fully vaccinated people compared to the previous `date`.                                                                                                           |
| `partially_vaccinated_percent`| float   | The percentage of people who were partially vaccinated as of this `date`.                                                                                                            |
| `at_least_one_dose_percent`   | float   | The percentage of people who received at least one dose any vaccine as of this `date`.                                                                                               |
| `fully_vaccinated_percent`    | float   | The percentage of people who were fully vaccinated as of this `date`.                                                                                                                |

### [cdph-vaccination-state-totals.csv](./cdph-vaccination-state-totals.csv)

California's Department of Public Health is releasing [state-level vaccination totals](https://public.tableau.com/profile/ca.open.data#!/vizhome/COVID-19VaccineDashboardPublic/Vaccine). Our team extracts and logs the data each day.

| field                        | type    | description                                                                                                                                                                          |
| ---------------------------- | ------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `date`                       | date    | The date for which data were reported in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format.                                                                                  |
| `doses_administered`          | integer | The total number of doses given as of this `date`.                                                                                                                                   |
| `new_doses_administered`      | integer | The number of new doses compared to the previous `date`.                                                                                                                             |
| `pfizer_doses`                | integer | The total number of Pfizer doses given as of this `date`.                                                                                                                            |
| `new_pfizer_doses`            | integer | The number of new Pfizer doses compared to the previous `date`.                                                                                                                      |
| `moderna_doses`               | integer | The total number of Moderna doses given as of this `date`.                                                                                                                           |
| `new_moderna_doses`           | integer | The number of new Moderna doses compared to the previous `date`.                                                                                                                     |
| `jj_doses`                    | integer | The total number of Johnson & Johnson doses given as of this `date`.                                                                                                                 |
| `new_jj_doses`                | integer | The number of new Johnson & Johnson doses compared to the previous `date`.                                                                                                           |
| `partially_vaccinated`        | integer | The total number of partially vaccinated people as of this `date`.                                                                                                                   |
| `new_partially_vaccinated`    | integer | The number of new partially vaccinated people compared to the previous `date`.                                                                                                       |
| `at_least_one_dose`           | integer | The total number of people who have received at least one dose any vaccine given as of this `date`.                                                                                  |
| `new_at_least_one_dose`       | integer | The number of new people who have received at least one dose any vaccine compared to the previous `date`.                                                                            |
| `fully_vaccinated`            | integer | The total number of fully vaccinated people as of this `date`.                                                                                                                       |
| `new_fully_vaccinated`        | integer | The number of new fully vaccinated people compared to the previous `date`.                                                                                                           |
| `partially_vaccinated_percent`| float   | The percentage of people who were partially vaccinated as of this `date`.                                                                                                            |
| `at_least_one_dose_percent`   | float   | The percentage of people who received at least one dose any vaccine as of this `date`.                                                                                               |
| `fully_vaccinated_percent`    | float   | The percentage of people who were fully vaccinated as of this `date`.                                                                                                                |

### [cdph-vaccination-zipcode-totals.csv](./cdph-vaccination-zipcode-totals.csv)

California's Department of Public Health is releasing zipcode-level vaccination totals. Our team extracts and logs the data each day. Population estimates from the U.S. Census Bureau, gathered by The Times, are used to calculate the percentage of the total population that is vaccinated.

| field                         | type    | description                                                                                                                                                                          |
| ----------------------------- | ------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `date`                        | date    | The date for which data were reported in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format.                                                                                  |
| `id`                        | string    | The unique identifer of the ZIP Code.                                                                                                                                                  |
| `county`                      | string  | The name of the county.                                                                                                                                                              |
| `fips`                        | string  | The [FIPS code](https://en.wikipedia.org/wiki/Federal_Information_Processing_Standards) given to the county by the federal government. Can be used to merge with other data sources. |
| `population`                  | integer | The number of people who live in the county.                                                                                                                                         |
| `partially_vaccinated`        | integer | The total number of partially vaccinated people as of this `date`.                                                                                                                   |
| `at_least_one_dose`           | integer | The total number of people who have received at least one dose any vaccine given as of this `date`.                                                                                  |
| `fully_vaccinated`            | integer | The total number of fully vaccinated people as of this `date`.                                                                                                                       |
| `partially_vaccinated_percent`| float   | The percentage of people who were partially vaccinated as of this `date`.                                                                                                            |
| `at_least_one_dose_percent`   | float   | The percentage of people who received at least one dose any vaccine as of this `date`.                                                                                               |
| `fully_vaccinated_percent`    | float   | The percentage of people who were fully vaccinated as of this `date`.                                                                                                                |

### [cdph-adult-and-senior-care-facilities.csv](./cdph-adult-and-senior-care-facilities.csv)

California's Department of Public Health is [listing the residential care facilities for the elderly and adult residential facilities](https://www.cdss.ca.gov/#covid19) across the state with COVID-19 outbreaks.

These are also sometimes known as assisted-living facilities. In some circumstances the true total of cases is obscured. The lowest number in the range is entered into the record in the staff or patients field and an accompanying `note` field includes the set of possible values.

| field                           | type    | description                                                                                                                                                                          |
| ------------------------------- | ------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `date`                          | date    | The date when the data were retrieved in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format.                                                                                  |
| `name`                          | string  | The name of the nursing home.                                                                                                                                                        |
| `county`                        | string  | The name of the county where the city is located.                                                                                                                                    |
| `fips`                          | string  | The [FIPS code](https://en.wikipedia.org/wiki/Federal_Information_Processing_Standards) given to the county by the federal government. Can be used to merge with other data sources. |
| `staff_confirmed_cases`         | integer | The cumulative number of confirmed coronavirus case amoung staff at that time.                                                                                                       |
| `patients_confirmed_cases`      | integer | The cumulative number of confirmed coronavirus case amoung patients at that time.                                                                                                    |
| `staff_confirmed_cases_note`    | string  | In cases where the `staff_confirmed_cases` are obscured, this explains the range of possible values.                                                                                 |
| `patients_confirmed_cases_note` | string  | In cases where the `patients_confirmed_cases` are obscured, this explains the range of possible values.                                                                              |
| `staff_deaths`                  | integer | The cumulative number of deaths amoung staff at that time.                                                                                                                      |
| `patients_deaths`               | integer | The cumulative number of deaths amoung patients at that time.                                                                                                                   |
| `staff_deaths_note`             | string  | In cases where the `staff_deaths` are obscured, this explains the range of possible values.                                                                                          |
| `patients_deaths_note`          | string  | In cases where the `patients_deaths` are obscured, this explains the range of possible values.                                                                                       |

### [cdph-adult-and-senior-care-totals.csv](./cdph-adult-and-senior-care-totals.csv)

California's Department of Social Services is releasing totals tracking the cumulative number of cases and deaths at the state's residential care facilities for the elderly and adult residential facilities. The source documents are available in the [pdf/adult-and-senior-care/](pdf/adult-and-senior-care/) directory of this repository.

These are also sometimes known as assisted-living facilities. Counts for staff and patients are combined in this dataset into a single total.

| field             | type    | description                                                                                         |
| ----------------- | ------- | --------------------------------------------------------------------------------------------------- |
| `date`            | date    | The date when the data were retrieved in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format. |
| `confirmed_cases` | integer | The cumulative number of confirmed coronavirus case amoung staff and patients at that time.         |
| `deaths`          | integer | The cumulative number of deaths case amoung staff and patients at that time.                        |
| `active_cases`    | integer | The number of active coronavirus case at that time.                                                 |
| `source_url`      | string  | The URL to the state data release.                                                                  |

### [cdph-skilled-nursing-facilities.csv](./cdph-skilled-nursing-facilities.csv)

California's Department of Social Services is [listing the skilled-nursing facilities](https://www.cdph.ca.gov/Programs/CID/DCDC/Pages/COVID-19/SNFsCOVID_19.aspx) across the state with COVID-19 outbreaks. The source documents are available in the [pdf/adult-and-senior-care/](pdf/adult-and-senior-care/) directory of this repository.

In some circumstances the true total of cases is obscured. The lowest number in the range is entered into the record in the staff or patients field and an accompanying `note` field includes the set of possible values.

| field                           | type    | description                                                                                                                                                                          |
| ------------------------------- | ------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `date`                          | date    | The date when the data were retrieved in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format.                                                                                  |
| `id`                            | string  | The facility's unique identifier with the state.                                                                                                                                     |
| `name`                          | string  | The name of the skilled-nursing facility.                                                                                                                                            |
| `county`                        | string  | The name of the county where the city is located.                                                                                                                                    |
| `fips`                          | string  | The [FIPS code](https://en.wikipedia.org/wiki/Federal_Information_Processing_Standards) given to the county by the federal government. Can be used to merge with other data sources. |
| `staff_confirmed_cases`         | integer | The current number of confirmed coronavirus case amoung staff at that time.                                                                                                          |
| `patients_confirmed_cases`      | integer | The current number of confirmed coronavirus case amoung patients at that time.                                                                                                       |
| `staff_confirmed_cases_note`    | string  | In cases where the `staff_confirmed_cases` are obscured, this explains the range of possible values.                                                                                 |
| `patients_confirmed_cases_note` | string  | In cases where the `patients_confirmed_cases` are obscured, this explains the range of possible values.                                                                              |
| `staff_deaths`                  | integer | The cumulative number of deaths case amoung staff at that time.                                                                                                                      |
| `patients_deaths`               | integer | The cumulative number of deaths case amoung patients at that time.                                                                                                                   |
| `staff_deaths_note`             | string  | In cases where the `staff_deaths` are obscured, this explains the range of possible values.                                                                                          |
| `patients_deaths_note`          | string  | In cases where the `patients_deaths` are obscured, this explains the range of possible values.                                                                                       |

### [cdph-skilled-nursing-totals.csv](./cdph-skilled-nursing-totals.csv)

California's Department of Public Health is releasing totals tracking the cumulative number of cases and deaths at the state's skilled nursing facilities.

In some circumstances the true total of cases is obscured. The lowest number in the range is entered into the record in the staff or patients field and an accompanying `note` field includes the set of possible values.

| field                           | type    | description                                                                                             |
| ------------------------------- | ------- | ------------------------------------------------------------------------------------------------------- |
| `date`                          | date    | The date when the data were retrieved in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format.     |
| `staff_active_cases`            | integer | The number of active coronavirus case among staff at that time.                                         |
| `patients_active_cases`         | integer | The number of active coronavirus case amoung patients at that time.                                     |
| `staff_confirmed_cases`         | integer | The cumulative number of confirmed coronavirus case among staff at that time.                           |
| `patients_confirmed_cases`      | integer | The cumulative number of confirmed coronavirus case among patients at that time.                        |
| `staff_deaths`                  | integer | The cumulative number of deaths case among staff at that time.                                          |
| `patients_deaths`               | integer | The cumulative number of deaths case among patients at that time.                                       |
| `staff_deaths_note`             | string  | In cases where the `staff_deaths` are obscured, this explains the range of possible values.             |
| `source_url`                    | string  | The URL to the state data release.                                                                      |

### [cdph-nursing-home-county-totals.csv](./cdph-nursing-home-county-totals.csv)

The total number of cases and deaths in skilled-nursing facilities, residential care facilities for the elderly and adult residential facilities aggregated by county.

These numbers are calculated by The Times using the facilities lists above. The state chooses not to provide precise numbers at facilities with fewer than 10 cases. When totaling by county, The Times substitutes the minimum value of one. The result is that the tallies are likely an undercount and should be considered the minimum possible value.

| field                                   | type    | description                                                                                                                                                                          |
| --------------------------------------- | ------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `date`                                  | date    | The date when the data were retrieved in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format.                                                                                  |
| `county`                                | string  | The name of the county where the city is located.                                                                                                                                    |
| `fips`                                  | string  | The [FIPS code](https://en.wikipedia.org/wiki/Federal_Information_Processing_Standards) given to the county by the federal government. Can be used to merge with other data sources. |
| `minimum_staff_confirmed_cases`         | integer | The minimum number of cumulative confirmed coronavirus case amoung staff at that time.                                                                                               |
| `minimum_patients_confirmed_cases`      | integer | The minimum number of cumulative confirmed coronavirus case amoung patients at that time.                                                                                            |
| `minimum_staff_deaths`                  | integer | The minimum number of cumulative deaths amoung staff at that time.                                                                                                                   |
| `minimum_patients_deaths`               | integer | The minimum number of cumulative deaths amoung patients at that time.                                                                                                                |

### [cdcr-prison-totals.csv](./cdcr-prison-totals.csv)

The cases, resolutions and deaths among inmates at the individual prison facilities operated by the California Department of Corrections and Rehabilitation.

The data is currently limited to July 22, 2020, forward.

| field                 | type    | description                                                                                                                                                                          |
| --------------------- | ------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `date`                | date    | The date when the data were collected in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format.                                                                                  |
| `code`                | string  | The unique identifier of the prison institution.                                                                                                                                     |
| `name`                | string  | The name of the prison institution.                                                                                                                                                  |
| `city`                | string  | The city where the prison institution is located.                                                                                                                                    |
| `county`              | string  | The county where the prison institution is located.                                                                                                                                  |
| `fips`                | string  | The [FIPS code](https://en.wikipedia.org/wiki/Federal_Information_Processing_Standards) given to the county by the federal government. Can be used to merge with other data sources. |
| `zipcode`             | string  | The [ZIP Code](https://en.wikipedia.org/wiki/ZIP_Code) where the agency is located.                                                                  |
| `x`                   | float   | The longitude of the area's centroid.                                                                                                                                                |
| `y`                   | float   | The latitude of the area's centroid.                                                                                                                                                 |
| `confirmed_cases`     | integer | The cumulative number of confirmed coronavirus case at that time.                                                                                                                    |
| `new_confirmed_cases` | integer | The net change in confirmed cases over the previous `date`.                                                                                                                          |
| `active_cases`        | integer | The number of active coronavirus case at that time.                                                                                                                                  |
| `released_cases`      | integer | The cumulative number of coronavirus cases released from the prison at that time.                                                                                                        |
| `resolved_cases`      | integer | The cumulative of coronavirus case where the patient ultimately recovered or had their cases otherwise resolved at that time.                                                            |
| `deaths`              | integer | The cumulative number of deaths at that time.                                                                                                                                        |
| `new_deaths`          | integer | The net change in deaths over the previous `date`.                                                                                                                                   |

### [cdcr-state-totals.csv](./cdcr-state-totals.csv)

The total number of cases amoung inmates at prisons run by the California Department of Corrections and Rehabiliation.

| field                 | type    | description                                                                                         |
| --------------------- | ------- | --------------------------------------------------------------------------------------------------- |
| `date`                | date    | The date when the data were collected in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format. |
| `confirmed_cases`     | integer | The cumulative number of confirmed coronavirus case at that time.                                   |
| `new_confirmed_cases` | integer | The net change in confirmed cases over the previous `date`.                                         |
| `active_cases`        | integer | The number of active coronavirus case at that time.                                                 |


### [school-districts-reopening.csv](./school-distircts-reopening.csv)

Number of students with an option to return to school districts calculated from combination of data from California Safe Schools For All and California Department of Education. 

| field                       | type    | description                                                                                            |
| ----------------------------| ------- | -------------------------------------------------------------------------------------------------------|
| `district`                  | string  | Name of public school district.                                                                        |
| `enr_total`                 | integer | Total students enrolled in the district.                                                               |
| `elem_enr`                  | integer | Total students enrolled in grades K-5. Subset of `enr_total`.                                          |
| `middle_enr`                | integer | Total students enrolled in grades 6-8. Subset of `enr_total`.                                          |
| `high_enr`                  | integer | Total students enrolled in grades 9-12. Subset of `enr_total`.                                         |
| `elem_in_school`            | integer | Students in grades K-5 that have the option to participate in an in-person or hybrid learning.         |
| `middle_in_school`          | integer | Students in grades 6-8 grades that have the option to participate in an in-person or hybrid learning.  |
| `high_in_school`            | integer | Students in grades 9-12 grades that have the option to participate in an in-person or hybrid learning. |
| `total_in_school `          | integer | Sum of `elem_in_school`,`middle_in_school` and `high_in_school`.                                       |
| `reopening_plan`            | string  | Link to district's reopening plan.                                                                     |
| `operational_status_elem`   | string  | Operational status as of `update_date` for the district's elementary schools.                          |
| `operational_status_middle` | string  | Operational status as of `update_date` for the district's middle schools.                              |
| `operational_status_high`   | string  | Operational status as of `update_date` for the district's high schools.                                |
| `elem_reopening_date`       | date    | Planned reopening date for the district's elementary schools as of `update date`.                      |
| `middle_reopening_date`     | date    | Planned reopening date for the district's middle schools as of `update date`.                          |
| `high_reopening_date`       | date    | Planned reopening date for the district's high schools as of `update date`.                            |
| `near_term_opening_date`    | date    | Earliest planned reopening date for the district as of `update date`.                                  |
| `update_date`               | date    | The date when the district submitted status report to the state.                                       |

### [charter-schools-reopening.csv](./charter-schools-reopening.csv)

Number of students with an option to return to individual charter schools calculated from combination of data from California Safe Schools For All and California Department of Education. 

| field                       | type    | description                                                                                            |
| ----------------------------| ------- | -------------------------------------------------------------------------------------------------------|
| `cdscode`                   | string  | A 14-digit code unique to the charter school. Assigned by California department of Education           |
| `district`                  | string  | Name of school district the charter schools is part of.                                                |
| `school`                    | string  | Name of the charter school.                                                                            |
| `enr_total`                 | integer | Total students enrolled                                                                                |
| `elem_enr`                  | integer | Total students enrolled in grades K-5. Subset of `enr_total`.                                          |
| `middle_enr`                | integer | Total students enrolled in grades 6-8. Subset of `enr_total`.                                          |
| `high_enr`                  | integer | Total students enrolled in grades 9-12. Subset of `enr_total`.                                         |
| `elem_in_school`            | integer | Students in grades K-5 that have the option to participate in an in-person or hybrid learning.         |
| `middle_in_school`          | integer | Students in grades 6-8 grades that have the option to participate in an in-person or hybrid learning.  |
| `high_in_school`            | integer | Students in grades 9-12 grades that have the option to participate in an in-person or hybrid learning. |
| `total_in_school `          | integer | Sum of `elem_in_school`,`middle_in_school` and `high_in_school`.                                       |
| `reopening_plan`            | string  | Link to school's reopening plan.                                                                       |
| `operational_status_elem`   | string  | Operational status as of `update_date`.                                                                |
| `operational_status_middle` | string  | Operational status as of `update_date`.                                                                |
| `operational_status_high`   | string  | Operational status as of `update_date`.                                                                |
| `elem_reopening_date`       | date    | Planned reopening date as of `update date`.                                                            |
| `middle_reopening_date`     | date    | Planned reopening date as of `update date`.                                                            |
| `high_reopening_date`       | date    | Planned reopening date as of `update date`.                                                            |
| `near_term_opening_date`    | date    | Earliest planned reopening date for the school as of `update date`.                                    |
| `update_date`               | date    | The date when the charter school submitted status report to the state.                                 |

### [cdc-vaccination-state-totals.csv](./cdc-vaccination-state-totals.csv)

State-level vaccination totals derived from the dashboard published by the U.S. Centers for Disease Control and Prevention.

| field                                   | type     | description                                                                                         |
| --------------------------------------- | -------- | --------------------------------------------------------------------------------------------------- |
| `date`                                  | date     | The date when the data were collected in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format. |
| `state`                                 | string   | The name of the state.                                                                              |
| `population`                            | integer  | The number of people who live in the state.                                                         |
| `doses_distributed`                     | integer  | The total number of doses sent to the state as of that `date`.                                       |
| `doses_administered`                    | integer  | The total number of shots given out in the state as of that `date`.                                  |
| `doses_administered_percent`            | float    | The percentage of distributed doses that have been administered as of that `date`.                  |
| `administered_dose1`                    | integer  | The number of first doses administered in the state of that `date`.                                 |
| `administered_dose1_percent`            | float    | The percentage of people in the state who have received at least one dose as of that `date`.        |
| `administered_dose2`                    | integer  | The number of second doses administered in the state of that `date`.                                |
| `administered_dose2_percent`            | float    | The percentage of people in the state who are fully vaccinated as of that `date`.                   |

### [latimes-beach-closures-area-list.csv](./latimes-beach-closures-area-list.csv)

The subcounty-level restrictions on beach access, compiled by the Los Angeles Times based on data released by the California Coastal Commission.

| field         | type    | description                                                                                                                                                                            |
| ------------- | ------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `county`      | string  | The name of the county where the agency is based.                                                                                                                                      |
| `fips`        | string  | The [FIPS code](https://en.wikipedia.org/wiki/Federal_Information_Processing_Standards) given to the `county` by the federal government. Can be used to merge with other data sources. |
| `area`        | string  | The name of the sub-county area being tracked.                                                                                                                                         |
| `state_park`  | boolean | An indicator if this area is a state park.                                                                                                                                             |
| `restriction` | string  | A description of the current level of restriction in this area.                                                                                                                        |

### [latimes-beach-closures-county-list.csv](./latimes-beach-closures-county-list.csv)

The county-level restrictions on beach access, compiled by the Los Angeles Times based on data released by the California Coastal Commission.

| field         | type   | description                                                                                                                                                                            |
| ------------- | ------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `county`      | string | The name of the county where the agency is based.                                                                                                                                      |
| `fips`        | string | The [FIPS code](https://en.wikipedia.org/wiki/Federal_Information_Processing_Standards) given to the `county` by the federal government. Can be used to merge with other data sources. |
| `status`      | string | A Times classification of the current level of restriction in this county                                                                                                              |
| `restriction` | string | A description of the current level of restriction in this county                                                                                                                       |

### [los-angeles-countywide-statistical-areas.json](./los-angeles-countywide-statistical-areas.json)

A GeoJSON file mapping out statistical tabulation areas created by the Los Angeles County Department of Public Health. Place-level data released by Los Angeles County correspond to these areas. Acquired via a California Public Records Act request.

| field        | type    | description                                                           |
| ------------ | ------- | --------------------------------------------------------------------- |
| `type`       | string  | The type of area being mapped. Options are `City` and`Unincorporated` |
| `city`       | string  | The name of the area's municipal parent, if it has one.               |
| `community`  | string  | The name of the area.                                                 |
| `label`      | boolean | A combination of the area's name and city. Creates a unique string.   |
| `centroid_x` | float   | The longitude of the area's centroid.                                 |
| `centroid_y` | float   | The latitude of the area's centroid.                                  |

### [latimes-project-roomkey-totals.csv](./latimes-project-roomkey-totals.csv)

Los Angeles County officials have launched an unprecedented effort to shield 15,000 homeless people from the coronavirus by moving them into hotel rooms. The Times is tracking the latest data from the Los Angeles County Emergency Operations Center and the Los Angeles County Department of Public Health.

| field                      | type    | description                                                                                             |
| -------------------------- | ------- | ------------------------------------------------------------------------------------------------------- |
| `date`                     | date    | The date on which data were reported in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format.      |
| `people_housed`            | integer | The current number of homeless people in Los Angeles County housed on this `date`.                      |
| `leased_rooms`             | integer | The current number hotel rooms leased on this `date`.                                                   |
| `rooms_ready_to_occupy`    | integer | The subset of leased rooms that were ready to occupy on this `date`.                                    |
| `rooms_occupied`           | integer | The subset of ready rooms that were occupied on this `date`.                                            |
| `homeless_confirmed_cases` | integer | The cumulative number of homeless people in Los Angeles County that had tested positive by this `date`. |

### [latimes-zipcode-polygons.geojson](./latimes-zipcode-polygons.geojson)

The ZIP Code Tabulation Areas (ZCTAs) used by The Times to map ZIP Code vaccination totals provided by the California Department of Public Health. The map file was acquired from the U.S. Census Bureau. It is limited to areas where vaccination data are available.

| field             | type    | description                                                                                                                                                                          |
| ----------------- | ------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `id`              | string  | The unique identifier of the city, neighborhood or other area.                                                                                                                       |
| `county`          | string  | The name of the county where the city is located.                                                                                                                                    |
| `fips`            | string  | The [FIPS code](https://en.wikipedia.org/wiki/Federal_Information_Processing_Standards) given to the county by the federal government. Can be used to merge with other data sources. |

## Getting started

The data published here can be easily imported to any data analysis tool, ranging from a simple spreadsheet to a more sophisticated analysis framework. This repository has be pre-configured to work with the [Python](https://www.python.org/) computer-programming language and a [Jupyter](https://jupyter.org/) computational notebook. You can install and run the code locally on your computer, or on the web with [Binder](https://mybinder.org/).

### Installing locally

[Make a fork](https://help.github.com/en/github/getting-started-with-github/fork-a-repo) of this repository, [clone it](https://help.github.com/en/github/creating-cloning-and-archiving-repositories/cloning-a-repository) to your computer, then move into the directory.

```
cd california-coronavirus-data
```

Install the Python tools you need with [pipenv](https://pipenv.pypa.io/en/latest/).

```
pipenv install
```

Start the Jupyter Lab programming environment.

```
pipenv run jupyter lab
```

Check out the example notebook at [notebooks/examples.ipynb](./notebooks/examples.ipynb).

### Running online with Binder

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/datadesk/california-coronavirus-data/master?urlpath=lab/tree/notebooks/examples.ipynb)

Click on the [Binder](https://mybinder.org/) badge above and this repository will boot up inside the site's system for running Jupyter notebooks over the web. After a few minutes you should have an Jupyter Lab environment up and running.

## How you can help

This survey is conducted by The Times' Data and Graphics Department. If you'd like to support its effort to keep California and the nation informed, the best thing you can do is [buy a digital subscription](https://www.latimes.com/subscriptions/) and encourage others to do the same. The coronavirus pandemic has had a significant effect on the country's economy and the news industry is no exception. Without support from readers like you projects like this would not be possible.

## Contact

To inquire about the data or about reuse, please contact Data and Graphics Editor [Ben Welsh](https://palewi.re/who-is-ben-welsh/) at [ben.welsh@latimes.com](mailto:ben.welsh@latimes.com)
