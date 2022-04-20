install.packages("tidyverse")
library(tidyverse)
install.packages("compare")
library(compare)
install.packages("dplyr")
library(dplyr)
install.packages("rapportools")
library(rapportools)
install.packages("stringr")
library(stringr)
install.packages("purrr")
library(purrr)

agora <- read_csv("Agora.csv")

agora_unique_users <- unique(agora[1], incomparables = FALSE)

#read.csv() read BMR.csv incorrectly at around the 80 thousandths entry
BMR <- read_csv("BMR.csv")

BMR_unique_users <- unique(BMR[2], incomparables = FALSE)

BMR_unique_users2 <- BMR[2] #difference in unqiue user amount probably due to seller vs customer status

agora_unique_users <- agora_unique_users %>%
  rename(username = Vendor)

Final_User_List <- intersect(agora_unique_users, BMR_unique_users)

#clean up some more to many dups
Hydra1 <- unique(HydraOldFormatUsers, incomparables = FALSE)

Hydra2 <- unique(HydraNewFormatUsers, incomparables = FALSE)

HydraClean <- rbind(Hydra1, Hydra2)

HydraClean <- unique(HydraClean, incomparables = FALSE)

#sort names together
HydraClean <- HydraClean[order(HydraClean$Username), ]

#remove the unescessary columns
HydraClean$...1 <- NULL
HydraClean$Rating <- NULL
#cleaning email data
HydraClean$Email <-gsub("'","",as.character(HydraClean$Email))
HydraClean$Email <-gsub("\\[","",as.character(HydraClean$Email))
HydraClean$Email <-gsub("\\]","",as.character(HydraClean$Email))

HydraClean2 = data.frame()

for(i in 1:length(HydraClean$Username)){
  
  temp <- data.frame("Username" = HydraClean$Username[i],"Email" = (c(strsplit(HydraClean$Email[i], ","[[1]]))), HydraClean$PGP[i])
  names(temp)[2] <- "Email"
  HydraClean2 <- rbind(HydraClean2,temp)
}

HydraClean2 <- unique(HydraClean2$Email)

HydraLength <- length(HydraClean$Username)

for(i in 1:length(HydraClean$Username)){

  print(i)
  if(is.null(HydraClean$Username[i+1])){

  }else{
    if(isTRUE(all.equal(HydraClean$Username[i], HydraClean$Username[i+1]))){

        #tempRating <- unique(c(as.numeric(HydraClean$Rating[i]), as.numeric(HydraClean$Rating[i+1])))

        #tempRating <- tempRating[!is.na(tempRating)]

        #tempRating <- min(tempRating)
          

        tempEmail <-unique(c(HydraClean$Email[i], HydraClean$Email[i+1]))

        tempEmail <- tempEmail[!is.na(tempEmail)]
        tempEmail <- tempEmail[!(tempEmail == "na")]
        
        if(is.empty(tempEmail)){
          tempEmail <- "na"
        }

        tempPGP = unique(c(HydraClean$PGP[i], HydraClean$PGP[i+1]))
        
        tempPGP <- tempPGP[!(tempPGP == "na")]
        tempPGP <- tempPGP[!is.na(tempPGP)]
        
        if(is.empty(tempPGP)){
          tempPGP <- "na"
        }
        
        #HydraClean$Rating[i+1] <- tempRating
        HydraClean$Email[i+1] <- tempEmail
        HydraClean$PGP[i+1] <- tempPGP

        HydraClean <- HydraClean[-i, ]

     }else{
       
     }
  }
}

PandoraUsers <- unique(PandoraUsers, incomparables = FALSE)

#sort names together
PandoraUsers <- PandoraUsers[order(PandoraUsers$Username), ]

#remove the unescessary columns
PandoraUsers$...1 <- NULL
PandoraUsers$Rating <- NULL
PandoraUsers$`Account Type` <- NULL

#Removing login screens data
PandoraUsers <- PandoraUsers[-1, ]
PandoraUsers <- PandoraUsers[-1, ]

for(i in 1:length(PandoraUsers$Username)){
    
    t <- str_split(PandoraUsers$Username[i], " ", n = 2)
    PandoraUsers$Username[i] <- t[[1]][1]
}
PandoraUsers <- unique(PandoraUsers, incomparables = FALSE)

HydraClean$Username <- tolower(HydraClean$Username)
HydraClean$Email <- tolower(HydraClean$Email)
PandoraUsers$Username <- tolower(PandoraUsers$Username)
PandoraUsers$Email <- tolower(PandoraUsers$Email)
BMR$username <- tolower(BMR$username)
BMR$gpg_email <- tolower(BMR$gpg_email)



################################## For sample Set Demo#######################

for(i in 1:nrow(PandoraUsers)){
  
    if(PandoraUsers$Email[i] == 'na'){
      PandoraUsers <- PandoraUsers[-i, ]
    }
  
  
}

#cleaning email data
PandoraUsers$Email <-gsub("'","",as.character(PandoraUsers$Email))
PandoraUsers$Email <-gsub("\\[","",as.character(PandoraUsers$Email))
PandoraUsers$Email <-gsub("\\]","",as.character(PandoraUsers$Email))

for(i in 1:nrow(HydraClean)){
  
  if(HydraClean$Email[i] == 'na'){
    HydraClean <- HydraClean[-i, ]
  }
  
  
}

#Looking at indexes for later classification model.

UsernameMatchesBMRHydraIndex <- discard(match(BMR$username, HydraClean$Username), is.na)
EmailMatchesBMRHydraIndex <- discard(match(BMR$gpg_email, HydraClean$Email), is.na)
PGPMatchesBMRHydraIndex <- discard(match(BMR$gpg, HydraClean$PGP), is.na)

UsernameMatchesHydraBMRIndex <- discard(match(BMR$username, HydraClean$Username), is.na)
EmailMatchesHydraBMRIndex <- discard(match(BMR$gpg_email, HydraClean$Email), is.na)
PGPMatchesHydraBMRIndex <- discard(match(BMR$gpg, HydraClean$PGP), is.na)

UsernameMatchesBMRPandoraIndex <- discard(match(BMR$username, PandoraUsers$Username), is.na)
EmailMatchesBMRPandoraIndex <- discard(match(BMR$gpg_email, PandoraUsers$Email), is.na)
PGPMatchesBMRPandoraIndex <- discard(match(BMR$gpg, PandoraUsers$PGP), is.na)

UsernameMatchesPandoraBMRIndex <- discard(match(BMR$username, PandoraUsers$Username), is.na)
EmailMatchesPandoraBMRIndex <- discard(match(BMR$gpg_email, PandoraUsers$Email), is.na)
PGPMatchesPandoraBMRIndex <- discard(match(BMR$gpg, PandoraUsers$PGP), is.na)

UsernameMatchesPandoraHydraIndex <- discard(match(PandoraUsers$Username, HydraClean$Username), is.na)
EmailMatchesPandoraHydraIndex <- discard(match(PandoraUsers$Email, HydraClean$Email), is.na)
PGPMatchesPandoraHydraIndex <- discard(match(PandoraUsers$PGP, HydraClean$PGP), is.na)

UsernameMatchesHydraPandoraIndex <- discard(match(PandoraUsers$Username, HydraClean$Username), is.na)
EmailMatchesHydraPandoraIndex <- discard(match(PandoraUsers$Email, HydraClean$Email), is.na)
PGPMatchesHydraPandoraIndex <- discard(match(PandoraUsers$PGP, HydraClean$PGP), is.na)

test <- intersect(BMR$gpg, HydraClean$PGP)

