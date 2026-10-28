# Final project proposal: Is the habitat the Endangered Species Act protects warming, and do the listing rules say so?

**Team:** Joseph Wong and Jacob Backus (working as a pair)

## Question

In Module 3 we found that the Fish and Wildlife Service's listing rules never called climate change a threat before
2008, and that about two in three have since the 2008 polar bear rule. That is what the rules *say*. For the final project
we want to put the rules on a map and ask:

> How much has the critical habitat of species listed since 1994 warmed since the mid-20th century, and did the listing
> rules call climate change a threat for the species whose habitat warmed most?

This matters because critical habitat is the part of a species' range the law singles out for protection, its
boundaries are drawn when it is designated, and the listing rule is where the Service first names the threats that
recovery planning responds to. If the most-warmed habitat belongs to species whose rules never called climate change a threat,
that is where the gap Delach et al. (2019) describe matters most.

## Data

- Our Module 3 listing rules (342 rules, 1994–2026) with their climate labels and the species each rule listed, exported
  from our Module 3 repository into `data/`.
- Final critical habitat, U.S. Fish and Wildlife Service ArcGIS feature service:
  <https://services.arcgis.com/QVENGdaPbd4LUkLV/arcgis/rest/services/USFWS_Critical_Habitat/FeatureServer/0>
- NOAA nClimGrid monthly temperature (1/24°, lower 48, 1895 on), through the Planetary Computer STAC API:
  <https://planetarycomputer.microsoft.com/api/stac/v1/collections/noaa-nclimgrid-monthly>
- NOAA Climate at a Glance, lower-48 annual temperature, to check our numbers:
  <https://www.ncei.noaa.gov/access/monitoring/climate-at-a-glance/national/time-series/110/tavg/12/12/1895-2025/data.csv>
- Census cartographic boundary files (states and divisions):
  <https://www2.census.gov/geo/tiger/GENZ2025/shp/cb_2025_us_state_5m.zip>
- Delach et al. (2019) per-species data on OSF: <https://osf.io/download/76ytr/>

## Analysis tasks

1. **Critical habitat (vector).** Read the critical habitat polygons for the species in our corpus from the feature
   service, keep the ones in the lower 48 with a spatial join to the state boundaries, and give each species the Census
   division where most of its habitat lies (overlay and area in an equal-area projection).
2. **Warming (raster).** Find nClimGrid's monthly mean temperature through a STAC search, stream it into a 1951–1980
   mean and a mean for the most recent 30 years, take the difference, and average it over each species' critical
   habitat with zonal statistics. Check the lower-48 average against NOAA's Climate at a Glance.
3. **Listing rules against warming (text as data).** Join habitat warming to each species' listing rule and its climate
   label, and compare species listed before 2008 with those whose rules call climate change a threat or a possible
   threat. Re-check the labels against our Module 3 hand labels and the rule text, and compare with Delach et al.'s
   coding of later documents.

## Optional elements

Vector data (B), raster data (C), an interactive map (D) and a web page (G); the label checks and the comparisons with
NOAA and Delach et al. also cover text as data (E) and verification against an independent source (F).

## Presentation

A notebook, plus a web page in `web/` with the main figures and an interactive `leafmap` map of warming and critical
habitat.
