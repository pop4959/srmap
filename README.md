# srmap
Python library to edit SpeedRunners maps.

Use `pip` to install:

    $ pip install srmap
    
Below is some sample code to get you started. This will create a new level and save it to the file `map.sr`. You can also load existing levels, and modify the level however you like before saving it.

```py
from srmap import level

lvl = level.Level()
lvl.save('map.sr')
```

Once you have the level, you will need to replace another one in the `{STEAM}/userdata/{NUMBER}/207140/remote/` directory with it, where `{STEAM}` is your Steam installation path, and `{NUMBER}` is a Steam ID associated with the account you will be opening the game with. Then, simply start the game and you can play/edit/publish your level.
