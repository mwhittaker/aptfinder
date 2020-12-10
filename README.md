# Apartment Finder [![Build Status][build_status]](https://travis-ci.org/mwhittaker/aptfinder)

Apartment finding bot inspired by [this article][apartment_finder_article].

## Getting Started
First, install all the required dependencies. We recommend using something like
conda:

```bash
conda create --name aptfinder python=3.6
source activate aptfinder
pip install -r requirements.txt
```

Then, create a settings JSON file. See `example_settings.json` for an example.
After that, run the apartment finder!

```bash
python -m aptfinder.main <settings_file>
```

[build_status]: https://travis-ci.org/mwhittaker/aptfinder.svg?branch=master
[apartment_finder_article]: https://www.dataquest.io/blog/apartment-finding-slackbot/
