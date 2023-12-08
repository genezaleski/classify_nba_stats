<a name="readme-top"></a>

[![Contributors][contributors-shield]][contributors-url]
[![LinkedIn][linkedin-shield]][linkedin-url]

<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/genezaleski/classify_nba_stats">
    <img src="images/logo.png" alt="Logo" width="80" height="80">
  </a>

<h3 align="center">Classifying the Quality of NBA Statistics</h3>

  <p align="center">
    Rating NBA statistics based on how good they are at predicting outcomes using ML
    <br />
    <a href="https://github.com/genezaleski/classify_nba_stats/classifyingNbaStatsXGBoost.pdf"><strong>Explore the docs »</strong></a>
    <br />
  </p>
</div>

<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
    </li>
    <li><a href="#usage">Usage</a></li>
  </ol>
</details>

<!-- ABOUT THE PROJECT -->
## About The Project

This project was done for my Data Mining II course in Spring 2022.

The goal of this project was to use machine learning to rate the importance of NBA stats in regards to how well they can predict positive outcomes (MVP, NBA Champions).

To do this, I scraped NBA.com back to 1996, cleaned the data, trained an XGBoost classifier on truth data I created by pulling the historical victors of MVP, etc. from the iternet.

Once finished I was able to visualize the accuracy of each stat as training data using Matplotlib.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

### Built With

* [![Python][python.link]][python-url]
* [![Pandas][pandas.link]][pandas-url]
* [![sklearn][skl.link]][skl-url]
* [![Ubuntu][ubuntu.link]][ubuntu-url]

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- GETTING STARTED -->
## Getting Started

This project was written on an Ubuntu 20.04 OS.

Python must be installed on this computer to run this project. 
Installation instructions for python can be found <a href="https://www.python.org/downloads/">here.</a>

Default libraries used in this project include:

    glob
    os
    requests

Additional python libraries that need to be installed include:

    imblearn
    matplotlib
    numpy
    pandas
    requests
    sklearn
    xgboost
    
An installation script can be found at the top level of this repository <a href="#readme-top">here.</a>

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- USAGE EXAMPLES -->
## Usage

An driver script can be found at the top level of this repository <a href="#readme-top">here.</a>

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- CONTACT -->
## Contact

Gene Zaleski - zaleskig8@students.rowan.edu.com

Project Link: [https://github.com/genezaleski/classify_nba_stats](https://github.com/genezaleski/classify_nba_stats)

<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/genezaleski/classify_nba_stats.svg?style=for-the-badge
[contributors-url]: https://github.com/genezaleski/classify_nba_stats/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/genezaleski/classify_nba_stats.svg?style=for-the-badge
[forks-url]: https://github.com/genezaleski/classify_nba_stats/network/members
[stars-shield]: https://img.shields.io/github/stars/genezaleski/classify_nba_stats.svg?style=for-the-badge
[stars-url]: https://github.com/genezaleski/classify_nba_stats/stargazers
[issues-shield]: https://img.shields.io/github/issues/genezaleski/classify_nba_stats.svg?style=for-the-badge
[issues-url]: https://github.com/genezaleski/classify_nba_stats/issues
[license-shield]: https://img.shields.io/github/license/genezaleski/classify_nba_stats.svg?style=for-the-badge
[license-url]: https://github.com/genezaleski/classify_nba_stats/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/gene-zaleski-56b2a0175
[product-screenshot]: images/screenshot.png
[python.link]: https://img.shields.io/badge/python-gray?logo=python&logoColor=#3776AB
[python-url]: https://www.python.org/
[pandas.link]: https://img.shields.io/badge/pandas-black?logo=pandas&logoColor=#150458
[pandas-url]: https://pandas.pydata.org/
[skl.link]: https://img.shields.io/badge/scikit_learn-fedcba?logo=scikitlearn&logoColor=#DE00A5
[skl-url]: https://scikit-learn.org/stable/
[ubuntu.link]: https://img.shields.io/badge/ubuntu-lightgray?logo=ubuntu&logoColor=#E95420
[ubuntu-url]: https://ubuntu.com/