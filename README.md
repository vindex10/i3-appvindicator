# i3 AppVindicator

An utility that shows a system tray icon for the app. Toggles show/hide app on click.
Under the hood i3-appvindicator uses [i3 scratchpad](https://i3wm.org/docs/userguide.html#_scratchpad).


## Dependencies:

* [PyGObject](https://pygobject.readthedocs.io/en/latest/)
* [libappindicator](https://launchpad.net/libappindicator)

on Debian `libappindicator` is replaced with [Ayatana indicators](https://github.com/AyatanaIndicators/libayatana-appindicator/).
Contribution to make i3-appvindicator Debian compatible is very welcome :)


## Installation

```
pip install git+https://github.com/vindex10/i3-appvindicator.git#egg=i3-appvindicator
```


## Usage

Hiding Evolution to tray:

```
i3-appvindicator -t 'Evolution Tray' -i 'evolution-mail' 'class="Evolution"'
```

* Middle click on the tray icon will toggle the controlled app
* Click on the icon will show a dropdown menu. `Toggle` will toggle the app

# All args


```
usage: i3-appvindicator [-h] [-t TITLE] [-i ICON] [-f] criteria [criteria ...]

positional arguments:
  criteria              Criteria to match window. Check i3 docs for syntax

optional arguments:
  -h, --help            show this help message and exit
  -t TITLE, --title TITLE
                        Indicator app title
  -i ICON, --icon ICON  Indicator app icon (find in /usr/share/icons)
  -f, --floating        The controlled app is floating
```


# TODO

* If the `i3-appvindicator` was launched before the controlled app (technically, when the controlled app was hidden),
middle click won't work. Add listener to run gtk indicator the moment the controlled app is launched
gtk app whenever the controlled app is launched.
