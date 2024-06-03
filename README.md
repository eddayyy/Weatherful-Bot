<div align="center">
    <img width=35% src="./data/media/Profile Picture.png">
    <h1>Weatherful Bot ☀️</h1>
    <a href="https://twitter.com/WeatherfulBot">
        <img alt="Status" src="https://img.shields.io/badge/Status-Live-brightgreen">
    </a>
    <img alt="Python Version" src="https://img.shields.io/badge/Python-v3.10%2B-blue">
    <img alt="AWS Lambda" src="https://img.shields.io/badge/AWS-Lambda-f4800b">
    <img alt="AWS S3" src="https://img.shields.io/badge/AWS-S3-43985a">
    <img alt="AWS EventBridge" src="https://img.shields.io/badge/AWS-EventBridge-ff00e7">
    <a href="https://opensource.org/licenses/MIT">
        <img alt="License" src="https://img.shields.io/badge/License-MIT-blue.svg">
    </a>
</div>



## Table of Contents
1. [Overview](#-overview)
2. [Features and Demo](#features-and-demo)
4. [License](#-license)

## 🌟 Overview

**[Weatherful Bot](https://twitter.com/WeatherfulBot)** is a Python-based automated system deployed on AWS Lambda designed to tweet real-time weather updates for Fullerton, California. Tweets are scheduled to occur bi-hourly with the current temperature, wind speeds, and humidity, daily at 6AM with sunrise and sunset times, and Sundays @ 12PM PST with the 7-day forecast. 

## **Features and Demo**

### Feature 1: Twitter Profile
- **Description**: The profile description aims to provide users with a clear description of the bot's purpose along with the bots tweet schedule. 

    - **Screenshot**: 

        ![Feature 1 Screenshot](./data/media/Profile%20Demo.png)

### Feature 2: Bi-Hourly Tweet
- **Description**: Tweet the weather every other hour in a clean format, along with emojis to make the tweets more visually appealing. 

    - **Screenshot**: 

        ![Feature 2 Screenshot](./data/media/Bi-Hourly-Tweet%20Demo.png)

### Feature 3: Sunset / Sunrise Tweet 
- **Description**: Every day at 6am the bot will tweet the sunrise and sunset times for that specific day. The tweet is well structured for easy readability and concise for clarity. 

    - **Screenshot**: 

        ![Feature 3 Screenshot](./data/media/Sunrise%20Sunset%20Demo.png)

### Feature 4: Weekly Forecast Tweet
- **Description**: Every Sunday at 12 PM PST the bot will tweet the 7-day forecast for the upcoming days. The tweet is formatted so that it distinguishes the type of weather that will occur on specific days (cloudy, rainy, sunny, etc.).

    - **Screenshot**: 

        ![Feature 4 Screenshot](./data/media/Weekly%20Forecast%20Demo.png)

## 📄 License

This project is licensed under the MIT License - see [LICENSE.md](LICENSE.md) for details.
