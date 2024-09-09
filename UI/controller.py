import flet as ft

from database.DAO import DAO


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model


    def handle_graph(self, e):
        goal_fatti = self._view.txt_goal_fatti.value
        if goal_fatti == None :
            self._view.create_alert("Non hai inserito un valore di goal fatti")
            return
        self._model.creaGrafo(float(goal_fatti))
        self._view.txtOut.controls.append(ft.Text(f"Numero di nodi : {self._model.grafoDetails()[0]},Numero di archi : {self._model.grafoDetails()[1]}"))
        self._view.update_page()
    def handle_details(self, e):
        pass
    def handle_tifosi(self,e):
        pass
    def top5(self,e):
        pass
    def fillDD(self):
        pass