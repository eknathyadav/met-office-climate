from attr import fields
from core.models import Region, Parameter, YearTemperature, MonthTemperature
from rest_framework import serializers


class MonthTemperatureSerializer(serializers.ModelSerializer):

    class Meta:
        model = MonthTemperature
        exclude = ('year', 'id')


class YearTempeartureSerializer(serializers.ModelSerializer):
    monthtemperature = MonthTemperatureSerializer(many=True, read_only=True)

    class Meta:
        model = YearTemperature
        fields = ['year', 'monthtemperature',
                  'win', 'spr', 'sum', 'aut', 'ann']


class ParameterSerializer(serializers.ModelSerializer):
    yeartemperature = YearTempeartureSerializer(many=True, read_only=True)

    class Meta:
        model = Parameter
        fields = ['parameter_name', 'yeartemperature']


class RegionSerializer(serializers.ModelSerializer):
    parameter = serializers.SerializerMethodField("get_parameter")

    class Meta:
        model = Region
        fields = ['id', 'regionName', 'parameter']

    def get_parameter(self, instance):
        name = self.context.get("parameter")
        print(name)
        if name == "ALL":
            parameter_type_instances = instance.parameter.all()
        else:
            parameter_type_instances = instance.parameter.filter(
                parameter_name=name)

            print(instance, parameter_type_instances)
        return ParameterSerializer(parameter_type_instances, many=True).data
