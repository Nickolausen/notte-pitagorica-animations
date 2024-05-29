# Animazioni Notte Pitagorica
Animazioni realizzate con ManimCE in occasione della **Notte Pitagorica** - evento organizzato dall'**Istituto Tecnico Tecnologico "Blaise Pascal"** di Cesena in data 07-05-2024 @ Palazzo del Ridotto, Cesena.

## Come ottenere le animazioni - compilare i file
1) Installa tutte le dependencies necessarie 
- https://docs.manim.community/en/stable/installation/windows.html per Windows
- https://docs.manim.community/en/stable/installation/macos.html per MacOS
- https://docs.manim.community/en/stable/installation/linux.html per Linux

2) Prepara il virtual enviroment e installa le dipendenze
```sh
source ./setup.sh
```

2) Esegui nel terminale il seguente comando:
```sh
./run.sh <nomefile.py>
```

## Flag opzionali
```sh
./run.sh -<l/m/h> <nomefile.py>
```
- `l/m/h` (default: `m`): livello di qualità (low/medium/high)


---
Credits:
- Gioele Foschi <[www.github.com/delpiter](www.github.com/delpiter)> per aver contribuito nella creazione di alcune animazioni e nella ricerca di altre già pronte;
- https://github.com/nyabkun/fourier-series-manim - repository contenente alcune animazioni utilizzate per CUNA sulla _Trasformata di Fourier_
