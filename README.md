# carplates

A simple python script to generate European-styled car license plates.

## Usage

 1. Install the required modules using:
 `python3 -m pip install -f requirements.txt`
 2. Adjust the configuration at the beginning of the file `main.py`.
 3. Run the script using:
`python3 main.py <plate_text>`

## Configuration

SmartyPants converts ASCII punctuation characters into "smart" typographic punctuation HTML entities. For example:

|Setting|Description|Type/Range|
|-|-|-|
|`corner_radius`|Corner angle radius.|`int`|
|`rounded`|Choose if the corners are rounded.|`bool`|
|`border`|Choose if the plate is outlined.|`bool`|
|`plate_size`|Plate dimensions.|`(int, int, int)`|
|`plate_color`|Plate background color.|`(int[r], int[g], int[b])`|
