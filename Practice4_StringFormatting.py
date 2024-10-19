team1_num = 5
team2_num = 6
team1_name = 'Мастера кода'
team2_name = 'Волшебники данных'
score_1 = 40
score_2 = 42
team1_time = 1552.512
team2_time = 2153.31451
tasks_total = 82
time_avg = 45.2
challenge_result = 'Победа команды Волшебники данных!'


print('В команде %s участноков: %s' % (team1_name, team1_num))
print('В команде %s участноков: %s' % (team2_name, team2_num))
total_participants = team1_num + team2_num
print('Итого участников: %s' % total_participants)

print('Командой {} решено задач : {}'.format(team1_name, score_1))
print('Время команды {} составляет: {} секунд'.format(team1_name, team1_time))
print('Командой {} решено задач : {}'.format(team2_name, score_2))
print('Время команды {} составляет: {} секунд'.format(team2_name, team2_time))

print(f'Результат соревнования: {challenge_result}')
print(f'Сегодня в общей сложности было решено {score_1+score_2} задач, '
      f'в среднем по {(team1_time + team2_time)/tasks_total} секунд на задачу')