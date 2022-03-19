# HW_lesson_5_casino_game
### Casino game Home Work

This is a project to demonstrate following topics:
- importing modules
- importing environment variables using `envparse`

Normally `settings.py` should not be committed and user's own variables used via:
```python
import envparse

env.read_envfile('settings.env')

MY_MONEY = int(os.environ.get('MY_MONEY'))
SPINWHEEL_SIZE = int(os.environ.get('SPINWHEEL_SIZE'))
```
### Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

### License
[MIT](https://choosealicense.com/licenses/mit/)
