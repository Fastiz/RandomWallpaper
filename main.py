import fnmatch
import os
import random


def main():
    try:
	__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

        f = open(os.path.join(__location__, "paths.txt"), "r")
        lines = f.read().splitlines()
    except:
        print("Error occurred when reading paths.txt file")
        return 1
    finally:
	f.close()

    wallpapers = []

    allowed_file_types = ['*.png', '*.jpg', '*.jpeg']

    for line in lines:

        try:
            entries = os.listdir(line)
        except:
            print('Wrong path (' + line + ')')
            break

        for entry in entries:
            if any(fnmatch.fnmatch(entry, p) for p in allowed_file_types):
                wallpapers.append(line + '/' + entry)

    if len(wallpapers) == 0:
        print('There are no wallpapers')
        return 1

    chosen_wallpaper = random.choice(wallpapers)

    print('Changing wallpaper to: ' + chosen_wallpaper)

    try:
        os.system('gsettings set org.gnome.desktop.background picture-uri file://' + chosen_wallpaper)
    except:
        print('An error occurred when changing the wallpaper')


main()
