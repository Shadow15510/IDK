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
/      \ /\   /    \       /o\    |__|                         /    \   /\ 
        /  \ /      \      |_|                            _   /      \ /  \
/\     /    \ /\      ###   .        ######  ######      /o\    /\    /    
  \   /      /  \    #####      ###  ######  ######      |_|   /  \  /     
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
   \        /  \          /|\   |_| .    |__|     .'       /    \   /\ /   
    \ /\   /    \              ` ``'         ###   ,  _   /      \ /  \    
     /  \ /      \ /\             _         ##### ', /-\          /    \   
    /    \        /  \         . / \         ### ,   |_|        /\      \ /
   /      \ /\   /    \          |_|         /|\ ,    `        /  \      / 
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
   /      \ /\ /      \ /  \       .''  |_|   ,'`' ',` |_|  /\ /      \ /  
           /  \        /    \         ,.,  .,`,  /\  ', ,` /  \        /   
     /\   /    \   /\ /      \ /\               /  \      /    \   /\ /    
    /  \ /      \ /  \        /  \   /\        /    \ /\ /      \ /  \     
   /    \        /    \      /    \ /  \   /\ /      /  \   /\   /    \    
  /      \      /      \ /\ /      /    \ /  \      /    \ /  \ /      \   
                        /  \      /      /    \    /      /    \           
                       /    \           /      \         /      \          """,
[
    ("vanaheim_1", '?', 42, 20, 'stand by'),
    ("vanaheim_2", '?', 26, 29, 'stand by'),
    
    ("vanaheim_charretier", '*', 45, 39, 'stand by'),
    (19, '*', 31, 12, 'stand by'),
    (20, '*', 41, 45, 'stand by'),
    (21, '*', 52, 22, 'stand by'),
    (22, '*', 52, 30, 'stand by'),
],

# Autres mondes (Vanaheim = 1)
    (28, 13, 2, 14, 68),  # Alfheim
    (54, 29, 3, 10, 58),  # Midgard
    (56, 42, 5, 11, 120), # Jotunheim
    
# Maisons
    (44, 11, 21, 5, 9), # Auberge
    (52, 35, 22, 20, 19),
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
[
    ("h_21_aubergiste", '*', 8, 1, 'stand by'),
    ("h_21", '*', 21, 6, 'stand by'),
],
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
[
    ("Freyja", '*', 2, 8, 'stand by'),
    ("Freyr", '*', 36, 3, 'stand by'),
],
    (20, 19, 1, 52, 35))
