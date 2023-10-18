
# Importing the dataset

Data <- read.csv("building_inventory.csv", header = TRUE)





library(ggplot2)
ggplot(Data, aes(x= Year.Acquired, y= Square.Footage, fill=Agency.Name)) +
  geom_(lwd=1.2) +
  #scale_fill_manual(values=c("#69b3a2", "turquoise", "red", "blue", "orange", "green", "yellow")) +
  #scale_color_manual(values=c("black", "firebrick4", "tan3")) +
  theme(text=element_text(size=20, angle=360))
