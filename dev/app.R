#
# This is a Shiny web application. You can run the application by clicking
# the 'Run App' button above.
#
# Find out more about building applications with Shiny here:
#
#    http://shiny.rstudio.com/
#

library(shiny)
library(tidyverse)

# columns available
# X, name, code, url, gasDayStart, gasInStorage
# injection, withdrawal, workingGasVolume, injectionCapacity, withdrawalCapacity, status,
# trend, full, info, country, short_company, company_name
# (trend, full, info, name, code, url, injection, withdrawal, workingGasVolume, injectionCapacity, withdrawalCapacity, status, short_company, company_name)

agsi_data <- read.csv("https://raw.githubusercontent.com/mogeke/agsi_data_driven_decision_support/main/agsi_2022_dropna.csv", sep=",")
agsi_data$country <- as.factor(agsi_data$country)
agsi_data$gasInStorage <- as.double(agsi_data$gasInStorage)
#agsi_data$gasDayStart <- as.Date(agsi_data$gasDayStart)


# Define UI for application
ui <- fluidPage(
  
  
  # Application title
  titlePanel("AGSI Dashboard"),
  
  sidebarLayout(
    sidebarPanel(
      selectInput("country", "Select country", levels(agsi_data$country)),
    ),
    
    mainPanel(
      # Output: Tabset w/ plot, summary, and table ----
      tabsetPanel(type = "tabs",
                  tabPanel("Available in storage",textOutput("storage_country")),
                  tabPanel("Table", tableOutput("country_table"))
      )
      #textOutput("population_district"),
      #textOutput("percent_district"),
      # render plot output to UI
      #plotOutput("graph")
    )
  )
)

# Define server logic required to draw a histogram
server <- function(input, output) {
  
  output$storage_country <- renderText({
    storage_country <- agsi_data %>%
      filter(country == input$country) %>%
      filter(gasDayStart == max(agsi_data$gasDayStart))
    
    paste("Gas in storage:", sum(storage_country[, 'gasInStorage'], na.rm = TRUE))
  })
  
  output$country_table <- renderTable({
    storage_country <- agsi_data %>%
      filter(country == input$country)
    storage_country <- aggregate(storage_country["gasInStorage"], by=storage_country["gasDayStart"], sum)
    #storage_country <- subset(storage_country, select = -c(trend, full, info, name, code, url, injection, withdrawal, workingGasVolume, injectionCapacity, withdrawalCapacity, status, short_company, company_name) )
    storage_country[rev(order(storage_country$gasDayStart)),]
  })
  
}

# Run the application
shinyApp(ui = ui, server = server)
