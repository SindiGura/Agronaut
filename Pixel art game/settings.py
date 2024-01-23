
#A level map shows where the tiles are going to be placed, 
#It is a list where each element represents a row

level_map = [
'                             ',
'                             ',
'                             ',
'            XXX              ',
'      P                      ',
'     XXXX                XX  ',
'                   X     XXX ',
'XX        XXXX     XX    XXXX',
'XXX               XXX      XX',
'XXXX            XXXXX      XX',
'XXXXXXXXX    XXXXXXXX    XXXX',
]

tile_size = 65
screen_width = len(level_map[0])*tile_size
screen_height = len(level_map)*tile_size

