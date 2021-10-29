# Microbit et REPL

Le mode REPL (Read-Evaluate-Print-Loop) permet à la carte micro:bit de lire et d'exécuter le code en temps réel au fur et à mesure que vous l'écrivez.

[Accessing the REPL](https://microbit-micropython.readthedocs.io/en/v1.0.1/devguide/repl.html)

## Sous Debian ou Ubuntu (linux)

J'utilise GtkTerm on peut aussi utiliser screen ou picocom ...

le port est /dev/ttyACM0 baudrate: 115200 configuration 8-N-1 8 bits de données pas de parité None et 1 bits de stop

## Sous Windows

On peut utiliser Tera Term ou Putty

## Autres

On peut aussi utiliser l'éditeur MU qui permet d'accéder au REPL

### En ligne avec Google Chrome
on peut travailler en ligne et utiliser le WebUSB
avec [Éditeur python pour Microbit](https://microbit-micropython.readthedocs.io/en/v1.0.1/devguide/repl.html)

Il faut ouvrir la liaison série Open Serial

# Utilisation de REPL

Il faut avoir la main, si un programme tourne, on pourra faire CTRL-C ou CTRL-D pour obtenir des chevrons >>>

On doit avoir la ligne : Type "help()" for more information.

Tapons cette ligne dans le terminal :

<code>
>>> help()
</code>

Voici la réponse :

<pre>
<code>
Welcome to MicroPython on the micro:bit!

Try these commands:
  display.scroll('Hello')
  running_time()
  sleep(1000)
  button_a.is_pressed()
What do these commands do? Can you improve them? HINT: use the up and down
arrow keys to get your command history. Press the TAB key to auto-complete
unfinished words (so 'di' becomes 'display' after you press TAB). These
tricks save a lot of typing and look cool!

Explore:
Type 'help(something)' to find out about it. Type 'dir(something)' to see what
it can do. Type 'dir()' to see what stuff is available. For goodness sake,
don't type 'import this'.

Control commands:
  CTRL-C        -- stop a running program
  CTRL-D        -- on a blank line, do a soft reset of the micro:bit
  CTRL-E        -- enter paste mode, turning off auto-indent

For a list of available modules, type help('modules')

For more information about Python, visit: http://python.org/
To find out about MicroPython, visit: http://micropython.org/
Python/micro:bit documentation is here: https://microbit-micropython.readthedocs.io/

</code>
</pre>

Vous avez des liens sur le langage Python, puis plus précisément sur le
langage MicroPython et enfin sur le langage MicroPython pour la carte Microbit.

Nous allons voir 5 choses dans ce document :
- Les différentes bibliothèques qui sont déjà implantées sur la carte MicroBit avec la commande  *help('modules')*
- La commande dir() qui permet pour une bibliothèque de connaître les objets et pour un objet ses différentes méthodes ou fonctions.
- La méthode help qui donne une aide ou des informations sur la bibliothèque ou l'objet en question.
- Comment récupérer des listes d'images et de broches
- Un exemple complet avec sources et réponses

# help('modules')

Tapons cette ligne dans le terminal :

<code>
>>> help('modules')
</code>

Voici la réponse :

<pre>
<code>
__main__          love              os                time
antigravity       machine           radio             ucollections
array             math              random            ustruct
audio             microbit          speech            utime
builtins          micropython       struct
collections       music             sys
gc                neopixel          this
Plus any modules on the filesystem
</code>
</pre>

Si on veut faire une liste des "modules"

On copie tous les modules avec la souris et on tape :

<pre>
<code>
>>> modules="""__main__          love              os                time
... antigravity       machine           radio             ucollections
... array             math              random            ustruct
... audio             microbit          speech            utime
... builtins          micropython       struct
... collections       music      sys
... gc      neopixel          this
... """.split()
>>> modules
['__main__', 'love', 'os', 'time', 'antigravity', 'machine', 'radio', 'ucollections', 'array', 'math', 'random', 'ustruct', 'audio', 'microbit', 'speech', 'utime', 'builtins', 'micropython', 'struct', 'collections', 'music', 'sys', 'gc', 'neopixel', 'this']
</code>
</pre>

Il faut mettre 3 guillemets après modules= puis copier tous les modules et terminer par 3 guillemets puis .split() pour obtenir la liste des modules comme on le voit après.

Connaître [split](https://python-reference.readthedocs.io/en/latest/docs/str/split.html)

Comme les bibliothèques time et utime sont identiques comme collections et ucollections ainsi que  struct et ustruct, on va les enlever avec :

<pre>
<code>
>>> modules.remove('time')
>>> modules.remove('struct')
>>> modules.remove('collections')
</code>
</pre>

Voici une liste remaniée pour ne pas avoir de problème de mémoire.

modules=['sys','os','gc','utime','micropython','microbit','machine','radio','array','builtins','ucollections','math','random','ustruct','audio','speech','music','neopixel','love','this','antigravity']

Pour utiliser une bibliothèque on utilise import

Par exemple :

<code>
import gc
</code>

Pour le faire depuis un élément d'une liste on utilise :

exec("import {module}".format(module=element))

Pour installer toutes les bibliothèques de modules :
<pre>
<code>
>>> for nom in modules :
...     exec("import {module}".format(module=nom))
...     print(nom)
</code>
</pre>

Voici la réponse :
<pre>
<code>
sys
os
gc
utime
micropython
microbit
machine
radio
array
builtins
ucollections
math
random
ustruct
audio
speech
music
neopixel
love
The Zen of MicroPython, by Nicholas H. Tollervey

Code,
Hack it,
Less is more,
Keep it simple,
Small is beautiful,

Be brave! Break things! Learn and have fun!
Express yourself with MicroPython.

Happy hacking! :-)
this
+-xkcd.com/353---------------------------------------------------+
|                                                                |
|                                                    \0/         |
|                                                  /   \         |
|        You're flying!                  MicroPython!  /|        |
|            How?                                      \ \       |
|            /                                                   |
|          0                                                     |
|         /|\                                                    |
|          |                                                     |
|-----____/_\______________________________----------------------|
|                                                                |
+----------------------------------------------------------------+
antigravity
</code>
</pre>

# dir()

**Attention** pour rechercher dans une bibliothèque, il faut que celle-ci soit installée avec :
 - import ma_bibliotheque ou bien
 - exec("import {module}".format(module='ma_bibliotheque'))

Si on veut connaître les fonctions ou objet de la bibliothèque microbit on peut faire :
<pre>
<code>
>>> dir(microbit)  
</code>
</pre>

Voici la réponse :
<pre>
<code>
['__name__', 'Image', 'display', 'button_a', 'button_b', 'accelerometer', 'compass', 'i2c', 'uart', 'spi', 'reset', 'sleep', 'running_time', 'panic', 'temperature', 'pin0', 'pin1', 'pin2', 'pin3', 'pin4', 'pin5', 'pin6', 'pin7', 'pin8', 'pin9', 'pin10', 'pin11', 'pin12', 'pin13', 'pin14', 'pin15', 'pin16', 'pin19', 'pin20']
</code>
</pre>

Comme on peut le voir la bibliothèque microbit sert à gérer le hardware, on retrouve :

- les broches de pin 0 à pin20
- les 2 boutons button_a et button_b
- l'afficheur display et les images Image
- la boussole (compass) et l'accéléromètre accelerometer
- des fonctions du temps : sleep, running_time
- liaison série uart et bus i2c,spi
- 2 fonctions particulières reset et panic

## On peut aussi retrouver les fonctions d'un objet

objet display de la bibliothèque microbit :

<pre>
<code>
>>> dir(microbit.display)
['get_pixel', 'set_pixel', 'show', 'scroll', 'clear', 'on', 'off', 'is_on', 'read_light_level']
</code>
</pre>

Cela est très pratique de retrouver facilement les fonctions ou objets d'une bibliothèque et les méthodes d'un objet.

# help()

<pre>
<code>
>>> help(microbit.display.set_pixel)   
Use set_pixel(x, y, b) to set the display at LED pixel (x,y) to brightness 'b'
which can be set between 0 (off) to 9 (full brightness).
</code>
</pre>

Avec l'aide help, on retrouve le rôle de la méthode set_pixel de l'objet display de la bibliothèque microbit.

Le . est une particularité des langages orientés objets.

Ainsi set_pixel est un élement de display qui est un élément de microbit.

On peut aussi avoir l'aide d'un objet :
<pre>
<code>
>>>help(microbit.display)
micro:bit's 5x5 LED display.
</code>
</pre>

# La liaison série UART de la bibliothèque microbit

<pre>
<code>
>>> dir(microbit.uart)
['init', 'any', 'read', 'readline', 'readinto', 'write', 'ODD', 'EVEN']
>>> help(microbit.uart)
Communicate with a serial device connected to micro:bit's I/O pins.
</code>
</pre>

### Pour avoir de l'aide sur une bibliothèque ou un objet

<pre>
<code>
>>> def aide(nom):
...     print(nom)
...     print(help(eval(nom)))
...     for m in dir(eval(nom)):
...         print(nom+'.'+m)
...         help(eval(nom+'.'+m))
...         print("-------------------")
...         gc.collect()
</code>
</pre>

On obtient de l'aide sur la bibliothèque ou l'objet ainsi que l'ensemble des fonctions ou méthodes de celui-ci ou celle-ci.

Exemple avec la liaison série UART

<pre>
<code>
>>> aide('microbit.uart')
microbit.uart
Communicate with a serial device connected to micro:bit's I/O pins.
None
microbit.uart.init
Use init() to set up communication. Use pins 0 (TX) and 1 (RX) with a baud
rate of 9600.
Override the defaults for 'baudrate', 'parity' and 'pins'.
-------------------
microbit.uart.any
If there are incoming characters waiting to be read, any() will return True.
Otherwise, returns False.
-------------------
microbit.uart.read
Use read() to read characters.
Use read(n) to read, at most, 'n' bytes of data.
-------------------
microbit.uart.readline
Use readline() to read a line that ends with a newline character.
-------------------
microbit.uart.readinto
Use readinto(buf) to read bytes into the buffer 'buf'.
Use readinto(buff, n) to read, at most, 'n' number of bytes into 'buf'.
-------------------
microbit.uart.write
Use write(buf) to write the bytes in buffer 'buf' to the connected device.
-------------------
microbit.uart.ODD
object 1 is of type int
  from_bytes -- <classmethod>
  to_bytes -- <function>
-------------------
microbit.uart.EVEN
object 2 is of type int
  from_bytes -- <classmethod>
  to_bytes -- <function>
-------------------
</code>
</pre>

**IMPORTANT** pour ne pas avoir de problèmes de mémoire et devoir faire un reset sur la carte Microbit pour continuer à travailler avec REPL.

*Il faut régulièrement faire un gc.collect() pour libérer de la mémoire.*

# liste des images
Dans le cas où aucune bibliothèque n'est installée, il faut mettre la bibliothèque microbit puis récupérer les images dans microbit.Image avec dir

<pre>
<code>
>>> import microbit
>>> images=sorted([ i for i in dir(microbit.Image) if i[0].isupper()])
>>> images
['ALL_ARROWS', 'ALL_CLOCKS', 'ANGRY', 'ARROW_E', 'ARROW_N', 'ARROW_NE', 'ARROW_NW', 'ARROW_S', 'ARROW_SE', 'ARROW_SW', 'ARROW_W', 'ASLEEP', 'BUTTERFLY', 'CHESSBOARD', 'CLOCK1', 'CLOCK10', 'CLOCK11', 'CLOCK12', 'CLOCK2', 'CLOCK3', 'CLOCK4', 'CLOCK5', 'CLOCK6', 'CLOCK7', 'CLOCK8', 'CLOCK9', 'CONFUSED', 'COW', 'DIAMOND', 'DIAMOND_SMALL', 'DUCK', 'FABULOUS', 'GHOST', 'GIRAFFE', 'HAPPY', 'HEART', 'HEART_SMALL', 'HOUSE', 'MEH', 'MUSIC_CROTCHET', 'MUSIC_QUAVER', 'MUSIC_QUAVERS', 'NO', 'PACMAN', 'PITCHFORK', 'RABBIT', 'ROLLERSKATE', 'SAD', 'SILLY', 'SKULL', 'SMILE', 'SNAKE', 'SQUARE', 'SQUARE_SMALL', 'STICKFIGURE', 'SURPRISED', 'SWORD', 'TARGET', 'TORTOISE', 'TRIANGLE', 'TRIANGLE_LEFT', 'TSHIRT', 'UMBRELLA', 'XMAS', 'YES']
</code>
</pre>

sorted permet de trier les images et la fonction  if i[0].isupper()] permet de supprimer les attributs et fonctions qui ne commencent pas par une majusculedans une compréhension de liste.

Finalement on ne garde que les images triées par ordre alphabétique.

# liste des broches et méthodes communes et distinctes

<pre>
<code>
>>> info_pin = {i:dir(eval('microbit.'+i)) for i in dir(microbit) if i.startswith("pin")}
>>> sub,sup=set(info_pin["pin0"]),set()
>>> for i in info_pin.values():
...     sub = sub.intersection(i)
...     sup = sup.union(i)
...     
>>> print(sup)            
{'set_analog_period_microseconds', 'set_pull', 'PULL_DOWN', 'is_touched', 'get_mode', 'get_pull', 'get_analog_period_microseconds', 'set_analog_period', 'read_digital', 'write_analog', 'read_analog', 'NO_PULL', 'write_digital', 'PULL_UP'}
>>> print(sub)
{'get_mode', 'get_pull', 'write_digital', 'read_digital', 'set_pull', 'NO_PULL', 'PULL_DOWN', 'PULL_UP', 'write_analog', 'set_analog_period', 'set_analog_period_microseconds'}
>>> print(sup-sub)
{'is_touched', 'get_analog_period_microseconds', 'read_analog'}
>>> broches=(sorted(info_pin.keys(), key=lambda x: int(x[3:])))
>>> print(broches)
['pin0', 'pin1', 'pin2', 'pin3', 'pin4', 'pin5', 'pin6', 'pin7', 'pin8', 'pin9', 'pin10', 'pin11', 'pin12', 'pin13', 'pin14', 'pin15', 'pin16', 'pin19', 'pin20']
</code>
</pre>

On utilise un nouvel objet le set() ensemble en français :
[5.4. Ensembles](https://docs.python.org/fr/3/tutorial/datastructures.html#sets)

Cela nous permet d'obtenir dans :
- sup  l'ensemble des méthodes possibles avec les broches (pins)
- sub l'ensemble des méthodes communes à toutes les broches
- sup-sub l'ensemble des méthodes qui sont spécifiques à quelques broches.

## Extra Python vers MicroPython pour Microbit

La cart Microbit ne contient que 32ko de RAM aussi ses bibliothèques sont limitées

Pour aller plus loin, nous allons piloter la carte Microbit en [python](Microbit_python_micropython.md)

# Voici un fichier complet [microbit_aide_bibliotheques.py](software/microbit_aide_bibliotheques.py)  

Vous le trouverez dans software à télécharger dans une carte microbit.

<pre>
<code>
modules=['sys','os','gc','utime','micropython','microbit','machine','radio','array','builtins','ucollections','math','random','ustruct','audio','speech','music','neopixel','love','this','antigravity']
# extrait de help('microbit') après avoir enlevé les doubles, les modules sont en fait les bibliothèques    
def aide(nom): #fonction avec un paramètre de bibliothèque
    print(nom)  # affiche le nom du module
    print(help(eval(nom))) # affiche l'aide sur la bibliothèque
    for m in dir(eval(nom)): # on liste les fonctions d'une bibliothèque
        print(nom+'.'+m) # on obtient le module.la fonction comme microbit.button_a
        if ( type(eval(nom+'.'+m)) != str) : help(eval(nom+'.'+m))# on n'affiche pas les fonctions attributs comme name par exemple
    print("--------------------") # mais on affiche l'aide sur la fonction de la bibliothèque
    print(gc.mem_free()) #on affiche la mémoire libre
    gc.collect() # pour libérer de l'espace mémoire (garbage collection)

for nom in modules : # prendre un nom parmi les bibliothèques
    exec("import {module}".format(module=nom)) # pour installer la bibliothèque
    print(nom) #on affiche le nom de la bibliothèque installée
print(gc.mem_free()) # on affiche la mémoire libre
gc.collect() # pour libérer de l'espace mémoire (garbage collection)
for nom in modules : # prendre un nom parmi les bibliothèques
    aide(nom) # on affiche, la bibliothèque et l'aide sur la bibliothèque et l'aide sur ses fonctions

print("__________Fin Module___________")

info = {i:dir(globals()[i]) for i in globals()} # on crée 1 dico avec tous les noms globaux et leurs fonctions
for i,j in info.items() : print(i,j) # on affiche le dictionnaire
print("--------------------")
print(gc.mem_free())  # on affiche la mémoire libre
gc.collect()                # pour libérer de l'espace mémoire (garbage collection)
aide('microbit.button_a')   # pour avoir l'aide sur le bouton A et ses fonctions
aide('microbit.display')    # pour avoir l'aide sur l'afficheur et ses fonctions
aide('microbit.pin0')       # pour avoir l'aide sur la broche 0 et ses fonctions (les autres pins sont proches)
aide('microbit.uart')       # pour avoir l'aide sur l'uart (liasion série) et ses fonctions
aide('microbit.spi')        # pour avoir l'aide sur le bus spi et ses fonctions
aide('microbit.i2c')        # pour avoir l'aide sur le bus i2c et ses fonctions
aide('microbit.compass')    # pour avoir l'aide sur la boussole et ses fonctions
aide('microbit.accelerometer')  # pour avoir l'aide sur l'accéléromètre et ses fonctions
aide('microbit.temperature')    # pour avoir l'aide sur le capteur de température et ses fonctions
pins=sorted([i for i in info['microbit'] if i.startswith("pin")], key=lambda x: int(x[3:])) #on trie les broches
# par ordre numérique, le tri se fait avec key on enlève pin avec x[3:] tri par nombre avec int pour ne pas avoir 10..19 entre 1 et 2
print("pins",pins) # on affiche la liste des broches
print(gc.mem_free())
gc.collect()
images=sorted([ i for i in dir(microbit.Image) if i[0].isupper()]) # on ne garde que les noms qui commencent par 1 majuscule
print("images",images) # affichage de la liste des images
</code>
</pre>

et voici le résultat :
<pre>
<code>
sys
os
gc
utime
micropython
microbit
machine
radio
array
builtins
ucollections
math
random
ustruct
audio
speech
music
neopixel
love
The Zen of MicroPython, by Nicholas H. Tollervey

Code,
Hack it,
Less is more,
Keep it simple,
Small is beautiful,

Be brave! Break things! Learn and have fun!
Express yourself with MicroPython.

Happy hacking! :-)
this
+-xkcd.com/353---------------------------------------------------+
|                                                                |
|                                                    \0/         |
|                                                  /   \         |
|        You're flying!                  MicroPython!  /|        |
|            How?                                      \ \       |
|            /                                                   |
|          0                                                     |
|         /|\                                                    |
|          |                                                     |
|-----____/_\______________________________----------------------|
|                                                                |
+----------------------------------------------------------------+
antigravity
3568
sys
object <module 'sys'> is of type module
  __name__ -- sys
  version -- 3.4.0
  version_info -- (3, 4, 0)
  implementation -- (name='micropython', version=(1, 9, 2))
  platform -- microbit
  byteorder -- little
  exit -- <function>
  print_exception -- <function>
None
sys.__name__
sys.version
sys.version_info
object (3, 4, 0) is of type tuple
  count -- <function>
  index -- <function>
sys.implementation
object (name='micropython', version=(1, 9, 2)) is of type tuple
sys.platform
sys.byteorder
sys.exit
object <function> is of type function
sys.print_exception
object <function> is of type function
--------------------
3376
os
object <module 'os'> is of type module
  __name__ -- os
  remove -- <function>
  listdir -- <function>
  size -- <function>
  uname -- <function>
None
os.__name__
os.remove
object <function> is of type function
os.listdir
object <function> is of type function
os.size
object <function> is of type function
os.uname
object <function> is of type function
--------------------
4240
gc
object <module 'gc'> is of type module
  __name__ -- gc
  collect -- <function>
  disable -- <function>
  enable -- <function>
  isenabled -- <function>
  mem_free -- <function>
  mem_alloc -- <function>
  threshold -- <function>
None
gc.__name__
gc.collect
object <function> is of type function
gc.disable
object <function> is of type function
gc.enable
object <function> is of type function
gc.isenabled
object <function> is of type function
gc.mem_free
object <function> is of type function
gc.mem_alloc
object <function> is of type function
gc.threshold
object <function> is of type function
--------------------
2912
utime
object <module 'utime'> is of type module
  __name__ -- utime
  sleep -- <function>
  sleep_ms -- <function>
  sleep_us -- <function>
  ticks_ms -- <function>
  ticks_us -- <function>
  ticks_add -- <function>
  ticks_diff -- <function>
None
utime.__name__
utime.sleep
object <function> is of type function
utime.sleep_ms
object <function> is of type function
utime.sleep_us
object <function> is of type function
utime.ticks_ms
object <function> is of type function
utime.ticks_us
object <function> is of type function
utime.ticks_add
object <function> is of type function
utime.ticks_diff
object <function> is of type function
--------------------
2864
micropython
object <module 'micropython'> is of type module
  __name__ -- micropython
  const -- <function>
  opt_level -- <function>
  mem_info -- <function>
  qstr_info -- <function>
  stack_use -- <function>
  heap_lock -- <function>
  heap_unlock -- <function>
  kbd_intr -- <function>
None
micropython.__name__
micropython.const
object <function> is of type function
micropython.opt_level
object <function> is of type function
micropython.mem_info
object <function> is of type function
micropython.qstr_info
object <function> is of type function
micropython.stack_use
object <function> is of type function
micropython.heap_lock
object <function> is of type function
micropython.heap_unlock
object <function> is of type function
micropython.kbd_intr
object <function> is of type function
--------------------
2000
microbit
Useful stuff to control the micro:bit hardware.
None
microbit.__name__
microbit.Image
Create and use built-in IMAGES to show on the display. Use:
Image(
  '09090:'
  '99999:'
  '99999:'
  '09990:'
  '00900:')
...to make a new 5x5 heart image. Numbers go from 0 (off) to 9 (brightest). Note
the colon ':' to set the end of a row.
microbit.display
micro:bit's 5x5 LED display.
microbit.button_a
micro:bit's 'A' button. When button is pressed down, is_pressed() is True.
microbit.button_b
micro:bit's 'B' button. When button is pressed down, is_pressed() is True.
microbit.accelerometer
Detect micro:bit's movement in 3D.
It measures tilt (X and Y) and up-down (Z) motion.
microbit.compass
Use micro:bit's compass to detect the direction it is heading in.
The compass can detect magnetic fields.
It uses the Earth's magnetic field to detect direction.
microbit.i2c
Communicate with one or more named devices connected to micro:bit. Each named
device has an 'address', communicates using I2C, and connects to the I/O pins.
microbit.uart
Communicate with a serial device connected to micro:bit's I/O pins.
microbit.spi
Communicate using a serial peripheral interface (SPI) device connected to
micro:bit's I/O pins.
microbit.reset
object <function> is of type function
microbit.sleep
Put micro:bit to sleep(time) for some milliseconds (1 second = 1000 ms) of time.
sleep(2000) gives micro:bit a 2 second nap.
microbit.running_time
Return running_time() in milliseconds since micro:bit's last reset.
microbit.panic
Put micro:bit in panic() mode and display an unhappy face.
Press reset button to exit panic() mode.
microbit.temperature
Return micro:bit's temperature in degrees Celcius.
microbit.pin0
micro:bit's pin 0 on the gold edge connector.
microbit.pin1
micro:bit's pin 1 on the gold edge connector.
microbit.pin2
micro:bit's pin 2 on the gold edge connector.
microbit.pin3
micro:bit's pin 3 on the gold edge connector.
microbit.pin4
micro:bit's pin 4 on the gold edge connector.
microbit.pin5
micro:bit's pin 5 on the gold edge connector.
microbit.pin6
micro:bit's pin 6 on the gold edge connector.
microbit.pin7
micro:bit's pin 7 on the gold edge connector.
microbit.pin8
micro:bit's pin 8 on the gold edge connector.
microbit.pin9
micro:bit's pin 9 on the gold edge connector.
microbit.pin10
micro:bit's pin 10 on the gold edge connector.
microbit.pin11
micro:bit's pin 11 on the gold edge connector.
microbit.pin12
micro:bit's pin 12 on the gold edge connector.
microbit.pin13
micro:bit's pin 13 on the gold edge connector.
microbit.pin14
micro:bit's pin 14 on the gold edge connector.
microbit.pin15
micro:bit's pin 15 on the gold edge connector.
microbit.pin16
micro:bit's pin 16 on the gold edge connector.
microbit.pin19
micro:bit's pin 19 on the gold edge connector.
microbit.pin20
micro:bit's pin 20 on the gold edge connector.
--------------------
5664
machine
object <module 'machine'> is of type module
  __name__ -- machine
  unique_id -- <function>
  reset -- <function>
  freq -- <function>
  disable_irq -- <function>
  enable_irq -- <function>
  mem8 -- <8-bit memory>
  mem16 -- <16-bit memory>
  mem32 -- <32-bit memory>
  time_pulse_us -- <function>
None
machine.__name__
machine.unique_id
object <function> is of type function
machine.reset
object <function> is of type function
machine.freq
object <function> is of type function
machine.disable_irq
object <function> is of type function
machine.enable_irq
object <function> is of type function
machine.mem8
object <8-bit memory> is of type mem
machine.mem16
object <16-bit memory> is of type mem
machine.mem32
object <32-bit memory> is of type mem
machine.time_pulse_us
object <function> is of type function
--------------------
1760
radio
object <module 'radio'> is of type module
  __name__ -- radio
  __init__ -- <function>
  reset -- <function>
  config -- <function>
  on -- <function>
  off -- <function>
  send_bytes -- <function>
  receive_bytes -- <function>
  send -- <function>
  receive -- <function>
  receive_bytes_into -- <function>
  receive_full -- <function>
  RATE_250KBIT -- 2
  RATE_1MBIT -- 0
  RATE_2MBIT -- 1
None
radio.__name__
radio.__init__
object <function> is of type function
radio.reset
object <function> is of type function
radio.config
object <function> is of type function
radio.on
object <function> is of type function
radio.off
object <function> is of type function
radio.send_bytes
object <function> is of type function
radio.receive_bytes
object <function> is of type function
radio.send
object <function> is of type function
radio.receive
object <function> is of type function
radio.receive_bytes_into
object <function> is of type function
radio.receive_full
object <function> is of type function
radio.RATE_250KBIT
object 2 is of type int
  from_bytes -- <classmethod>
  to_bytes -- <function>
radio.RATE_1MBIT
object 0 is of type int
  from_bytes -- <classmethod>
  to_bytes -- <function>
radio.RATE_2MBIT
object 1 is of type int
  from_bytes -- <classmethod>
  to_bytes -- <function>
--------------------
4800
array
object <module 'array'> is of type module
  __name__ -- array
  array -- <class 'array'>
None
array.__name__
array.array
object <class 'array'> is of type type
  append -- <function>
  extend -- <function>
--------------------
5600
builtins
object <module 'builtins'> is of type module
  __name__ -- builtins
  __build_class__ -- <function>
  __import__ -- <function>
  __repl_print__ -- <function>
  bool -- <class 'bool'>
  bytes -- <class 'bytes'>
  bytearray -- <class 'bytearray'>
  dict -- <class 'dict'>
  enumerate -- <class 'enumerate'>
  filter -- <class 'filter'>
  float -- <class 'float'>
  frozenset -- <class 'frozenset'>
  int -- <class 'int'>
  list -- <class 'list'>
  map -- <class 'map'>
  object -- <class 'object'>
  range -- <class 'range'>
  reversed -- <class 'reversed'>
  set -- <class 'set'>
  slice -- <class 'slice'>
  str -- <class 'str'>
  super -- <class 'super'>
  tuple -- <class 'tuple'>
  type -- <class 'type'>
  zip -- <class 'zip'>
  classmethod -- <class 'classmethod'>
  staticmethod -- <class 'staticmethod'>
  Ellipsis -- Ellipsis
  abs -- <function>
  all -- <function>
  any -- <function>
  bin -- <function>
  callable -- <function>
  chr -- <function>
  dir -- <function>
  divmod -- <function>
  eval -- <function>
  exec -- <function>
  getattr -- <function>
  setattr -- <function>
  globals -- <function>
  hasattr -- <function>
  hash -- <function>
  help -- <function>
  hex -- <function>
  id -- <function>
  input -- <function>
  isinstance -- <function>
  issubclass -- <function>
  iter -- <function>
  len -- <function>
  locals -- <function>
  max -- <function>
  min -- <function>
  next -- <function>
  oct -- <function>
  ord -- <function>
  pow -- <function>
  print -- <function>
  repr -- <function>
  round -- <function>
  sorted -- <function>
  sum -- <function>
  BaseException -- <class 'BaseException'>
  ArithmeticError -- <class 'ArithmeticError'>
  AssertionError -- <class 'AssertionError'>
  AttributeError -- <class 'AttributeError'>
  EOFError -- <class 'EOFError'>
  Exception -- <class 'Exception'>
  GeneratorExit -- <class 'GeneratorExit'>
  ImportError -- <class 'ImportError'>
  IndentationError -- <class 'IndentationError'>
  IndexError -- <class 'IndexError'>
  KeyboardInterrupt -- <class 'KeyboardInterrupt'>
  KeyError -- <class 'KeyError'>
  LookupError -- <class 'LookupError'>
  MemoryError -- <class 'MemoryError'>
  NameError -- <class 'NameError'>
  NotImplementedError -- <class 'NotImplementedError'>
  OSError -- <class 'OSError'>
  OverflowError -- <class 'OverflowError'>
  RuntimeError -- <class 'RuntimeError'>
  StopIteration -- <class 'StopIteration'>
  SyntaxError -- <class 'SyntaxError'>
  SystemExit -- <class 'SystemExit'>
  TypeError -- <class 'TypeError'>
  UnicodeError -- <class 'UnicodeError'>
  ValueError -- <class 'ValueError'>
  ZeroDivisionError -- <class 'ZeroDivisionError'>
  open -- <function>
None
builtins.__name__
builtins.__build_class__
object <function> is of type function
builtins.__import__
object <function> is of type function
builtins.__repl_print__
object <function> is of type function
builtins.bool
object <class 'bool'> is of type type
builtins.bytes
object <class 'bytes'> is of type type
  find -- <function>
  rfind -- <function>
  index -- <function>
  rindex -- <function>
  join -- <function>
  split -- <function>
  rsplit -- <function>
  startswith -- <function>
  endswith -- <function>
  strip -- <function>
  lstrip -- <function>
  rstrip -- <function>
  format -- <function>
  replace -- <function>
  count -- <function>
  lower -- <function>
  upper -- <function>
  isspace -- <function>
  isalpha -- <function>
  isdigit -- <function>
  isupper -- <function>
  islower -- <function>
builtins.bytearray
object <class 'bytearray'> is of type type
  append -- <function>
  extend -- <function>
builtins.dict
object <class 'dict'> is of type type
  clear -- <function>
  copy -- <function>
  fromkeys -- <classmethod>
  get -- <function>
  items -- <function>
  keys -- <function>
  pop -- <function>
  popitem -- <function>
  setdefault -- <function>
  update -- <function>
  values -- <function>
  __getitem__ -- <function>
  __setitem__ -- <function>
  __delitem__ -- <function>
builtins.enumerate
object <class 'enumerate'> is of type type
builtins.filter
object <class 'filter'> is of type type
builtins.float
object <class 'float'> is of type type
builtins.frozenset
object <class 'frozenset'> is of type type
  add -- <function>
  clear -- <function>
  copy -- <function>
  discard -- <function>
  difference -- <function>
  difference_update -- <function>
  intersection -- <function>
  intersection_update -- <function>
  isdisjoint -- <function>
  issubset -- <function>
  issuperset -- <function>
  pop -- <function>
  remove -- <function>
  symmetric_difference -- <function>
  symmetric_difference_update -- <function>
  union -- <function>
  update -- <function>
  __contains__ -- <function>
builtins.int
object <class 'int'> is of type type
  from_bytes -- <classmethod>
  to_bytes -- <function>
builtins.list
object <class 'list'> is of type type
  append -- <function>
  clear -- <function>
  copy -- <function>
  count -- <function>
  extend -- <function>
  index -- <function>
  insert -- <function>
  pop -- <function>
  remove -- <function>
  reverse -- <function>
  sort -- <function>
builtins.map
object <class 'map'> is of type type
builtins.object
object <class 'object'> is of type type
builtins.range
object <class 'range'> is of type type
builtins.reversed
object <class 'reversed'> is of type type
builtins.set
object <class 'set'> is of type type
  add -- <function>
  clear -- <function>
  copy -- <function>
  discard -- <function>
  difference -- <function>
  difference_update -- <function>
  intersection -- <function>
  intersection_update -- <function>
  isdisjoint -- <function>
  issubset -- <function>
  issuperset -- <function>
  pop -- <function>
  remove -- <function>
  symmetric_difference -- <function>
  symmetric_difference_update -- <function>
  union -- <function>
  update -- <function>
  __contains__ -- <function>
builtins.slice
object <class 'slice'> is of type type
builtins.str
object <class 'str'> is of type type
  find -- <function>
  rfind -- <function>
  index -- <function>
  rindex -- <function>
  join -- <function>
  split -- <function>
  rsplit -- <function>
  startswith -- <function>
  endswith -- <function>
  strip -- <function>
  lstrip -- <function>
  rstrip -- <function>
  format -- <function>
  replace -- <function>
  count -- <function>
  lower -- <function>
  upper -- <function>
  isspace -- <function>
  isalpha -- <function>
  isdigit -- <function>
  isupper -- <function>
  islower -- <function>
builtins.super
object <class 'super'> is of type type
builtins.tuple
object <class 'tuple'> is of type type
  count -- <function>
  index -- <function>
builtins.type
object <class 'type'> is of type type
builtins.zip
object <class 'zip'> is of type type
builtins.classmethod
object <class 'classmethod'> is of type type
builtins.staticmethod
object <class 'staticmethod'> is of type type
builtins.Ellipsis
object Ellipsis is of type
builtins.abs
object <function> is of type function
builtins.all
object <function> is of type function
builtins.any
object <function> is of type function
builtins.bin
object <function> is of type function
builtins.callable
object <function> is of type function
builtins.chr
object <function> is of type function
builtins.dir
object <function> is of type function
builtins.divmod
object <function> is of type function
builtins.eval
object <function> is of type function
builtins.exec
object <function> is of type function
builtins.getattr
object <function> is of type function
builtins.setattr
object <function> is of type function
builtins.globals
object <function> is of type function
builtins.hasattr
object <function> is of type function
builtins.hash
object <function> is of type function
builtins.help
object <function> is of type function
builtins.hex
object <function> is of type function
builtins.id
object <function> is of type function
builtins.input
object <function> is of type function
builtins.isinstance
object <function> is of type function
builtins.issubclass
object <function> is of type function
builtins.iter
object <function> is of type function
builtins.len
object <function> is of type function
builtins.locals
object <function> is of type function
builtins.max
object <function> is of type function
builtins.min
object <function> is of type function
builtins.next
object <function> is of type function
builtins.oct
object <function> is of type function
builtins.ord
object <function> is of type function
builtins.pow
object <function> is of type function
builtins.print
object <function> is of type function
builtins.repr
object <function> is of type function
builtins.round
object <function> is of type function
builtins.sorted
object <function> is of type function
builtins.sum
object <function> is of type function
builtins.BaseException
object <class 'BaseException'> is of type type
  __init__ -- <function>
builtins.ArithmeticError
object <class 'ArithmeticError'> is of type type
builtins.AssertionError
object <class 'AssertionError'> is of type type
builtins.AttributeError
object <class 'AttributeError'> is of type type
builtins.EOFError
object <class 'EOFError'> is of type type
builtins.Exception
object <class 'Exception'> is of type type
builtins.GeneratorExit
object <class 'GeneratorExit'> is of type type
builtins.ImportError
object <class 'ImportError'> is of type type
builtins.IndentationError
object <class 'IndentationError'> is of type type
builtins.IndexError
object <class 'IndexError'> is of type type
builtins.KeyboardInterrupt
object <class 'KeyboardInterrupt'> is of type type
builtins.KeyError
object <class 'KeyError'> is of type type
builtins.LookupError
object <class 'LookupError'> is of type type
builtins.MemoryError
object <class 'MemoryError'> is of type type
builtins.NameError
object <class 'NameError'> is of type type
builtins.NotImplementedError
object <class 'NotImplementedError'> is of type type
builtins.OSError
object <class 'OSError'> is of type type
builtins.OverflowError
object <class 'OverflowError'> is of type type
builtins.RuntimeError
object <class 'RuntimeError'> is of type type
builtins.StopIteration
object <class 'StopIteration'> is of type type
builtins.SyntaxError
object <class 'SyntaxError'> is of type type
builtins.SystemExit
object <class 'SystemExit'> is of type type
builtins.TypeError
object <class 'TypeError'> is of type type
builtins.UnicodeError
object <class 'UnicodeError'> is of type type
builtins.ValueError
object <class 'ValueError'> is of type type
builtins.ZeroDivisionError
object <class 'ZeroDivisionError'> is of type type
builtins.open
object <function> is of type function
--------------------
1216
ucollections
object <module 'ucollections'> is of type module
  __name__ -- ucollections
  namedtuple -- <function>
  OrderedDict -- <class 'OrderedDict'>
None
ucollections.__name__
ucollections.namedtuple
object <function> is of type function
ucollections.OrderedDict
object <class 'OrderedDict'> is of type type
  clear -- <function>
  copy -- <function>
  fromkeys -- <classmethod>
  get -- <function>
  items -- <function>
  keys -- <function>
  pop -- <function>
  popitem -- <function>
  setdefault -- <function>
  update -- <function>
  values -- <function>
  __getitem__ -- <function>
  __setitem__ -- <function>
  __delitem__ -- <function>
--------------------
5040
math
object <module 'math'> is of type module
  __name__ -- math
  e -- 2.71828
  pi -- 3.14159
  sqrt -- <function>
  pow -- <function>
  exp -- <function>
  log -- <function>
  cos -- <function>
  sin -- <function>
  tan -- <function>
  acos -- <function>
  asin -- <function>
  atan -- <function>
  atan2 -- <function>
  ceil -- <function>
  copysign -- <function>
  fabs -- <function>
  floor -- <function>
  fmod -- <function>
  frexp -- <function>
  ldexp -- <function>
  modf -- <function>
  isfinite -- <function>
  isinf -- <function>
  isnan -- <function>
  trunc -- <function>
  radians -- <function>
  degrees -- <function>
None
math.__name__
math.e
object 2.71828 is of type float
math.pi
object 3.14159 is of type float
math.sqrt
object <function> is of type function
math.pow
object <function> is of type function
math.exp
object <function> is of type function
math.log
object <function> is of type function
math.cos
object <function> is of type function
math.sin
object <function> is of type function
math.tan
object <function> is of type function
math.acos
object <function> is of type function
math.asin
object <function> is of type function
math.atan
object <function> is of type function
math.atan2
object <function> is of type function
math.ceil
object <function> is of type function
math.copysign
object <function> is of type function
math.fabs
object <function> is of type function
math.floor
object <function> is of type function
math.fmod
object <function> is of type function
math.frexp
object <function> is of type function
math.ldexp
object <function> is of type function
math.modf
object <function> is of type function
math.isfinite
object <function> is of type function
math.isinf
object <function> is of type function
math.isnan
object <function> is of type function
math.trunc
object <function> is of type function
math.radians
object <function> is of type function
math.degrees
object <function> is of type function
--------------------
4704
random
object <module 'random'> is of type module
  __name__ -- random
  getrandbits -- <function>
  seed -- <function>
  randrange -- <function>
  randint -- <function>
  choice -- <function>
  random -- <function>
  uniform -- <function>
None
random.__name__
random.getrandbits
object <function> is of type function
random.seed
object <function> is of type function
random.randrange
object <function> is of type function
random.randint
object <function> is of type function
random.choice
object <function> is of type function
random.random
object <function> is of type function
random.uniform
object <function> is of type function
--------------------
2816
ustruct
object <module 'ustruct'> is of type module
  __name__ -- ustruct
  calcsize -- <function>
  pack -- <function>
  pack_into -- <function>
  unpack -- <function>
  unpack_from -- <function>
None
ustruct.__name__
ustruct.calcsize
object <function> is of type function
ustruct.pack
object <function> is of type function
ustruct.pack_into
object <function> is of type function
ustruct.unpack
object <function> is of type function
ustruct.unpack_from
object <function> is of type function
--------------------
3632
audio
object <module 'audio'> is of type module
  __name__ -- audio
  stop -- <function>
  play -- <function>
  is_playing -- <function>
  AudioFrame -- <class 'AudioFrame'>
None
audio.__name__
audio.stop
object <function> is of type function
audio.play
object <function> is of type function
audio.is_playing
object <function> is of type function
audio.AudioFrame
object <class 'AudioFrame'> is of type type
  copyfrom -- <function>
--------------------
4144
speech
object <module 'speech'> is of type module
  __name__ -- speech
  say -- <function>
  sing -- <function>
  pronounce -- <function>
  translate -- <function>
None
speech.__name__
speech.say
object <function> is of type function
speech.sing
object <function> is of type function
speech.pronounce
object <function> is of type function
speech.translate
object <function> is of type function
--------------------
4144
music
Plug in a speaker with crocodile clips and make micro:bit go bleep and bloop.
None
music.__name__
music.__init__
object <function> is of type function
music.reset
If things go wrong, reset() the music to its default settings.
music.set_tempo
Use set_tempo(number, bpm) to make a beat last a 'number' of ticks long and
played at 'bpm' beats per minute.
music.get_tempo
Use get_tempo() to return the number of ticks in a beat and number of beats
per minute.
music.play
Use play(music) to make micro:bit play 'music' list of notes. Try out the
built in music to see how it works. E.g. music.play(music.PUNCHLINE).
music.pitch
Use pitch(freq, length) to make micro:bit play a note at 'freq' frequency for
'length' milliseconds. E.g. pitch(440, 1000) will play concert 'A' for 1 second.
music.stop
Use to stop() the music that is playing.
music.DADADADUM
object ('r4:2', 'g', 'g', 'g', 'eb:8', 'r:2', 'f', 'f', 'f', 'd:8') is of type tuple
  count -- <function>
  index -- <function>
music.ENTERTAINER
object ('d4:1', 'd#', 'e', 'c5:2', 'e4:1', 'c5:2', 'e4:1', 'c5:3', 'c:1', 'd', 'd#', 'e', 'c', 'd', 'e:2', 'b4:1', 'd5:2', 'c:4') is of type tuple
  count -- <function>
  index -- <function>
music.PRELUDE
object ('c4:1', 'e', 'g', 'c5', 'e', 'g4', 'c5', 'e', 'c4', 'e', 'g', 'c5', 'e', 'g4', 'c5', 'e', 'c4', 'd', 'g', 'd5', 'f', 'g4', 'd5', 'f', 'c4', 'd', 'g', 'd5', 'f', 'g4', 'd5', 'f', 'b3', 'd4', 'g', 'd5', 'f', 'g4', 'd5', 'f', 'b3', 'd4', 'g', 'd5', 'f', 'g4', 'd5', 'f', 'c4', 'e', 'g', 'c5', 'e', 'g4', 'c5', 'e', 'c4', 'e', 'g', 'c5', 'e', 'g4', 'c5', 'e') is of type tuple
  count -- <function>
  index -- <function>
music.ODE
object ('e4', 'e', 'f', 'g', 'g', 'f', 'e', 'd', 'c', 'c', 'd', 'e', 'e:6', 'd:2', 'd:8', 'e:4', 'e', 'f', 'g', 'g', 'f', 'e', 'd', 'c', 'c', 'd', 'e', 'd:6', 'c:2', 'c:8') is of type tuple
  count -- <function>
  index -- <function>
music.NYAN
object ('f#5:2', 'g#', 'c#:1', 'd#:2', 'b4:1', 'd5:1', 'c#', 'b4:2', 'b', 'c#5', 'd', 'd:1', 'c#', 'b4:1', 'c#5:1', 'd#', 'f#', 'g#', 'd#', 'f#', 'c#', 'd', 'b4', 'c#5', 'b4', 'd#5:2', 'f#', 'g#:1', 'd#', 'f#', 'c#', 'd#', 'b4', 'd5', 'd#', 'd', 'c#', 'b4', 'c#5', 'd:2', 'b4:1', 'c#5', 'd#', 'f#', 'c#', 'd', 'c#', 'b4', 'c#5:2', 'b4', 'c#5', 'b4', 'f#:1', 'g#', 'b:2', 'f#:1', 'g#', 'b', 'c#5', 'd#', 'b4', 'e5', 'd#', 'e', 'f#', 'b4:2', 'b', 'f#:1', 'g#', 'b', 'f#', 'e5', 'd#', 'c#', 'b4', 'f#', 'd#', 'e', 'f#', 'b:2', 'f#:1', 'g#', 'b:2', 'f#:1', 'g#', 'b', 'b', 'c#5', 'd#', 'b4', 'f#', 'g#', 'f#', 'b:2', 'b:1', 'a#', 'b', 'f#', 'g#', 'b', 'e5', 'd#', 'e', 'f#', 'b4:2', 'c#5') is of type tuple
  count -- <function>
  index -- <function>
music.RINGTONE
object ('c4:1', 'd', 'e:2', 'g', 'd:1', 'e', 'f:2', 'a', 'e:1', 'f', 'g:2', 'b', 'c5:4') is of type tuple
  count -- <function>
  index -- <function>
music.FUNK
object ('c2:2', 'c', 'd#', 'c:1', 'f:2', 'c:1', 'f:2', 'f#', 'g', 'c', 'c', 'g', 'c:1', 'f#:2', 'c:1', 'f#:2', 'f', 'd#') is of type tuple
  count -- <function>
  index -- <function>
music.BLUES
object ('c2:2', 'e', 'g', 'a', 'a#', 'a', 'g', 'e', 'c2:2', 'e', 'g', 'a', 'a#', 'a', 'g', 'e', 'f', 'a', 'c3', 'd', 'd#', 'd', 'c', 'a2', 'c2:2', 'e', 'g', 'a', 'a#', 'a', 'g', 'e', 'g', 'b', 'd3', 'f', 'f2', 'a', 'c3', 'd#', 'c2:2', 'e', 'g', 'e', 'g', 'f', 'e', 'd') is of type tuple
  count -- <function>
  index -- <function>
music.BIRTHDAY
object ('c4:3', 'c:1', 'd:4', 'c:4', 'f', 'e:8', 'c:3', 'c:1', 'd:4', 'c:4', 'g', 'f:8', 'c:3', 'c:1', 'c5:4', 'a4', 'f', 'e', 'd', 'a#:3', 'a#:1', 'a:4', 'f', 'g', 'f:8') is of type tuple
  count -- <function>
  index -- <function>
music.WEDDING
object ('c4:4', 'f:3', 'f:1', 'f:8', 'c:4', 'g:3', 'e:1', 'f:8', 'c:4', 'f:3', 'a:1', 'c5:4', 'a4:3', 'f:1', 'f:4', 'e:3', 'f:1', 'g:8') is of type tuple
  count -- <function>
  index -- <function>
music.FUNERAL
object ('c3:4', 'c:3', 'c:1', 'c:4', 'd#:3', 'd:1', 'd:3', 'c:1', 'c:3', 'b2:1', 'c3:4') is of type tuple
  count -- <function>
  index -- <function>
music.PUNCHLINE
object ('c4:3', 'g3:1', 'f#', 'g', 'g#:3', 'g', 'r', 'b', 'c4') is of type tuple
  count -- <function>
  index -- <function>
music.PYTHON
object ('d5:1', 'b4', 'r', 'b', 'b', 'a#', 'b', 'g5', 'r', 'd', 'd', 'r', 'b4', 'c5', 'r', 'c', 'c', 'r', 'd', 'e:5', 'c:1', 'a4', 'r', 'a', 'a', 'g#', 'a', 'f#5', 'r', 'e', 'e', 'r', 'c', 'b4', 'r', 'b', 'b', 'r', 'c5', 'd:5', 'd:1', 'b4', 'r', 'b', 'b', 'a#', 'b', 'b5', 'r', 'g', 'g', 'r', 'd', 'c#', 'r', 'a', 'a', 'r', 'a', 'a:5', 'g:1', 'f#:2', 'a:1', 'a', 'g#', 'a', 'e:2', 'a:1', 'a', 'g#', 'a', 'd', 'r', 'c#', 'd', 'r', 'c#', 'd:2', 'r:3') is of type tuple
  count -- <function>
  index -- <function>
music.BADDY
object ('c3:3', 'r', 'd:2', 'd#', 'r', 'c', 'r', 'f#:8') is of type tuple
  count -- <function>
  index -- <function>
music.CHASE
object ('a4:1', 'b', 'c5', 'b4', 'a:2', 'r', 'a:1', 'b', 'c5', 'b4', 'a:2', 'r', 'a:2', 'e5', 'd#', 'e', 'f', 'e', 'd#', 'e', 'b4:1', 'c5', 'd', 'c', 'b4:2', 'r', 'b:1', 'c5', 'd', 'c', 'b4:2', 'r', 'b:2', 'e5', 'd#', 'e', 'f', 'e', 'd#', 'e') is of type tuple
  count -- <function>
  index -- <function>
music.BA_DING
object ('b5:1', 'e6:3') is of type tuple
  count -- <function>
  index -- <function>
music.WAWAWAWAA
object ('e3:3', 'r:1', 'd#:3', 'r:1', 'd:4', 'r:1', 'c#:8') is of type tuple
  count -- <function>
  index -- <function>
music.JUMP_UP
object ('c5:1', 'd', 'e', 'f', 'g') is of type tuple
  count -- <function>
  index -- <function>
music.JUMP_DOWN
object ('g5:1', 'f', 'e', 'd', 'c') is of type tuple
  count -- <function>
  index -- <function>
music.POWER_UP
object ('g4:1', 'c5', 'e', 'g:2', 'e:1', 'g:3') is of type tuple
  count -- <function>
  index -- <function>
music.POWER_DOWN
object ('g5:1', 'd#', 'c', 'g4:2', 'b:1', 'c5:3') is of type tuple
  count -- <function>
  index -- <function>
--------------------
3056
neopixel
object <module 'neopixel'> is of type module
  __name__ -- neopixel
  NeoPixel -- <class 'NeoPixel'>
None
neopixel.__name__
neopixel.NeoPixel
object <class 'NeoPixel'> is of type type
  clear -- <function>
  show -- <function>
--------------------
5520
love
All you need. Use love.badaboom() to repeat the effect.
None
love.__name__
love.__init__
object <function> is of type function
love.badaboom
Hear my soul speak:
The very instant that I saw you, did
My heart fly to your service.
--------------------
5184
this
The Zen of Python defines what it is to be Pythonic. It wouldn't fit on this
device so we've written a Zen of MicroPython instead.
None
this.__name__
this.__init__
object <function> is of type function
this.authors
Use authors() to reveal the names of the people who created this software.
--------------------
5200
antigravity
See: http://xkcd.com/353/
None
antigravity.__name__
antigravity.__init__
object <function> is of type function
--------------------
5568
__________Fin Module___________
aide []
music ['__name__', '__init__', 'reset', 'set_tempo', 'get_tempo', 'play', 'pitch', 'stop', 'DADADADUM', 'ENTERTAINER', 'PRELUDE', 'ODE', 'NYAN', 'RINGTONE', 'FUNK', 'BLUES', 'BIRTHDAY', 'WEDDING', 'FUNERAL', 'PUNCHLINE', 'PYTHON', 'BADDY', 'CHASE', 'BA_DING', 'WAWAWAWAA', 'JUMP_UP', 'JUMP_DOWN', 'POWER_UP', 'POWER_DOWN']
os ['__name__', 'remove', 'listdir', 'size', 'uname']
modules ['append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']
array ['__name__', 'array']
radio ['__name__', '__init__', 'reset', 'config', 'on', 'off', 'send_bytes', 'receive_bytes', 'send', 'receive', 'receive_bytes_into', 'receive_full', 'RATE_250KBIT', 'RATE_1MBIT', 'RATE_2MBIT']
machine ['__name__', 'unique_id', 'reset', 'freq', 'disable_irq', 'enable_irq', 'mem8', 'mem16', 'mem32', 'time_pulse_us']
antigravity ['__name__', '__init__']
micropython ['__name__', 'const', 'opt_level', 'mem_info', 'qstr_info', 'stack_use', 'heap_lock', 'heap_unlock', 'kbd_intr']
ustruct ['__name__', 'calcsize', 'pack', 'pack_into', 'unpack', 'unpack_from']
sys ['__name__', 'version', 'version_info', 'implementation', 'platform', 'byteorder', 'exit', 'print_exception']
gc ['__name__', 'collect', 'disable', 'enable', 'isenabled', 'mem_free', 'mem_alloc', 'threshold']
random ['__name__', 'getrandbits', 'seed', 'randrange', 'randint', 'choice', 'random', 'uniform']
builtins ['__name__', '__build_class__', '__import__', '__repl_print__', 'bool', 'bytes', 'bytearray', 'dict', 'enumerate', 'filter', 'float', 'frozenset', 'int', 'list', 'map', 'object', 'range', 'reversed', 'set', 'slice', 'str', 'super', 'tuple', 'type', 'zip', 'classmethod', 'staticmethod', 'Ellipsis', 'abs', 'all', 'any', 'bin', 'callable', 'chr', 'dir', 'divmod', 'eval', 'exec', 'getattr', 'setattr', 'globals', 'hasattr', 'hash', 'help', 'hex', 'id', 'input', 'isinstance', 'issubclass', 'iter', 'len', 'locals', 'max', 'min', 'next', 'oct', 'ord', 'pow', 'print', 'repr', 'round', 'sorted', 'sum', 'BaseException', 'ArithmeticError', 'AssertionError', 'AttributeError', 'EOFError', 'Exception', 'GeneratorExit', 'ImportError', 'IndentationError', 'IndexError', 'KeyboardInterrupt', 'KeyError', 'LookupError', 'MemoryError', 'NameError', 'NotImplementedError', 'OSError', 'OverflowError', 'RuntimeError', 'StopIteration', 'SyntaxError', 'SystemExit', 'TypeError', 'UnicodeError', 'ValueError', 'ZeroDivisionError', 'open']
this ['__name__', '__init__', 'authors']
neopixel ['__name__', 'NeoPixel']
microbit ['__name__', 'Image', 'display', 'button_a', 'button_b', 'accelerometer', 'compass', 'i2c', 'uart', 'spi', 'reset', 'sleep', 'running_time', 'panic', 'temperature', 'pin0', 'pin1', 'pin2', 'pin3', 'pin4', 'pin5', 'pin6', 'pin7', 'pin8', 'pin9', 'pin10', 'pin11', 'pin12', 'pin13', 'pin14', 'pin15', 'pin16', 'pin19', 'pin20']
ucollections ['__name__', 'namedtuple', 'OrderedDict']
speech ['__name__', 'say', 'sing', 'pronounce', 'translate']
__name__ ['find', 'rfind', 'index', 'rindex', 'join', 'split', 'rsplit', 'startswith', 'endswith', 'strip', 'lstrip', 'rstrip', 'format', 'replace', 'count', 'lower', 'upper', 'isspace', 'isalpha', 'isdigit', 'isupper', 'islower']
nom ['find', 'rfind', 'index', 'rindex', 'join', 'split', 'rsplit', 'startswith', 'endswith', 'strip', 'lstrip', 'rstrip', 'format', 'replace', 'count', 'lower', 'upper', 'isspace', 'isalpha', 'isdigit', 'isupper', 'islower']
audio ['__name__', 'stop', 'play', 'is_playing', 'AudioFrame']
math ['__name__', 'e', 'pi', 'sqrt', 'pow', 'exp', 'log', 'cos', 'sin', 'tan', 'acos', 'asin', 'atan', 'atan2', 'ceil', 'copysign', 'fabs', 'floor', 'fmod', 'frexp', 'ldexp', 'modf', 'isfinite', 'isinf', 'isnan', 'trunc', 'radians', 'degrees']
utime ['__name__', 'sleep', 'sleep_ms', 'sleep_us', 'ticks_ms', 'ticks_us', 'ticks_add', 'ticks_diff']
love ['__name__', '__init__', 'badaboom']
--------------------
3536
microbit.button_a
micro:bit's 'A' button. When button is pressed down, is_pressed() is True.
None
microbit.button_a.is_pressed
If the button is pressed down, is_pressed() is True, else False.
microbit.button_a.was_pressed
Use was_pressed() to learn if the button was pressed since the last time
was_pressed() was called. Returns True or False.
microbit.button_a.get_presses
Use get_presses() to get the running total of button presses, and also
reset this counter to zero.
--------------------
2000
microbit.display
micro:bit's 5x5 LED display.
None
microbit.display.get_pixel
Use get_pixel(x, y) to return the display's brightness at LED pixel (x,y).
Brightness can be from 0 (LED is off) to 9 (maximum LED brightness).
microbit.display.set_pixel
Use set_pixel(x, y, b) to set the display at LED pixel (x,y) to brightness 'b'
which can be set between 0 (off) to 9 (full brightness).
microbit.display.show
Use show(x) to print the string or images 'x' to the display. Try show('Hi!').
Use show(s, i) to show string 's', one character at a time with a delay of
'i' milliseconds.
microbit.display.scroll
Use scroll(s) to scroll the string 's' across the display.
Use scroll(s, i) to scroll string 's' with a delay of 'i' milliseconds after
each character.
microbit.display.clear
Use clear() to clear micro:bit's display.
microbit.display.on
Use on() to turn on the display.
microbit.display.off
Use off() to turn off the display.
microbit.display.is_on
Use is_on() to query if the micro:bit's display is on (True) or off (False).
microbit.display.read_light_level
Use read_light_level() to get the ambient light level, between 0 (dark) and 255 (bright).
--------------------
1104
microbit.pin0
micro:bit's pin 0 on the gold edge connector.
None
microbit.pin0.write_digital
micro:bit, write_digital(choice) to the pin. You have two 'choice' values,
0 (lo) or 1 (hi).
microbit.pin0.read_digital
micro:bit, read_digital() value from the pin as either 0 (lo) or 1 (hi).
microbit.pin0.write_analog
micro:bit, write_analog(value) to the pin. You can use any value between
0 and 1023.
microbit.pin0.read_analog
micro:bit, read_analog() value from the pin. Wow, analog has lots of values
(0 - 65535). Digital has only 0 and 1.
microbit.pin0.set_analog_period
object <function> is of type function
microbit.pin0.set_analog_period_microseconds
object <function> is of type function
microbit.pin0.is_touched
If pin is_touched() on micro:bit, return True. If nothing is touching the pin,
return False.
microbit.pin0.PULL_UP
object 3 is of type int
  from_bytes -- <classmethod>
  to_bytes -- <function>
microbit.pin0.PULL_DOWN
object 1 is of type int
  from_bytes -- <classmethod>
  to_bytes -- <function>
microbit.pin0.NO_PULL
object 0 is of type int
  from_bytes -- <classmethod>
  to_bytes -- <function>
microbit.pin0.get_pull
object <function> is of type function
microbit.pin0.set_pull
object <function> is of type function
microbit.pin0.get_mode
object <function> is of type function
--------------------
2144
microbit.uart
Communicate with a serial device connected to micro:bit's I/O pins.
None
microbit.uart.init
Use init() to set up communication. Use pins 0 (TX) and 1 (RX) with a baud
rate of 9600.
Override the defaults for 'baudrate', 'parity' and 'pins'.
microbit.uart.any
If there are incoming characters waiting to be read, any() will return True.
Otherwise, returns False.
microbit.uart.read
Use read() to read characters.
Use read(n) to read, at most, 'n' bytes of data.
microbit.uart.readline
Use readline() to read a line that ends with a newline character.
microbit.uart.readinto
Use readinto(buf) to read bytes into the buffer 'buf'.
Use readinto(buff, n) to read, at most, 'n' number of bytes into 'buf'.
microbit.uart.write
Use write(buf) to write the bytes in buffer 'buf' to the connected device.
microbit.uart.ODD
object 1 is of type int
  from_bytes -- <classmethod>
  to_bytes -- <function>
microbit.uart.EVEN
object 2 is of type int
  from_bytes -- <classmethod>
  to_bytes -- <function>
--------------------
2224
microbit.spi
Communicate using a serial peripheral interface (SPI) device connected to
micro:bit's I/O pins.
None
microbit.spi.init
Use init() to set up communication. Override the defaults for baudrate, mode,
SCLK, MOSI and MISO. The default connections are pin13 for SCLK, pin15 for
MOSI and pin14 for MISO.
microbit.spi.write
Use write(buf) to write bytes in buffer 'buf' to the connected device.
microbit.spi.read
Use read(n) to read 'n' bytes of data.
microbit.spi.write_readinto
Use write_readinto(out, in) to write the 'out' buffer to the connected device
and read any response into the 'in' buffer. The length of the buffers should
be the same. The buffers can be the same object.
--------------------
1568
microbit.i2c
Communicate with one or more named devices connected to micro:bit. Each named
device has an 'address', communicates using I2C, and connects to the I/O pins.
None
microbit.i2c.init
Use init(frequency, scl, sda) to set the bus frequency and pins.
microbit.i2c.scan
object <function> is of type function
microbit.i2c.read
Use read(address, n) to read 'n' bytes from the device with this address.
microbit.i2c.write
Use write(address, buffer) to write to the 'buffer' of the device at this 'address'.
--------------------
1552
microbit.compass
Use micro:bit's compass to detect the direction it is heading in.
The compass can detect magnetic fields.
It uses the Earth's magnetic field to detect direction.
None
microbit.compass.heading
Gives a compass heading between 0-360 with 0 as north.
microbit.compass.is_calibrated
If micro:bit's compass is_calibrated() and adjusted for accuracy, return True.
If compass hasn't been adjusted for accuracy, return False.
microbit.compass.calibrate
If micro:bit is confused, calibrate() the compass to adjust the its accuracy.
It will ask you to rotate the device to draw a circle on the display.
microbit.compass.clear_calibration
Reset micro:bit's compass using clear_calibration() command.
Run calibrate() to improve accuracy.
microbit.compass.get_x
Return magnetic field detected along micro:bit's X axis.
Usually, the compass returns the earth's magnetic field in micro-Tesla units.
Unless...a strong magnet is nearby!
microbit.compass.get_y
Return magnetic field detected along micro:bit's Y axis.
Usually, the compass returns the earth's magnetic field in micro-Tesla units.
Unless...a strong magnet is nearby!
microbit.compass.get_z
Return magnetic field detected along micro:bit's Z axis.
Usually, the compass returns the earth's magnetic field in micro-Tesla units.
Unless...a strong magnet is nearby!
microbit.compass.get_field_strength
Return strength of magnetic field around micro:bit.
--------------------
3712
microbit.accelerometer
Detect micro:bit's movement in 3D.
It measures tilt (X and Y) and up-down (Z) motion.
None
microbit.accelerometer.get_x
Return micro:bit's tilt (X acceleration) in milli-g's.
microbit.accelerometer.get_y
Return micro:bit's tilt (Y acceleration) in milli-g's.
microbit.accelerometer.get_z
Return micro:bit's up-down motion (Z acceleration) in milli-g's.
Z is a positive number when moving up. Moving down, Z is a negative number.
microbit.accelerometer.get_values
object <function> is of type function
microbit.accelerometer.current_gesture
object <function> is of type function
microbit.accelerometer.is_gesture
object <function> is of type function
microbit.accelerometer.was_gesture
object <function> is of type function
microbit.accelerometer.get_gestures
object <function> is of type function
--------------------
3712
microbit.temperature
Return micro:bit's temperature in degrees Celcius.
None
--------------------
3648
pins ['pin0', 'pin1', 'pin2', 'pin3', 'pin4', 'pin5', 'pin6', 'pin7', 'pin8', 'pin9', 'pin10', 'pin11', 'pin12', 'pin13', 'pin14', 'pin15', 'pin16', 'pin19', 'pin20']
1984
images ['ALL_ARROWS', 'ALL_CLOCKS', 'ANGRY', 'ARROW_E', 'ARROW_N', 'ARROW_NE', 'ARROW_NW', 'ARROW_S', 'ARROW_SE', 'ARROW_SW', 'ARROW_W', 'ASLEEP', 'BUTTERFLY', 'CHESSBOARD', 'CLOCK1', 'CLOCK10', 'CLOCK11', 'CLOCK12', 'CLOCK2', 'CLOCK3', 'CLOCK4', 'CLOCK5', 'CLOCK6', 'CLOCK7', 'CLOCK8', 'CLOCK9', 'CONFUSED', 'COW', 'DIAMOND', 'DIAMOND_SMALL', 'DUCK', 'FABULOUS', 'GHOST', 'GIRAFFE', 'HAPPY', 'HEART', 'HEART_SMALL', 'HOUSE', 'MEH', 'MUSIC_CROTCHET', 'MUSIC_QUAVER', 'MUSIC_QUAVERS', 'NO', 'PACMAN', 'PITCHFORK', 'RABBIT', 'ROLLERSKATE', 'SAD', 'SILLY', 'SKULL', 'SMILE', 'SNAKE', 'SQUARE', 'SQUARE_SMALL', 'STICKFIGURE', 'SURPRISED', 'SWORD', 'TARGET', 'TORTOISE', 'TRIANGLE', 'TRIANGLE_LEFT', 'TSHIRT', 'UMBRELLA', 'XMAS', 'YES']
MicroPython v1.9.2-34-gd64154c73 on 2017-09-01; micro:bit v1.0.1 with nRF51822
Type "help()" for more information.
>>>
</code>
</pre>
