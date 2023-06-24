from django.http import JsonResponse
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.parsers import JSONParser

from test_project.calculator.calculator import calculate
from test_project.Exceptions.exceptions import *


class MainClass(APIView):
    def post(self, request):
        data = JSONParser().parse(request)
        expression = data['expression']
        variables = data['variables']

        try:
            result = calculate(expression, variables)
            response = {'result': result}
        except NoParamExceprion as e:
            message = e.message
            response = {'result': None, 'error': message}
        except ZeroDivisionError:
            message = "Деление на 0"  # -
            response = {'result': None, 'error': message}
        except Exception:
            message = "Ошибка в данных: проверьте правильность ввода"
            response = {'result': None, 'error': message}

        return JsonResponse(response, status=status.HTTP_200_OK, safe=False)
