from django.views import generic

from models import Game


class IndexView(generic.TemplateView):
    template_name = 'crafter/index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['games'] = Game.objects.all()
        return context

class GameView(generic.TemplateView):
    template_name = 'crafter/game.html'

    def get_context_data(self, **kwargs):
        context = super(GameView, self).get_context_data(**kwargs)

        game_id = self.kwargs['game_id']
        context['game'] = Game.objects.get(pk=game_id)
        return context