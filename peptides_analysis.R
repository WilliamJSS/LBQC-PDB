# Download Packages
#install.packages("Peptides", dependencies=TRUE)
#install.packages("tidyverse")
#install.packages("ggpubr")

# Reading Rpeptides
library(Peptides)

# Importing and filtering dataset
df <- read.csv("LBQCPDB.csv")
#df <- df[1:5,]
sequences <- as.character(df$Sequence)

## Peptides description ##

# Molecular Weight and Charge correlation
mz <- as.numeric(mz(sequences))
df$mz <- mz

# Charge
ch <- as.numeric(charge(sequences, pH = 7, pKscale = "Lehninger"))
df$ch <- ch


# Hydrophobicity
hd <- as.numeric(hydrophobicity(sequences, scale = "KyteDoolittle"))
df$hd <- hd

# Molecular Weight
mw <- as.numeric(mw(
  sequences,
  monoisotopic = FALSE,
  avgScale = "expasy",
  label = "none",
  aaShift = NULL
))

df$mw <- mw

# Compute the Boman (Potential Protein Interaction) index
bw <- as.numeric(boman(sequences))
df$bw <- bw

# Plot regression
#library(tidyverse)
#library(ggpubr)
#theme_set(theme_pubr())

# Total Charge x Docking Score
#ggplot(df, aes(x = df$Docking.score..1st.model., y = df$ch)) +
#  geom_point() +
#  stat_smooth()

# Total Molecular Weigth x Docking Score
#ggplot(df, aes(x = df$mw, y = df$Docking.score..1st.model.)) +
#  geom_point() +
#  stat_smooth()

# Recording new table
#write.csv(df,"LBQCPDB_descriptions.csv", row.names = TRUE, col.names = TRUE)
