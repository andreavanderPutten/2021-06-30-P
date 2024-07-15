import flet as ft

from database.DAO import DAO


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model

    def fillDD(self):
       localizzazioni = DAO.getLocalizzazioni()
       self._view.dd_locazione.options = list(map(lambda x: ft.dropdown.Option(x), localizzazioni))

    def handle_graph(self, e):
        self._model.creaGrafo()
        self._view.txt_result.controls.append(ft.Text(f"Numero di nodi : {self._model.grafoDetails()[0]}, Numero di archi : {self._model.grafoDetails()[1]}"))
        self._view.update_page()
    def handle_statistiche(self,e):
        localizzazione = self._view.dd_locazione.value
        if localizzazione== "" or localizzazione == None :
            self._view.create_alert("Non hai scelto la localizzazione, sceglila prima di schiacciare statistiche")
        lista_connesse = self._model.statistiche(localizzazione)
        self._view.txt_result.controls.append(ft.Text(f"Adiacenti a :{localizzazione}"))
        for elemento in lista_connesse :
            self._view.txt_result.controls.append(ft.Text(f"{elemento[1]} ----> {elemento[2]["weight"]}"))
        self._view.update_page()
    def handle_path(self, e):
        sol,costo = self._model.trova_percorso(self._view.dd_locazione.value)
        self._view.txtOut2.controls.append(ft.Text(f"Percorso massimo ha il costo {costo}"))
        for arco in sol :
            self._view.txtOut2.controls.append(ft.Text(f"{arco[0]} ----> {arco[1]}"))
        self._view.update_page()