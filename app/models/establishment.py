from pyairtable import Table
from app.config import settings
# pyairtable has an orm but for instance is to overengineer

class Establishment(Table):
  def __init__(self, api, base_id, table_name):
    super().__init__(api, base_id, table_name)

  def all_establishments(self):
    establishiments = super().all()
    ef = [e['fields'] for e in establishiments]
    return ef


def establishments():
    e = Establishment(settings.API_KEY, settings.BASE_ID, 'establishment')
    return e.all_establishments()
