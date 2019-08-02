def get_answer_list():
	dict = {1:"A",2:"B",3:"C",4:"D"}
	answer_list = ["A","B","C","D"]
	for i in range(1,5):
		for j in range(1,5):
			if i == j:
				continue
			answer_list.append("{}{}".format(dict[i], dict[j] ))
	for i in range(1,5):
		for j in range(1,5):
			for k in range(1,5):
				if i==j or j==k or i==k:
					continue
				answer_list.append("{}{}{}".format(dict[i], dict[j], dict[k] ))
	for i in range(1,5):
		for j in range(1,5):
			for k in range(1,5):
				for l in range(1,5):
					if i==j or i==k or i==l or j==k or j==l or k==l:
						continue
					answer_list.append("{}{}{}{}".format(dict[i], dict[j], dict[k] ,dict[l]))
	return answer_list