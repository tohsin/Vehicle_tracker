from flask_restful import Resource, reqparse, Api , abort
import json
from models import LogData, db

class LogDataResource(Resource):
    update_parser = reqparse.RequestParser()
    update_parser.add_argument('device_id', type=str, required=True, help='device ID required')
    update_parser.add_argument('irValue', type=str, required=False)
    update_parser.add_argument('fullValue', type=str, required=False)
    update_parser.add_argument('visibleValue', type=str, required=False)
    update_parser.add_argument('luxValue', type=str, required=False)
    update_parser.add_argument('tslFound', type=bool, required=False)
    update_parser.add_argument('temperatureValue', type=str, required=False)
    update_parser.add_argument('humidityValue', type=str, required=False)
    update_parser.add_argument('heatIndexValue', type=str, required=False)
    update_parser.add_argument('dhtFound', type=bool, required=False)
    update_parser.add_argument('long', type=str, required=False)
    update_parser.add_argument('lat', type=str, required=False)
    update_parser.add_argument('age', type=str, required=False)
    update_parser.add_argument('date', type=str, required=False)
    update_parser.add_argument('speed', type=str, required=False)
    update_parser.add_argument('hdop', type=str, required=False)
    update_parser.add_argument('satellites_found', type=bool, required=False)


    def post(self):
        args = LogDataResource.update_parser.parse_args()
        log_data = LogData()
        for key, value in args.items():
            if value is not None:
                setattr(log_data, key, value)
        db.session.add(log_data)
        db.session.commit()
        return {'status': 'OK'}, 200
