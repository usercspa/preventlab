install.packages("tidyverse")
library(dplyr)
library(readr)
library(ggplot2)
library(ggthemes)
library(scales)
library(maps)
library(mapproj)

list.files(path = "../input")

#load data
fireData1 <- read.csv("../input/california-fire-perimeters/California_Fire_Perimeters.csv")

head(fireData1) 


