import unittest
from app import app, db
from models import LogData

class TestLogDataResource(unittest.TestCase):
    def setUp(self):
        app.config['TESTING'] = True
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
        db.init_app(app)
        with app.app_context():
            db.create_all()

        self.client = app.test_client()

    def tearDown(self):
        with app.app_context():
            db.drop_all()

    def test_post_log_data(self):
        payload = {
            'device_id': 'device_1',
            'irValue': '10.5',
            'fullValue': '20.5',
            'visibleValue': '30.5',
            'luxValue': '40.5',
            'tslFound': True,
            'temperatureValue': '25.5',
            'humidityValue': '50.5',
            'heatIndexValue': '30.5',
            'dhtFound': True,
            'long': '10.1234',
            'lat': '20.5678',
            'age': '30.5',
            'date': '1633217271',
            'speed': '5.5',
            'hdop': '1.5',
            'satellites_found': True
        }

        response = self.client.post('/log_data', json=payload)
        self.assertEqual(response.status_code, 200)

        # check if the data was stored in the database
        with app.app_context():
            log_data = LogData.query.filter_by(device_id='device_1').first()
            self.assertIsNotNone(log_data)
            self.assertEqual(log_data.irValue, '10.5')
            self.assertEqual(log_data.fullValue, '20.5')
            self.assertEqual(log_data.visibleValue, '30.5')
            self.assertEqual(log_data.luxValue, '40.5')
            self.assertEqual(log_data.tslFound, True)
            self.assertEqual(log_data.temperatureValue, '25.5')
            self.assertEqual(log_data.humidityValue, '50.5')
            self.assertEqual(log_data.heatIndexValue,'30.5')
            self.assertEqual(log_data.dhtFound, True)
            self.assertEqual(log_data.long, '10.1234')
            self.assertEqual(log_data.lat, '20.5678')
            self.assertEqual(log_data.age, '30.5')
            self.assertEqual(log_data.date, '1633217271')
            self.assertEqual(log_data.speed, '5.5')
            self.assertEqual(log_data.hdop, '1.5')
            self.assertEqual(log_data.satellites_found, True)

if __name__ == '__main__':
    unittest.main()
