import random
import webbrowser

websites = ['http://facebook.com','http://linkedin.com','https://www.youtube.com']

random = random.SystemRandom()

webbrowser.open(random.choice(websites))
