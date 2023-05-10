from flask_restful import Resource, reqparse, Api , abort
import json
from models import LogData, db


class LastLogDataResource(Resource):
    def get(self, device_id):
        log_data = LogData.query.filter_by(device_id=device_id).order_by(LogData.date.desc()).first()
        if log_data is None:
            return {'error': 'No log data found for device ID {}'.format(device_id)}, 404
        else:
            return {
                'device_id': log_data.device_id,
                'irValue': log_data.irValue,
                'fullValue': log_data.fullValue,
                'visibleValue': log_data.visibleValue,
                'luxValue': log_data.luxValue,
                'tslFound': log_data.tslFound,
                'temperatureValue': log_data.temperatureValue,
                'humidityValue': log_data.humidityValue,
                'heatIndexValue': log_data.heatIndexValue,
                'dhtFound': log_data.dhtFound,
                'long': log_data.long,
                'lat': log_data.lat,
                'age': log_data.age,
                'date': log_data.date,
                'speed': log_data.speed,
                'hdop': log_data.hdop,
                'satellites_found': log_data.satellites_found,
            }, 200
