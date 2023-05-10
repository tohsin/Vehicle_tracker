from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()

class LogData(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    device_id  = db.Column(db.String(150))

    # light values
    irValue = db.Column(db.String(50), nullable=True)
    fullValue = db.Column(db.String(50), nullable=True)
    visibleValue = db.Column(db.String(50), nullable=True)
    luxValue = db.Column(db.String(50), nullable=True)
    tslFound = db.Column(db.Boolean, default=False)

    # temperature values
    temperatureValue = db.Column(db.String(50), nullable=True)
    humidityValue = db.Column(db.String(50), nullable=True)
    heatIndexValue = db.Column(db.String(50), nullable=True)
    dhtFound = db.Column(db.Boolean, default=False)

    #gps values
    long = db.Column(db.String(50), nullable=True)
    lat = db.Column(db.String(50), nullable=True)
    age = db.Column(db.String(50), nullable=True)
    date = db.Column(db.String(50), nullable=True)
    speed = db.Column(db.String(50), nullable=True)
    hdop = db.Column(db.String(50), nullable=True)
    satellites_found = db.Column(db.Boolean, default=False)
    
    def __repr__(self):
        return '<LogData {}>'.format(self.device_id)

    def json(self):
        return {
            'id': self.id,
            'device_id': self.device_id,
            'irValue': str(self.irValue),
            'fullValue': str(self.fullValue),
            'visibleValue': str(self.visibleValue),
            'luxValue': str(self.luxValue),
            'tslFound': self.tslFound,
            'temperatureValue': str(self.temperatureValue),
            'humidityValue': str(self.humidityValue),
            'heatIndexValue': str(self.heatIndexValue),
            'dhtFound': self.dhtFound,
            'long': str(self.long),
            'lat': str(self.lat),
            'age': str(self.age),
            'date': str(self.date),
            'speed': str(self.speed),
            'hdop': str(self.hdop),
            'satellites_found': self.satellites_found
        }





