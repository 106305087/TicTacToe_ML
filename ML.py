df_old = pd.read_csv('/content/logs.log', header=None, names=['Timestamp', 'Game', 'First Move', 'First Move Player', 'Winner', 'Duration'],
                 delimiter='/', parse_dates=[0])
data = []
for i in range(len(df_old)):
  game_number = df_old.iloc[i]['Game'].split(' ')[1]
  first_move = df_old.iloc[i]['First Move'].replace('First Move - ', '')
  first_move_player = df_old.iloc[i]['First Move Player'].replace('First Move Player - ', '')
  winner = df_old.iloc[i]['Winner'].split('-')[1].split(' ')[1]

  data.append({'Game Number': int(game_number),
          'First_move': first_move,
          'First_move_player': first_move_player,
          'Winner': winner})

df = pd.DataFrame(data)

game_counts = df['Winner'].value_counts()
O_win = 0
X_win = 0
for i in range(len(df)):
  if df['Winner'][i] == 'O':
    O_win += 1
  elif df['Winner'][i] == 'X':
    X_win += 1

O_win_rate = (O_win/30)*100
X_win_rate = (X_win/30)*100

print('O_win_rate: {}'.format(O_win_rate))
print('X_win_rate: {}'.format(X_win_rate))

move = []
winner = []
for i in range(len(df)):
  if df['First_move'][i][1] == '1' and df['First_move'][i][4] == '1':
    move.append('center')
  elif df['First_move'][i][1] == '1' or df['First_move'][i][4] == '1':
    move.append('middle')
  else:
    move.append('corner')

for i in range(len(df)):
  if df['Winner'][i] == 'O':
    winner.append(1)
  elif df['Winner'][i] == 'X':
    winner.append(2)
  else:
    winner.append(0)

df['Move'] = move
df['Winner'] = winner

df_encoded = pd.get_dummies(df, columns=['Move'])

X = df_encoded.drop(columns=['Winner', 'First_move', 'First_move_player', 'Game Number'])
y = df_encoded['Winner']

model = LinearRegression()
model.fit(X, y)

coefficients = model.coef_
intercept = model.intercept_

output = {
    "Coefficients": coefficients,
    "Intercept": intercept,
    "Model": model
}

print(output)
