import flet as ft


class View(ft.UserControl):
    def __init__(self, page: ft.Page):
        super().__init__()
        # page stuff
        self._page = page
        self._page.title = "Template application using MVC and DAO"
        self._page.horizontal_alignment = 'CENTER'
        self._page.theme_mode = ft.ThemeMode.LIGHT
        # controller (it is not initialized. Must be initialized in the main, after the controller is created)
        self._controller = None
        # graphical elements
        self._title = None
        self.dd_locazione = None
        self.btn_statistiche = None
        self.txt_result = None
        self.txt_container = None
        self.btn_ricerca_cammino = None

        self.txtN = None
        self.txtOut2 = None
        self.btn_path = None


    def load_interface(self):
        # title
        self._title = ft.Text("23/07/2018 - Ufo sighting", color="blue", size=24)
        self._page.controls.append(self._title)

        #ROW with some controls
        self.dd_locazione = ft.Dropdown(label="locazione")
        self.btn_grafo = ft.ElevatedButton(text="Crea Grafo", on_click=self._controller.handle_graph)


        # button for the "creat graph" reply
        self.btn_statistiche = ft.ElevatedButton(text="Statistiche", on_click=self._controller.handle_statistiche)
        row1 = ft.Row([self.dd_locazione,self.btn_statistiche,self.btn_grafo],
                      alignment=ft.MainAxisAlignment.CENTER)
        self._page.controls.append(row1)

        self.btn_ricerca_cammino = ft.Dropdown(label="Ricerca cammino")
        row2 = ft.Row([self.btn_ricerca_cammino],
                      alignment=ft.MainAxisAlignment.CENTER)



        # List View where the reply is printed
        self.txt_result = ft.ListView(expand=1, spacing=10, padding=20, auto_scroll=True)
        self._page.controls.append(self.txt_result)
        self._page.update()

        self.btn_path = ft.ElevatedButton(text="Calcola percorso", on_click=self._controller.handle_path)

        row2 = ft.Row([self.btn_path],
                      alignment=ft.MainAxisAlignment.CENTER)
        self._page.controls.append(row2)

        self.txtOut2 = ft.ListView(expand=1, spacing=10, padding=20, auto_scroll=True)
        self._page.controls.append(self.txtOut2)
        self._controller.fillDD()
        self._page.update()
    @property
    def controller(self):
        return self._controller

    @controller.setter
    def controller(self, controller):
        self._controller = controller

    def set_controller(self, controller):
        self._controller = controller

    def create_alert(self, message):
        dlg = ft.AlertDialog(title=ft.Text(message))
        self._page.dialog = dlg
        dlg.open = True
        self._page.update()

    def update_page(self):
        self._page.update()
