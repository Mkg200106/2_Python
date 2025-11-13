import random
import time
from django.shortcuts import render, redirect
from .models import Score

# Create your views here.
def guess_number(request):
    # If there's no active game, start one
    if 'number' not in request.session:
        level = request.GET.get('level', 'Easy')
        max_number = {'Easy': 10, 'Medium': 50, 'Hard': 100}.get(level, 10)

        request.session['level'] = level
        request.session['number'] = random.randint(1, max_number)
        request.session['attempts'] = 0
        request.session['message'] = f'Guess a number between 1 and {max_number}!'
        # 🔹 Do NOT set start_time yet — will start on first POST

    message = request.session.get('message', '')
    number = request.session['number']
    attempts = request.session['attempts']
    level = request.session['level']

    if request.method == 'POST':
        player_name = request.POST.get('player_name', 'Player')

        # 🔹 Start timer only when first guess happens
        if 'start_time' not in request.session:
            request.session['start_time'] = time.time()

        try:
            guess = int(request.POST.get('guess'))
            request.session['attempts'] = attempts + 1

            if guess < number:
                message = 'Too low! Try again.'
            elif guess > number:
                message = 'Too high! Try again.'
            else:
                end_time = time.time()
                start_time = request.session.get('start_time', end_time)
                time_taken = end_time - start_time

                message = (
                    f'🎉 Correct! You guessed {number} in '
                    f'{attempts + 1} tries and {time_taken:.1f} seconds.'
                )

                # Save score
                Score.objects.create(
                    player_name=player_name,
                    attempts=attempts + 1,
                    level=level,
                    time_taken=time_taken
                )

                # Reset game data
                for key in ['number', 'attempts', 'start_time']:
                    request.session.pop(key, None)

        except (ValueError, TypeError):
            message = 'Please enter a valid number.'

        request.session['message'] = message

    # Show top 5 fastest players
    scores = Score.objects.order_by('time_taken', 'attempts')[:5]

    return render(request, 'game/index.html', {
        'message': message,
        'level': level,
        'scores': scores
    })

def reset_game(request):
    request.session.flush()
    return redirect('/')
