# Simit - Unit Converter Using Text Similarity
 
Simit is modified pint unit converter that can read string (using text similarity) to call pint unit

Whats the different with pint ?
In pint u can read string using pint pasre expression like code below

```sh
ureg.parse_expression('centimeter')
```
but, unit that defined using string must that the same. using simit u can use text similarity to check what unit that u want to use. example

```sh
# pint string parse 
ureg.parse_expression('centimrt') # ERROR / Not Valid

# simit 
sim.conv('centimrt') # Valid
```

### Installation

You can install this lib using pip
Run the command below to install

```sh
$ pip install simit
```


### Dependencies

| Library | Descriptions |
| ------ | ------ |
| pint | Popular python unit converter |
| python-Levenshtein  | The Levenshtein Python C extension module to compute text similarity score |

### Example

```sh
from simit import SimUnit

sim = SimUnit()
print(1 * sim.conv('kilometr') + 500 * sim.conv('metr'))
# OUTPUT : 1.5 Kilometer
```

the first unit will be the base unit

## Thank You
