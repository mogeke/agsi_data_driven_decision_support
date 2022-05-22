library(tidyverse)
agsi_data <- read.csv("https://raw.githubusercontent.com/mogeke/agsi_data_driven_decision_support/main/agsi_2022_dropna.csv", sep=",")
agsi_data$country <- as.factor(agsi_data$country)
agsi_data$gasInStorage <- as.double(agsi_data$gasInStorage)
#agsi_data$gasDayStart <- as.Date(agsi_data$gasDayStart)


#filter stuff
#storage_country <- agsi_data %>%
 # filter(country == "AT") %>%
  #filter(gasDayStart == "2022-05-09")


#get last da
max(agsi_data$gasDayStart)