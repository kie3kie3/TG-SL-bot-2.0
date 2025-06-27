roles = [
    ['Кальянщик', 'hookah'],
    ["Бармен", 'bar'],
    ["Хоста", 'hosta']
]
abc = [
    ':cloud:',
    ':beer:',
    ':ribbon:'
    ]
rolesActions = {
    'hookah': ['come_hookah', 'checkList_hookah'],
    'hookah_evening': ['come_hookah_evening', 'checkList_hookah_evening'],
    'bar' : ['come_bar', 'checkList_bar'],
    'hosta' : ['come_hosta', 'checkList_hosta']
}
rolesDict = {
    'hookah': 'КМ утро',
    'hookah_evening' : 'КМ вечер',
    'bar' : "Бар",
    'hosta' : "Хоста"
}
actionsDecript = {
    'come' : 'приход',
    'checkList' : 'чек лист'
}
roles_come = {
    'hookah': [10, 45, 1],
    'hookah_evening' : [16, 50, 0],
    'bar' : [10, 45, 1],
    'hosta' : [13, 50, 0]
}
roles_checkList = {
    'hookah': [],
    'hookah_evening' : [],
    'bar' : [],
    'hosta' : []
}