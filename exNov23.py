class SecretList(list):
    def __str__(self):
        try:
            return f"[{str(self[0])}]"
        except:
            return "[]"