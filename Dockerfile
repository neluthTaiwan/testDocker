FROM rocker/r-ver:4.1.2

ARG WHEN

RUN R -e "options(repos = \
  list(CRAN = 'http://mran.revolutionanalytics.com/snapshot/${WHEN}/')); \
  install.packages('tidystringdist')"

COPY script.R script.R

CMD R -e "source('script.R')" 
