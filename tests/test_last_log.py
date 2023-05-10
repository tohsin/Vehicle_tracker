from flask_testing import TestCase
from app import create_app, db
from models import LogData


class TestLastLogDataResource(TestCase):
    
    def create_app(self):
        app = create_app()
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
        app.config['TESTING'] = True
        return app

    def setUp(self):
        db.create_all()
        self.log_data_1 = LogData(device_id='device_1', irValue='10.5', fullValue='20.5', visibleValue='30.5', luxValue='40.5', tslFound=True,
                                  temperatureValue='25.5', humidityValue='50.5', heatIndexValue='30.5', dhtFound=True,
                                  long='10.1234', lat='20.5678', age='30.5', date='1633217271', speed='5.5', hdop='1.5', satellites_found=True)
        self.log_data_2 = LogData(device_id='device_1', irValue='11.5', fullValue='21.5', visibleValue='31.5', luxValue='41.5', tslFound=True,
                                  temperatureValue='26.5', humidityValue='51.5', heatIndexValue='31.5', dhtFound=True,
                                  long='11.1234', lat='21.5678', age='31.5', date='1633217272', speed='6.5', hdop='2.5', satellites_found=True)
        db.session.add_all([self.log_data_1, self.log_data_2])
        db.session.commit()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_last_log_data_resource_returns_latest_log_data(self):
        response = self.client.get('/last-log/device_1')
        self.assert200(response)
        data = response.json
        self.assertEqual(data['device_id'], 'device_1')
        self.assertEqual(data['irValue'], '11.5')
        self.assertEqual(data['fullValue'], '21.5')
        self.assertEqual(data['visibleValue'], '31.5')
        self.assertEqual(data['luxValue'], '41.5')
        self.assertEqual(data['tslFound'], True)
        self.assertEqual(data['temperatureValue'], '26.5')
        self.assertEqual(data['humidityValue'], '51.5')
        self.assertEqual(data['heatIndexValue'], '31.5')
        self.assertEqual(data['dhtFound'], True)
        self.assertEqual(data['long'], '11.1234')
        self.assertEqual(data['lat'], '21.5678')
        self.assertEqual(data['age'], '31.5')
        self.assertEqual(data['date'], '1633217272')
        self.assertEqual(data['speed'], '6.5')
        self.assertEqual(data['hdop'], '2.5')
        self.assertEqual(data['satellites_found'], True)

    def test_last_log_data_resource_returns_404_if_device_id_does_not_exist(self):
        response = self.client.get('/last-log/non_existent_device')
        self.assert404(response)
        data = response.json
        self.assertEqual(data['error'], 'No log data found for device ID non_existent_device')
