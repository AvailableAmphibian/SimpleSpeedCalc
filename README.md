# SimpleSpeedCalc

## English
Simple speed tune calculator for a Jamire LightHomunculus Lushen setup for Summoners War in Python.

### Details

Don't hesitate to contact me if you need an explanation or found a mistake !

This calculator is used with the Light Homunculus' S3 : `Fast Pace`.

The speedtune aimed is the followed :
- Jamire plays (s1 or s2)
- HomunLight casts S3 on Lushen ⇾ *atb resets and is set to `100` thanks to `Fast Pace`*
- Lushen casts S3
- Jamire casts S3
- HomunLight casts S3 on herself ⇾ *atb resets and is set to `100` thanks to `Fast Pace`* (again)
- HomunLight casts S2
- Lushen casts S3 (again)
 
### How to use it ?

You can execute the script [here](https://replit.com/@HFDrae/SquareCreepyVariety#main.py), you just need to modify the
last line to match your needs !

> If you want to use another monster, you need to provide the base speed with the following pattern :
> ```python
> display_needed_speed(200, True, nuker_bs=120) # change the 120 to match your needs !
> ```

You also have the possibility to clone the project or only download it and execute it on your computer using the
following command :
Windows (cmd) :
```
> python3 path\to\file\speed_calc.py
```
Unix :
```sh
$ python3 path/to/file/speed_calc.py
```
Or directly copying the file's content in [`repl`](https://replit.com/languages/python3) !

## Français
Calculateur pour le speed tune nécessaire à la compo `Jamire Lushen HomunLight` sur Summoners War en Python.

### Détails

Si jamais vous trouvez la moindre erreur ou avez besoin d'une explication, n'hésitez pas à me contacter !

Ce calculator est utilisé avec le S3 de l'Homunculus Lumière : `Rythme Rapide`.

On va viser le speed tune suivant :
- Jamire joue (s1 or s2)
- HomunLight fait S3 sur Lushen ⇾ *on met tous les atb à `100` grâce à `Rythme Rapide`*
- Lushen fait S3
- Jamire fait S3 
- HomunLight fait S3 sur elle ⇾ *on met tous les atb à `100` grâce à `Rythme Rapide`* (encore)
- HomunLight fait S2
- Lushen fait S3 (encore)

### Comment l'utiliser ?

Vous avez la possibilité de lancer le programme d'[ici](https://replit.com/@HFDrae/SquareCreepyVariety#main.py),
il faudra juste modifier la dernière ligne du programme pour obtenir le résultat voulu !

> Si vous voulez utiliser un autre monstre, vous avez besoin de fournir la base speed de celui-ci en suivant la ligne suivante :
> ```python
> display_needed_speed(200, True, nuker_bs=120) # Changez le 120 selon vos besoins !
> ```

Vous avez aussi la possibilité de cloner le projet ou simplement le télécharger et l'éxécuter sur votre machine en utilisant la commande suivante :
```
> python3 path\to\file\speed_calc.py
```
Unix :
```sh
$ python3 path/to/file/speed_calc.py
```

Sinon, le plus simple est probablement d'aller copier le contenu du script sur [`repl.it`](https://replit.com/languages/python3) !
