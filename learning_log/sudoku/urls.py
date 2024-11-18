from django.urls import path

from . import views
app_name = "sudoku"
urlpatterns = [path("", views.main, name="main"),
               path("<int:lv>", views.game, name="sudoku")]