# HeliosPredict
HeliosPredict is a solar power prediction algorithm designed to forecast the power production of a solar plant using historical production data and weather conditions at the time of production.

This algorithm is based on data collected from a 3 kW home rooftop solar unit. The system has recorded production data for 882 days, but only 269 days of weather data were available for analysis.

During those 269 days, the 3 kW unit produced **3,240.36 kWh** of energy, while the cumulative UV index at its geographical location was **20253**. It is important to note that **1 unit of UV index does not equate to 1 kWh of raw energy**. Most of the sunlight received is either reflected back or converted into heat (energy loss). Even the best solar panels on the market rarely exceed 20% efficiency, and this figure is often optimistic for most consumer-grade panels.

The solar plant used to collect this data is an ON-GRID system, though this algorithm may be more relevant to users of OFF-GRID systems.

**Additional Information**
-The UV Index ranges from 0 to 10.

-Higher temperatures do not equate to higher power production. In fact, excessive heat can reduce the efficiency of solar panels.

-The region where the solar plant is located has a subtropical semi-arid climate.