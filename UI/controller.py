import flet as ft

class Controller:
    def __init__(self, view, model):
        self._view = view
        self._model = model

    def handle_hello(self, e):
        name = self._view.txt_name.value
        if not name:
            self._view.create_alert("Inserire il nome")
            return
        self._view.txt_result.controls.append(ft.Text(f"Hello, {name}!"))
        self._view.update_page()

    def trovaAeroporti(self, e):
        minimo = self._view._min_companies.value
        if not minimo:
            self._view.txt_result.controls.clear()
            self._view.txt_result.controls.append(ft.Text("Inserire minimo"))
            self._view.update_page()
            return

        try:
            minimo = int(minimo)
        except ValueError:
            self._view.txt_result.controls.clear()
            self._view.txt_result.controls.append(ft.Text("Inserire un numero valido"))
            self._view.update_page()
            return

        aeroporti = self._model.trovaAeroporti(minimo)
        if not aeroporti:
            self._view.txt_result.controls.clear()
            self._view.txt_result.controls.append(ft.Text("Nessun aeroporto trovato"))
            self._view.update_page()
            return

        # Riempimento dropdown
        self._view._airport_origin.options.clear()
        self._view._airport_dest.options.clear()
        for a in aeroporti:
            option = ft.dropdown.Option(key=a.ID, text=a.AIRPORT)
            self._view._airport_origin.options.append(option)
            self._view._airport_dest.options.append(option)

        # Costruzione grafo
        grafo = self._model.buildGraph(minimo)
        self._view.txt_result.controls.clear()
        self._view.txt_result.controls.append(ft.Text("Grafo creato"))
        self._view.txt_result.controls.append(ft.Text(f"Nodi: {len(grafo.nodes)} - Archi: {len(grafo.edges)}"))
        self._view.update_page()

    def percorso(self, e):
        try:
            id1 = int(self._view._airport_origin.value)
            id2 = int(self._view._airport_dest.value)
        except (ValueError, TypeError):
            self._view.txt_result.controls.clear()
            self._view.txt_result.controls.append(ft.Text("Selezionare due aeroporti validi"))
            self._view.update_page()
            return

        path = self._model.trovaPercorso(id1, id2)
        self._view.txt_result.controls.clear()

        if path is None:
            self._view.txt_result.controls.append(ft.Text("❌ Nessun percorso trovato"))
        else:
            self._view.txt_result.controls.append(ft.Text("✈️ Percorso trovato:"))
            for pid in path:
                aeroporto = self._model.idMap.get(pid)
                nome = aeroporto.AIRPORT if aeroporto else str(pid)
                self._view.txt_result.controls.append(ft.Text(nome))

        self._view.update_page()
