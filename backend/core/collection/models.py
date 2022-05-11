from collections import namedtuple
from datetime import datetime

from .. import db



CollectionInterface = namedtuple(
    'CollectionInterface', [
        'mode', 'isEmpty', 'pumpActive', 'pumpDuration', 
        'pumpInterval', 'lightLevel', 'temperature', 
        'humidity', 'soilMoisture', 'soilMoistureTarget',
        
    ], 
)



class Collection(db.Model):
    
    """ """
    
    id = db.Column(db.Integer, primary_key=True)

    mode = db.Column(db.Integer)

    isEmpty = db.Column(db.Boolean)
    pumpActive = db.Column(db.Boolean)
    pumpDuration = db.Column(db.Float)
    pumpInterval = db.Column(db.Float)

    lightLevel = db.Column(db.Float,)
    temperature = db.Column(db.Float)
    humidity = db.Column(db.Float)
    soilMoisture = db.Column(db.Float)
    soilMoistureTarget = db.Column(db.Float)
    created = db.Column(db.DateTime, default=datetime.utcnow)
    
    
    def __repr__(self):
        return '<Collection: id {}, mode {}'.format(self.id, self.mode)


    @property
    def serialized(self):
        return {
            'id': self.id,
            'created': self.created,
            'mode': self.mode, 
            'isEmpty': self.isEmpty, 
            'pumpActive': self.pumpActive, 
            'pumpDuration': self.pumpDuration,             
            'pumpInterval': self.pumpInterval, 
            'lightLevel': self.lightLevel, 
            'temperature': self.temperature, 
            'humidity': self.humidity, 
            'soilMoisture': self.soilMoisture, 
            'soilMoistureTarget': self.soilMoistureTarget
        }




