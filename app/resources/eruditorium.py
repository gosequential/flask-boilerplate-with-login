from flask_restful import Resource

class Weather(Resource):
    def get(self):
        return "The weather in Boston today is ..."
    def post(self):
        pass

class PricingData(Resource):
    def get(self):
        return "Dow Jones was down by 122 points today."