# carplates

A simple python script to generate European-styled car license plates.

## Usage

 1. Install the required modules using:
 `python3 -m pip install -f requirements.txt`
 2. Adjust the configuration at the beginning of the file `main.py`
 3. Run the script using:
`python3 main.py <plate_text>`

## Configuration

SmartyPants converts ASCII punctuation characters into "smart" typographic punctuation HTML entities. For example:

|Setting|Description|Type/Range|
|-|-|-|
|`corner_radius`|Corner angle radius.|`int`|
|`rounded`|Rounded corners.|`bool`|
|`border`|Black plate outline.|`bool`|
|`plate_size`|Plate dimensions.|(`int`, `int`)|
|`plate_color`|Plate background color.|(`int` <sup>0 &rarr; 255</sup>, `int` <sup>0 &rarr; 255</sup> `int` <sup>0 &rarr; 255</sup>)|
|`lstrip_witdh`|Euroband width.|`int` <sup>0 &rarr; plateWidth</sup>|
|`lstrip_color`|Euroband color.|(`int` <sup>0 &rarr; 255</sup>, `int` <sup>0 &rarr; 255</sup> `int` <sup>0 &rarr; 255</sup>)|
|`letter_cc`|Country abbreviation .|`str` <sup>len 0 &rarr; 3</sup>|

