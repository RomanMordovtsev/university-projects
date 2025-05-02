from spemix import SpeechMixin

class Exceptiki(SpeechMixin):
    def nam(self):
        a = SpeechMixin.naming(self)
        try:
            if '0' in a or '1' in a or '2' in a or '3' in a or '4' in a or '5' in a or '6' in a or '7' in a or '8' in a or '9' in a:
                raise Exception('Nos so good')
        except Exception:
            print("Doesn't suit")
            raise
        else:
            return a






