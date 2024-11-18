from django.shortcuts import render
from . import sudoku
# Create your views here.

def validation(removed): 
	app = sudoku.SudokuGenerator(9, removed)
	app.fill_values()
	correct = app.get_board()
	game_board, answer = app.remove_cells()
	answer_sort = sorted(answer)
	answer_sort = list(map(str,((map(lambda x: correct[x[0]][x[1]], answer_sort)))))
	return game_board, answer_sort

def game(request, lv):
	data, correct = validation(lv)
	print("correct", correct)
	if request.method == "POST":
		print("request.POST=", request.POST, type(request.POST))
		answer = dict(request.POST)["abc"]
		print("Change", answer)
		if answer == correct:
			return render(request, "yes.html")
		else:
			print(answer)
			print(correct)
			return render(request, "no.html")
	else:
		return render(request, "sudoku.html", {
			"data": data
			})

def main(request):
	return render(request, "main.html")