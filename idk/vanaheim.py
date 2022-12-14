vanaheim = (r"""
                /  \          /  \     /\          /  \   /    \   /\   /  
          /\   /    \        /    \   /  \   /\   /    \ /      \ /  \ /   
         /  \ /      \   /\ /      \ /    \ /  \ /     /\        /    \    
        /    \   /\     /  \        / /\   /    \     /  \      /      \   
    /\ /      \ /  \   /    \        /  \ / /\   \ /\/    \                
   /  \        /    \ /      \ /\   /    \ /  \   /  \ /\                 /
  /    \      /      \        /  \ /      /    \ /    /  \  /\   /\      / 
 /      \ /\          /\     /    \      /      \    /    \/  \ /  \      /
         /  \        /  \   /      \        _       /     /    \    \ /\ / 
   /\   /    \      /    \                 / \_          /           /  \  
  /  \ /      \ /\ /      \        __      |_ o\                 /\ /    \ 
 /    \        /  \         _     /<>\     |^|_|                /  \       
/      \ /\   /    \       /o\    |_^|                         /    \   /\ 
        /  \ /      \      |^|                            _   /      \ /  \
/\     /    \ /\      ###   .        ######  ######      /o\    /\    /    
  \   /      /  \    #####      ###  ######  ######      |^|   /  \  /     
   \   /\   /    \    ###   '. ##### #####    #####           /    \   /\  
    \ /  \ /      \   /|\    `  ###  ####      ####   ###    /      \ /  \ 
     /    \               __    /|\                  #####   /\      /    \
 /\ /      \ /\          /  \ .`'    ####      ####   ###   /  \    /      
/  \        /  \         |__|        #####    #####   /|\  /    \          
    \      /    \         ,' . ``    ######  ######       /      \ /\      
     \ /\ /      \ /\         '`'.,  ######  ######    ###        /  \     
      /  \        /  \    ###     ``'                 #####      /    \   /
/\   /    \      /    \  #####   _        __           ###   /\ /      \ / 
  \ /      \ /\ /         ###   / \ '    /<>\   `      /|\  /  \        /  
   \        /  \          /|\   |^| .    |^_|     .'       /    \   /\ /   
    \ /\   /    \              ` ``'         ###   ,  _   /      \ /  \    
     /  \ /      \ /\             _         ##### ', /-\          /    \   
    /    \        /  \         . / \         ### ,   |^|        /\      \ /
   /      \ /\   /    \          |^|         /|\ ,    `        /  \      / 
           /  \ /      \       ,.     _            ',` ''     /    \   /\  
          /    \          ###       _/ \   ###    _____  '   /      \ /  \ 
         /      \ /\     #####     /o  |  #####  /_____\ `'     /\   /    \
     /\          /  \     ###   `'.|___|   ###   |<>_<>|       /  \ /      
    /  \        /    \    /|\     '',.,    /|\   |_|^|_|  ,   /    \       
   /    \   /\ /      \        __     `,'.``` .',  .``'   `  /      \ /\   
  /      \ /  \               /<>\  ###              ,,.'            /  \  
          /    \              |__| #####          ###               /    \ 
      /\ /      \ /\            '   ###          #####            /\      \
     /  \        /  \           `   /|\  _        ###   _        /  \      
    /    \      /    \   /\       ..    /o\      ./|\  /o\      /    \   /\
   /      \ /\ /      \ /  \       .''  |^|   ,'`' ',` |^|  /\ /      \ /  
           /  \        /    \         ,.,  .,`,  /\  ', ,` /  \        /   
     /\   /    \   /\ /      \ /\               /  \      /    \   /\ /    
    /  \ /      \ /  \        /  \   /\        /    \ /\ /      \ /  \     
   /    \        /    \      /    \ /  \   /\ /      /  \   /\   /    \    
  /      \      /      \ /\ /      /    \ /  \      /    \ /  \ /      \   
                        /  \      /      /    \    /      /    \           
                       /    \           /      \         /      \          """,
# Autres mondes (Vanaheim = 1)
    (28, 13, 2, 14, 68),  # Alfheim
    (54, 29, 3, 10, 58),  # Midgard
    (56, 42, 5, 11, 120), # Jotunheim
    
# Maisons
    (44, 11, 21, 5, 9), # Auberge
    (52, 35, 22, 20, 19), # Palais de Hel
    (58, 15, 49, 7, 14),
    (36, 12, 50, 15, 14),
    (33, 26, 51, 5, 9),
    (42, 26, 52, 4, 14),
    (34, 30, 53, 5, 9),
    (41, 42, 54, 10, 9),
)



h_21 = (r"""
|=======================|
|         |             |
|         |-------------|
|                       |
|  +--+   +--+   +--+   |
|  |  |   |  |   |  |   |
|  +--+   +--+   +--+   |
|                       |
|                       |
|===|^|=================|""",
    (5, 9, 1, 44, 11)) 


h_22 = (r"""
|=======================|==============|
|=======================|==============|
|                       |              |
|   _         _         |     __       |
|  (_)       (_)        |    |__|      |
|  |=|       |=|        |    |__|      |
|  |_|       |_|        |    |__|      |
|                       |              |
|                       |              |
|                 |=]  [|]  [==========|
|   _         _   |                    |
|  (_)       (_)  |                    |
|  |=|       |=|  |   |=======[]=======|
|  |_|       |_|  |   |                |
|                 |   |                |
|                 |   |                |
|                 |   |                |
|                 |   |                |
|/\=/\=/\=/\=/\=/\=| |=/\=/\=/\=/\=/\==|
|\/=\/=\/=\/=\/=\/=]^[=\/=\/=\/=\/=\/==|""",
    (20, 19, 1, 52, 35))


h_49 = (r"""
               
 |--|--|--|--| 
 |           | 
 |       ### | 
 |      #####| 
 |       [O] | 
 |           | 
/==]  [=======\
|             |
|         +-+ |
|         | | |
|         +-+ |
|             |
|             |
\=====|^|=====/""",
    (7, 14, 1, 58, 15),
)


h_50 = (r"""
/-------------||---\
|            /__\  |
|            |==|  |
|                  |
|  +---+           |
|  |   |           |
|  |   |           |
|  +---+           |
|                  |
|                  |
|                  |
|=/  \========/  \=|
|                  |
|                  |
\-------------|^|--/""",
    (15, 14, 1, 36, 12),
)


h_51 = (r"""
|--------|
|[==][==]|
|        |
|        |
|        |
| +-+    |
| | |    |
| +-+    |
|        |
|---|^|--|""",
    (5, 9, 1, 33, 26),
)


h_52 = (r"""
/====[O]====[O]====\
|       |  |       |
| |_    |  |    _| |
| |_|   |  |   |_| |
|                  |
|-------]  [-------|
|               [=]|
|       |  |    /_\|
| |_    |  |       |
| |_|   |  |       |
|       |  |       |
|-------/  \-------|
|                  |
|                  |
\==|^|======[O]====/""",
    (4, 14, 1, 42, 26),
)


h_53 = (r"""
|--------|
|        |
|     +-+|
|     | ||
|     +-+|
|        |
|[=]     |
|/-\     |
|        |
|---|^|--|""",
    (5, 9, 1, 34, 30),
)


h_54 = (r"""
     |======_=|
|-|--|     /_\|
|# ##|     |=||
|# ##|        |
|# ##/   +--+ |
|#       |  | |
|# ##\   +--+ |
|-|--|        |
     |        |
     |===|^|==|""",
    (10, 9, 1, 41, 42),
)

vanaheim_entities = (
    [0, '*', 1, 45, 39, 'stand by'],
    [0, '*', 1, 31, 12, 'stand by'],
    [0, '*', 1, 41, 45, 'stand by'],
    [0, '*', 1, 52, 22, 'stand by'],
    [0, '*', 1, 52, 30, 'stand by'],
    ["vanaheim_aubergiste", '*', 21, 8, 1, 'stand by'],
    [0, '*', 21, 21, 6, 'stand by'],
    ["Freyja", '*', 22, 2, 8, 'stand by'],
    ["Freyr", '*', 22, 36, 3, 'stand by'],
    [0, '*', 49, 9, 10, 'stand by'],
    [0, '*', 49, 9, 11, 'stand by'],
    [0, '*', 50, 8, 5, 'stand by'],
    [0, '*', 50, 8, 9, 'stand by'],
    [0, '*', 51, 7, 3, 'stand by'],
    [0, '*', 51, 2, 4, 'stand by'],
    [0, '*', 52, 16, 9, 'stand by'],
    [0, '*', 53, 5, 2, 'stand by'],
    [0, '*', 54, 7, 2, 'stand by'],
    [0, '*', 54, 2, 3, 'stand by'],

)