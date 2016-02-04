class Note(object):
    @classmethod
    def get_sample_notes(cls):
        notes = {'notes': [{'id': 1, 'data':'Hello World'}, {'id':2, 'data': 'Second note'}]}
        return notes
