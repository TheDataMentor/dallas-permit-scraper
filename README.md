# Dallas Permit Scraper

A Python web scraper that downloads and combines permit reports from Dallas City Hall for the months of January through September 2024.

## Table of Contents

- [Overview](#overview)
- [Installation](#installation)
- [Usage](#usage)
- [Dependencies](#dependencies)
- [License](#license)

## Overview

This project aims to provide an easy way to download permit reports from Dallas City Hall's website and combine them into a single DataFrame for analysis. The scraper navigates through links for each month's report, downloads Excel files, and consolidates their contents.

## Installation

To run this project, you need Python installed on your machine along with some libraries. You can install them using pip:

```bash
pip install requests beautifulsoup4 pandas openpyxl
