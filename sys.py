import pickle

game_data = {
    'player-position':'N23 E45',
    'pockets':['key','pocket knife','polished stone'],
    'backpack':['rope','hammer','apple'],
    'money':158.50
}

save_file=open('save_file','wb')
pickle.dump(game_data,save_file)
save_file.close()

load_file=open('save_file','rb')
loaded_game_data=pickle.load(load_file)
load_file.close()

print(loaded_game_data)