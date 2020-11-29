install.packages("tidyverse")
library("tidyverse")
require("ggplot")
require("dplyr")

list.files(path = "../input")

#load data
fireData1 <- read.csv("../input/california-fire-perimeters/California_Fire_Perimeters.csv")

head(fireData1) 


