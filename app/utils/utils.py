class Utils:
    def prueba(self, **kwargs):
        response = {
            'mensaje': kwargs['msg']}
        if 'datos' in kwargs:
            response['datos'] = kwargs['datos']
        return response

    def arreglar_nombre(self, nombre):
        return nombre.upper().replace(" ", "").replace("Á", "A").replace("É", "E").replace("Í", "I").replace("Ó", "O").replace("Ú", "U")
