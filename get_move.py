from random import randint

def _get_move(ai, map):

	if not ai.you.is_dangerous and not ai.enemy.is_dangerous: # Nobody dang
		path = map.get_breadth_first_path(ai.you.pos, char_goal=map.icon.super_pellet)
		move = map.get_move_between(ai.you.pos, path[0])
		return move

	elif ai.you.is_dangerous and not ai.enemy.is_dangerous: # I'm dang, enemy is not
		path = map.get_breadth_first_path(ai.you.pos, pos_goal=ai.enemy.pos)
		move = map.get_move_between(ai.you.pos, path[0])
		return move

	elif ai.enemy.is_dangerous and not ai.you.is_dangerous: # Enemy is dang, I am not
		if (map.super_pellets_left > 0):
			path = map.get_breadth_first_path(ai.you.pos, char_goal=map.icon.super_pellet)
			move = map.get_move_between(ai.you.pos, path[0])
			return move
		else:
			path = map.get_breadth_first_path(ai.you.pos, char_goal=map.icon.pellet)
			move = map.get_move_between(ai.you.pos, path[0])
			return move
	
	else: # Both is dang
		path = map.get_breadth_first_path(ai.you.pos, char_goal=map.icon.pellet)
		move = map.get_move_between(ai.you.pos, path[0])
		return move

	return randint(0,3)