setwd("~/Documents/dataScience/HOPfinance/datasets/")

library(quantmod)
library(dplyr)

# ticker symbols from S&P 500
stockLabel <- read.csv("~/Documents/dataScience/HOPfinance/datasets/stocklabel.csv", stringsAsFactors = F) %>%
  filter(!stock %in% c("LMT", "NWL", "NBL"))

# set dates of interest
date.start  <- "2011-09-15"
date.end    <- "2016-09-15"

# pull data
data <- new.env()
getSymbols(stockLabel$stock, src = 'google', env = data, adjust = T)

# cut train data
list <- eapply(data, "[", paste(date.start, date.end, sep="/"))

p <- as.character(seq(as.Date("2011/9/15"), as.Date("2016/9/15"), by = 7))

# export

for (i in 1:length(list)){

  t <- list[[i]]
  t <- t %>% data.frame()
  t <- t[rownames(t) %in% p,]
  
  t <- rbind(t, c(NA, NA, NA, NA, NA))
  
  if (!is.null(t) & nrow(t) == 255){
    
      write.csv(t[1:254,], file = paste0("~/Documents/dataScience/HOPfinance/datasets/training/", 
                                 names(list)[i], ".csv"), na = '')
        
      print(paste0(i, " ", names(list[i]), " exported"))
  
  } else {
    
    print(paste0(i, " ", names(list[i]), " not exported"))
    
  }
  
}

# cut test data

test.date.start <- "2016-09-22"
test.date.end <- "2016-09-29"

testList <- eapply(data, "[", paste(test.date.start, test.date.end, sep="/"))

for (i in 1:length(testList)){
  
  t <- testList[[i]]
  t <- t %>% data.frame()
  t <- t[rownames(t) %in% c(test.date.start, test.date.end),]
  
  write.csv(t, file = paste0("~/Documents/dataScience/HOPfinance/datasets/validation/", 
                                       names(list)[i], ".csv"), na = '')
    
    print(paste0(i, " ", names(list[i]), " exported"))
  
}

# oil

oil <- read.csv("CHRIS-CME_CL1.csv", stringsAsFactors = F) %>% 
  select(Date, Open, High, Low, Last, Volume) %>%
  filter(Date %in% p) %>%
  mutate(Date = as.Date(Date)) %>%
  arrange(Date)

write.csv(oil, file = "training/_oil.csv", na = '', row.names = F)