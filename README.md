# Branch-Predictor-Store-Location
A Python script to evaluate branch predictors and find the closest stores based on geographical coordinates. 

## Table of Contents
- [Introduction](#introduction)
- [Branch Predictor Evaluation](#branch-predictor-evaluation)
- [Store Location](#store-location)

## Introduction
The "Branch Predictor & Store Location" script is designed to help you evaluate different branch predictors and understand their impact on the performance of a CPU. It also provides functionality to find the closest stores to a given geographical location using the haversine distance formula.

## Branch Predictor Evaluation
The script can evaluate several branch predictors commonly used in computer architecture. It measures the IPC (Instructions Per Cycle) and misprediction rate for each predictor. The available predictors include:
- Not Taken
- Taken
- Perfect
- Bimodal
- 2-Level
- Combined

## Store Location
The script reads store data from a CSV file containing information such as store ID, address, city, state, zipcode, latitude, and longitude. Using the haversine distance formula, the script can find the Nth closest store to a specified geographical location.
