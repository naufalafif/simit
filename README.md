# Simit - Unit Converter Using Text Similarity

### Requirments 

| Library | Descriptions |
| ------ | ------ |
| pint | Popular python unit converter |
| python-Levenshtein  | The Levenshtein Python C extension module to compute text similarity score |

  - run command below to install requirment package
```sh
$ pip install python-Levenshtein pint
```
- or u can just run 
```sh
$ pip install -r requirments.txt
```


### How to use & Example
  - Download or clone this repo https://github.com/naufalafif/simit.git (using terminal or command prompt)
```sh
$ git clone https://github.com/naufalafif/simit
```

### Example

```sh
from simit import SimUnit

sim = SimUnit()
print(1 * sim.conv('kilometr') + 500 * sim.conv('metr'))
# OUTPUT : 1.5 Kilometer
```

the first unit will be the base unit

## Thank You
